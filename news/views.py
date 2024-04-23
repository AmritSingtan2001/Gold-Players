from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from . models import Resources
from django.views import generic


class ResourcseListView(generic.ListView):
    model = Resources
    template_name ='news/resources.html'
    context_object_name ='resources'
    paginate_by =3


class ResourceDetailView(generic.DetailView):
    model = Resources 
    template_name ='news/resource_detail.html'
    context_object_name ='resource_detail'
    slug_url_kwarg = 'slug' 

''' news related rescources '''
class NewsResourcseListView(generic.ListView):
    model = Resources
    template_name ='news/resources.html'
    context_object_name ='resources'
    paginate_by =3

    def get_queryset(self):
        return Resources.objects.filter(resource_type='news')
    

''' insights related rescources '''
class InsightsResourcseListView(generic.ListView):
    model = Resources
    template_name ='news/resources.html'
    context_object_name ='resources'
    paginate_by =3

    def get_queryset(self):
        return Resources.objects.filter(resource_type='insights')
    

''' case studies related rescources '''
class CaseStudiesResourcseListView(generic.ListView):
    model = Resources
    template_name ='news/resources.html'
    context_object_name ='resources'
    paginate_by =3

    def get_queryset(self):
        return Resources.objects.filter(resource_type='case_studies')