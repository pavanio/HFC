from django.shortcuts import render, redirect
from .models import *
import json
import itertools
from .import forms
from TFC.models import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives,EmailMessage
from django.conf import settings
import uuid
from HFCCore.models import Community_Member
# Create your views here.
def screening_result(email,name,screening_status):
    #from_email=settings.EMAIL_HOST_USER
	from_email='HackForChange Team<noreply@hackforchange.co.in>'
	to=[email,]
	subject="Screening Result"
	headers = {'Reply-To': 'suman@hackforchange.co.in'}
	html_content = render_to_string('HFC/screen_result_email.html', {'name':name,'screening_status':screening_status})
	msg = EmailMessage(subject, html_content, from_email ,to,headers=headers)
	msg.content_subtype = "html"
	msg.send(fail_silently=True)
	print("Mail sended successfully")  
	
def screening(request, screening_uuid):
	mentors = Community_Member.objects.filter(type  ='Mentor')[:6]
	screening_uuid = screening_uuid
	screen = Screenings.objects.get(screening_uuid=screening_uuid)
	if screen.status=="Passed" or screen.status=="Failed":
		return render(request, 'ScreeningApp/screening_error.html')
	screening_id = screen.screening_id
	questions = Screenings_Questions.objects.filter(screening_id=screening_id)
	ques_list = []
	user_ans_list = []
	for question in questions:
		ques_list.append(question)
	if request.method == "POST":
		data = request.POST.dict()
		if 'csrfmiddlewaretoken' in data:
			del data['csrfmiddlewaretoken']
		#print(data)
		#answerss=request.POST.get(question.id)
		#print(answerss)
		true_count=false_count=0
		for qid,ans in data.items():
			obj=Screenings_Questions.objects.get(pk=qid)
			#print(obj)
			obj.candidate_ans=ans
			obj.save()
			print(obj.screening_id)
			""""if (obj.correct_ans == obj.candidate_ans):
				obj.answer_correctness=True
				obj.save()
				true_count=true_count+1
				#print(ques.answer_correctness)
			else:
				obj.answer_correctness=False
				obj.save()
				false_count=false_count+1
		
		total=true_count+false_count
		percentage=int((true_count/total)*100)
		screeningid=obj.screening_id.screening_id 
	
		screening_obj=Screenings.objects.filter(screening_id = screeningid).update(screening_result=percentage)
		if (percentage >=70):
			screening_obj=Screenings.objects.filter(screening_id = screeningid).update(status='Passed')
		else:
			screening_obj=Screenings.objects.filter(screening_id = screeningid).update(status='Failed')
		screen_obj=Screenings.objects.get(screening_id = screeningid)
		cand_id=screen_obj.candidate_id.candidate_id
		print(cand_id)
		candidate_obj=Candidate.objects.get(candidate_id=cand_id)
		#print(type(candidate_obj))
		candidate_email=candidate_obj.email
		candidate_name=candidate_obj.name
		screening_status=screen_obj.status
		print(screening_status)
		print(screen_obj.screening_result)
		try:
			vol=Volunteer.objects.get(email=candidate_email)
			org=vol.organization
			print(org)
			org_admin=Team_Member.objects.filter(organization=org).filter(role='Admin').values('member_email')
			print(org_admin)
			print(org_admin[0]['member_email'])
			#screening_result(candidate_email,candidate_name,screening_status)
		except:
			print(candidate_email)
			print(candidate_name)
			try:
				#screening_result(candidate_email,candidate_name,screening_status)
				pass
			except:
				print("Error in sending Screening Result to Mentor/Contributor ")"""

		return redirect('screening_preview', screening_uuid)

	return render(request, 'ScreeningApp/screening.html', {'questions': questions, 'screening_uuid': screening_uuid,'mentors':mentors})


def screening_preview(request, screening_uuid):
	mentors = Community_Member.objects.filter(type  ='Mentor')[:6]
	screening_uuid = screening_uuid
	screen = Screenings.objects.get(screening_uuid=screening_uuid)
	screening_id = screen.screening_id
	questions = Screenings_Questions.objects.filter(screening_id=screening_id)
	#print (questions)
	ques_list = []
	user_ans_list = []
	if request.method == 'POST':
		data = request.POST.dict()
		print(data)
		if 'csrfmiddlewaretoken' in data:
			del data['csrfmiddlewaretoken']
		true_count=false_count=0
		for qid,ans in data.items():
			obj=Screenings_Questions.objects.get(pk=qid)
			obj.candidate_ans=ans
			obj.save()
			if (obj.correct_ans == obj.candidate_ans):
				obj.answer_correctness=True
				obj.save()
				true_count=true_count+1
				print(obj.answer_correctness)
			else:
				obj.answer_correctness=False
				obj.save()
				print(obj.answer_correctness)
				false_count=false_count+1
		total=true_count+false_count
		percentage=int((true_count/total)*100)
		screeningid=obj.screening_id.screening_id 
		screening_obj=Screenings.objects.filter(screening_id = screeningid).update(screening_result=percentage)
		if (percentage >=70):
			screening_obj=Screenings.objects.filter(screening_id = screeningid).update(status='Passed')
			screen_obj=Screenings.objects.get(screening_id = screeningid)
			cand_id=screen_obj.candidate_id.candidate_id
			candidate_obj=Candidate.objects.get(candidate_id=cand_id)
			name=candidate_obj.name
			screening_status=screen_obj.status
			return render(request, 'ScreeningApp/screening_result_pass.html',{'name':name,'screening_status':screening_status})

		else:
			screening_obj=Screenings.objects.filter(screening_id = screeningid).update(status='Failed')
			screen_obj=Screenings.objects.get(screening_id = screeningid)
			cand_id=screen_obj.candidate_id.candidate_id
			candidate_obj=Candidate.objects.get(candidate_id=cand_id)
			name=candidate_obj.name
			screening_status=screen_obj.status
			return render(request, 'ScreeningApp/screening_result_fail.html',{'name':name,'screening_status':screening_status})
		
		

	return render(request, 'ScreeningApp/screening_submission.html', {'questions': questions,'mentors':mentors})
