from django.shortcuts import render
from . models import Careers
from django.views import generic


'''careers view '''
class CareersListView(generic.ListView):
    model = Careers
    template_name ='careers/careers.html'
    context_object_name= 'careers'

