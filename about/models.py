from django.db import models
from ckeditor.fields import RichTextField


'''organization setting'''
class OrganizationSetting(models.Model):
    logo =models.ImageField(verbose_name='Organization Logo',upload_to='aboutus/')
    fav_icon = models.ImageField(verbose_name='Organization Fav Icon',upload_to='aboutus/')
    site_name = models.CharField(verbose_name='Organization Name',max_length=150)
    phone_number = models.CharField(verbose_name='Organization Phone Number',max_length=150)
    email = models.EmailField(verbose_name='Organization Email')
    fb_url = models.URLField(verbose_name='Facebook Page URL', null=True,blank=True)
    tw_url = models.URLField(verbose_name='Twitter URL', null=True,blank=True)
    insta_url = models.URLField(verbose_name='Instagram Page URL', null=True,blank=True)
    linkedin_url = models.URLField(verbose_name='Linkedin URL', null=True,blank=True)



    def __str__(self) -> str:
        return self.site_name




'''about '''
class About(models.Model):
    title = models.CharField(verbose_name='About Title',max_length=150)
    image = models.ImageField(verbose_name='About Image',upload_to='aboutus/')
    short_descriptions = RichTextField(verbose_name='About Short Descriptions')
    descriptions = RichTextField(verbose_name='About Descriptions')

    def __str__(self) -> str:
        return self.title


''' company objectives model '''
class Objective(models.Model):
    title = models.CharField(verbose_name='Objective Title',max_length=150)
    image = models.ImageField(verbose_name='Objective Image',upload_to='aboutus/')
    descriptions = RichTextField(verbose_name='Descriptions')

    class Meta:
        ordering =['id']
        verbose_name = 'Our Objective'
        verbose_name_plural = "Our Objectives"



    def __str__(self) -> str:
        return self.title