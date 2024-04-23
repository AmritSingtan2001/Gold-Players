# Generated by Django 5.0.4 on 2024-04-23 05:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_sector_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='short_descriptions',
            field=ckeditor.fields.RichTextField(default=1, max_length=500, verbose_name='Short Description'),
            preserve_default=False,
        ),
    ]
