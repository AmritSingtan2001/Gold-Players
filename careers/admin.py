from django.contrib import admin
from . models import Careers,Category

class CategoryAdmin(admin.ModelAdmin):
    model =Category
    list_display=['category_name']
admin.site.register(Category,CategoryAdmin)

class CareersAdmin(admin.ModelAdmin):
    model = Careers
    list_display =['job_title','created_date','valid_date']
admin.site.register(Careers, CareersAdmin)