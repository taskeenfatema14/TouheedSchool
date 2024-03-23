# Generated by Django 3.2.5 on 2024-03-23 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_auto_20240322_1035'),
        ('accounts', '0003_auto_20240320_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='schools.school'),
        ),
    ]
