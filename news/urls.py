
from django.urls import path
from . import views
from .views import ResourcseListView
app_name ='resources'


urlpatterns = [
    path('', ResourcseListView.as_view(), name='all_resources'),
    path('blog', views.blog, name='blog'),
    path('blog/detail', views.blog_detail, name='blog_detail'),
    
]
