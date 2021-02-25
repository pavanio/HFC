from django.conf import settings
import requests
import json
from ScreeningApp.models import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail,EmailMessage
from .models import Problem_Statement, Partner, Project, Community_Organization, Community_Member
from django.apps import apps
import requests


def SendSubscribeMail(email):
    API_KEY = settings.MAILCHIMP_API_KEY
    LIST_ID = settings.MAILCHIMP_SUBSCRIBE_LIST_ID
    API_ENDPOINT = "https://us7.api.mailchimp.com/3.0/lists/"+LIST_ID+"/members/"
    data = {
            "email_address":email,
            "status":"subscribed"
            }
    headers={'Authorization':API_KEY }
    try:
        r = requests.post(url = API_ENDPOINT,headers=headers,data=json.dumps(data))
        print("added to mailchimp")
        print(r)
    except:
        return False

def mentor_signup_mail(email):
    base_url = settings.BASE_URL
    candidate=Candidate.objects.get(email=email)
    name=candidate.name
    email=candidate.email
    #from_email=settings.EMAIL_HOST_USER
    from_email='HackForChange Team<noreply@hackforchange.co.in>'
    to_list=[email,]
    subject="Welcome to HackForChange"
    headers = {'Reply-To': 'suman@hackforchange.co.in'}
    #msg = MIMEMultipart('alternative')
    html_content = render_to_string('HFC/mentor_welcome_email.html', {'name':name,'base_url':base_url})
    #msg = EmailMultiAlternatives(subject, html_content, from_email , [to])
    msg = EmailMessage(subject, html_content, from_email ,to_list,headers=headers)
    msg.content_subtype = "html"
    msg.send(fail_silently=True)
    print("Mail sended successfully")
