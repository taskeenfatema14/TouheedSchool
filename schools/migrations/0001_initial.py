<<<<<<< HEAD
# Generated by Django 3.2.5 on 2024-03-09 16:43

from django.db import migrations, models
import django.db.models.deletion
import uuid
=======
# Generated by Django 3.2.5 on 2024-03-12 13:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
>>>>>>> 975c23fccd25bfa91203a5d28141f3a2ff19f347


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='School',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
=======
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=20)),
                ('event_title', models.CharField(max_length=80)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('event_time', models.TimeField(blank=True, null=True)),
                ('event_location', models.TextField(blank=True, null=True)),
                ('event_desc', models.TextField(blank=True, null=True)),
                ('event_image', models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('event_videos', models.FileField(blank=True, null=True, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'avi', 'mov', 'wmv', 'flv'])])),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
>>>>>>> 975c23fccd25bfa91203a5d28141f3a2ff19f347
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='schoolImage')),
<<<<<<< HEAD
=======
                ('video', models.FileField(blank=True, null=True, upload_to='landing_page', validators=[django.core.validators.FileExtensionValidator(['mp4', 'avi', 'mov'])])),
>>>>>>> 975c23fccd25bfa91203a5d28141f3a2ff19f347
                ('facility', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('principle', models.TextField()),
                ('contact_no', models.IntegerField()),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('event_title', models.TextField()),
                ('event_desc', models.TextField(blank=True, null=True)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
                ('event_location', models.TextField(blank=True, default='Gangolli - karnataka.', null=True)),
                ('event_image', models.ImageField(blank=True, help_text='Best Image Resolution width: 580 x Height: 565', null=True, upload_to='images/event/thumbnail/')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='schools.school')),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
=======
            name='EventSpeaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_name', models.CharField(max_length=50)),
                ('speaker_image', models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])])),
                ('speaker_desc', models.TextField(max_length=100)),
                ('events', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_speakers', to='schools.events')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='schools.school'),
>>>>>>> 975c23fccd25bfa91203a5d28141f3a2ff19f347
        ),
    ]
