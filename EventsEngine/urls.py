from django.urls import path
#from .views import *
from EventsEngine import views
from django.conf.urls import include
from django.http import HttpResponse
from django.contrib import admin
#from .feeds import LatestBlogEntries
handler404 = 'HFCCore.views.error_404'
handler500 = 'HFCCore.views.error_500'

#app_name="EventsEngine"
urlpatterns = [
    path('ongoing-events/',views.EventList.as_view(),name='events'),
    path('ongoing-events/<title_slug>',views.EventDetailView.as_view(),name = 'event_detail'),
    path('ongoing-events/<title_slug>/signup',views.EventSignUpView.as_view(),name = 'event_sign_up'),


]
