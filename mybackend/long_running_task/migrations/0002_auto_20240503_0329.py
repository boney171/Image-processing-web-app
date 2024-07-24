from uuid import uuid4
from django.db import migrations, models

def generate_uuids_for_longrunningtask(apps, schema_editor):
    LongRunningTask = apps.get_model('long_running_task', 'LongRunningTask')
    for task in LongRunningTask.objects.all():
        task.id = uuid4()
        task.save()

class Migration(migrations.Migration):

    dependencies = [
        ('long_running_task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='longrunningtask',
            name='name',
        ),
        migrations.AddField(
            model_name='longrunningtask',
            name='location',
            field=models.CharField(default='http://127.0.0.1:8000/long_running_task/get-progress/{id}', max_length=100),
        ),
        migrations.AddField(
            model_name='longrunningtask',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='longrunningtask',
            name='result',
            field=models.CharField(default='http://127.0.0.1:8000/media/{location}', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='longrunningtask',
            name='status',
            field=models.CharField(default='INQUEUE', max_length=10),
        ),
        # Adding a temporary UUID field
        migrations.AddField(
            model_name='longrunningtask',
            name='new_id',
            field=models.UUIDField(default=uuid4, editable=False),
        ),
        # Populating new UUIDs
        migrations.RunPython(generate_uuids_for_longrunningtask, reverse_code=migrations.RunPython.noop),
        # Removing old primary key field
        migrations.RemoveField(
            model_name='longrunningtask',
            name='id',
        ),
        # Rename the new UUID field to 'id'
        migrations.RenameField(
            model_name='longrunningtask',
            old_name='new_id',
            new_name='id',
        ),
        # Set the new 'id' as the primary key
        migrations.AlterField(
            model_name='longrunningtask',
            name='id',
            field=models.UUIDField(editable=False, primary_key=True),
        ),
    ]
