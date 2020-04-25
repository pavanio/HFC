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

		for key, value in data.items():
			user_ans_list.append(value)
		#print(user_ans_list)

		screening_question_obj = Screenings_Questions.objects.filter(
            screening_id=screening_id)
		#print(screening_question_obj)
		for ans, ques in zip(user_ans_list, ques_list):
			ques.candidate_ans = ans
			ques.save()
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

		for key, value in data.items():
			user_ans_list.append(value)
		#print(user_ans_list)

		
		for ans, ques in zip(user_ans_list, ques_list):
			ques.candidate_ans = ans
			ques.save()
			if (ques.correct_ans == ques.candidate_ans):
				ques.answer_correctness=True
				ques.save()
				#print(ques.answer_correctness)
			else:
				ques.answer_correctness=False
				ques.save()
				
				#print(ques.answer_correctness)
		return redirect('screening_preview_submit', screening_uuid)

	return render(request, 'ScreeningApp/screening_preview.html', {'questions': questions})


def screening_preview_submit(request, screening_uuid):
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
		for key, value in data.items():
			user_ans_list.append(value)
		
		for ans, ques in zip(user_ans_list, ques_list):
			ques.candidate_ans = ans
			ques.save()
		return render(request, 'ScreeningApp/thanks.html')
	return render(request, 'ScreeningApp/screening_submission.html', {'questions': questions})
