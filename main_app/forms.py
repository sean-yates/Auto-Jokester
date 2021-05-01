from django.forms import ModelForm
from .models import Joke, Comment

class JokeForm(ModelForm):
  class Meta:
    model = Joke
    fields = [
        'joke', 
        'source', 
        'category', 
        'createdBy',
        ]


class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = [
      'text'
    ]