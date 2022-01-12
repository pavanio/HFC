from django.shortcuts import render, redirect
from ScreeningApp.models import Candidate
from .models import *
from HFCCore.forms import Community_member_form,Chapter_contributor_form,Event_signup_form
from HFCCore.models import Partner, Community_Member, Community_Organization, Expertise
from HFCCore.utils import SendSubscribeMail,community_member_signup_mail
from EventsEngine.utils import event_signup_mail,name_spliter
from django.contrib.syndication.views import Feed
from django.views import View,generic
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage
from datetime import date
from .utils import event_email_internal
from django.conf import settings

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
        event_speakers = Event_Speakers.objects.filter(event = event.id)
        print(event_speakers)
        return render(request, 'EventsEngine/event_detail.html', {'event':event,'contributors':contributors,'event_speakers': event_speakers})

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
        event = Events.objects.get(title_slug = title_slug)
        contributors = Community_Member.objects.filter(type='Contributor')
        expertise_area_id = request.GET.get('profession')
        expertises = Expertise.objects.filter(category_of_expertise = expertise_area_id,is_published = 'True')
        #form = Community_member_form()
        form = Event_signup_form()
        event.update_registration()
        if event.registration == "Registrations Closed":
            return redirect('event_expired',title_slug)
        else:
            #print(form)
            return render(request, 'EventsEngine/event_signup.html', {'form':form,'event':event,'contributors':contributors,'expertises':expertises})
            
        
    
    def post(self,request,title_slug):
        form = Event_signup_form(request.POST)
        event = Events.objects.get(title_slug = title_slug)
        #community_org=Community_Organization.objects.get(organization_name_slug=hfc_chapter_slug)
        print(form.is_valid())
        print(request.POST)
        if form.is_valid():
            data = request.POST.getlist('name')
            print(data)
            name = " ".join(data)
            print(name)
            contributor = form.save(commit = False)
            contributor.type = "Contributor"
            contributor.name = name
            email = contributor.email
            #print(Candidate.objects.filter(email=email).exists())
            if Candidate.objects.filter(email=email).exists() != True:
                contributor.save()
                contributor.event.add(event)            
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
                event_mailing_list = settings.EVENT_MAILING_LIST
                to_list=[event_mailing_list,]
                headers = {'Reply-To': email}
                print("working")
                msg = EmailMessage('New member signup for event', html_content,'HackForChange Team<noreply@hackforchange.co.in>' ,to_list,headers=headers)
                msg.content_subtype = "html"
                msg.send(fail_silently = True)
                print("Event Signup details internal email sended successfully")
            except:
                print('Error in sending internal email for event signup')
            return render(request, 'EventsEngine/event_signup_thanks.html', {'event':event})
        else:
            form = Event_signup_form()
            return render(request, 'EventsEngine/event_signup.html', {'form':form})

def event_signup_thanks(request):
    if 'event' in request.session:
        event_title = request.session['event']
        #del request.session['event']
        print(event_title)
        event_obj = Events.objects.get(title_slug = event_title)
    if 'email' in request.session:
        email = request.session['email']
        contributor = Community_Member.objects.filter(email=email).first()
        contributor.event.add(event_obj)
        try:
            event_email_internal(email,event_obj)
        except:
            print("Error in sending Event recurring signup internal email")
        try:
            event_signup_mail(email,event_obj.email_confirmation,event_obj.title)
        except:
            print("error in sending email to recurring event participants")
    return render(request, 'EventsEngine/event_signup_thanks.html',{'event':event_obj})

class EventSignupWithGoogle(View):
    def get(self,request,title_slug):
        if 'name' and 'email' in request.session:
            name = request.session['name']
            email = request.session['email']
        first_name,last_name = name_spliter(name)
        event = Events.objects.get(title_slug = title_slug)
        contributors = Community_Member.objects.filter(type='Contributor')
        expertise_area_id = request.GET.get('profession')
        expertises = Expertise.objects.filter(category_of_expertise = expertise_area_id,is_published = 'True')
        form = Event_signup_form()
        event.update_registration()
        if event.registration == "Registrations Closed":
            return redirect('event_expired',title_slug)
        else:
            return render(request, 'EventsEngine/event_signup.html', {'form':form,'event':event,'contributors':contributors,'expertises':expertises,'first_name':first_name,'email':email,'last_name':last_name})
           
           
    def post(self,request,title_slug):
        form = Event_signup_form(request.POST)
        event = Events.objects.get(title_slug = title_slug)
        #community_org=Community_Organization.objects.get(organization_name_slug=hfc_chapter_slug)
        print(form.is_valid())
        if form.is_valid():
            data = request.POST.getlist('name')
            print(data)
            name = " ".join(data)
            print(name)
            contributor = form.save(commit = False)
            contributor.type = "Contributor"
            contributor.name = name
            #contributor.organization_id = community_org
            email = contributor.email
            #print(Candidate.objects.filter(email=email).exists())
            if Candidate.objects.filter(email=email).exists() != True:
                contributor.save()
                contributor.event.add(event)               
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
                event_mailing_list = settings.EVENT_MAILING_LIST
                to_list=[event_mailing_list,]
                headers = {'Reply-To': email}
                print("working")
                msg = EmailMessage('New member signup for event', html_content,'HackForChange Team<noreply@hackforchange.co.in>' ,to_list,headers=headers)
                msg.content_subtype = "html"
                msg.send(fail_silently = True)
                print("Event Signup details internal email sended successfully")
            except:
                print('Error in sending internal email for event signup')
            return render(request, 'EventsEngine/event_signup_thanks.html', {'event':event})

