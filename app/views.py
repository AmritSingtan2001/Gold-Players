from django.shortcuts import render, HttpResponse


def index(request):
    return render(request,'app/index.html')

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

