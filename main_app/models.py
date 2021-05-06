from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

CATEGORIES = (
    # ('R', 'Random'),
    ('Y', 'Yo Mama'),
    ('D', 'Dad'),
    ('H', 'Chuck Norris'),
    ('P', 'Pun'),
    # ('K', 'Knock Knock'),
    # ('B', 'Bar'),
    ('C', 'Computer'),
    # ('S', 'Sports'),
    # ('A', 'Animal'),
)

class Joke(models.Model):
    joke = models.CharField(max_length=10000) # what is the max length from the apis?
    
    source = models.CharField(max_length=50, blank=True, null=True,)

    favorites = models.ManyToManyField(User, blank=True, related_name = 'favorites')
    
    dislikes = models.ManyToManyField(User, blank=True, related_name = 'dislikes')

    category = models.CharField(max_length=50, choices=CATEGORIES, default=CATEGORIES[0][0])

    createdBy = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)

    modified_date = models.DateTimeField(auto_now=True)

    approved = models.BooleanField(default=False)

    reviewed = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.joke}'


class Comment(models.Model):
    text = models.CharField(max_length=4000)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text}'
    
    def get_absolute_url(self):
        return reverse('joke_details', args=[self.joke.id])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    moderator = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    
