# Generated by Django 5.0.4 on 2024-04-23 08:46

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True)),
                ('image', models.ImageField(upload_to='careerimage/', verbose_name='Company Logo')),
                ('job_title', models.CharField(max_length=150, verbose_name='Job Title')),
                ('location', models.CharField(max_length=150, verbose_name='Location')),
                ('salary', models.CharField(blank=True, max_length=150, null=True, verbose_name='Salary')),
                ('valid_date', models.DateField(verbose_name='Valid Date')),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='Job Descriptions(responsibility,qualification)')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=150, verbose_name='Job Title'))),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
