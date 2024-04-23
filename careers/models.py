from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

''' career category'''
class Category(models.Model):
    category_name = models.CharField(verbose_name='Career Category Name' ,max_length=150)


    def __str__(self):
        return self.category_name
    

'''career model '''
class Careers(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True, verbose_name='Choose Career Category')
    company_logo = models.ImageField(upload_to='careerimage/', verbose_name='Company Logo')
    job_title = models.CharField(verbose_name='Job Title', max_length=150)
    location = models.CharField(verbose_name='Location', max_length=150)
    salary = models.CharField(verbose_name='Salary', max_length=150, null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    valid_date = models.DateField(verbose_name='Valid Date')
    descriptions = RichTextField(verbose_name='Job Descriptions(responsibility,qualification)')
    slug = AutoSlugField(populate_from ='job_title', default=None, unique=True)

    class Meta:
        ordering =['-id']

    def __str__(self):
        return str(self.job_title)
    