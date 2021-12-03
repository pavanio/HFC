from django.shortcuts import render, redirect
from django.http import HttpResponse
from ScreeningApp.models import Candidate
from .models import *
from HFCCore.forms import Community_member_form,Chapter_contributor_form
from HFCCore.models import Partner, Community_Member, Community_Organization, Expertise
from HFCCore.utils import SendSubscribeMail,community_member_signup_mail
from EventsEngine.utils import event_signup_mail
from django.contrib.syndication.views import Feed
from django.views import View,generic
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage
from datetime import date
from .utils import event_email_internal


class EventList(generic.ListView):
    def get(self, request):
        event_list = Events.objects.all().exclude(status ='Draft')
        partners = Partner.objects.all()
        for i in event_list:
            i.update_registration()
        return render(request, 'EventsEngine/event_list.html', {'event_list': event_list,'partners':partners})

class EventDetailView(View):
    def get(self, request, title_slug):
        event = Events.objects.get(title_slug = title_slug)
        event.update_registration()
        contributors = Community_Member.objects.filter(type='Contributor') 
        return render(request, 'EventsEngine/event_detail.html', {'event':event,'contributors':contributors})

class EventFeed(Feed):
    title = "HackForChange Events"
    link = "/events/latest/feed/"
    description = "Updates on the HFC Events"

    def items(self):
        return Events.objects.filter(status = 'Published').order_by('-end_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
    def item_pubdate(self, item):
        return datetime.datetime.combine(item.created_on, datetime.time(10, 23))

class EventSignUpExpiredView(View):
    def get(self, request, title_slug):
        event = Events.objects.get(title_slug = title_slug)
        event.update_registration()
        if event.registration == "Registrations Open":
            return redirect('event_sign_up',title_slug)
        else:
            return render(request, 'EventsEngine/event_signup_expire.html', {'event':event})

class EventSignUpView(View):
    def get(self, request, title_slug):
        if 'name' and 'email' in request.session:
            name = request.session['name']
            email = request.session['email']
            print('name:',name)
        event = Events.objects.get(title_slug = title_slug)
        contributors = Community_Member.objects.filter(type='Contributor')
        expertise_area_id = request.GET.get('profession')
        expertises = Expertise.objects.filter(category_of_expertise = expertise_area_id,is_published = 'True')
        form = Community_member_form()
        event.update_registration()
        if event.registration == "Registrations Closed":
            return redirect('event_expired',title_slug)
        else:
            #print(form)
            return render(request, 'EventsEngine/event_signup.html', {'form':form,'event':event,'contributors':contributors,'expertises':expertises,'name':name,'email':email})
            
        
    
    def post(self,request,title_slug):
        form = Chapter_contributor_form(request.POST)
        event = Events.objects.get(title_slug = title_slug)
        #community_org=Community_Organization.objects.get(organization_name_slug=hfc_chapter_slug)
        print(form.is_valid())
        if form.is_valid():
            area_of_expertise = request.POST.getlist('area_of_expertise')
            city = request.POST.get('city')
            community_org = Community_Organization.objects.filter(city = city).first()
            print(community_org)
            contributor = form.save(commit = False)
            contributor.type = "Contributor"
            contributor.organization_id = community_org

            email = contributor.email
            #print(Candidate.objects.filter(email=email).exists())
            if Candidate.objects.filter(email=email).exists() != True:
                contributor.save()                
                SendSubscribeMail(email)

                form.save_m2m()

            else :
                contributor = Community_Member.objects.filter(email=email).first()
                print(contributor)
            try:
                event_signup_mail(email,event.email_confirmation,event.title)
            except:
                print('Error in sending email for event signup')
            try:
                html_content = render_to_string('EventsEngine/event_participant_detail_internal_email.html', {'contributor':contributor, 'event':event})
                to_list=['team@hackforchange.co.in',]
                headers = {'Reply-To': email}
                print("working")
                msg = EmailMessage('New member signup for event', html_content,'HackForChange Team<noreply@hackforchange.co.in>' ,to_list,headers=headers)
                msg.content_subtype = "html"
                msg.send(fail_silently = True)
                print("Event Signup details internal email sended successfully")
            except:
                print('Error in sending internal email for event signup')
            return render(request, 'EventsEngine/event_signup_thanks.html', {'event':event})

def member_exist(request):
    email = request.GET.get('email')
    try:
        user = Community_Member.objects.filter(email = email).exists()
        user_exist = True
        print( user_exist)

    except:
        user_exist = False
        print( user_exist)
    return HttpResponse(user_exist)

def event_signup_thanks(request):
    if 'event' in request.session:
        event_title = request.session['event']
        #del request.session['event']
        print(event_title)
        event = Events.objects.get(title_slug = event_title)
    if 'email' in request.session:
        email = request.session['email']
        try:
            event_email_internal(email)
        except:
            print("Error in sending Event recurring signup internal email")
        try:
            event_signup_mail(email,event.email_confirmation,event.title)
        except:
            print("error in sending email to recurring event participants")
    return render(request, 'EventsEngine/event_signup_thanks.html',{'event':event})

class EventSignupWithGoogle(View):
    def get(self,request,title_slug):
        if 'name' and 'email' in request.session:
            name = request.session['name']
            email = request.session['email']
        event = Events.objects.get(title_slug = title_slug)
        contributors = Community_Member.objects.filter(type='Contributor')
        expertise_area_id = request.GET.get('profession')
        expertises = Expertise.objects.filter(category_of_expertise = expertise_area_id,is_published = 'True')
        form = Community_member_form()
        event.update_registration()
        if event.registration == "Registrations Closed":
            return redirect('event_expired',title_slug)
        else:
            #print(form)
            if name and email:
                return render(request, 'EventsEngine/event_signup.html', {'form':form,'event':event,'contributors':contributors,'expertises':expertises,'name':name,'email':email})
            else:
                return render(request, 'EventsEngine/event_signup.html', {'form':form,'event':event,'contributors':contributors,'expertises':expertises})
           
    def post(self,request,title_slug):
        form = Chapter_contributor_form(request.POST)
        event = Events.objects.get(title_slug = title_slug)
        #community_org=Community_Organization.objects.get(organization_name_slug=hfc_chapter_slug)
        print(form.is_valid())
        if form.is_valid():
            area_of_expertise = request.POST.getlist('area_of_expertise')
            city = request.POST.get('city')
            community_org = Community_Organization.objects.filter(city = city).first()
            print(community_org)
            contributor = form.save(commit = False)
            contributor.type = "Contributor"
            contributor.organization_id = community_org
            email = contributor.email
            #print(Candidate.objects.filter(email=email).exists())
            if Candidate.objects.filter(email=email).exists() != True:
                contributor.save()                
                SendSubscribeMail(email)
                form.save_m2m()
            else :
                contributor = Community_Member.objects.filter(email=email).first()
                print(contributor)
            try:
                event_signup_mail(email,event.email_confirmation,event.title)
            except:
                print('Error in sending email for event signup')
            try:
                html_content = render_to_string('EventsEngine/event_participant_detail_internal_email.html', {'contributor':contributor, 'event':event})
                to_list=['team@hackforchange.co.in',]
                headers = {'Reply-To': email}
                print("working")
                msg = EmailMessage('New member signup for event', html_content,'HackForChange Team<noreply@hackforchange.co.in>' ,to_list,headers=headers)
                msg.content_subtype = "html"
                msg.send(fail_silently = True)
                print("Event Signup details internal email sended successfully")
            except:
                print('Error in sending internal email for event signup')
            return render(request, 'EventsEngine/event_signup_thanks.html', {'event':event})

