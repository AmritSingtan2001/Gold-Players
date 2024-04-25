from django.urls import path
from . import views 
from . views import ObjectiveCreatView,ObjectivesListView,ObjectivesDetailView


app_name ='dashboard'

urlpatterns = [
        path('',views.index,name='index'),
        path('about/', views.aboutUs, name='about'),
        path('about/organizatin/setting', views.organizationsetting, name='organizations_setting'),
        path('about/objectives/add',ObjectiveCreatView.as_view(), name='objective_create'),
        path('about/objective',ObjectivesListView.as_view(), name='objective'),
        path('about/objective/detail/<int:id>',ObjectivesDetailView.as_view(), name='objective_detail'),
        path('about/objective/delete/<int:id>', views.objective_delete, name='objective_delete')

]