# Generated by Django 3.2.25 on 2024-05-03 03:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('long_running_task', '0002_auto_20240503_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='longrunningtask',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
