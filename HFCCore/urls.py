from django.urls import path
from HFCCore import views
from django.conf.urls import include
from django.http import HttpResponse

#app_name="HFCCore"
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('problem-statements', views.ProblemStatementsView.as_view(), name='problem_statements'),
    path('problem-statements/<title_slug>', views.ProblemDiscriptionView.as_view(), name='problem_discription'),
    path('problem-statements/issue-area/<issue_area_slug>', views.ProblemsWithIssueareaView.as_view(), name='problem_statements_with_issuearea'),
    path('mentor/signup', views.MentorSignup.as_view(), name='mentor_signup'),
    path('center/<hfc_center_slug>/signup', views.CenterContributorSignup.as_view(), name='center_signup'),
    path('community/signup', views.CommunityMemberSignup.as_view(), name='community_member_signup'),
    path('<hfc_chapter_slug>/signup', views.ChapterContributorSignup.as_view(), name='chapter_signup'),
    path('ajax/load-expertise',views.load_area_of_expertise,name='load_area_of_expertise'),
    path('thanks',views.thanks,name='thanks'),
    path('problem-statement/suggest', views.ProblemStatementsSubmitView.as_view(), name='problem_statements_submit'),
    path('projects', views.ProjectsView.as_view(), name='projects'),
    path('community', views.CommunityView.as_view(), name='community'),
    path('about',views.AboutView.as_view(),name='about'),
    path('privacy-policy',views.PrivacyPolicyView.as_view(),name = 'privacy'),
    path('terms-conditions',views.TermsAndConditionView.as_view(),name = 'terms_conditions'),
    path('contact',views.ContactView.as_view(),name = 'contact'),
    path('donate',views.DonateView.as_view(),name = 'donate'),
    path('blog/',include('andablog.urls',namespace='andablog')),
    path('robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file"),
    path('', include('ScreeningApp.urls')),
]
