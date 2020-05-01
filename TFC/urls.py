from django.urls import path
from TFC  import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('organizations',views.OrganizationListView.as_view(),name='organization_list'),
    path('organizations/signup',views.OrganizationCreateView.as_view(),name='organization signup',),
]