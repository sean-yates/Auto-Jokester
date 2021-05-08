from django.forms import ModelForm
from .models import Joke, Comment, Profile, User

class JokeForm(ModelForm):
  class Meta:
    model = Joke
    fields = [
        'joke', 
        'category', 
        
        ]



class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = [
      'text'
    ]

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = [
      'bio',
      'profile_pic',
      'website_url',
      'facebook_url',
      'twitter_url', 
      'instagram_url'
    ]


class UserUpdateForm(ModelForm):
    class Meta:
        model=User
        fields=['username']