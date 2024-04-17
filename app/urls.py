
from django.urls import path
from . import views
app_name ='app'


urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('blog/detail', views.blog_detail, name='blog_detail'),
]
