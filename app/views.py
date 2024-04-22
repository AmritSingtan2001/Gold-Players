from typing import Any
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from .models import Banner,AboutSolution,Solutions,SolutionSubCategory,Sector,Location,Client,Testimonials
from news.models import Resources
from django.views import generic

class IndexView(generic.ListView):
    model = Banner
    template_name ='app/index.html'
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = self.get_queryset
        context['allsolutions'] = Solutions.objects.all()
        context['sectors'] = Sector.objects.all()
        context['locations'] = Location.objects.all()
        context['clients'] = Client.objects.all()
        context['all_news'] = Resources.objects.filter(resource_type='news')
        context['insights'] = Resources.objects.filter(resource_type='insights')
        context['case_studies'] = Resources.objects.filter(resource_type='case_studies')
        context['testimonials'] = Testimonials.objects.all()
        return context


def aboutus(request):
    return render(request,'app/about.html')

def blog(request):
    return render(request,'app/blog.html')

def blog_detail(request):
    return render(request,'app/blog-single.html')

def solution(request):
    about_solution = AboutSolution.objects.first()
    allsolutions= Solutions.objects.all()
    return render(request,'app/solutions.html',{'about_solution':about_solution,'allsolutions':allsolutions})


class SolutionDetailView(generic.DetailView):
    model = Solutions
    template_name = 'app/solution_detail.html'
    context_object_name = 'detail'
    slug_url_kwarg = 'slug' 


class SolutionSubDetailView(generic.DetailView):
    model = SolutionSubCategory
    template_name = 'app/solution_sub_category_detail.html'
    context_object_name = 'detail'
    slug_url_kwarg = 'slug' 

def sectors(request):
    return render(request,'app/sectors.html')

def sector_detail(request):
    return render(request,'app/sectors_detail.html')

def location(request):
    return render(request,'app/location.html')

def testimonials(request):
    return render(request,'app/testimonials.html')

def careers(request):
    return render(request,'app/careers.html')

