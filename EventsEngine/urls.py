from django.urls import path
from .views import *
from EventsEngine import views
from django.conf.urls import include
from django.http import HttpResponse
from django.contrib import admin
#from .feeds import LatestBlogEntries
handler404 = 'HFCCore.views.error_404'
handler500 = 'HFCCore.views.error_500'

#app_name="EventsEngine"
urlpatterns = [
    path('events/',views.EventList.as_view(),name='events'),
    path('events/<title_slug>/',views.EventDetailView.as_view(),name = 'event_detail'),
    path('events/<title_slug>/signup/expired',views.EventSignUpExpiredView.as_view(),name = 'event_expired'),
    path('events/latest/feed/',EventFeed(), name='event-feed'),
    path('events/<title_slug>/signup',views.EventSignUpView.as_view(),name = 'event_sign_up'),
    #path('events/verify-user/',views.member_exist,name='member_exist'),
    path('events/thank-you/',views.event_signup_thanks,name='event-thank-you'),
    path('events/<title_slug>/google-signup',views.EventSignupWithGoogle.as_view(),name = 'event_google_sign_up'),


]
