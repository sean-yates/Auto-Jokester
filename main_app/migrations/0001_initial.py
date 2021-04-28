# Generated by Django 3.2 on 2021-04-28 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joke', models.CharField(max_length=1000)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('dislikes', models.ManyToManyField(blank=True, null=True, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('favorites', models.ManyToManyField(blank=True, null=True, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
