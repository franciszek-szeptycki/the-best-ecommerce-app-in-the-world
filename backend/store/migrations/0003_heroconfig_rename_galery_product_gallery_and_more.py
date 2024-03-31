# Generated by Django 5.0.3 on 2024-03-31 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_productgallery_options_sliderconfiguration'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('image', models.ImageField(default='placeholder.png', upload_to='hero/')),
            ],
            options={
                'verbose_name_plural': 'Hero config',
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='galery',
            new_name='gallery',
        ),
        migrations.DeleteModel(
            name='SliderConfiguration',
        ),
    ]
