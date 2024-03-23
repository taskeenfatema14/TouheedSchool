# Generated by Django 3.2.5 on 2024-03-23 12:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=20)),
                ('event_title', models.CharField(max_length=80)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('event_time', models.TimeField(blank=True, null=True)),
                ('event_location', models.TextField(blank=True, null=True)),
                ('event_desc', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='img/thumbnails')),
                ('event_videos', models.FileField(blank=True, null=True, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'avi', 'mov', 'wmv', 'flv'])])),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='schools.school')),
            ],
        ),
        migrations.CreateModel(
            name='EventSpeaker',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('speaker_name', models.CharField(max_length=50)),
                ('speaker_image', models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('speaker_desc', models.TextField(max_length=100)),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_speakers', to='events.events')),
            ],
        ),
        migrations.CreateModel(
            name='EventImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=' ', null=True, upload_to='img', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.events')),
            ],
        ),
    ]
