from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

''' bannar model '''
class Banner(models.Model):
    bannar_image = models.ImageField(upload_to='bannerimage/')


    def __str__(self):
        return str(self.id)
    

class Solutions(models.Model):
    icon_image = models.ImageField(verbose_name='Solution Icon Image',upload_to='solutionimages/')
    image = models.ImageField(verbose_name='Solution Main Image',upload_to='solutionimages/')
    title = models.CharField(verbose_name='Solution Name',max_length=150)
    short_descriptions = models.TextField(verbose_name='Enter short descriptions', max_length=300)
    descriptions = models.TextField(verbose_name='Enter descriptions')
    class Meta:
        ordering =['id']
        verbose_name='Solution'
        verbose_name_plural = 'Solutions'

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('solution-detail', kwargs={'pk': self.pk})

'''Sector model '''
class Sector(models.Model):
    icon_image = models.ImageField(upload_to='sectorsicon/',verbose_name='Choose Icon Image')
    title = models.CharField(max_length=150,verbose_name='Enter Title')
    descriptions = models.TextField(verbose_name='Enter descriptions')
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
    country = models.CharField(verbose_name='Enter Country', max_length=150)
    logo = models.ImageField(upload_to='logo/')
    company_name = models.CharField(max_length=150)
    post_box = models.CharField(verbose_name='Enter Post Box Number', max_length=150,null=True,blank=True)
    postal_code = models.CharField(verbose_name='Enter Postal Code', max_length=150, null=True,blank=True)
    address = models.CharField(verbose_name='Enter Address', max_length=150)
    office_hours = models.DateTimeField(verbose_name='Select Office Hours')
    phone_number = models.CharField(verbose_name='Enter Phone Number', max_length=150)
    map_image  = models.ImageField(verbose_name='Please Upload map image like jpb,png',upload_to='mapimage/')
    map_url = models.URLField(verbose_name='Google Map Url', null=True,blank=True)

    class Meta:
        ordering =['id']
        verbose_name='Location'
        verbose_name_plural = 'Locations'

    def __str__(self) -> str:
        return self.company_name
    
    def get_absolute_url(self):
        return reverse('location-detail', kwargs={'pk': self.pk})


    
