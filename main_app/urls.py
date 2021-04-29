from django.urls import path
from . import views

# Paths/Routes
urlpatterns = [
    path('', views.home, name='home'),
    path('randomJoke/', views.randomJoke, name='randomJoke'),
    path('jokeById/', views.jokeById, name='jokeById'),
    path('jokeByType/', views.jokeByType, name='jokeByType'),
    path('jokeSearch/', views.jokeSearch, name='jokeSearch'),
    path('accounts/signup/', views.signup, name='signup'),
    path('allJokes', views.allJokes, name='allJokes'),
    path('submitjoke', views.submitjoke, name='submitjoke'),
    path('postsubmit', views.postsubmit, name='postsubmit'),
]
