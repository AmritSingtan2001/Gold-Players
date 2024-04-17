from django.shortcuts import render, HttpResponse


def index(request):
    return render(request,'app/index.html')


def blog(request):
    return render(request,'app/blog.html')

def blog_detail(request):
    return render(request,'app/blog-single.html')