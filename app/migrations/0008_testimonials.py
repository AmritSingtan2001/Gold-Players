# Generated by Django 5.0.4 on 2024-04-22 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testimonialsimage/')),
                ('name', models.CharField(max_length=150)),
                ('descriptions', models.TextField()),
                ('position', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
