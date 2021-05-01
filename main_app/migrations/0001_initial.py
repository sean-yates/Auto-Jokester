# Generated by Django 3.2 on 2021-05-01 19:53

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
                ('joke', models.CharField(max_length=10000)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(choices=[('Y', 'Yo Mama'), ('D', 'Dad'), ('H', 'Chuck Norris'), ('P', 'Pun'), ('C', 'Computer')], default='Y', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('appproved', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('favorites', models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('joke', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.joke')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
