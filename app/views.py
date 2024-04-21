from typing import Any
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from .models import Banner,Solutions,Sector
from django.views import generic

class IndexView(generic.ListView):
    model = Banner
    template_name ='app/index.html'
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = self.get_queryset
        context['allsolutions'] = Solutions.objects.all()
        context['sectors'] = Sector.objects.all()
        return context


def aboutus(request):
    return render(request,'app/about.html')

def blog(request):
    return render(request,'app/blog.html')

def blog_detail(request):
    return render(request,'app/blog-single.html')

def solution(request):
    return render(request,'app/solutions.html')


def solution_detail(request):
    return render(request,'app/solution_detail.html')

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

