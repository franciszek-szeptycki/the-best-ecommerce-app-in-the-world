# Generated by Django 5.0.3 on 2024-04-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_websiteconfig_delete_heroconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteconfig',
            name='slider_images',
            field=models.ManyToManyField(related_name='sliders', to='store.productgallery'),
        ),
    ]