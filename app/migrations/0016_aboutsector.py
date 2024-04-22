# Generated by Django 5.0.4 on 2024-04-22 10:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_solutionsubcategory_short_descriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='sectorimage/')),
                ('short_descriptions', ckeditor.fields.RichTextField()),
                ('descriptions', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
