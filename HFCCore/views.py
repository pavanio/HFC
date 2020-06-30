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
# Create your views here.
def screeninglink_mail(email):
    candidate=Candidate.objects.get(email=email)
    name=candidate.name
    screening=Screenings.objects.create(candidate_id=candidate)
    screeninguuid=screening.screening_uuid
    print(screeninguuid)
    email=candidate.email
    from_email=settings.EMAIL_HOST_USER
    to=[email]
    subject="Screening Link"
    msg = MIMEMultipart('alternative')
    html_content = render_to_string('TFC/email.html', {'screeninguuid':screeninguuid,'name':name})
    msg = EmailMultiAlternatives(subject, html_content, from_email , [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=True)
def thanks(request):
    return render(request,'HFC/thanks.html')
class Home(View):
    def get(self, request):
        return render(request,'HFC/hfc_home.html')

class ProblemStatementsView(generic.ListView):
    def get(self, request):
        problems_list = Problem_Statement.objects.all()
        return render(request, 'HFC/problem_statements.html', {'problems_list': problems_list})

class ProblemsWithIssueareaView(generic.ListView):
    def get(self, request, issue_area_slug):
        problems_list = Problem_Statement.objects.filter(issue_area_slug=issue_area_slug)
        all_problems = Problem_Statement.objects.all()
        return render(request, 'HFC/problem_statements_with_issue_area.html', {'problems_list': problems_list, 'all_problems': all_problems})

class ProblemDiscriptionView(View):
    def get(self, request, title_slug):
        problem = Problem_Statement.objects.get(title_slug=title_slug)
        print(problem.partner_id)
        partner = Partner.objects.get(name=problem.partner_id)
        focus_areas = partner.focus_area.split(',')
        return render(request, 'HFC/problem_discription.html', {'problem': problem, 'focus_areas': focus_areas})

def load_area_of_expertise(request):
    expertise_area_id = request.GET.get('profession')
    print(expertise_area_id)
    expertises=Expertise.objects.filter(category_of_expertise=expertise_area_id)
    print(expertises)
    return render(request,'TFC/areaofexpertise.html',{'expertises':expertises})

class MentorSignup(View):
    def get(self,request):
        form=Mentor_form()
        return render(request,'HFC/mentor_signup.html',{'form':form})
    def post(self,request):
        form=Mentor_form(request.POST)
        print(request.POST)
        if form.is_valid():
            #form.save()
            area_of_expertise=request.POST.getlist('area_of_expertise')
            mentor=form.save(commit=False)
            mentor.type="Mentor"
            mentor.save()
            form.save_m2m()
            email=mentor.email
            print(email)
            try:
                screeninglink_mail(email)
            except:
                print('Error in sending email screening link to Mentor')
            #messages.success(request,"Volunteer Registration Form Submitted Successfully")
            return redirect('thanks')
class CenterContributorSignup(View):
    def get(self,request):
        form=Center_contributor_form()
        return render(request,'HFC/center_contributor_signup.html',{'form':form}) 
    def post(self,request):
        form=Center_contributor_form(request.POST)
        print(request.POST)
        if form.is_valid():
            #form.save()
            area_of_expertise=request.POST.getlist('area_of_expertise')
            contributor=form.save(commit=False)
            contributor.type="Contributor"
            contributor.save()
            form.save_m2m()
            email=contributor.email
            print(email)
            try:
                screeninglink_mail(email)
            except:
                print('Error in sending email screening link to Contributor')
            #messages.success(request,"Volunteer Registration Form Submitted Successfully")
            return redirect('thanks')


