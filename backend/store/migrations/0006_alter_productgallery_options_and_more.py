# Generated by Django 5.0.3 on 2024-04-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_websiteconfig_slider_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productgallery',
            options={'verbose_name_plural': 'Product gallery'},
        ),
        migrations.AddField(
            model_name='websiteconfig',
            name='about_text',
            field=models.TextField(blank=True),
        ),
    ]
