from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


app_name ='dashboard'
urlpatterns = [
        path('',views.index,name='index'),
        path('about/', views.aboutUs, name='about'),
        path('about/organizatin/setting', views.organizationsetting, name='organizations_setting')

]+ static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)