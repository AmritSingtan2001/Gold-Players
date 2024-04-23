# Generated by Django 5.0.4 on 2024-04-23 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_office'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='logo',
            field=models.ImageField(default=1, upload_to='Office Image/', verbose_name='Office Logo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='office',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Office Image/'),
        ),
    ]
