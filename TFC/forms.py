from django import forms
from django.forms import ModelForm
from .models import *
from ScreeningApp.models import *

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
    field_order=['name','email','contact_number','dob','gender','highest_education','availability','current_occupation',
        'years_of_experience','profession','area_of_expertise']
    class Meta:
        model=Volunteer
        #fields=('__all__')
        exclude=('level_of_expertise','organization')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['profession'].queryset
        #self.fields['area_of_expertise'].widget = forms.CheckboxSelectMultiple()
        #self.fields['area_of_expertise'].queryset=Expertise.objects.all()

class MemberCreateForm(ModelForm):
    class Meta:
        model=Team_Member
        fields=['member_name','member_email','member_phone_number']