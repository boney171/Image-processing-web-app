# Generated by Django 3.2.25 on 2024-05-28 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_processing', '0011_alter_imagedbmodel_id'),
        ('long_running_task', '0010_taskdbmodel_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdbmodel',
            name='image_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='image_processing.imagedbmodel'),
        ),
    ]