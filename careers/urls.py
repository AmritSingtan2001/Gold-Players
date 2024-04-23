
from django.urls import path
from . import views
from .views import CareersListView
app_name ='careers'


urlpatterns = [
    path('', CareersListView.as_view(), name='careers'),
]
