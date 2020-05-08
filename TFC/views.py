from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic import CreateView,ListView
from TFC.models import *
from django.urls import reverse_lazy,reverse
from .forms import *
from django.http import Http404
from django.contrib.auth.hashers import make_password
from django.contrib.sites.models import Site
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate
import django.contrib.auth
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout as auth_logout


def subdomaincheck(request):
    request.subdomain = None
    host = request.META.get('HTTP_HOST', '')
    host_s = host.replace('www.', '').split('.')
    if len(host_s) > 2:
        request.subdomain = ''.join(host_s[:-2])
    return request.subdomain

class Home(View):
    def get(self, request):
        subdomain=subdomaincheck(request)
        
        print(subdomain)
        if subdomain == None:
            return render(request,'TFC/home.html')
        else:
            #subdomain=request.subdomain
            org=Organization.objects.get(subdomain=subdomain)
            return render(request,'TFC/orghome.html',{'org':org})
        
            
            
class OrganizationCreateView(CreateView):
    model=Organization
    template_name='TFC/organization_signup.html'
    fields=['name','website','partner_desc','phone_number','email','address' ,'city','state','zip_code',
        'upi_id','logo']
    #reverse_lazy('organization_list')
    def get_success_url(self):
        return reverse('organization_list')

class OrganizationListView(ListView):
    def get(self,request):
         subdomain=subdomaincheck(request)
         if subdomain==None:
             organization=Organization.objects.all()
             return render(request,'TFC/organization_list.html',{'organization':organization})


     


class PasswordResetView(View):
    form_class = TeamMemberSignupForm()
    
    def get(self,request,auth_token):
        fields=['password',]
        form=TeamMemberSignupForm()
        return render(request,"TFC/password_set.html",{'form':form})
    
    def post(self,request,auth_token):
        form = TeamMemberSignupForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
        try:
            member=Team_Member.objects.get(auth_token=auth_token)
            member.password=make_password(password)
            member.auth_token=None
            member.save()
            return redirect('login')
        except Team_Member.DoesNotExist:
            raise Http404("No  matches the given query.")
        
class LoginView(View):
    def get(self,request):
       subdomain=subdomaincheck(request)
       org=Organization.objects.get(subdomain=subdomain)
       form=LoginForm()
       fields=['member_email','password']
       return render(request,"TFC/login.html",{'form':form,'org':org})
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            member_email=form.cleaned_data['member_email']
            password=form.cleaned_data['password']
            member=Team_Member.objects.get(member_email=member_email)
            member_password=member.password
            
            match=check_password(password,member_password)
            if match:
                request.session['member']=member.member_id
                print(request.session['member'])
                return redirect('dashboard')
            else:
                return redirect('login')
                

    
class MemberListView(View):
    def get(self,request,organization):
        subdomain=subdomaincheck(request)
        org=Organization.objects.get(subdomain=subdomain)
        member_id=request.session['member']
        if member_id == None:
            return redirect('login')
        else:
            return render(request,'TFC/members.html',{'organization':organization,'org':org})

class OrgDashboard(View):
    def get(self,request,):
        subdomain=subdomaincheck(request)
        org=Organization.objects.get(subdomain=subdomain)
        member_id=request.session['member']
        print(member_id)
        member=Team_Member.objects.get(member_id=member_id)
        organization=member.organization
        if member_id == None:
            return redirect('login')
        else:
            return render(request,'TFC/orgdashboard.html',{'organization':organization})

def logout(request):
    auth_logout(request)
    return redirect('login')

