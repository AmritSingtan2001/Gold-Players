from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect,get_object_or_404
from django.views import View
from . decorators import login_required
from django.contrib import messages
from . forms import *
from app.models import *
from about.models import *
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


