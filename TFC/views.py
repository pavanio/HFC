from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView,ListView
from TFC.models import *
from django.urls import reverse_lazy,reverse


class Home(View):
    def get(self, request):
        return render(request,'TFC/home.html')

class OrganizationCreateView(CreateView):
    model=Organization
    template_name='TFC/organization_signup.html'
    fields=['name','website','partner_desc','phone_number','email','address' ,'city','state','zip_code',
        'upi_id','logo']
    #reverse_lazy('organization_list')
    def get_success_url(self):
        return reverse('organization_list')

class OrganizationListView(ListView):
    model=Organization
    template_name = 'TFC/organization_list.html'
    context_object_name = 'organization'