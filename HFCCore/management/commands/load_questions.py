from django.core.management.base import BaseCommand
import yaml
import re
from ScreeningApp.models import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        load_questions()

def load_questions():
    with open(r'HFCCore\management\commands\questions.yaml', 'r',encoding = "utf8",errors = "ignore") as file:
        print("file accessed")
        main_dict = yaml.load(file, Loader = yaml.FullLoader)
    category_of_expertise = Expertise_Area.objects.get(area_of_expertise = "Engineering")
    for expertise,questions in main_dict.items():
        expertise_obj,flag = Expertise.objects.get_or_create(expertise = expertise , category_of_expertise = category_of_expertise)
        for question in questions:
            question = Question.objects.create(category_of_expertise = category_of_expertise, expertise = expertise_obj,
		 	level = 'Intermediate', topic = expertise , qtype = 'multiple choice', question = question['question'] , 
		 	option_1 = question.get('option_1'), option_2 = question.get('option_2') , option_3 = question.get('option_3') , 
		 	option_4 = question.get('option_4'),answer = question.get('ans'),question_img = question.get('question_img'))
        print(expertise + "questions are added")
