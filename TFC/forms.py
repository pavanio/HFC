from django import forms
from django.forms import ModelForm
from .models import *

class OrganizationSignupForm(ModelForm):
    
    class Meta:
        model=Organization
        fields=['name','website','partner_desc','phone_number','email','address' ,'city','state','zip_code',
        'upi_id','logo']
        success_url = 'organization_list'
        """widgets = {
            'password': forms.PasswordInput(),
        }"""


class TeamMemberSignupForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Team_Member
        fields=['member_email','password']
        success_url='organization_list'
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(ModelForm):
     password = forms.CharField(widget=forms.PasswordInput)
     class Meta:
         model=Team_Member
         fields=['member_email','password']
         widgets = {
            'password': forms.PasswordInput(),
        }
class VolunteerForm(ModelForm):
    class Meta:
        model=Volunteer
        fields=('__all__')
        exclude=('level_of_expertise','area_of_expertise')

class MemberCreateForm(ModelForm):
    class Meta:
        model=Team_Member
        fields=['member_name','member_email','member_phone_number']