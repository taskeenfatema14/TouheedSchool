# Generated by Django 5.0.3 on 2024-03-19 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_alter_eventimages_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='event_image',
        ),
    ]
