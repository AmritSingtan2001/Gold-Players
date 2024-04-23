from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

class Careers(models.Model):
    image = models.ImageField(upload_to='careerimage/', verbose_name='Company Logo')
    job_title = models.CharField(verbose_name='Job Title', max_length=150)
    location = models.CharField(verbose_name='Location', max_length=150)
    salary = models.CharField(verbose_name='Salary', max_length=150, null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    valid_date = models.DateField(verbose_name='Valid Date')
    descriptions = RichTextField(verbose_name='Job Descriptions(responsibility,qualification)')
    slug = AutoSlugField(populate_from=job_title)

    class Meta:
        ordering =['-id']

    def __str__(self):
        return self.job_title
    