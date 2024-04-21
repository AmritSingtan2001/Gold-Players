from django.db import models

''' bannar model '''
class Banner(models.Model):
    bannar_image = models.ImageField(upload_to='bannerimage/')


    def __str__(self):
        return str(self.id)
    
