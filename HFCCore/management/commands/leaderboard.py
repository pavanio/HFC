from django.core.management.base import BaseCommand
from HFCCore.models import *
import requests
from collections import defaultdict
import json

headers = {
    'Accept': 'application/vnd.github.v3+json',
}
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        load_leader_board()

def load_leader_board():
    projects = Project.objects.all()
    contribution_count = defaultdict(list)
    contribution_dict = {}
    for project in projects:
        project_repo = project.project_link[len("https://github.com/CTSC/"):]
        print(project_repo)
        response = requests.get('https://api.github.com/repos/CTSC/'+project_repo+'/contributors', headers = headers).json()
        for item in response:
            contribution_count[item['login']].append(str(item['contributions']))
        count = 0
    print(contribution_count)
    for key in contribution_count:
        for i in contribution_count[key]:
            count = count + int(i)
            contribution_dict[key] = count
        count = 0
    print(contribution_dict)
    for key,value in contribution_dict.items():
        try:
            community_member = Community_Member.objects.get(coder_profile__contains = key)
            community_member.commit = value
            community_member.save()
            print(key,"updated")
        except:
            print(key,'Not exist in community member')
            expertise_area = Expertise_Area.objects.get(area_of_expertise = "Engineering")
            community_member = Community_Member.objects.create(name = key,email = key+"@gmail.com",contact_number = "1234567891",
            highest_education = "Masters",level_of_expertise = "Intermediate",profession = expertise_area,years_of_experience = "2+ years",coder_profile = key,commit = value)
            print("Added to community")
