from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('randomJoke/', views.randomJoke, name='randomJoke'),
    path('jokeById/', views.jokeById, name='jokeById'),
    path('jokeByType/', views.jokeByType, name='jokeByType'),
    path('jokeSearch/', views.jokeSearch, name='jokeSearch'),
    path('accounts/signup/', views.signup, name='signup'),
]
