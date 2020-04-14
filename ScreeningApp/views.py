from django.shortcuts import render
from .models import *
import json

# Create your views here.
def screening(request,screening_uuid):
	screen=Candidate_Screening.objects.get(screening_uuid=screening_uuid)
	screenid=screen.screening_id
	#print(screenid)
	id1=screenid.screening_id
	#print(id1)
	screen_table=Screening_Question.objects.get(screening_id=id1)
	question=Question.objects.order_by('?')[:5]

	
	return render(request,'ScreeningApp/screening.html',{'question':question})

