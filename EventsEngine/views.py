from django.shortcuts import render

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


class EventSignUpView(View):
    def get(self, request, title_slug):
        event = Events.objects.get(title_slug = title_slug)
        contributors = Community_Member.objects.filter(type='Contributor')
        expertise_area_id = request.GET.get('profession')
        expertises = Expertise.objects.filter(category_of_expertise = expertise_area_id,is_published = 'True')
        form = Community_member_form()
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
