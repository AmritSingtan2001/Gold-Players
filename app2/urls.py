from django.urls import path
from . import views 
app_name ='dashboard'

urlpatterns = [
        path('',views.index,name='index'),
        path('about/', views.aboutUs, name='about'),
        path('about/organizatin/setting', views.organizationsetting, name='organizations_setting'),
        path('about/objective',views.organization_objectives, name='objective')

]