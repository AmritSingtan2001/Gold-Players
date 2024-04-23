# Generated by Django 5.0.4 on 2024-04-23 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0003_alter_careers_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, verbose_name='Career Category Name')),
            ],
        ),
        migrations.RenameField(
            model_name='careers',
            old_name='image',
            new_name='company_logo',
        ),
        migrations.AddField(
            model_name='careers',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='careers.category', verbose_name='Choose Career Category'),
        ),
    ]
