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
from .utils import SendSubscribeMail,mentor_signup_mail,community_member_signup_mail,job_screeninglink_mail
from django.views.generic.edit import FormView 
from django.urls import reverse_lazy
from blog.models import Post
from EventsEngine.models import Events
from collections import defaultdict
headers = {
    'Accept': 'application/vnd.github.v3+json',
}
#Entry = apps.get_model('andablog', 'Entry')
# Create your views here.
def load_area_of_expertise(request):
    expertise_area_id = request.GET.get('profession')
    expertises = Expertise.objects.filter(category_of_expertise = expertise_area_id,is_published = 'True')
    return render(request,'HFC/areaofexpertise.html',{'expertises':expertises})

def screeninglink_mail(email):
    base_url = settings.BASE_URL
    candidate = Candidate.objects.get(email = email)
    name = candidate.name
    screening = Screenings.objects.create(candidate_id = candidate)
    screeninguuid = screening.screening_uuid
    email = candidate.email
    from_email = 'HackForChange Team<noreply@hackforchange.co.in>'
    to_list = [email,]
    subject = "Thank you for joining HackForChange"
    headers = {'Reply-To': 'suman@hackforchange.co.in'}
    html_content = render_to_string('HFC/screening_email.html', {'screeninguuid':screeninguuid,'name':name,'base_url':base_url})
    msg = EmailMessage(subject, html_content, from_email ,to_list,headers = headers)
    msg.content_subtype = "html"
    msg.send(fail_silently = True)
    print("Mail sended successfully")

def thanks(request):
    return render(request,'HFC/thanks.html')

class Home(View):
    def get(self, request):
        blogs = Post.objects.filter(status = 'Published')[:3]
        return render(request,'HFC/hfc_home.html',{'blogs':blogs})

class ProblemStatementsView(generic.ListView):
    def get(self, request):
        problems_list = Problem_Statement.objects.all().exclude(status ='Draft')
        issue_areas = Issue_Area.objects.all()
        return render(request, 'HFC/problem_statements.html', {'problems_list': problems_list,'issue_areas':issue_areas})

class ProblemsWithIssueareaView(generic.ListView):
    def get(self, request, issue_area_slug):
        issue_area = Issue_Area.objects.get(issue_area_slug = issue_area_slug)
        problems_list = Problem_Statement.objects.filter(issue_area = issue_area)
        issue_areas = Issue_Area.objects.all()
        return render(request, 'HFC/problem_statements_with_issue_area.html', {'problems_list': problems_list,'issue_areas': issue_areas})

class ProblemDiscriptionView(View):
    def get(self, request, title_slug):
        problem = Problem_Statement.objects.get(title_slug = title_slug)
        try:
            partner = Partner.objects.get(name = problem.partner_id)
        except:
            print('No Partner for this problem statement')
            partner = ' '
        try:
            focus_areas = partner.focus_area.split(',')
        except:
            focus_areas = ' '
        issue_areas = Issue_Area.objects.all()
        return render(request, 'HFC/problem_discription.html', {'problem': problem, 'focus_areas': focus_areas,'issue_areas': issue_areas,'partner':partner})

class MentorSignup(View):
    def get(self,request):
        form = Mentor_form()
        mentors = Community_Member.objects.filter(type  = 'Mentor')[:6]
        return render(request,'HFC/mentor_signup.html',{'form':form,'mentors':mentors})
    def post(self,request):
        form = Mentor_form(request.POST)
        text = "Thanks for signing up as a Mentor"
        if form.is_valid():
            print(form.is_valid())
            area_of_expertise = request.POST.getlist('area_of_expertise')
            mentor=form.save(commit = False)
            mentor.type = "Mentor"
            mentor.save()
            form.save_m2m()
            email = mentor.email
            SendSubscribeMail(email)
            try:
                mentor_signup_mail(email)
                message = "A new Mentor signed up"
                to_list = ['',]
                send_mail('New signup ', message,'noreply@hackforchange.co.in',to_list)
            except:
                print('Error in sending  welcome email to Mentor')
            return render(request, 'HFC/thanks.html',{'text':text})

class CenterContributorSignup(View):
    def get(self,request,hfc_center_slug):
        form = Center_contributor_form()
        center = Community_Organization.objects.get(organization_name_slug = hfc_center_slug)
        contributors = Community_Member.objects.filter(type  = 'Contributor')
        return render(request,'HFC/center_contributor_signup.html',{'form':form,'contributors':contributors,'center':center}) 
    def post(self,request,hfc_center_slug):
        form = Center_contributor_form(request.POST)
        community_org = Community_Organization.objects.get(organization_name_slug = hfc_center_slug)
        print(form.is_valid())
        center_name = community_org.organization_name
        if form.is_valid():
            area_of_expertise = request.POST.getlist('area_of_expertise')
            contributor = form.save(commit = False)
            contributor.type = "Contributor"
            contributor.organization_id = community_org
            contributor.save()
            form.save_m2m()
            email = contributor.email
            SendSubscribeMail(email)
            try:
                screeninglink_mail(email)
                message = "A new contributor signed up to {0} center".format(community_org.organization_name)
                to_list = ['team@hackforchange.co.in',]
                send_mail('New signup ', message,'HackForChange Team<noreply@hackforchange.co.in',to_list)
            except:
                print('Error in sending email screening link to Contributor')
            return render(request, 'HFC/center_signup_thanks.html',{'center_name':center_name})

class ChapterContributorSignup(View):
    def get(self,request,hfc_chapter_slug):
        form = Chapter_contributor_form()
        chapter = Community_Organization.objects.get(organization_name_slug = hfc_chapter_slug)
        contributors = Community_Member.objects.filter(type  = 'Contributor')
        return render(request,'HFC/chapter_contributor_signup.html',{'form':form,'chapter':chapter,'contributors':contributors}) 
    def post(self,request,hfc_chapter_slug):
        form = Chapter_contributor_form(request.POST)
        community_org = Community_Organization.objects.get(organization_name_slug = hfc_chapter_slug)
        print(form.is_valid())
        chapter_name = community_org.organization_name
        if form.is_valid():
            area_of_expertise = request.POST.getlist('area_of_expertise')
            contributor = form.save(commit = False)
            contributor.type = "Contributor"
            contributor.organization_id = community_org
            contributor.save()
            form.save_m2m()
            email = contributor.email
            SendSubscribeMail(email)
            try:
                screeninglink_mail(email)
                message = "A new contributor signed up to {0} chapter".format(community_org.organization_name)
                to_list=['',]
                send_mail('New signup ', message,'HackForChange Team<noreply@hackforchange.co.in>',to_list)
            except:
                print('Error in sending email screening link to Contributor')
            return render(request, 'HFC/chapter_signup_thanks.html',{'chapter_name':chapter_name})

class Center(View):
    def get(self,request,hfc_center_slug):
        center = Community_Organization.objects.filter(organization_name_slug = hfc_center_slug).first()
        contributors = Community_Member.objects.filter(type  = 'Contributor')
        contributors_list = Community_Member.objects.filter(type='Contributor').order_by('-commit')
        return render(request, 'HFC/community_center.html',{'center': center,'contributors':contributors,'contributors_list':contributors_list})

class Chapter(View):
    def get(self,request,hfc_chapter_slug):
        chapter = Community_Organization.objects.filter(organization_name_slug = hfc_chapter_slug).first()
        contributors = Community_Member.objects.filter(type  = 'Contributor')
        contributors_list = Community_Member.objects.filter(type='Contributor').order_by('-commit')
        return render(request, 'HFC/community_chapter.html',{'chapter': chapter,'contributors':contributors,'contributors_list':contributors_list})    

class ProjectsView(generic.ListView):
    def get(self, request):
        projects_list = Project.objects.all()
        issue_areas = Issue_Area.objects.all()
        partners = Partner.objects.all()
        project_partner = Project_Partner.objects.all()
        funding_partner ={}
        community_partner = defaultdict(list)
        for proj in projects_list:
            fund_partner = Project_Partner.objects.filter(project_id = proj.id,project_involvement = 'Funding')
            social_partner = Project_Partner.objects.filter(project_id = proj.id ).exclude(project_involvement = 'Funding')
            for item in fund_partner:
                for obj in item.partner.all():
                    funding_partner[proj] = obj
            for item in social_partner:
                for obj in item.partner.all():
                    community_partner[proj].append(obj)
        print(funding_partner)
        print(community_partner)
        #project_zip = zip(projects_list,funding_partner,community_partner)
        return render(request, 'HFC/projects_list.html', {'issue_areas': issue_areas,'partners':partners,'projects_list':projects_list,'funding_partner':funding_partner,'community_partner':community_partner })

class ProjectDetailView(View):
    def get(self, request, project_slug):
        project = Project.objects.get(project_slug = project_slug)
        print(project.id)
        funding = Project_Partner.objects.filter(project_id = project.id,project_involvement = 'Funding')
        """for item in funding:
            partner = item.partner.all()
        for itm in partner:
            #partner_detail = Partner.objects.get(org_id = itm)
            print(itm.email)"""
        #partner_fund = funding.partner.all()
        #print(partner_fund)
        community_partners = Project_Partner.objects.filter(project_id = project.id ).exclude(project_involvement = 'Funding')
        """print(community_partners)
        for item in community_partners:
            partner = item.partner.all()"""
        
        issue_areas = Issue_Area.objects.all()
        #partners = {'funding':funding,'community_partners':community_partners,}
        contributors = Community_Member.objects.filter(type='Contributor')
        return render(request, 'HFC/project_detail.html', {'project':project,'issue_areas': issue_areas,'funding':funding,'community_partners':community_partners,'contributors':contributors})


class CommunityView(View):
    def get(self, request):
        hfc_centers = Community_Organization.objects.filter(type = 'Center',is_public = 'True')
        hfc_chapters = Community_Organization.objects.filter(type = 'Chapter',is_public = 'True')
        centre_count = {}
        chapter_count = []
        for centre in hfc_centers:
            print(centre.community_member_set.count())
            centre_count[centre.organization_name] = centre.community_member_set.count()
        print(centre_count)
        for chapter in hfc_chapters:
            print(chapter.community_member_set.count())
        mentors_list = Community_Member.objects.filter(type = 'Mentor')
        contributors_list = Community_Member.objects.filter(type='Contributor').order_by('-commit')
        return render(request, 'HFC/community.html', {'hfc_centers': hfc_centers, 'hfc_chapters': hfc_chapters, 'centre_count': centre_count, 'mentors_list': mentors_list, 'contributors_list':contributors_list})

class ProblemStatementsSubmitView(View):
    def get(self,request):
        form = Problem_Statement_form()
        issue_areas = Issue_Area.objects.all()
        return render(request,'HFC/problem_statements_submit.html',{'form':form,'issue_areas': issue_areas})
    def post(self,request):
        form = Problem_Statement_form(request.POST)
        print(request.POST)
        text="Thanks for submitting the problem statement."
        if form.is_valid():
            problem = form.save(commit = False)
            problem.status = "Draft"
            issue_areas = Issue_Area.objects.all()
            email = problem.email
            SendSubscribeMail(email)
            form.save()
            try:
                html_content = render_to_string('HFC/problem_statement_detail_internal_email.html', {'problem':problem,'issue_area': issue_areas})
                to_list=['team@hackforchange.co.in',]
                msg = EmailMessage('New Problem Statement Submission', html_content,'HackForChange Team<noreply@hackforchange.co.in>' ,to_list,)
                msg.content_subtype = "html"
                msg.send(fail_silently = True)
                print("Problem Submission email sent successfully")
            except:
                print('Error in sending notification email to HFC Team')
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
        sender_name = data['name']
        sender_email = data['email']
        subject = "New contact us  message"
        to_list = ['contact@hackforchange.co.in',] 
        message = "{0} has sent you a new message:\n\n{1} and his email is {2}".format(sender_name, data['message'],sender_email)
        send_mail('New Enquiry', message,sender_email,to_list)
        return render(request, 'HFC/contact_thanks.html')
        
class DonateView(View):
    def get(self,request):
        return render(request,'HFC/donate.html')

class CommunityMemberSignup(View):
    def get(self,request):
        form = Community_member_form()
        contributors = Community_Member.objects.filter(type  = 'Contributor')
        return render(request,'HFC/community_member.html',{'form':form,'contributors':contributors}) 
    def post(self,request):
        form = Chapter_contributor_form(request.POST)
        #community_org=Community_Organization.objects.get(organization_name_slug=hfc_chapter_slug)
        print(form.is_valid())
        if form.is_valid():
            area_of_expertise = request.POST.getlist('area_of_expertise')
            city = request.POST.get('city')
            community_org = Community_Organization.objects.get(city = city)
            print(community_org)
            contributor = form.save(commit = False)
            contributor.type = "Contributor"
            contributor.organization_id = community_org
            contributor.save()
            form.save_m2m()
            email = contributor.email
            SendSubscribeMail(email)
            try:
                community_member_signup_mail(email)
                html_content = render_to_string('HFC/community_member_detail_internal_email.html', {'contributor':contributor})
                to_list=['team@hackforchange.co.in',]
                msg = EmailMessage('New community member signup', html_content,'HackForChange Team<noreply@hackforchange.co.in>' ,to_list,)
                msg.content_subtype = "html"
                msg.send(fail_silently = True)
                print("Community member details email sended successfully")
            except:
                print('Error in sending welcome email to community member')
            return render(request, 'HFC/community_signup_thanks.html')

class SendUserEmails(FormView):
    template_name = 'HFC/admin_email_form.html'
    form_class = SendEmailForm
    success_url = reverse_lazy('admin:HFCCore_community_member_changelist')
    def form_valid(self, form):
        users = form.cleaned_data['users']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = 'HackForChange Team<noreply@hackforchange.co.in>'
        headers = {'Reply-To': 'suman@hackforchange.co.in'}
        for user in users:
            msg = MIMEMultipart('alternative')
            html_content = render_to_string('HFC/invitation_email.html', {'message':message,'name':user.name})
            msg = EmailMessage(subject, html_content, from_email ,[user.email,],headers = headers)
            msg.content_subtype = "html"
            msg.send(fail_silently = True)
        return super(SendUserEmails, self).form_valid(form)

def admin_redirect(request):
    return redirect(settings.ADMIN_LINK)

def error_404(request,exception):
        data = {}
        return render(request,'HFC/404.html', data)

def error_500(request,*args, **argv):
        data = {}
        return render(request,'HFC/500.html', data)


class IssueAreaView(View):
    def get(self, request, issue_area_slug):
        issue = Issue_Area.objects.get(issue_area_slug = issue_area_slug)
        issue_areas = Issue_Area.objects.all()
        problem_statement_list = Problem_Statement.objects.filter(issue_area = issue)
        partners = set()
        for problem in problem_statement_list:
            try:
                partner = Partner.objects.get(name = problem.partner_id)
                partners.add(partner)
                print(partner.logo)
            except:
                continue
        return render(request, 'HFC/issue_area_detail.html', {'issue':issue,'issue_areas': issue_areas,'problem_statement_list':problem_statement_list,'partners':partners})

class IssueAreaListView(View):
    def get(self, request):
        issue_areas = Issue_Area.objects.all()
        return render(request, 'HFC/issue_area.html', {'issue_areas':issue_areas})

class JobView(View):
    def get(self, request):
        form = Job_Application_form()
        partners = Partner.objects.all()
        return render(request,'HFC/job_application.html',{'form':form,'partners': partners})
    def post(self,request,*args, **kwargs):
        form = Chapter_contributor_form(request.POST)
        #community_org = Community_Organization.objects.get(organization_name_slug = hfc_chapter_slug)
        print(form.is_valid())
        #print(request.POST)
        #chapter_name = community_org.organization_name
        if form.is_valid():
            area_of_expertise = request.POST.getlist('area_of_expertise')
            #city = request.POST.get('city')
            applicant = form.save(commit = False)
            applicant.type = "Contributor"
            #contributor.organization_id = community_org
            applicant.save()
            form.save_m2m()
            email = applicant.email
            SendSubscribeMail(email)
            try:
                job_screeninglink_mail(email)
                html_content = render_to_string('HFC/applicant_detail_internal_email.html', {'applicant':applicant})
                to_list=['team@hackforchange.co.in',]
                msg = EmailMessage('New Job Applicant', html_content,'HackForChange Team<noreply@hackforchange.co.in>' ,to_list,)
                msg.content_subtype = "html"
                msg.send(fail_silently = True)
                print("Applicant details email sended successfully")
                #send_mail('New Job Applicant ', message,'HackForChange Team<noreply@hackforchange.co.in>',to_list)
            except:
                print('Error in sending email screening link to job applicant')
            return render(request, 'HFC/job_application_thanks.html')
    



