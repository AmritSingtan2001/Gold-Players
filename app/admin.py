from django.contrib import admin
from . models import Banner, Solutions,Sector

class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display =['id','bannar_image'] 
admin.site.register(Banner, BannerAdmin)

class SolutionAdmin(admin.ModelAdmin):
    model = Solutions
    list_display =['title','icon_image','image','short_descriptions']
admin.site.register(Solutions,SolutionAdmin)


class SectorAdmin(admin.ModelAdmin):
    model= Sector
    list_display =['id','title','icon_image']
admin.site.register(Sector, SectorAdmin)