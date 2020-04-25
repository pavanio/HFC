from django.urls import path
from ScreeningApp  import views


urlpatterns = [
	path('screenings/<screening_uuid>',views.screening,name='screening'),
	path('screenings/screening_preview/<screening_uuid>',views.screening_preview,name='screening_preview'),
	path('screenings/screening_preview_submit/<screening_uuid>',views.screening_preview_submit,name='screening_preview_submit')




]