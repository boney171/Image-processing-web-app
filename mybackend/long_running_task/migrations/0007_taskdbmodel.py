# Generated by Django 3.2.25 on 2024-05-05 23:01

from django.db import migrations, models
import django_dto.dto


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('long_running_task', '0006_delete_taskdbmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDBModel',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(default='INQUEUE', max_length=10)),
                ('percentage', models.IntegerField(default=0)),
                ('location', models.CharField(default='http://127.0.0.1:8000/long_running_task/get-progress/{id}', max_length=100)),
                ('result', models.CharField(default='http://127.0.0.1:8000/media/{location}', max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            bases=(models.Model, django_dto.dto.DTOMixin),
        ),
    ]
