from django.contrib import admin
from . models import Banner

class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display =['id','bannar_image'] 
admin.site.register(Banner, BannerAdmin)
