from django.urls import path
from django.conf.urls import include
from .views import *

urlpatterns = [
    path('editor/', include('django_summernote.urls')),
    path('',PostList.as_view(), name='blog'),
    path('latest/feed/',BlogFeed(), name='blog-feed'),
    path('<slug:title_slug>',PostDetail.as_view(), name='blog-detail'),
    

]
