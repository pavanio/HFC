from django.conf import settings
import requests
import json
from EventsEngine.models import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail,EmailMessage
from django.apps import apps
import requests
from django.conf import settings

import os

import datetime
from datetime import timedelta
import pytz
from google.oauth2 import service_account
from googleapiclient.discovery import build

from ScreeningApp.models import Candidate


def event_signup_mail(email,content,title):
    base_url = settings.BASE_URL
    candidate = Candidate.objects.filter(email = email).first()
    name = candidate.name
    email = candidate.email
    from_email = 'HackForChange Team<noreply@hackforchange.co.in>'
    to_list = [email,]
    subject = "Congratulations, You are signed up for "  + title
    headers = {'Reply-To': 'suman@hackforchange.co.in'}
    html_content = render_to_string('EventsEngine/event_participant_welcome_email.html', {'name':name,'base_url':base_url, 'content': content})
    msg = EmailMessage(subject, html_content, from_email ,to_list,headers = headers)
    msg.content_subtype = "html"
    msg.send(fail_silently = True)
    print("Participant Welcome Mail sended successfully")

def create_event(title,start_date,end_date,description):
    service_account_email = os.environ.get('service_account_email')
    SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

    credentials = service_account.Credentials.from_service_account_file('google-credentials.json')
    scoped_credentials = credentials.with_scopes(SCOPES)


    def build_service():
        service = build("calendar", "v3", credentials=scoped_credentials)
        return service


    
    service = build_service()
 
    event = {
    'summary': title,
    'description': description,
    'start': {
        'dateTime': start_date.isoformat(),
        'timeZone': 'Asia/Kolkata',
    },
    'end': {
        'dateTime': end_date.isoformat(),
        'timeZone': 'Asia/Kolkata',
    },
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }

    event = service.events().insert(calendarId=os.environ.get('calendarId'), body=event).execute()
    print(event)
    