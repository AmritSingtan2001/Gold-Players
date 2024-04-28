from django.urls import path
from . import views 
from . views import *


app_name ='dashboard'

urlpatterns = [
        path('',views.index,name='index'),
        path('about/', views.aboutUs, name='about'),
        path('about/organizatin/setting', views.organizationsetting, name='organizations_setting'),
        path('about/objectives/add',ObjectiveCreatView.as_view(), name='objective_create'),
        path('about/objective',ObjectivesListView.as_view(), name='objective'),
        path('about/objective/detail/<int:id>',ObjectivesDetailView.as_view(), name='objective_detail'),
        path('about/objective/delete/<int:id>', views.objective_delete, name='objective_delete'),
        path('location', LocationListView.as_view(), name='locations'),
        path('location/add', LocationCreateView.as_view(), name='add_new_location'),
        path('location/update/<int:id>',LocationUpdateDetailView.as_view(), name='location_detail_update'),
        path('location/delete/<int:id>', views.location_delete, name='delete_location'),
        path('office', OfficeLocationListView.as_view(), name='office'),
        path('office/add', OfficeLocationCreateView.as_view(), name='add_office'),
        path('office/update/<int:id>',OfficeUpdateDetailView.as_view(),name='office_detail_update'),
        path('office/delete/<int:id>',views.office_delete, name='office_delete'),

        path('career/category', CareerCategoryListView.as_view(), name='career_category'),
        path('career/category/delete/<int:id>',views.delete_career_category, name='delete_category'),
        path('career/category/update',views.update_category, name='category_update'),

        path('careers', CareerListView.as_view(), name='careers_list'),
        path('careers/add',CareerCreateView.as_view(), name='career_create'),
        path('careers/update/<int:id>',CareerUpdateView.as_view(), name='career_update'),
        path('careers/delete/<int:id>', views.delete_career,name='delete_career'),

        path('testimonials', TestimonialsListView.as_view(), name='testimonials'),
        path('testimonials/add', TestimonialsCreateView.as_view(), name='testimonials_add'),
        path('testimonials/update/<int:id>', TestimonialsUpdateView.as_view(), name='testimonials_update'),
        path('testimonials/delete/<int:id>', views.delete_testimonials, name='delete_testimonials'),

        path('clients', ClientListCreateView.as_view(), name='client_list'),
        path('clients/delete/<int:id>',views.delete_client, name='delete_client'),


        path('resources/<slug:resource_type>',NewsResourcesListView.as_view(), name='resources_news'),
        path('resources/create/<slug:resource_type>/', NewsResourcesCreateView.as_view(), name='news_resources_create'),
        path('resources/update/<slug:slug>',NewsResourcesUpdateView.as_view(), name='resource_update'),
        path('resources/delete/<slug:slug>', views.delete_resources,name='delete_resources'),


        path('about/sector', views.aboutSector, name='about_sector'),
]