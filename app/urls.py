
from django.urls import path
from . import views
from .views import IndexView,SolutionDetailView,SolutionSubDetailView,SectorbDetailView,LocationsList,TestimonialsListView
app_name ='app'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about-us',views.aboutus, name='about'),
    path('solution',views.solution, name='solution'),
    path('solution/<slug:slug>',SolutionDetailView.as_view(), name='solution_detail'),
    path('solution/detail/<slug:slug>',SolutionSubDetailView.as_view(), name='solution_sub_detail'),
    path('sectors', views.sectors, name='sectors'),
    path('sectors/<slug:slug>', SectorbDetailView.as_view(), name='sector_detail'),
    path('location', LocationsList.as_view(), name='location'),
    path('testimonials', TestimonialsListView.as_view(), name='testimonials'),
]
