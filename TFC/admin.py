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

#admin.site.register(Team_Member)

class VolunteerAdmin(admin.ModelAdmin):
	list_display=('name','email','mobile','age','gender','address','city','state','zip_code','education','availability','current_occupation','years_of_experience','profession')
	class meta:
		model=Volunteer
admin.site.register(Volunteer,VolunteerAdmin)