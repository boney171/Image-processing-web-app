# Generated by Django 3.2.25 on 2024-05-14 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('long_running_task', '0008_taskdbmodel_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskdbmodel',
            old_name='image',
            new_name='image_id',
        ),
    ]
