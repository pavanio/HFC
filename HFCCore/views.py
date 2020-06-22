from django.shortcuts import render
from django.views import View, generic
from .models import Problem_Statement, Partner
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