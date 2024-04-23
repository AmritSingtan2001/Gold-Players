from django.shortcuts import render
from .models import Banner,AboutSolution,Office,Solutions,SolutionSubCategory,AboutSector,Sector,Location,Client,Testimonials
from news.models import Resources
from django.views import generic

class IndexView(generic.ListView):
    model = Banner
    template_name ='app/index.html'
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = self.get_queryset
        context['allsolutions'] = Solutions.objects.all()
        context['sectors'] = Sector.objects.all()
        context['locations'] = Location.objects.all()
        context['clients'] = Client.objects.all()
        context['all_news'] = Resources.objects.filter(resource_type='news')
        context['insights'] = Resources.objects.filter(resource_type='insights')
        context['case_studies'] = Resources.objects.filter(resource_type='case_studies')
        context['testimonials'] = Testimonials.objects.all()
        return context


def aboutus(request):
    return render(request,'app/about.html')



def solution(request):
    about_solution = AboutSolution.objects.first()
    allsolutions= Solutions.objects.all()
    return render(request,'app/solutions.html',{'about_solution':about_solution,'allsolutions':allsolutions})


class SolutionDetailView(generic.DetailView):
    model = Solutions
    template_name = 'app/solution_detail.html'
    context_object_name = 'detail'
    slug_url_kwarg = 'slug' 


class SolutionSubDetailView(generic.DetailView):
    model = SolutionSubCategory
    template_name = 'app/solution_sub_category_detail.html'
    context_object_name = 'detail'
    slug_url_kwarg = 'slug' 

def sectors(request):
    about_sectors = AboutSector.objects.first()
    sectors = Sector.objects.all()
    return render(request,'app/sectors.html',{'about_sectors':about_sectors,'sectors':sectors})


class SectorbDetailView(generic.DetailView):
    model = Sector
    template_name = 'app/sectors_detail.html'
    context_object_name = 'detail'
    slug_url_kwarg = 'slug'


class LocationsList(generic.ListView):
    model = Location
    template_name = 'app/location.html'
    context_object_name = 'locations'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['locations'] = self.get_queryset()
        context['offices'] = Office.objects.all()
        return context
        


class TestimonialsListView(generic.ListView):
    model = Testimonials
    template_name = 'app/testimonials.html'
    context_object_name = 'testimonials'

    
 
def careers(request):
    return render(request,'app/careers.html')

