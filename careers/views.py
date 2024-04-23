from typing import Any
from django.shortcuts import render
from . models import Careers
from django.views import generic
from .froms import JobSearchForm


'''careers view '''
class CareersListView(generic.ListView):
    model = Careers
    template_name ='careers/careers.html'
    context_object_name= 'careers'
    paginate_by =5

    def get_queryset(self):
        queryset = super().get_queryset()
        form = JobSearchForm(self.request.GET)

        if form.is_valid():
            keywords = form.cleaned_data.get('keywords')
            location = form.cleaned_data.get('location')
            category = form.cleaned_data.get('category')

            if keywords:
                queryset = queryset.filter(job_title__icontains=keywords)
            if location:
                queryset = queryset.filter(location__icontains=location)
            if category:
                queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = JobSearchForm(self.request.GET)
        return context

'''career detail'''
class CareerDetailView(generic.DetailView):
    model = Careers 
    template_name ='careers/career_detail.html'
    context_object_name ='career_detail'
    slug_url_kwarg = 'slug'