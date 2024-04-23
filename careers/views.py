from django.shortcuts import render
from . models import Careers
from django.views import generic


'''careers view '''
class CareersListView(generic.ListView):
    model = Careers
    template_name ='careers/careers.html'
    context_object_name= 'careers'

'''career detail'''
class CareerDetailView(generic.DetailView):
    model = Careers 
    template_name ='careers/career_detail.html'
    context_object_name ='career_detail'
    slug_url_kwarg = 'slug'