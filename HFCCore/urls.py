from django.urls import path
from HFCCore import views

#app_name="HFCCore"
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('problem-statements', views.ProblemStatementsView.as_view(), name='problem_statements'),
    path('problem-statements/<title_slug>', views.ProblemDiscriptionView.as_view(), name='problem_discription'),
    path('problem-Statements/<issue_area_slug>', views.ProblemsWithIssueareaView.as_view(), name='problem_statements_with_issuearea'),
    path('projects', views.ProjectsView.as_view(), name='projects'),
    path('community', views.CommunityView.as_view(), name='community')
]