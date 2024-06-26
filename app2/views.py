from django.http import HttpRequest
from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from . decorators import login_required
from django.contrib import messages
from . forms import *
from app.models import *
from about.models import *
from careers.models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


''''index page'''
@login_required
def index(request):
    return render(request,'app2/index.html')



'''bannar '''
class BannarListView(generic.ListView):
    model = Banner
    context_object_name ='banners'
    template_name ='app2/banner.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BannerForm()  
        return context
    

class BannerCreateView(generic.CreateView):
    model = Banner
    form_class = BannerForm
    
    def get_success_url(self) -> str:
        messages.success(self.request,'Banner Created successfully !')
        return reverse_lazy('dashboard:banners')

@login_required
def delete_banner(request, id):
    instance = get_object_or_404(Banner, id=id)
    instance.delete()
    messages.success(request, "Deleted Successfully!")
    return redirect('dashboard:banners')

    
    
''' about organization'''
@login_required
def aboutUs(request):
    instance = None
    try:
        if id:
            instance = About.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the AboutUS.')
        return redirect('dashboard:aboutUs')

    if request.method == 'POST':
        form = AboutUSForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance: 
                messages.success(request, 'AboutUS edited successfully.')
                return redirect('dashboard:about') 
            else: 
                messages.success(request, 'AboutUS added successfully.')
                return redirect('dashboard:about') 
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = AboutUSForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_about_us.html', context)

'''organization settings '''
@login_required
def organizationsetting(request):
    instance = None
    try:
        if id:
            instance = OrganizationSetting.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the AboutUS.')
        return redirect('dashboard:organizations_setting')

    if request.method == 'POST':
        form = OrganizationSettingForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance: 
                messages.success(request, 'AboutUS edited successfully.')
                return redirect('dashboard:organizations_setting') 
            else: 
                messages.success(request, 'AboutUS added successfully.')
                return redirect('dashboard:organizations_setting') 
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = OrganizationSettingForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/organization_setting.html', context)

'''objectives '''
@method_decorator(login_required, name='dispatch')
class ObjectiveCreatView(generic.CreateView):
    model = Objective
    template_name = 'app2/objectivs_detail.html'
    form_class = ObjectiveForm
    def get_success_url(self):
        return reverse_lazy('dashboard:objective')
    
@method_decorator(login_required, name='dispatch')
class ObjectivesListView(generic.ListView):
    model = Objective
    template_name ='app2/objectivs.html'
    context_object_name ='objectives'
    paginate_by =5

@method_decorator(login_required, name='dispatch')
class ObjectivesDetailView(generic.UpdateView):
    model = Objective
    template_name ='app2/objectivs_detail.html'
    context_object_name ='objective_detail'
    pk_url_kwarg ='id'
    form_class = ObjectiveForm
    def get_success_url(self):
        messages.success(self.request,'Updated Successfully !')
        return reverse_lazy('dashboard:objective_detail', kwargs={'id': self.object.id})

@login_required
def objective_delete(request, id):
    objective = get_object_or_404(Objective, id=id)
    objective.delete()
    messages.success(request, "Deleted Successfully!")
    return redirect('dashboard:objective')



'''' Location '''
@method_decorator(login_required, name='dispatch')
class LocationListView(generic.ListView):
    model = Location
    template_name ='app2/location.html'
    context_object_name ='locations'


@method_decorator(login_required, name='dispatch')
class LocationCreateView(generic.CreateView):
    model = Location
    template_name ='app2/location_form.html'
    form_class = LocationForm
    def get_success_url(self):
        return reverse_lazy('dashboard:locations')
    

@method_decorator(login_required, name='dispatch')
class LocationUpdateDetailView(generic.UpdateView):
    model = Location
    template_name ='app2/location_form.html'
    pk_url_kwarg ='id'
    form_class = LocationForm
    def get_success_url(self):
        messages.success(self.request,'Updated Successfully !')
        return reverse_lazy('dashboard:location_detail_update', kwargs={'id': self.object.id})

@login_required
def location_delete(request, id):
    instance = get_object_or_404(Location, id=id)
    instance.delete()
    messages.success(request, "Deleted Successfully!")
    return redirect('dashboard:locations')


''' office section '''
@method_decorator(login_required, name='dispatch')
class OfficeLocationListView(generic.ListView):
    model = Office
    template_name ='app2/office.html'
    context_object_name ='office_locations'


@method_decorator(login_required, name='dispatch')
class OfficeLocationCreateView(generic.CreateView):
    model = Office
    template_name ='app2/office_form.html'
    form_class = OfficeForm
    def get_success_url(self):
        return reverse_lazy('dashboard:office')

@method_decorator(login_required, name='dispatch')
class OfficeUpdateDetailView(generic.UpdateView):
    model = Office
    template_name ='app2/office_form.html'
    pk_url_kwarg ='id'
    form_class = OfficeForm
    def get_success_url(self):
        messages.success(self.request,'Updated Successfully !')
        return reverse_lazy('dashboard:office_detail_update', kwargs={'id': self.object.id})


@login_required
def office_delete(request, id):
    instance = get_object_or_404(Office, id=id)
    instance.delete()
    messages.success(request, "Deleted Successfully!")
    return redirect('dashboard:office')


''' career category '''
@method_decorator(login_required, name='dispatch')
class CareerCategoryListView(generic.ListView):
    model = Category
    context_object_name ='categories'
    template_name ='app2/career_category.html'

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(**kwargs)
        context['form'] = CareerCategoryForm
        return context
    
    def post(self, request, *args, **kwargs):
        form = CareerCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
@login_required
def update_category(request):
    if request.method =="POST":
        id = request.POST.get('category_id')
        instance = Category.objects.get(id=id)
        instance.category_name = request.POST.get('category_name')
        instance.save()
        return redirect('dashboard:career_category')
    else:
        return redirect('dashboard:career_category')
    
@login_required   
def delete_career_category(request,id):
    instance = Category.objects.get(id=id)
    instance.delete()
    messages.success(request,'Category Delete Successfully !')
    return redirect('dashboard:career_category')


''' Careers '''
@method_decorator(login_required, name='dispatch')
class CareerListView(generic.ListView):
    model = Careers
    template_name ='app2/careers.html'
    context_object_name ='careers'
    paginate_by =5


@method_decorator(login_required, name='dispatch')
class CareerCreateView(generic.CreateView):
    model = Careers
    template_name ='app2/career_form.html'
    form_class = CareerForm
    def get_success_url(self):
        messages.success(self.request,"Career Added Successfully !")
        return reverse_lazy('dashboard:careers_list')



@method_decorator(login_required, name='dispatch')
class CareerUpdateView(generic.UpdateView):
    model = Careers
    template_name ='app2/career_form.html'
    pk_url_kwarg ='id'
    form_class = CareerForm
    def get_success_url(self):
        messages.success(self.request,'Career Updated Successfully !')
        return reverse_lazy('dashboard:career_update', kwargs={'id': self.object.id})
    

@login_required
def delete_career(request,id):
    Careers.objects.get(id=id).delete()
    messages.success(request,"Deleted Successfully !")
    return redirect('dashboard:careers_list')

    
'''testimonials '''
@method_decorator(login_required, name='dispatch')
class TestimonialsListView(generic.ListView):
    model = Testimonials
    template_name ='app2/testimonials.html'
    context_object_name ='testimonials'
    paginate_by =5

@method_decorator(login_required, name='dispatch')
class TestimonialsCreateView(generic.CreateView):
    model = Testimonials 
    template_name ='app2/testimonials_form.html'
    form_class = TestimonialsForm
    def get_success_url(self):
        messages.success(self.request,"New Testimonials Created Successfully !")
        return reverse_lazy('dashboard:testimonials')


@method_decorator(login_required, name='dispatch')
class TestimonialsUpdateView(generic.UpdateView):
    model = Testimonials
    template_name ='app2/testimonials_form.html'
    pk_url_kwarg ='id'
    form_class = TestimonialsForm
    def get_success_url(self):
        messages.success(self.request,'Testimonials Updated Successfully !')
        return reverse_lazy('dashboard:testimonials_update', kwargs={'id': self.object.id})
    
@login_required
def delete_testimonials(request, id):
    Testimonials.objects.get(id=id).delete()
    messages.success(request,'Testimonials Deleted Successfully !')
    return redirect('dashboard:testimonials')


'''client section '''
@method_decorator(login_required, name='dispatch')
class ClientListCreateView(generic.ListView):
    model = Client
    context_object_name ='clients'
    template_name ='app2/client_list.html'
    paginate_by =5

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(**kwargs)
        context['form'] = ClientForm
        return context
    
    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        

@login_required
def delete_client(request, id):
    Client.objects.get(id=id).delete()
    messages.success(request,'Client Deleted Successfully !')
    return redirect('dashboard:client_list')



''' resources '''
@method_decorator(login_required, name='dispatch')
class NewsResourcesListView(generic.ListView):
    model = Resources
    template_name = 'app2/resources_list.html'
    paginate_by = 5

    def get_queryset(self):
        resources_slug = self.kwargs.get('resource_type')
        return self.model.objects.filter(resource_type=resources_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resources_slug = self.kwargs.get('resource_type')
        context['resource_type'] = resources_slug
        return context
   
@method_decorator(login_required, name='dispatch')
class NewsResourcesCreateView(generic.CreateView):
    model = Resources
    template_name = 'app2/resources_form.html'
    form_class = ResourcesForm  

    def form_valid(self, form):
        form.instance.resource_type = self.kwargs.get('resource_type')
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request,f"New - {self.kwargs.get('resource_type')} created successfully !")
        return reverse_lazy('dashboard:resources_news', kwargs={'resource_type': self.kwargs.get('resource_type')})
    

@method_decorator(login_required, name='dispatch')
class NewsResourcesUpdateView(generic.UpdateView):
    model = Resources
    template_name = 'app2/resources_form.html'
    form_class = ResourcesForm  
    slug_url_kwarg ='slug'
    
    def get_success_url(self):
        messages.success(self.request,f"Update successfully !")
        return reverse_lazy('dashboard:resource_update', kwargs={'slug': self.object.slug})
    

@login_required
def delete_resources(request, slug):
    instance =Resources.objects.get(slug=slug)
    resource_type= instance.resource_type
    instance.delete()
    messages.success(request,'Deleted Successfully !')
    return redirect('dashboard:resources_news', resource_type)


''' about sector '''
@login_required
def aboutSector(request):
    instance = None
    try:
        if id:
            instance = AboutSector.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the About Sector.')
        return redirect('dashboard:about_sector')

    if request.method == 'POST':
        form = AboutSectorForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance: 
                messages.success(request, 'About Sector edited successfully.')
                return redirect('dashboard:about_sector') 
            else: 
                messages.success(request, 'About Sector added successfully.')
                return redirect('dashboard:about_sector') 
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = AboutSectorForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/about_sector.html', context)

    
'''sectors'''
@method_decorator(login_required, name='dispatch')
class SectorListView(generic.ListView):
    model = Sector
    context_object_name ='sectors'
    template_name ='app2/sector_list.html'
    paginate_by = 5

@method_decorator(login_required, name='dispatch')
class SectorCreateView(generic.CreateView):
    model = Sector
    form_class = SectorForm
    template_name ='app2/sector_form.html'
    context_object_name ='forms'
    
    def get_success_url(self) -> str:
        messages.success(self.request,"New Sector created successfully !")
        return reverse_lazy("dashboard:sector_create")
    
@method_decorator(login_required, name='dispatch')
class SectorUpdateView(generic.UpdateView):
    model = Sector
    form_class = SectorForm
    slug_url_kwarg ='slug'
    template_name ='app2/sector_form.html'

    def get_success_url(self) -> str:
        messages.success(self.request,'Sector updated successfully')
        return reverse_lazy('dashboard:update_sector', kwargs={'slug': self.object.slug})
    
@login_required
def delete_sectors(request, slug):
    Sector.objects.get(slug=slug).delete()
    messages.success(request,'Deleted Successfully !')
    return redirect('dashboard:sectors')


'''solution '''
@login_required
def aboutSolution(request):
    instance = None
    try:
        if id:
            instance = AboutSolution.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the About Solution.')
        return redirect('dashboard:solution')

    if request.method == 'POST':
        form = AboutSolutionForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance: 
                messages.success(request, 'About Solution edited successfully.')
                return redirect('dashboard:solution') 
            else: 
                messages.success(request, 'About Solution added successfully.')
                return redirect('dashboard:solution') 
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = AboutSolutionForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/about_solution.html', context)




''' solution '''
@method_decorator(login_required, name='dispatch')
class SolutionListView(generic.ListView): 
    model = Solutions
    context_object_name ='solutions'
    template_name='app2/soliton_list.html'
    paginate_by =5

@method_decorator(login_required, name='dispatch')
class SolutionCreateView(generic.CreateView):
    model = Solutions
    form_class = SolutionForm
    template_name ='app2/solution_form.html'
    context_object_name ='forms'
    
    def get_success_url(self) -> str:
        messages.success(self.request,"New Solution created successfully !")
        return reverse_lazy("dashboard:sector_create")
    
@method_decorator(login_required, name='dispatch')
class SolutionUpdateView(generic.UpdateView):
    model= Solutions
    form_class = SolutionForm
    slug_url_kwarg ='slug'
    template_name ='app2/solution_form.html'
    def get_success_url(self) -> str:
        messages.success(self.request,f'{self.object.title} - updated successfully')
        return reverse_lazy('dashboard:solution_update', kwargs={'slug': self.object.slug})
    

@login_required
def delete_solution(request, slug):
    Solutions.objects.get(slug=slug).delete()
    messages.success(request,'Deleted Successfully !')
    return redirect('dashboard:solution_list')



''' solution sub category '''
@method_decorator(login_required, name='dispatch')
class SolutionSubCategoryListView(generic.ListView):
    model = SolutionSubCategory
    template_name ='app2/solution_sub_category.html'
    context_object_name ='solution_sub_categories'
    paginate_by =5
    

@method_decorator(login_required, name='dispatch')
class SolutionSubCategoryCreateView(generic.CreateView):
    model = SolutionSubCategory
    form_class = SolutionSubCategoryForm
    template_name ='app2/solution_sub_category_form.html'

    def get_success_url(self) -> str:
        messages.success(self.request,"Solution sub-category created successfully !")
        return reverse_lazy("dashboard:solution_sub_category_create")
    
@method_decorator(login_required, name='dispatch')
class SolutionSubCategoryUpdateView(generic.UpdateView):
    model= SolutionSubCategory
    form_class = SolutionSubCategoryForm
    slug_url_kwarg ='slug'
    template_name ='app2/solution_sub_category_form.html'
    def get_success_url(self) -> str:
        messages.success(self.request,f'{self.object.sub_category_name} - updated successfully')
        return reverse_lazy('dashboard:solution_sub_category_update', kwargs={'slug': self.object.slug})
    
@login_required
def delete_SolutionSubCategor(request, slug):
    SolutionSubCategory.objects.get(slug=slug).delete()
    messages.success(request,'Deleted Successfully !')
    return redirect('dashboard:solution_sub_category')


'''associated company '''
@method_decorator(login_required, name='dispatch')
class AssocialtedCompanyListView(generic.ListView):
    model = AssocialtedCompany
    context_object_name='associated_companies'
    template_name ='app2/associated_company.html'
    paginate_by =5

@method_decorator(login_required, name='dispatch')
class AssociatedCreateView(generic.CreateView):
    model = AssocialtedCompany
    form_class = AssocialtedCompanyForm
    template_name ='app2/associated_company_form.html'

    def get_success_url(self) -> str:
        messages.success(self.request,"New associated company added successfully !")
        return reverse_lazy("dashboard:associated_company_create")
    

@method_decorator(login_required, name='dispatch')
class AssociatedCompanyUpdateView(generic.UpdateView):
    model = AssocialtedCompany
    form_class = AssocialtedCompanyForm
    pk_url_kwarg ='id'
    template_name ='app2/associated_company_form.html'

    def get_success_url(self) -> str:
        messages.success(self.request,f'{self.object.company_name} - updated successfully')
        return reverse_lazy('dashboard:associated_company_update', kwargs={'id': self.object.id})
    

@login_required
def delete_Associated_company(request, id):
    AssocialtedCompany.objects.get(id=id).delete()
    messages.success(request,'Associated Company Deleted Successfully !')
    return redirect('dashboard:associated_company_list')