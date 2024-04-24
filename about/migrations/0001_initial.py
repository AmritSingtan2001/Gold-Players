# Generated by Django 5.0.4 on 2024-04-24 04:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='About Title')),
                ('image', models.ImageField(upload_to='aboutus/', verbose_name='About Image')),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='About Descriptions')),
            ],
        ),
    ]