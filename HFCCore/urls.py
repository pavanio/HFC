from django.urls import path
from HFCCore import views
from django.conf.urls import include

#app_name="HFCCore"
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('problem-statements', views.ProblemStatementsView.as_view(), name='problem_statements'),
    path('problem-statements/<title_slug>', views.ProblemDiscriptionView.as_view(), name='problem_discription'),
    path('problem-Statements/<issue_area_slug>', views.ProblemsWithIssueareaView.as_view(), name='problem_statements_with_issuearea'),
    path('mentor/signup', views.MentorSignup.as_view(), name='mentor_signup'),
    path('contributor/signup', views.CenterContributorSignup.as_view(), name='contributor_signup'),
    path('<hfc_chapter>/signup', views.ChapterContributorSignup.as_view(), name='chapter_signup'),
    path('ajax/load-expertise',views.load_area_of_expertise,name='load_area_of_expertise'),
    path('thanks',views.thanks,name='thanks'),
    path('problem-statements-submit', views.ProblemStatementsSubmitView.as_view(), name='problem_statements_submit'),
    

    path('projects', views.ProjectsView.as_view(), name='projects'),
    path('community', views.CommunityView.as_view(), name='community'),
    path('', include('ScreeningApp.urls')),
]