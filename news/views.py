from django.shortcuts import render
from . models import Resources
from django.views import generic


class ResourcseListView(generic.ListView):
    model = Resources
    template_name ='news/resources.html'
    context_object_name ='resources'


def blog(request):
    return render(request,'app/blog.html')

def blog_detail(request):
    return render(request,'app/blog-single.html')