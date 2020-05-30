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
from django.contrib import messages


def subdomaincheck(request):
    request.subdomain = None
    host = request.META.get('HTTP_HOST', '')
    print(host)
    host_s = host.replace('www.', '').split('.')
    print(host_s)
    if len(host_s) > 2:
        request.subdomain = ''.join(host_s[:-2])
        print(request.subdomain)
        if request.subdomain.endswith('staging'):
            request.subdomain=request.subdomain.replace('staging','')
    return request.subdomain
def admin_redirect(request):
    subdomain=subdomaincheck(request)
    print(subdomain , "redirected")
    if subdomain != None :
        if request.path.startswith(reverse('admin:index')):
            org=Organization.objects.get(subdomain=subdomain)
            return redirect('home')
    else:
        return redirect(reverse('admin:index')) 

def thanks(request):
    subdomain=subdomaincheck(request)
    org=Organization.objects.get(subdomain=subdomain)

    return render(request,'TFC/thanks.html',{'org':org})

class Home(View):
    def get(self, request):
        subdomain=subdomaincheck(request)
        
        print(subdomain)
        if subdomain == None or subdomain == "":
            return render(request,'TFC/home.html')
        else:
            #subdomain=request.subdomain
            org=Organization.objects.get(subdomain=subdomain)
            return render(request,'TFC/orghome.html',{'org':org})
        
            
            
class OrganizationCreateView(View):
    def get(self,request):
        subdomain=subdomaincheck(request)
        if subdomain == None or subdomain == "":
            form=OrganizationSignupForm()
            return render(request,'TFC/organization_signup.html',{'form':form})
    def post(self,request):
        form=OrganizationSignupForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            website=form.cleaned_data['website']
            partner_desc=form.cleaned_data['partner_desc']
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            address=form.cleaned_data['address']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zip_code=form.cleaned_data['zip_code']
            upi_id=form.cleaned_data['upi_id']
            logo=form.cleaned_data['logo']
            if Organization.objects.filter(email=email).exists():
                messages.error(request,"Email already exist")
                return render(request,'TFC/organization_signup.html',{'form':form})
            else:
                form.save()
                messages.success(request,"Organization Created Successfully")
                return redirect('organization_list')

    def get_success_url(self):
        return reverse('organization_list')

class OrganizationListView(ListView):
    def get(self,request):
         subdomain=subdomaincheck(request)
         if subdomain==None or subdomain=="":
             organization=Organization.objects.all()
             return render(request,'TFC/organization_list.html',{'organization':organization})


     


class PasswordResetView(View):
    form_class = TeamMemberSignupForm()
    
    def get(self,request,auth_token):
        subdomain=subdomaincheck(request)
        org=Organization.objects.get(subdomain=subdomain)
        fields=['password',]
        form=TeamMemberSignupForm()
        return render(request,"TFC/password_set.html",{'form':form,'org':org})
    
    def post(self,request,auth_token):
        form = TeamMemberSignupForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
        try:
            member=Team_Member.objects.get(auth_token=auth_token)
            member.password=make_password(password)
            member.auth_token=None
            member.save()
            messages.success(request,"Password Created Successfully")

            return redirect('login')
        except Team_Member.DoesNotExist:
            messages.error(request,"Password Not  Created")
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
            subdomain=subdomaincheck(request)
            org=Organization.objects.get(subdomain=subdomain)
            member_email=form.cleaned_data['member_email']
            password=form.cleaned_data['password']
            member=Team_Member.objects.get(member_email=member_email)
            member_password=member.password
            
            match=check_password(password,member_password)

            if match and  org.name == member.organization.name:
                request.session['member']=member.member_id
                print(request.session['member'])
                messages.success(request,"Successfully Log in to dashboard")
                return redirect('dashboard')
            else:
                messages.error(request,"Email or Password is wrong")
                return redirect('login')
                

class MemberCreateView(View):
    def get(self,request):
        subdomain=subdomaincheck(request)
        org=Organization.objects.get(subdomain=subdomain)
        member=request.session['member']
        if member == None:
            return redirect('login')
        else:
            form=MemberCreateForm()
            return render(request,'TFC/member_signup.html',{'form':form,'org':org})
    def post(self,request):
        form=MemberCreateForm(request.POST)
        if form.is_valid():
            subdomain=subdomaincheck(request)
            org=Organization.objects.get(subdomain=subdomain)
            member_name = form.cleaned_data['member_name']
            member_email = form.cleaned_data['member_email']
            member_phone_number = form.cleaned_data['member_phone_number']
            member=Team_Member(member_name=member_name,member_email=member_email,member_phone_number=member_phone_number,role='Member')
            #member.organization.add(org)
            member.organization=org
            member.save()
            
            messages.success(request,"Member Created Successfully")
            return redirect('team_member')    
class MemberListView(View):
    def get(self,request):
        subdomain=subdomaincheck(request)
        org=Organization.objects.get(subdomain=subdomain)
        member=request.session['member']
        if member == None:
            return redirect('login')
        else:
            return render(request,'TFC/members.html',{'org':org})
class MemberUpdate(View):
    def get(self,request,member_id):
        subdomain=subdomaincheck(request)
        org=Organization.objects.get(subdomain=subdomain)
        member=request.session['member']
        if member == None:
            return redirect('login')
        else:
            form=MemberCreateForm()
            member=Team_Member.objects.get(member_id=member_id)
            return render(request,'TFC/memberupdate.html',{'form':form,'org':org,'member':member})
    def post(self,request,member_id):
        member=Team_Member.objects.get(member_id=member_id)
        form=MemberCreateForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            messages.success(request,"Member Updated Successfully")
            return redirect ('team_member')
class MemberDelete(View):
    def get(self,request,member_id):
        subdomain=subdomaincheck(request)
        org=Organization.objects.get(subdomain=subdomain)
        member=request.session['member']
        if member == None:
            return redirect('login')
        else:
            member=Team_Member.objects.get(member_id=member_id)
            return render(request,'TFC/memberdelete.html',{'org':org,'member':member})
    def post(self,request,member_id):
        member=Team_Member.objects.get(member_id=member_id)
        member.delete()
        messages.success(request,"Member Deleted Successfully")
        return redirect ('team_member')




class OrgDashboard(View):
    def get(self,request):
        subdomain=subdomaincheck(request)
        org=Organization.objects.get(subdomain=subdomain)
        
        member=request.session['member']
        print(member)
        member=Team_Member.objects.get(member_id=member)
        organization=member.organization.name
        print(member.organization.name)
        print(org.name)
        
        if org.name == member.organization.name:
            return render(request,'TFC/orgdashboard.html',{'org':org})
            
            
        else:
            return redirect('login')
            
            


def logout(request):
    auth_logout(request)
    messages.success(request,"Successfully Log out From your dashboard")
    return redirect('login')

class VolunteerCreateView(View):
    def get(self,request):
        subdomain=subdomaincheck(request)
        org=Organization.objects.get(subdomain=subdomain)
        form=VolunteerForm()
        #print(form)
        return render(request,'TFC/volunteer_signup.html',{'form':form,'org':org})
    def post(self,request):
        form=VolunteerForm(request.POST)
        print(request.POST)
        if form.is_valid():
            subdomain=subdomaincheck(request)
            org=Organization.objects.get(subdomain=subdomain)
            area_of_expertise=request.POST.getlist('area_of_expertise')
            
            vol=form.save(commit=False)
            vol.organization=org
            vol.save()
            vol.area_of_expertise.set(area_of_expertise)
            vol.save()
            print(vol.area_of_expertise)
            messages.success(request,"Volunteer Registration Form Submitted Successfully")
            return redirect('thanks')
class VolunteerList(View):
    def get(self,request):
        subdomain=subdomaincheck(request)
        org=Organization.objects.get(subdomain=subdomain)
        member=request.session['member']
        if member == None:
            return redirect('login')
        else:
            return render(request,'TFC/volunter_list.html',{'org':org})


def load_area_of_expertise(request):
    expertise_area_id = request.GET.get('profession')
    print(expertise_area_id)
    expertises=Expertise.objects.filter(category_of_expertise=expertise_area_id)
    print(expertises)
    return render(request,'TFC/areaofexpertise.html',{'expertises':expertises})
            

