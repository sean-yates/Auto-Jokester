from django.contrib import admin

from .models import Joke, Comment, Profile
# Register your models here.
admin.site.register(Joke)
admin.site.register(Comment)
admin.site.register(Profile)