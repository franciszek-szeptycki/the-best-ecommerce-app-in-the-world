# Generated by Django 5.0.3 on 2024-04-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_img_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteconfig',
            name='about_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
