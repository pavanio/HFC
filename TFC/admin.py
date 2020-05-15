from django.contrib import admin
from .models import *

class Team_MemberInline(admin.TabularInline):
	model = Team_Member
	
	exclude=['password',]
	extra=0
	readonly_fields=('auth_token',)
	
	
	
	

class OrganizationAdmin(admin.ModelAdmin):
	list_display = ('name','website','partner_desc','phone_number','email','logo','address','city','state','zip_code','subdomain','thankyou_template','upi_id')
	inlines =[Team_MemberInline]
	class meta:
		model=Organization
admin.site.register(Organization,OrganizationAdmin)


class Team_MemberAdmin(admin.ModelAdmin):
	readonly_fields=('organization',)
	list_display=('organization','member_name','member_email','member_phone_number','role')
	
	exclude=['password',]
	class meta:
		model=Team_Member
admin.site.register(Team_Member,Team_MemberAdmin)

class VolunteerAdmin(admin.ModelAdmin):
	list_display=('name','email','contact_number','dob','gender','highest_education','availability','current_occupation','years_of_experience','profession')
	exclude=['level_of_expertise','area_of_expertise']
	class meta:
		model=Volunteer
admin.site.register(Volunteer,VolunteerAdmin)