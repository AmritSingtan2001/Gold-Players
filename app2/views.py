from django.http import HttpRequest
from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect,get_object_or_404
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
    context_object_name ='resources'
    template_name ='app2/resources_list.html'

    def get_context_data(self, *args, **kwargs):
        context= super().get_context_data(**kwargs)
        resources_slug = self.kwargs.get('resource_type')
        context['resource_type'] = resources_slug
        context['news_resources'] = self.model.objects.filter(resource_type=resources_slug)
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
class AboutSectorListView(generic.ListView):
    model = AboutSector
    template_name ='app2/about_sector.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_sector'] = self.get_queryset().first()
        return context
    