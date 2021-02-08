from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View, generic
from .models import Problem_Statement, Partner
from .forms import *
from ScreeningApp.models import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import uuid 
from django.core.mail import send_mail,EmailMessage
from .models import Problem_Statement, Partner, Project, Community_Organization, Community_Member
from django.apps import apps
import requests
import operator
headers = {
    'Accept': 'application/vnd.github.v3+json',
}
Entry = apps.get_model('andablog', 'Entry')
# Create your views here.
def screeninglink_mail(email):
    debug_flag = settings.DEBUG
    candidate=Candidate.objects.get(email=email)
    name=candidate.name
    screening=Screenings.objects.create(candidate_id=candidate)
    screeninguuid=screening.screening_uuid
    print(screeninguuid)
    email=candidate.email
    #from_email=settings.EMAIL_HOST_USER
    from_email='Hack For Change<noreply@hackforchange.co.in>'
    to=[email]
    subject="Screening Link"
    #msg = MIMEMultipart('alternative')
    html_content = render_to_string('HFC/screening_email.html', {'screeninguuid':screeninguuid,'name':name,'debug_flag':debug_flag})
    #msg = EmailMultiAlternatives(subject, html_content, from_email , [to])
    msg = EmailMessage(subject, html_content, from_email , [to])
    msg.content_subtype = "html"
    msg.send(fail_silently=True)
    print("Mail sended successfully")
def thanks(request):
    return render(request,'HFC/thanks.html')
class Home(View):
    def get(self, request):
        entries = Entry.objects.all()[:3]
        return render(request,'HFC/hfc_home.html',{'entries':entries})

class ProblemStatementsView(generic.ListView):
    def get(self, request):
        problems_list = Problem_Statement.objects.all()
        print(problems_list)
        issue_areas = Issue_Area.objects.all()
        return render(request, 'HFC/problem_statements.html', {'problems_list': problems_list,'issue_areas':issue_areas})

class ProblemsWithIssueareaView(generic.ListView):
    def get(self, request, issue_area_slug):
        issue_area = Issue_Area.objects.get(issue_area_slug = issue_area_slug)
        problems_list = Problem_Statement.objects.filter(issue_area=issue_area)
        print( problems_list)
        issue_areas = Issue_Area.objects.all()
        return render(request, 'HFC/problem_statements_with_issue_area.html', {'problems_list': problems_list,'issue_areas': issue_areas})

class ProblemDiscriptionView(View):
    def get(self, request, title_slug):
        problem = Problem_Statement.objects.get(title_slug=title_slug)
        print(problem.partner_id)
        try:
            partner = Partner.objects.get(name=problem.partner_id)
        except:
            print('No Partner for this problem statement')
            partner=' '
        try:
            focus_areas = partner.focus_area.split(',')
        except:
            focus_areas =' '
        issue_areas = Issue_Area.objects.all()
        return render(request, 'HFC/problem_discription.html', {'problem': problem, 'focus_areas': focus_areas,'issue_areas': issue_areas,'partner':partner})

def load_area_of_expertise(request):
    expertise_area_id = request.GET.get('profession')
    expertises=Expertise.objects.filter(category_of_expertise=expertise_area_id)
    return render(request,'HFC/areaofexpertise.html',{'expertises':expertises})

class MentorSignup(View):
    def get(self,request):
        form=Mentor_form()
        mentors = Community_Member.objects.filter(type  ='Mentor')[:6]
        return render(request,'HFC/mentor_signup.html',{'form':form,'mentors':mentors})
    def post(self,request):
        form=Mentor_form(request.POST)
        print(request.POST)
        text = "Thanks for signing up as a Mentor"
        if form.is_valid():
            print(form.is_valid())
            area_of_expertise=request.POST.getlist('area_of_expertise')
            mentor=form.save(commit=False)
            mentor.type="Mentor"
            mentor.save()
            form.save_m2m()
            email=mentor.email
            print(email)
            try:
                #screeninglink_mail(email)
                message = "A new Mentor signed up"
                to_list=['team@hackforchange.co.in',]
                send_mail('New signup ', message,'noreply@hackforchange.co.in',to_list)
                #print("Screening email not send for now")
            except:
                print('Error in sending email screening link to Mentor')
            #messages.success(request,"Volunteer Registration Form Submitted Successfully")
            return render(request, 'HFC/thanks.html',{'text':text})
class CenterContributorSignup(View):
    def get(self,request,hfc_center_slug):
        form=Center_contributor_form()
        center = Community_Organization.objects.get(organization_name_slug=hfc_center_slug)
        contributors = Community_Member.objects.filter(type  ='Contributor')
        return render(request,'HFC/center_contributor_signup.html',{'form':form,'contributors':contributors,'center':center}) 
    def post(self,request,hfc_center_slug):
        form=Center_contributor_form(request.POST)
        community_org=Community_Organization.objects.get(organization_name_slug=hfc_center_slug)
        print(request.POST)
        print(form.is_valid())
        text = "Thanks for signing up as a contributor."
        if form.is_valid():
            #form.save()
            area_of_expertise=request.POST.getlist('area_of_expertise')
            contributor=form.save(commit=False)
            contributor.type="Contributor"
            contributor.organization_id=community_org
            contributor.save()
            form.save_m2m()
            email=contributor.email
            print(email)
            try:
                screeninglink_mail(email)
                message = "A new contributor signed up to {0} center".format(community_org.organization_name)
                to_list=['team@hackforchange.co.in',]
                send_mail('New signup ', message,'Hack for change<noreply@hackforchange.co.in',to_list)
                #print("Screening email not send for now")
            except:
                print('Error in sending email screening link to Contributor')
            return render(request, 'HFC/thanks.html',{'text':text})

class ChapterContributorSignup(View):
    def get(self,request,hfc_chapter_slug):
        form=Chapter_contributor_form()
        print(hfc_chapter_slug)
        chapter = Community_Organization.objects.get(organization_name_slug=hfc_chapter_slug)
        contributors = Community_Member.objects.filter(type  ='Contributor')
        return render(request,'HFC/chapter_contributor_signup.html',{'form':form,'chapter':chapter,'contributors':contributors}) 
    def post(self,request,hfc_chapter_slug):
        form=Chapter_contributor_form(request.POST)
        community_org=Community_Organization.objects.get(organization_name_slug=hfc_chapter_slug)
        print(request.POST)
        print(form.is_valid())
        text = "Thanks for signing up as a contributor."
        if form.is_valid():
            #form.save()
            area_of_expertise=request.POST.getlist('area_of_expertise')
            contributor=form.save(commit=False)
            contributor.type="Contributor"
            contributor.organization_id=community_org
            contributor.save()
            form.save_m2m()
            email=contributor.email
            print(email)
            try:
                screeninglink_mail(email)
                #print("Screening email not send for now")
                message = "A new contributor signed up to {0} chapter".format(community_org.organization_name)
                to_list=['team@hackforchange.co.in',]
                send_mail('New signup ', message,'Hack for change<noreply@hackforchange.co.in>',to_list)
            except:
                print('Error in sending email screening link to Contributor')
            return render(request, 'HFC/thanks.html',{'text':text})

class ProjectsView(generic.ListView):
    def get(self, request):
        projects_list = Project.objects.all()
        issue_areas = Issue_Area.objects.all()
        return render(request, 'HFC/projects_list.html', {'projects_list':projects_list,'issue_areas': issue_areas})

class CommunityView(View):
    def get(self, request):
        hfc_centers=Community_Organization.objects.filter(type='Center')
        hfc_chapters=Community_Organization.objects.filter(type='Chapter')
        
        centre_count = {}
        chapter_count = []
        for centre in hfc_centers:
            print(centre.community_member_set.count())
            centre_count[centre.organization_name]=centre.community_member_set.count()
        
            #centre_count = centre_count.count()
        print("<<<<<<<<<<<<<<<<<<")
        print(centre_count)
        for chapter in hfc_chapters:
            print(chapter.community_member_set.count())
        mentors_list = Community_Member.objects.filter(type='Mentor')
        contributors_list = Community_Member.objects.filter(type='Contributor').order_by('-commit')
        
        return render(request, 'HFC/community.html', {'hfc_centers': hfc_centers, 'hfc_chapters': hfc_chapters, 'centre_count': centre_count, 'mentors_list': mentors_list, 'contributors_list':contributors_list,})

class ProblemStatementsSubmitView(View):
    def get(self,request):
        form=Problem_Statement_form()
        issue_areas = Issue_Area.objects.all()
        return render(request,'HFC/problem_statements_submit.html',{'form':form,'issue_areas': issue_areas})
    def post(self,request):
        form=Problem_Statement_form(request.POST)
        print(request.POST)
        text="Thanks for submitting the problem statement"
        if form.is_valid():
            problem=form.save(commit=False)
            problem.status="Draft"
            form.save()
            return render(request, 'HFC/thanks.html',{'text':text})

class AboutView(View):
    def get(self,request):
        return render(request,'HFC/about.html')
class PrivacyPolicyView(View):
    def get(self,request):
        issue_areas = Issue_Area.objects.all()
        return render(request,'HFC/privacy_policy.html',{'issue_areas': issue_areas})
class TermsAndConditionView(View):
    def get(self,request):
        issue_areas = Issue_Area.objects.all()
        return render(request,'HFC/terms_conditions.html',{'issue_areas': issue_areas})
class ContactView(View):
    def get(self,request):
        return render(request,'HFC/contact.html')
    def post(self,request):
        data = request.POST.dict()
        if 'csrfmiddlewaretoken' in data:
            del data['csrfmiddlewaretoken']
        print(data)
        text ="Thanks for contacting us."
        sender_name = data['name']
        sender_email=data['email']
        subject="New contact us  message"
        #From_mail=settings.EMAIL_HOST_USER
        to_list=['sambit@ctsc-india.org','contact@hackforchange.co.in'] 
        message = "{0} has sent you a new message:\n\n{1} and his email is {2}".format(sender_name, data['message'],sender_email)
        #content =data[message]
        #send_mail(subject,content,From_mail,to_list,fail_silently=False)
        #send_mail('New Enquiry', message, sender_email,to_list)
        send_mail('New Enquiry', message,sender_email,to_list)
        return render(request, 'HFC/thanks.html',{'text':text})
class DonateView(View):
    def get(self,request):
        return render(request,'HFC/donate.html')

class CommunityMemberSignup(View):
    def get(self,request):
        form=Community_member_form()
        contributors = Community_Member.objects.filter(type  ='Contributor')
        return render(request,'HFC/community_member.html',{'form':form,'contributors':contributors}) 
    def post(self,request):
        form=Chapter_contributor_form(request.POST)
        #community_org=Community_Organization.objects.get(organization_name_slug=hfc_chapter_slug)
        print(request.POST)
        print(form.is_valid())
        text = "Thanks for signing up as a community member."
        if form.is_valid():
            #form.save()
            area_of_expertise=request.POST.getlist('area_of_expertise')
            city = request.POST.get('city')
            print(city)
            community_org = Community_Organization.objects.get(city=city)
            print(community_org)
            contributor=form.save(commit=False)
            contributor.type="Contributor"
            contributor.organization_id=community_org
            contributor.save()
            form.save_m2m()
            email=contributor.email
            print(email)
            try:
                #screeninglink_mail(email)
                #print("Screening email not send for now")
                message = "A new community member signed up to {0} chapter".format(community_org.organization_name)
                to_list=['team@hackforchange.co.in',]
                send_mail('New signup ', message,'Hack for change<noreply@hackforchange.co.in>',to_list)
            except:
                print('Error in sending email screening link to Contributor')
            return render(request, 'HFC/thanks.html',{'text':text})



