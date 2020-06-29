from django.shortcuts import render, redirect
from .models import *
import json
import itertools
from .import forms
from TFC.models import *
# Create your views here.


def screening(request, screening_uuid):
	screening_uuid = screening_uuid
	screen = Screenings.objects.get(screening_uuid=screening_uuid)
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
			if (obj.correct_ans == obj.candidate_ans):
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
		try:
			vol=Volunteer.objects.get(email=candidate_email)
			org=vol.organization
			print(org)
			org_admin=Team_Member.objects.filter(organization=org).filter(role='Admin').values('member_email')
			print(org_admin)
			print(org_admin[0]['member_email'])
		except:
			print(candidate_email)

		

		return redirect('screening_preview', screening_uuid)

	return render(request, 'ScreeningApp/screening.html', {'questions': questions, 'screening_uuid': screening_uuid})


def screening_preview(request, screening_uuid):
	screening_uuid = screening_uuid
	screen = Screenings.objects.get(screening_uuid=screening_uuid)
	screening_id = screen.screening_id
	questions = Screenings_Questions.objects.filter(screening_id=screening_id)
	#print (questions)
	ques_list = []
	user_ans_list = []

	for question in questions:
		ques_list.append(question)

	if request.method == 'POST':
		data = request.POST.dict()

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
				#print(ques.answer_correctness)
			else:
				obj.answer_correctness=False
				obj.save()
				#print(ques.answer_correctness)
		return render(request, 'ScreeningApp/thanks.html')
		

	return render(request, 'ScreeningApp/screening_submission.html', {'questions': questions})