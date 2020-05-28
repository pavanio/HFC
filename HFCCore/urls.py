from django.urls import path
from HFCCore  import views


urlpatterns = [
    path('',views.Home.as_view(),name='home'),
]