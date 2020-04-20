from django.shortcuts import render
from .models import *
import json
import itertools
# Create your views here.


def screening(request, screening_uuid):
	screening_uuid = screening_uuid
	screen = Screenings.objects.get(screening_uuid=screening_uuid)
	screening_id=screen.screening_id
	#screening_id = screen.screening_id
	print(screening_id)
	#question_dict=[]
	question_list=list(Screenings_Questions.objects.filter(screening_id=screening_id))
	#for ques in question_list:
	qid=Screenings_Questions.objects.filter(question__in=question_list)
	print(qid)
	#print(question)
	questions=Question.objects.filter(question__in=question_list)
	#print(questions)
	# question_id_list = []
	user_ans_list = []

	if request.method == "POST":
		data = request.POST.dict()
		if 'csrfmiddlewaretoken' in data:
			del data['csrfmiddlewaretoken']
		for key, value in data.items():
			question_id_list.append(key)
			user_ans_list.append(value)
		print(user_ans_list)
		print(question_id_list)
		for ans in user_ans_list:
			screening_question = Screenings_Questions(screening_id=
	 		screen, candidate_ans=ans )
			screening_question.save()

		

	return render(request, 'ScreeningApp/screening.html', {'questions': questions})
