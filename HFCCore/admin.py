from django.contrib import admin
from .models import *
from TFC.admin import Team_MemberInline


class PartnerAdmin(admin.ModelAdmin):
	list_display = ('name','website','partner_desc','phone_number','email','logo','address','city','state','zip_code','subdomain','thankyou_template','upi_id')
	inlines =[Team_MemberInline]
	class meta:
		model=Partner
admin.site.register(Partner,PartnerAdmin)



