
from django.urls import path
from . import views
app_name ='account'


urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.userlogout, name="logout"),
    path('profile', views.userprofile, name ="profile"),
    path('change/password', views.change_password_view, name='change_password'),
]
