from django.contrib import admin
from .models import *
from TFC.admin import Team_MemberInline
from .models import Community_Organization, Project, Problem_Statement, Community_Member
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from .forms import SendEmailForm
from django.shortcuts import render
from .views import screeninglink_mail
from django.contrib import messages
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe

class Issue_Area_Admin(SummernoteModelAdmin):
	list_display = ('issue_area','issue_sub_header','issue_brief','issue_overview','context','technology_intervention','related_information')
	summernote_fields = ('issue_brief','issue_overview','context','technology_intervention',)
	class meta:
		model = Issue_Area

class Problem_StatementInline(admin.TabularInline):
	model = Problem_Statement
	extra = 0

class PartnerAdmin(admin.ModelAdmin):
	list_display = ('name','website','partner_desc','phone_number','email','logo','address','city','state','zip_code','focus_area','subdomain','thankyou_template','upi_id')
	inlines = [Team_MemberInline, Problem_StatementInline]
	class meta:
		model = Partner

class Problem_StatementAdmin(SummernoteModelAdmin):
	list_display = ('problem_statement', 'overview', 'background_info','proposed_solution', 'related_link','partner_id', 'status','issuearea','title_slug')
	summernote_fields = ('overview', 'background_info', 'related_link','proposed_solution',)
	class Meta:
		model = Problem_Statement
	
class Project_PartnerInline(admin.TabularInline):
	model = Project_Partner
	extra = 0

class ProjectAdmin(SummernoteModelAdmin):
	list_display = ('name', 'project_link', 'project_icon', 'project_overview', 'website_link', 'goal','project_slug')
	summernote_fields = ('project_overview','goal')
	inlines = [Project_PartnerInline,]
	class Meta:
		model = Project

class Community_MemberInline(admin.TabularInline):
	model = Community_Member
	extra = 0

class Community_OrganizationAdmin(admin.ModelAdmin):
	list_display = ('organization_name', 'type', 'website', 'logo', 'coordinator_name', 'coordinator_email', 'coordinator_mobile','organization_name_slug','get_project','city','is_public')
	inlines = [Community_MemberInline]
	class Meta:
		model = Community_Organization

class Community_MemberAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'level_of_expertise', 'areaofexpertise', 'type', 'coder_profile', 'linkedin_profile','image', 'organization_id','commit','get_project','get_event')
	actions = ['send_email','send_screening_invitation',]
	list_filter = ('type','event')
	class Meta:
		model = Community_Member
	def send_screening_invitation(self, request, queryset):
		for profile in queryset:
			try:
				screeninglink_mail(profile.email)
				messages.success(request,"Email send successfully")
			except:
				messages.error(request,"Email sending failed")
	send_screening_invitation.short_description = "Send screening invitation"
	def send_email(self, request, queryset):
		form = SendEmailForm(initial = {'users': queryset})
		return render(request, 'HFC/admin_email_form.html', {'form': form})
	send_email.short_description = "Send email"


	

admin.site.register(Partner,PartnerAdmin)
admin.site.register(Problem_Statement, Problem_StatementAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Community_Organization, Community_OrganizationAdmin)
admin.site.register(Community_Member, Community_MemberAdmin)
admin.site.register(Issue_Area,Issue_Area_Admin)
#admin.site.register(Project_Partner,Project_PartnerAdmin)
