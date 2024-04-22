from django.contrib import admin
from . models import Banner, Solutions,Sector,Location,Client,Testimonials

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


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display =['company_name','address']
admin.site.register(Location, LocationAdmin)


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display =['id','client_logo']
admin.site.register(Client, ClientAdmin)


class TestimonialsAdmin(admin.ModelAdmin):
    model =Testimonials
    list_display =['name','image','position']
admin.site.register(Testimonials,TestimonialsAdmin)