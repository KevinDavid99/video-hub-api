# Generated by Django 4.1.4 on 2023-06-05 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_api', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_post',
            new_name='post',
        ),
    ]