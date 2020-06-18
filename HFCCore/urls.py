from django.urls import path
from HFCCore import views

app_name="HFCCore"
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('problem-statements', views.ProblemStatementsView.as_view(), name='problem_statements'),
    path('problem-discription/<title>', views.ProblemDiscriptionView.as_view(), name='problem_discription'),
    path('problem-Statements/<issue_area>', views.ProblemsWithIssueareaView.as_view(), name='problem_statements_with_issuearea')
]