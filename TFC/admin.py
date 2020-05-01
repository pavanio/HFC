from django.contrib import admin
from .models import *

class Team_MemberInline(admin.TabularInline):
	model = Team_Member
	exclude=['password']
	extra=0
	

class OrganizationAdmin(admin.ModelAdmin):
	list_display = ('name','website','partner_desc','phone_number','email','logo','address','city','state','zip_code','subdomain','thankyou_template','upi_id')
	inlines =[Team_MemberInline]
	class meta:
		model=Organization
admin.site.register(Organization,OrganizationAdmin)

