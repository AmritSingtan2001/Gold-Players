from django.contrib import admin
from . models import Office,Banner,AboutSolution, Solutions,SolutionSubCategory,Sector,AboutSector,Location,Client,Testimonials,AssocialtedCompany

class AboutSolutionAdmin(admin.ModelAdmin):
    model = AboutSolution
    list_display =['title','bannar_image']
admin.site.register(AboutSolution, AboutSolutionAdmin)

class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display =['id','bannar_image'] 
admin.site.register(Banner, BannerAdmin)

class SolutionAdmin(admin.ModelAdmin):
    model = Solutions
    list_display =['title','icon_image','image','short_descriptions']
admin.site.register(Solutions,SolutionAdmin)


class SolutionSubCategoryAdmin(admin.ModelAdmin):
    model = SolutionSubCategory
    list_display =['sub_category_name','category','image']
admin.site.register(SolutionSubCategory,SolutionSubCategoryAdmin)


class AboutSectorAdmin(admin.ModelAdmin):
    model =AboutSector
    list_display =['title','image']
admin.site.register(AboutSector, AboutSectorAdmin)

class SectorAdmin(admin.ModelAdmin):
    model= Sector
    list_display =['id','title','icon_image']
admin.site.register(Sector, SectorAdmin)


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display =['company_name','address']
admin.site.register(Location, LocationAdmin)


class OfficeAdmin(admin.ModelAdmin):
    model  = Office
    list_display =['office_name','image','map_url']
admin.site.register(Office,OfficeAdmin)


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display =['id','client_logo']
admin.site.register(Client, ClientAdmin)


class TestimonialsAdmin(admin.ModelAdmin):
    model =Testimonials
    list_display =['name','image','position']
admin.site.register(Testimonials,TestimonialsAdmin)


class AssocialtedCompanyAdmin(admin.ModelAdmin):
    model = AssocialtedCompany
    list_display =['company_name','company_logo','website_url']
admin.site.register(AssocialtedCompany, AssocialtedCompanyAdmin)