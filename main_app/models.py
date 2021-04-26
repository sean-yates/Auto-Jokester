from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
 
# Create your models here.
class User(models.Model):
 name = models.CharField(max_length=100)
 email = models.CharField(max_length=100)
 
 def __str__(self):
   return self.name
 
 # Add this method
 def get_absolute_url(self):
   return reverse('detail', kwargs={'user_id': self.id})
