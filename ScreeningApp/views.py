from django.shortcuts import render, redirect
from .models import *
import json
import itertools
from .import forms
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
		print(data)
		#answerss=request.POST.get(question.id)
		#print(answerss)
		
		for qid,ans in data.items():
			obj=Screenings_Questions.objects.get(pk=qid)
			print(obj)
			obj.candidate_ans=ans
			obj.save()
			print(obj.candidate_ans)
			if (obj.correct_ans == obj.candidate_ans):
				obj.answer_correctness=True
				obj.save()
				#print(ques.answer_correctness)
			else:
				obj.answer_correctness=False
				obj.save()


		
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

		for qid,ans in data.items():
			obj=Screenings_Questions.objects.get(pk=qid)
			print(obj)
			obj.candidate_ans=ans
			obj.save()
			print(obj.candidate_ans)
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