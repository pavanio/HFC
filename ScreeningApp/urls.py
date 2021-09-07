from django.urls import path
from ScreeningApp  import views

urlpatterns = [
	path('screenings/<screening_uuid>/',views.Screening.as_view(),name='screening'),
	path('screenings/<screening_uuid>/screening-preview/',views.Screening_Preview.as_view(),name='screening_preview'),
	path('screenings/<screening_uuid>/result/',views.Result.as_view(),name='result'),
	path('screenings/<screening_uuid>/result/feedback/',views.Feedback.as_view(),name='feedback'),

]
