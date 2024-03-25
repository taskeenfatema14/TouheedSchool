# Generated by Django 3.2.5 on 2024-03-25 12:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='school')),
                ('video', models.FileField(blank=True, null=True, upload_to='landing_page', validators=[django.core.validators.FileExtensionValidator(['mp4', 'avi', 'mov'])])),
                ('facility', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('principle', models.TextField()),
                ('contact_no', models.IntegerField()),
                ('school_email', models.EmailField(max_length=255, verbose_name='email_address')),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user_email', models.EmailField(max_length=255, verbose_name='email_address')),
                ('full_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_us', to='schools.school')),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
    ]
