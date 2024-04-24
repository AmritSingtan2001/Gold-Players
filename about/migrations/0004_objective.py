# Generated by Django 5.0.4 on 2024-04-24 05:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_about_short_descriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Objective Title')),
                ('image', models.ImageField(upload_to='aboutus/', verbose_name='Objective Image')),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='Descriptions')),
            ],
            options={
                'verbose_name': 'Our Objective',
                'verbose_name_plural': 'Our Objectives',
                'ordering': ['id'],
            },
        ),
    ]