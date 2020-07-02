from django.shortcuts import render
from django.http import HttpResponse
from django.views import View, generic
from .models import Problem_Statement, Partner
from .forms import Mentor_form,Problem_Statement_form
# Create your views here.
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
class ProblemStatementsSubmitView(View):
    def get(self,request):
        form=Problem_Statement_form()
        return render(request,'HFC/problem_statements_submit.html',{'form':form})
    def post(self,request):
        form=Problem_Statement_form(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,"Problem Statement Form Submitted Successfully")
            return HttpResponse('thanks')
       
def load_area_of_expertise(request):
    expertise_area_id = request.GET.get('profession')
    print(expertise_area_id)
    expertises=Expertise.objects.filter(category_of_expertise=expertise_area_id)
    print(expertises)
    return render(request,'TFC/areaofexpertise.html',{'expertises':expertises})

class MentorSignup(View):
    def get(self,request):
        # subdomain=subdomaincheck(request)
        # org=Organization.objects.get(subdomain=subdomain)
        form=Mentor_form()
        #print(form)
        return render(request,'HFC/mentor_signup.html',{'form':form})
    def post(self,request):
        form=Mentor_form(request.POST)
        print(request.POST)
        if form.is_valid():
            # subdomain=subdomaincheck(request)
            # org=Organization.objects.get(subdomain=subdomain)
            area_of_expertise=request.POST.getlist('area_of_expertise')
            
            vol=form.save(commit=False)
            # vol.organization=org
            vol.save()
            form.save_m2m()
            email=vol.email
            # screeninglink_mail(email,org,subdomain)
            print(vol.email)           
            messages.success(request,"Volunteer Registration Form Submitted Successfully")            
            return redirect('thanks')