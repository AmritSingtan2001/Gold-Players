from django.urls import path
from . import views 
from . views import *


app_name ='dashboard'

urlpatterns = [
        path('',views.index,name='index'),

        path('banners/', BannarListView.as_view(), name="banners"),
        path('banners/create', BannerCreateView.as_view(), name='banner_create'),
        path('banners/delete/<int:id>', views.delete_banner, name='banner_delete'),

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
        path('sectors',SectorListView.as_view(), name='sectors'),
        path('sectors/create',SectorCreateView.as_view(), name='sector_create'),
        path('sectors/update/<slug:slug>',SectorUpdateView.as_view(), name='update_sector'),
        path('sectors/delete/<slug:slug>', views.delete_sectors, name='delete_sectors'),


        path('about/solution', views.aboutSolution, name='solution'),
        path('solutions', SolutionListView.as_view(), name='solution_list'),
        path('solutions/create', SolutionCreateView.as_view(), name='solution_create'),
        path('solutions/update/<slug:slug>', SolutionUpdateView.as_view(), name='solution_update'),
        path('solutions/delete/<slug:slug>', views.delete_solution, name='delete_solution'),


        path('solution/sub-category',SolutionSubCategoryListView.as_view(), name='solution_sub_category'),
        path('solution/sub-category/create',SolutionSubCategoryCreateView.as_view(), name='solution_sub_category_create'),
        path('solution/sub-category/update/<slug:slug>',SolutionSubCategoryUpdateView.as_view(), name='solution_sub_category_update'),
        path('solution/sub-category/delete/<slug:slug>', views.delete_SolutionSubCategor, name='delete_solution_sub_category'),


        path('associated/company',AssocialtedCompanyListView.as_view(), name='associated_company_list'),
        path('associated/company/create',AssociatedCreateView.as_view(), name='associated_company_create'),
        path('associated/compnay/update/<int:id>',AssociatedCompanyUpdateView.as_view(), name='associated_company_update'),
        path('associated/company/delete/<int:id>', views.delete_Associated_company, name='associated_company_delete'),


]