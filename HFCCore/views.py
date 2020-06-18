from django.shortcuts import render
from django.views import View, generic
from .models import Problem_Statement
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request,'HFC/hfc_home.html')

class ProblemStatementsView(generic.ListView):
    def get(self, request):
        problems_list = Problem_Statement.objects.all()
        return render(request, 'HFC/problem_statements.html', {'problems_list': problems_list})

class ProblemsWithIssueareaView(generic.ListView):
    def get(self, request, issue_area):
        problems_list = Problem_Statement.objects.filter(issue_area=issue_area)
        return render(request, 'HFC/problem_statements.html', {'problems_list': problems_list})

class ProblemDiscriptionView(View):
    def get(self, request, title):
        problem = Problem_Statement.objects.get(title=title)
        return render(request, 'HFC/problem_discription.html', {'problem': problem})