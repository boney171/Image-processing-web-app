# Generated by Django 5.0.4 on 2024-04-24 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_processing', '0005_image_meta_size_byte'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ImageDBModel',
        ),
    ]
