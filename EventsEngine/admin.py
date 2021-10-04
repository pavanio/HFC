from django.contrib import admin

from .models import Events, EventType

from django_summernote.admin import SummernoteModelAdmin


class Events_Admin(SummernoteModelAdmin):
	list_display = ( 'title','title_slug', 'start_date', 'end_date', 'description', 'agenda','status','email_confirmation' ,'registration' )
	summernote_fields = ('description', 'agenda','email_confirmation')
    
	class meta:
		model = Events

admin.site.register(Events,Events_Admin)

admin.site.register(EventType)


  