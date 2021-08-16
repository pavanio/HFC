from celery import shared_task
from django.conf import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail,EmailMessage
from ScreeningApp.models import *
from datetime import datetime
from HFC.celery import app
#@app.task(bind=True)
@shared_task(name = 'first_screening_reminder')
def first_screening_reminder():
    screenings = Screenings.objects.filter(status = 'Open')
    today = datetime.today().date()
    for screening in screenings:
        if screening.first_reminder_date == today:
            candidate_id = screening.candidate_id
            screeninguuid = screening.screening_uuid
            #first_reminder_mail(candidate_id,screeninguuid)
            print(candidate_id ," first reminder mail send")
        
@shared_task(name = 'second_screening_reminder')
def second_screening_reminder():
    screenings = Screenings.objects.filter(status = 'Open')
    today = datetime.today().date()
    for screening in screenings:
        if screening.second_reminder_date == today:
            candidate_id = screening.candidate_id
            screeninguuid = screening.screening_uuid
            #second_reminder_mail(candidate_id,screeninguuid)
            print(candidate_id ," second reminder mail send")

@shared_task(name = 'third_screening_reminder')
def third_screening_reminder():
    screenings = Screenings.objects.filter(status = 'Open')
    today = datetime.today().date()
    for screening in screenings:
        if screening.third_reminder_date == today:
            candidate_id = screening.candidate_id
            screeninguuid = screening.screening_uuid
            #third_reminder_mail(candidate_id,screeninguuid)
            print(candidate_id ," third reminder mail send")

def first_reminder_mail(candidate_id,screeninguuid):
    base_url = settings.BASE_URL
    candidate_obj = Candidate.objects.get(candidate_id = candidate_id)
    name = candidate_obj.name
    to_list = [candidate_obj.email,]
    subject = "Pending online evaluation"
    from_email = 'HackForChange Team<noreply@hackforchange.co.in>'
    headers = {'Reply-To': 'suman@hackforchange.co.in'}
    html_content = render_to_string('HFC/first_reminder_email.html', {'name':name,'base_url':base_url,'screeninguuid':screeninguuid})
    msg = EmailMessage(subject, html_content, from_email ,to_list,headers = headers)
    msg.content_subtype = "html"
    msg.send(fail_silently = True)
    print("Mail sended successfully")

def second_reminder_mail(candidate_id,screeninguuid):
    base_url = settings.BASE_URL
    candidate_obj = Candidate.objects.get(candidate_id = candidate_id)
    name = candidate_obj.name
    to_list = [candidate_obj.email,]
    subject = "Gentle reminder to proceed with the online evaluation"
    from_email = 'HackForChange Team<noreply@hackforchange.co.in>'
    headers = {'Reply-To': 'suman@hackforchange.co.in'}
    html_content = render_to_string('HFC/second_reminder_email.html', {'name':name,'base_url':base_url,'screeninguuid':screeninguuid})
    msg = EmailMessage(subject, html_content, from_email ,to_list,headers = headers)
    msg.content_subtype = "html"
    msg.send(fail_silently = True)
    print("Mail sended successfully")

def third_reminder_mail(candidate_id,screeninguuid):
    base_url = settings.BASE_URL
    candidate_obj = Candidate.objects.get(candidate_id = candidate_id)
    name = candidate_obj.name
    to_list = [candidate_obj.email,]
    subject = "Seems like you are having difficulties"
    from_email = 'HackForChange Team<noreply@hackforchange.co.in>'
    headers = {'Reply-To': 'suman@hackforchange.co.in'}
    html_content = render_to_string('HFC/third_reminder_email.html', {'name':name,'base_url':base_url,'screeninguuid':screeninguuid})
    msg = EmailMessage(subject, html_content, from_email ,to_list,headers = headers)
    msg.content_subtype = "html"
    msg.send(fail_silently = True)
    print("Mail sended successfully")

