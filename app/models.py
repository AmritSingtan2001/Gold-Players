from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField



''' bannar model '''
class Banner(models.Model):
    bannar_image = models.ImageField(upload_to='bannerimage/', verbose_name='Select Banner Image *')


    def __str__(self):
        return str(self.id)
    

'''about slution'''
class AboutSolution(models.Model):
    title = models.CharField(verbose_name='Title *',max_length=150)
    bannar_image  = models.ImageField(verbose_name='Bannar Image *',upload_to='bannarimage/', null=True,blank=True)
    descriptions = RichTextField(verbose_name='Descriptions *')

    def __str__(self):
        return self.title
    


class Solutions(models.Model):
    icon_image = models.ImageField(verbose_name='Solution Icon Image *',upload_to='solutionimages/')
    image = models.ImageField(verbose_name='Solution Main Image *',upload_to='solutionimages/')
    title = models.CharField(verbose_name='Solution Name *',max_length=150)
    short_descriptions = models.TextField(verbose_name='Enter short descriptions *', max_length=300)
    descriptions = RichTextField(verbose_name='Enter descriptions *')
    slug = AutoSlugField(populate_from='title', unique=True, default=None)

    class Meta:
        ordering =['id']
        verbose_name='Solution'
        verbose_name_plural = 'Solutions'

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('solution-detail', kwargs={'pk': self.pk})
    

''' solution sub-category'''
class SolutionSubCategory(models.Model):
    category = models.ForeignKey( Solutions, on_delete= models.CASCADE, related_name='solution_sub_category',verbose_name='Select Category *')
    sub_category_name = models.CharField(verbose_name='Sub Category Name *', max_length=150)
    image = models.ImageField(verbose_name='Select Main Image *',upload_to='solutionimages/')
    short_descriptions = RichTextField(verbose_name='Short Descriptions *')
    descriptions = RichTextField(verbose_name='Descriptions *')
    slug = AutoSlugField(populate_from='sub_category_name *', unique=True, default=None)

    def __str__(self):
        return self.sub_category_name

'''About sector '''
class AboutSector(models.Model):
    title = models.CharField(verbose_name='Title * ',max_length=150)
    image = models.ImageField(verbose_name='Select Image * ',upload_to='sectorimage/')
    short_descriptions = RichTextField(verbose_name='Enter Short Descriptions * ')
    descriptions = RichTextField(verbose_name='Enter Descriptions * ')

    def __str__(self):
        return self.title
    



'''Sector model '''
class Sector(models.Model):
    icon_image = models.ImageField(upload_to='sectorsicon/',verbose_name='Choose Icon Image * ')
    image = models.ImageField(upload_to='sectorimage/', verbose_name='Select Image * ')
    title = models.CharField(max_length=150,verbose_name='Enter Title * ')
    short_descriptions =RichTextField(verbose_name='Short Description *',max_length=500)
    descriptions = RichTextField(verbose_name='Enter descriptions * ')
    slug = AutoSlugField(populate_from='title', unique=True, default=None)

    class Meta:
        ordering =['id']
        verbose_name='Sector'
        verbose_name_plural = 'Sectors'

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('sector-detail', kwargs={'pk': self.pk})


''' location model '''
class Location(models.Model):
    country = models.CharField(verbose_name='Enter Country * ', max_length=150)
    logo = models.ImageField(upload_to='logo/',verbose_name='Select Logo * ')
    company_name = models.CharField(max_length=150,verbose_name='Enter Company Name * ')
    post_box = models.CharField(verbose_name='Enter Post Box Number', max_length=150,null=True,blank=True)
    postal_code = models.CharField(verbose_name='Enter Postal Code', max_length=150, null=True,blank=True)
    address = models.CharField(verbose_name='Enter Address * ', max_length=150)
    office_hours = models.CharField(max_length=150, verbose_name='Select Office Hours * ')
    phone_number = models.CharField(verbose_name='Enter Phone Number * ', max_length=150)
    map_image  = models.ImageField(verbose_name='Please Upload map image like jpb,png * ',upload_to='mapimage/')
    map_url = models.URLField(verbose_name='Google Map Url * ', null=True,blank=True)

    class Meta:
        ordering =['id']
        verbose_name='Location'
        verbose_name_plural = 'Locations'

    def __str__(self) -> str:
        return self.company_name
    
    def get_absolute_url(self):
        return reverse('location-detail', kwargs={'pk': self.pk})
    

'''office model'''
class Office(models.Model):
    office_name = models.CharField(max_length=150, verbose_name='Office Name *')
    logo = models.ImageField(upload_to='Office Image/', verbose_name='Office Logo *')
    image  = models.ImageField(verbose_name='Office Image *', upload_to='Office Image/')
    map_url = models.URLField(verbose_name='Map URL *')
    descriptions = RichTextField(verbose_name='Short Description About Office Maximum 200 characters  *', max_length=200)


    def __str__(self):
        return self.office_name
    
    class Meta:
        ordering =['id']
    


''' client models '''
class Client(models.Model):
    client_logo = models.ImageField(upload_to='clientlogo/',verbose_name='Clent Logo *')

    def __str__(self):
        return str(self.id)

'''TESTIMONIALS '''
class Testimonials(models.Model):
    name = models.CharField(max_length=150, verbose_name='Enter Name *')
    position = models.CharField(max_length=150, null=True, blank=True, verbose_name='Enter Position')
    image = models.ImageField(upload_to='testimonialsimage/', verbose_name='Select Image *')
    descriptions = models.TextField(verbose_name='Enter Descriptions *')

    def __str__(self):
        return self.name



    