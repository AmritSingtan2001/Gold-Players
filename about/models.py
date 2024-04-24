from django.db import models
from ckeditor.fields import RichTextField


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