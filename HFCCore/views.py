from django.shortcuts import render
from django.views import View, generic
from .models import Problem_Statement, Partner, Project, Community_Organization, Community_Member
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
        return render(request, 'HFC/problem_discription.html', {'problem': problem, 'focus_areas': focus_areas, 'partner':partner})

class ProjectsView(generic.ListView):
    def get(self, request):
        projects_list = Project.objects.all()
        problem_statements=Problem_Statement.objects.all()
        return render(request, 'HFC/projects_list.html', {'projects_list':projects_list, 'problem_statements':problem_statements})

class CommunityView(View):
    def get(self, request):
        hfc_centers=Community_Organization.objects.filter(type='Center')
        hfc_chapters=Community_Organization.objects.filter(type='Chapter')
        centre_count = {}
        chapter_count = []
        for centre in hfc_centers:
            print(centre.community_member_set.count())
            print("'''''''''''''''''''''''''''")
            centre_count[centre.organization_name]=centre.community_member_set.count()
            print(centre_count)
            #centre_count = centre_count.count()
        print("<<<<<<<<<<<<<<<<<<")
        print(centre_count)
        for chapter in hfc_chapters:
            print(chapter.community_member_set.count())
            print("LLLLLLLLLLLLLLLLLLLLLLLLLL")
        mentors_list = Community_Member.objects.filter(type='Mentor')
        contributors_list = Community_Member.objects.filter(type='Contributor')
        return render(request, 'HFC/community.html', {'hfc_centers': hfc_centers, 'hfc_chapters': hfc_chapters, 'centre_count': centre_count, 'mentors_list': mentors_list, 'contributors_list':contributors_list})
