# Generated by Django 5.0.4 on 2024-04-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_objective'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='aboutus/', verbose_name='Organization Logo')),
                ('fav_icon', models.ImageField(upload_to='aboutus/', verbose_name='Organization Fav Icon')),
                ('site_name', models.CharField(max_length=150, verbose_name='Organization Name')),
                ('phone_number', models.CharField(max_length=150, verbose_name='Organization Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Organization Email')),
                ('fb_url', models.URLField(blank=True, null=True, verbose_name='Facebook Page URL')),
                ('tw_url', models.URLField(blank=True, null=True, verbose_name='Twitter URL')),
                ('insta_url', models.URLField(blank=True, null=True, verbose_name='Instagram Page URL')),
                ('linkedin_url', models.URLField(blank=True, null=True, verbose_name='Linkedin URL')),
            ],
        ),
    ]