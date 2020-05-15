from django.contrib import admin
from .models import *
from TFC.admin import Team_MemberInline
from .models import Community_Organization, Project, Problem_Statement

class PartnerAdmin(admin.ModelAdmin):
	list_display = ('name','website','partner_desc','phone_number','email','logo','address','city','state','zip_code','subdomain','thankyou_template','upi_id')
	inlines =[Team_MemberInline]
	class meta:
		model=Partner

class Problem_StatementAdmin(admin.ModelAdmin):
	list_display = ('title', 'summary', 'background_info', 'related_link', 'proposed_solution', 'partner_id', 'status')
	class Meta:
		model= Problem_Statement

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'project_link', 'project_icon', 'project_desc', 'website_link', 'goal', 'funded_by')
	class Meta:
		model = Project

class Community_OrganizationAdmin(admin.ModelAdmin):
	list_display = ('organization_name', 'type', 'website', 'logo', 'coordinator_name', 'coordinator_email', 'coordinator_mobile')
	class Meta:
		model = Community_Organization

admin.site.register(Partner,PartnerAdmin)
admin.site.register(Problem_Statement, Problem_StatementAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Community_Organization, Community_OrganizationAdmin)


