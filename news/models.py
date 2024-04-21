from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

RESOURCES_TYPE =[
    ('news','News'),
    ('insights','Insights'),
    ('case_studies','Case Studies')
]

'''RESOURCES model'''
class Resources(models.Model):
    resource_type = models.CharField(max_length=150, verbose_name='Select Resource Type',choices=RESOURCES_TYPE, default='news')
    title = models.CharField(max_length=150, verbose_name='Title')
    image = models.ImageField(upload_to='resourcesimage/',verbose_name='Select Image')
    descriptions = RichTextField(verbose_name='Descriptions')
    slug = AutoSlugField(populate_from ='title', default=None, unique=True)


    class Meta:
        ordering =['id']
        verbose_name='Resources'
        verbose_name_plural = 'Resources'

    def __str__(self) -> str:
        return self.title
    
    

        