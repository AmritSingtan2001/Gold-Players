from django.contrib import admin
from . models import Resources

class ResourcesAdmin(admin.ModelAdmin):
    model = Resources
    list_display =['title','image']
admin.site.register(Resources, ResourcesAdmin)