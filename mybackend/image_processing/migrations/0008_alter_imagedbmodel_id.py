import uuid
from django.db import migrations

def populate_uuid(apps, schema_editor):
    ImageDBModel = apps.get_model('image_processing', 'ImageDBModel')
    for instance in ImageDBModel.objects.all():
        instance.uuid = uuid.uuid4()
        instance.save()

class Migration(migrations.Migration):

    dependencies = [
        ('image_processing', '0007_alter_imagedbmodel_id'),
    ]

    operations = [
        migrations.RunPython(populate_uuid),
    ]