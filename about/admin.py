from django.contrib import admin
from .models import About,Objective

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