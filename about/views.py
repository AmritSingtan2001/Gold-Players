from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from about.models import About,Objective
from django.views import generic


class AboutDetailView(generic.DetailView):
    model = About
    template_name = 'about/about.html'
    context_object_name = 'about_us'  

    def get_object(self, queryset=None):
        return About.objects.first() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = self.get_object()
        context['objectives'] = Objective.objects.all()
        return context