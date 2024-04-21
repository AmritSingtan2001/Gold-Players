from django.contrib import admin
from . models import Banner, Solutions

class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display =['id','bannar_image'] 
admin.site.register(Banner, BannerAdmin)

class SolutionAdmin(admin.ModelAdmin):
    model = Solutions
    list_display =['title','icon_image','image']
admin.site.register(Solutions,SolutionAdmin)
