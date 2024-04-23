
from django.urls import path
from . import views
from .views import ResourcseListView,ResourceDetailView,NewsResourcseListView,InsightsResourcseListView,CaseStudiesResourcseListView
app_name ='resources'


urlpatterns = [
    path('', ResourcseListView.as_view(), name='all_resources'),
    path('detail/<slug:slug>', ResourceDetailView.as_view(), name='resource_detail'),
    path('news',NewsResourcseListView.as_view(), name='resources_news'),
    path('insights',InsightsResourcseListView.as_view(), name='resources_insight'),
    path('case-studies',CaseStudiesResourcseListView.as_view(), name='resources_case_studies'),

]
