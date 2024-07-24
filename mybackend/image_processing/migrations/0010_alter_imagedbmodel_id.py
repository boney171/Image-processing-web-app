from uuid import uuid4
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('image_processing', '0009_alter_imagedbmodel_id'),
    ]

    operations = [
        # Assuming 'id' was an AutoField or another type and you need to change it to UUID
        migrations.RunSQL(
            sql="""
                ALTER TABLE image_processing_imagedbmodel DROP CONSTRAINT IF EXISTS image_processing_imagedbmodel_pkey;
                ALTER TABLE image_processing_imagedbmodel DROP COLUMN id;
            """,
            reverse_sql="""
                ALTER TABLE image_processing_imagedbmodel ADD COLUMN id serial NOT NULL;
                ALTER TABLE image_processing_imagedbmodel ADD CONSTRAINT image_processing_imagedbmodel_pkey PRIMARY KEY (id);
            """
        ),
        migrations.AddField(
            model_name='imagedbmodel',
            name='id',
            field=models.UUIDField(default=uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
