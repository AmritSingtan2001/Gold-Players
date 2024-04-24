from django.contrib import admin
from .models import About,Objective,OrganizationSetting

admin.site.site_header = 'Gold Player'                   
admin.site.index_title = 'Gold Player'                 
admin.site.site_title = 'Gold Player'



class OrganizationSettingAdmin(admin.ModelAdmin):
    model = OrganizationSetting
    list_display =['site_name','phone_number','email','logo']

    def has_add_permission(self, request):
        existing_objects_count = self.model.objects.count()
        return existing_objects_count == 0
    
admin.site.register(OrganizationSetting,OrganizationSettingAdmin)

class AboutAdmin(admin.ModelAdmin):
    model = About
    list_display =['title','image']

    def has_add_permission(self, request):
        existing_objects_count = self.model.objects.count()
        return existing_objects_count == 0

admin.site.register(About,AboutAdmin)


class ObjectiveAdmin(admin.ModelAdmin):
    model = Objective
    list_display =['title','image']
admin.site.register(Objective,ObjectiveAdmin)