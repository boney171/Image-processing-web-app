# Generated by Django 5.0.4 on 2024-04-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_processing', '0007_alter_imagedbmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedbmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
