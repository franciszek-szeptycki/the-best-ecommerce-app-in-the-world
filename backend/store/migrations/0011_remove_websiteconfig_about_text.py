# Generated by Django 5.0.3 on 2024-04-06 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_websiteconfig_about_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websiteconfig',
            name='about_text',
        ),
    ]
