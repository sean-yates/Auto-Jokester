# Generated by Django 3.2 on 2021-05-06 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_merge_0003_joke_reviewed_0005_remove_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='moderator',
            field=models.BooleanField(default=False),
        ),
    ]