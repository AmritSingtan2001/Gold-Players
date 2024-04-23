from django.contrib import admin
from . models import Careers

class CareersAdmin(admin.ModelAdmin):
    model = Careers
    list_display =['job_title','created_date','valid_date']
admin.site.register(Careers, CareersAdmin)