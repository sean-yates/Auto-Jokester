# Generated by Django 3.2 on 2021-05-01 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210501_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='joke',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.joke'),
            preserve_default=False,
        ),
    ]
