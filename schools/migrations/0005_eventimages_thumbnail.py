# Generated by Django 5.0.3 on 2024-03-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_remove_events_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventimages',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='img/thumbnails'),
        ),
    ]
