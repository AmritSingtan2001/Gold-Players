# Generated by Django 5.0.4 on 2024-04-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careers',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
