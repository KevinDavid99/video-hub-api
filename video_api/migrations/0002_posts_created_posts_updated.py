# Generated by Django 4.1.4 on 2023-06-04 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('video_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='posts',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
