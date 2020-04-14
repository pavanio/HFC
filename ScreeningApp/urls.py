from django.urls import path
from ScreeningApp  import views


urlpatterns = [
	path('screening/<screening_uuid>',views.screening,name='screening'),




]