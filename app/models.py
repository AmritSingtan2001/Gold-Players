from django.db import models
from django.urls import reverse

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
    
