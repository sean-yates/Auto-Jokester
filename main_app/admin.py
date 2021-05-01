from django.contrib import admin

from .models import Joke, Comment
# Register your models here.
admin.site.register(Joke)
admin.site.register(Comment)