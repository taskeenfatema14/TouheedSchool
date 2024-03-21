# Generated by Django 3.2.5 on 2024-03-21 12:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_eventimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='event_image',
        ),
        migrations.AddField(
            model_name='events',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='img/thumbnails'),
        ),
        migrations.AlterField(
            model_name='events',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
