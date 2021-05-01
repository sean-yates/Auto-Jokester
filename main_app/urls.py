from django.urls import path
from . import views

# Paths/Routes
urlpatterns = [
    path('', views.home, name='home'),
    
    path('joke_random/', views.joke_random, name='joke_random'),
    # path('<str:category>/', views.joke_random, name='joke_random'),
    path('<str:category>_joke_by_id/', views.joke_by_id, name='joke_by_id'),
    path('<str:category>_joke_search/', views.joke_search, name='joke_search'),
    path('jokes/<int:joke_id>/comments/', views.comments, name='joke_comments'),
    path('jokes/<int:joke_id>/comments/add_comment/', views.add_comment, name='add_comment'),
    path('<str:category>/', views.joke_category, name='joke_category'),

    path('accounts/signup/', views.signup, name='signup'),
    path('allJokes', views.allJokes, name='allJokes'),
    path('submitjoke', views.submitjoke, name='submitjoke'),
    path('postsubmit', views.postsubmit, name='postsubmit'),
    path('profile', views.profilePage, name='profilepage'),
    path('myfavoritejokes', views.myfavoritejokes, name='myfavoritejokes'),
]
