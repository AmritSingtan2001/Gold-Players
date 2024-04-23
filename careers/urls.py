
from django.urls import path
from . import views
from .views import CareersListView,CareerDetailView
app_name ='careers'


urlpatterns = [
    path('', CareersListView.as_view(), name='careers'),
    path('<slug:slug>', CareerDetailView.as_view(), name='career_detail'),
]
