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
