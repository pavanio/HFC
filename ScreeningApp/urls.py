from django.urls import path
from ScreeningApp  import views

urlpatterns = [
	path('screenings/<screening_uuid>/',views.screening,name='screening'),
	path('screenings/<screening_uuid>/screening-preview/',views.screening_preview,name='screening_preview'),
	path('screenings/<screening_uuid>/result/',views.result,name='result')

]
