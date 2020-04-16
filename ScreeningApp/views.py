from django.shortcuts import render
from .models import *
import json

# Create your views here.
def screening(request,screening_uuid):
	#screen=Screenings.objects.get(screening_uuid=screening_uuid)
	#id1=screenid.screening_id
	#print(id1)
	#screen_table=Screenings_Questions.objects.get(screening_id=id1)
	question=Question.objects.order_by('?')[:5]
	
	for q in range(0,len(question)):
		print(q)

	if request.method=="POST":
		data = request.POST.dict()
		print(data)
		for key, value in data.items():
			print(key,value)




	

	
	return render(request,'ScreeningApp/screening.html',{'question':question})

