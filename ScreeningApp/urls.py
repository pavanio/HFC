from django.urls import path
from ScreeningApp  import views


urlpatterns = [
	path('screenings/<screening_uuid>',views.screening,name='screening'),




]