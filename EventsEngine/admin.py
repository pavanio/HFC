from django.contrib import admin
from .models import Events, EventType,Event_Speakers
from django_summernote.admin import SummernoteModelAdmin


class Event_SpeakerAdmin(admin.TabularInline):
	list_display = ('speaker','speaker_details')
	model = Event_Speakers

class Events_Admin(SummernoteModelAdmin):
	list_display = ( 'title','title_slug', 'start_date', 'end_date', 'description', 'agenda','status','total_seat','email_confirmation', )
	summernote_fields = ('description', 'agenda','email_confirmation')
	exclude = ['registration','created_on']
	inlines = [Event_SpeakerAdmin]
    
	class Meta:
		model = Events


admin.site.register(Events,Events_Admin)
admin.site.register(EventType)
#admin.site.register(Event_Speaker,Event_SpeakerAdmin)

