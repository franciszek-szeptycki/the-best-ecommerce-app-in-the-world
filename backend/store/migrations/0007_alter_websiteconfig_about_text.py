# Generated by Django 5.0.3 on 2024-04-06 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_productgallery_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteconfig',
            name='about_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
