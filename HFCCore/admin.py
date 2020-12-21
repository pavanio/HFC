from django.contrib import admin
from .models import *
from TFC.admin import Team_MemberInline
from .models import Community_Organization, Project, Problem_Statement, Community_Member

class Issue_Area_Admin(admin.ModelAdmin):
	list_display = ('issue_area','issue_area_slug')
	class meta:
		model=Issue_Area
class Problem_StatementInline(admin.TabularInline):
	model = Problem_Statement
	extra=0
class PartnerAdmin(admin.ModelAdmin):
	list_display = ('name','website','partner_desc','phone_number','email','logo','address','city','state','zip_code','focus_area','subdomain','thankyou_template','upi_id')
	inlines =[Team_MemberInline, Problem_StatementInline]
	class meta:
		model=Partner

class Problem_StatementAdmin(admin.ModelAdmin):
	list_display = ('title', 'summary', 'background_info', 'related_link','partner_id', 'status','issuearea','title_slug')
	"""def has_module_permission(self, request):
		return False"""
	class Meta:
		model= Problem_Statement

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'project_link', 'project_icon', 'project_desc', 'website_link', 'goal', 'funded_by')
	class Meta:
		model = Project

class Community_MemberInline(admin.TabularInline):
	model = Community_Member
	extra=0

class Community_OrganizationAdmin(admin.ModelAdmin):
	list_display = ('organization_name', 'type', 'website', 'logo', 'coordinator_name', 'coordinator_email', 'coordinator_mobile','organization_name_slug')
	inlines = [Community_MemberInline]
	class Meta:
		model = Community_Organization

class Community_MemberAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'level_of_expertise', 'areaofexpertise', 'type', 'coder_profile', 'linkedin_profile','image', 'organization_id')
	#def has_module_permission(self, request):
		#return False
	class Meta:
		model = Community_Member


admin.site.register(Partner,PartnerAdmin)
admin.site.register(Problem_Statement, Problem_StatementAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Community_Organization, Community_OrganizationAdmin)
admin.site.register(Community_Member, Community_MemberAdmin)
admin.site.register(Issue_Area,Issue_Area_Admin)

