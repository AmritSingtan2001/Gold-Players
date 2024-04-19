
from django.urls import path
from . import views
app_name ='app'


urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('blog/detail', views.blog_detail, name='blog_detail'),
    path('about-us',views.aboutus, name='about'),
    path('solution',views.solution, name='solution'),
    path('solution/detail',views.solution_detail, name='solution_detail'),
    path('sectors', views.sectors, name='sectors'),
    path('sectors/detail', views.sector_detail, name='sector_detail'),
    path('location', views.location, name='location'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('careers', views.careers, name='careers'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
