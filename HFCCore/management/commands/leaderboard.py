from django.core.management.base import BaseCommand
from HFCCore.models import *
import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        load_leader_board()


def load_leader_board():
    projects=Project.objects.all()
    for project in projects:
        project_repo= project.project_link[len("https://github.com/CTSC/"):]
        project_obj = Project.objects.get(name=project.name)
        print(project_obj)
        print(project_repo)
        response = requests.get('https://api.github.com/repos/CTSC/'+project_repo+'/contributors', headers=headers).json()
        for item in response:
            try:
                community_member = Community_Member.objects.get(coder_profile__contains=item['login'],project =project_obj )
                community_member.commit = item['contributions']
                community_member.avatar_url =item['avatar_url']
                community_member.save()
                print(item['login'],"updated")

                    
            except:
                print(item['login'],'Not exist in community member')
                expertise_area = Expertise_Area.objects.get(area_of_expertise="Engineering")
                community_member=Community_Member.objects.create(name = item['login'],email=item['login']+"@gmail.com",contact_number="1234567891",
                highest_education="Masters",level_of_expertise="Intermediate",profession=expertise_area,years_of_experience="2+ years",coder_profile=item['login'],commit=item['contributions'],avatar_url=item['avatar_url'],project=project_obj)
                print("Added to community")

        
    #print(contribution_list)"""
    
