from django.db.models.query import QuerySet
from django.shortcuts import render
from about.models import About,Objective
from news.models import Resources
from app.models import Client
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
        context['resources'] = Resources.objects.all()[:4]
        context['clients'] = Client.objects.all()
        return context