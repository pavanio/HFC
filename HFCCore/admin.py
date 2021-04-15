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

class Issue_Area_Admin(admin.ModelAdmin):
	list_display = ('issue_area','issue_area_slug')
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

class Problem_StatementAdmin(admin.ModelAdmin):
	list_display = ('title', 'summary', 'background_info', 'related_link','partner_id', 'status','issuearea','title_slug')
	class Meta:
		model = Problem_Statement

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'project_link', 'project_icon', 'project_desc', 'website_link', 'goal', 'funded_by')
	class Meta:
		model = Project

class Community_MemberInline(admin.TabularInline):
	model = Community_Member
	extra = 0

class Community_OrganizationAdmin(admin.ModelAdmin):
	list_display = ('organization_name', 'type', 'website', 'logo', 'coordinator_name', 'coordinator_email', 'coordinator_mobile','organization_name_slug','get_project','city')
	inlines = [Community_MemberInline]
	class Meta:
		model = Community_Organization

class Community_MemberAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'level_of_expertise', 'areaofexpertise', 'type', 'coder_profile', 'linkedin_profile','image', 'organization_id','commit','get_project')
	actions = ['send_email','send_screening_invitation',]
	list_filter = ('type',)
	class Meta:
		model = Community_Member
	def send_screening_invitation(self, request, queryset):
		for profile in queryset:
			screeninglink_mail(profile.email)
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
