
from django.urls import path
from . import views
from .views import AboutDetailView
app_name ='about'


urlpatterns = [
    path('', AboutDetailView.as_view(), name='about_us'),
]
