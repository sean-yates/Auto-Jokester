from django.urls import path
from . import views

# Paths/Routes
urlpatterns = [
    path('', views.home, name='home'),
    
    path('joke_random/', views.joke_random, name='joke_random'),
    path('joke_random/<str:category>/', views.joke_random, name='joke_random'),
    path('<str:category>_joke_by_id/', views.joke_by_id, name='joke_by_id'),
    path('<str:category>_joke_search/', views.joke_search, name='joke_search'),

    # path('dad_joke_random/', views.dad_joke_random, name='dad_joke_random'),
    # path('dad_joke_by_id/', views.dad_joke_by_id, name='dad_joke_by_id'),
    # # path('dad_joke_by_type/', views.dad_joke_by_type, name='dad_joke_by_type'),
    # path('dad_joke_search/', views.dad_joke_search, name='dad_joke_search'),

    # path('yomama_joke_random/', views.yomama_joke_random, name='yomama_joke_random'),
    # path('yomama_joke_by_id/', views.yomama_joke_by_id, name='yomama_joke_by_id'),
    # # path('yomama_joke_by_type/', views.yomama_joke_by_type, name='yomama_joke_by_type'),
    # path('yomama_joke_search/', views.yomama_joke_search, name='yomama_joke_search'),

    # path('knockknock_joke_random/', views.knockknock_joke_random, name='knockknock_joke_random'),
    # path('knockknock_joke_by_id/', views.knockknock_joke_by_id, name='knockknock_joke_by_id'),
    # # path('knockknock_joke_by_type/', views.knockknock_joke_by_type, name='knockknock_joke_by_type'),
    # path('knockknock_joke_search/', views.knockknock_joke_search, name='knockknock_joke_search'),

    # path('bar_joke_random/', views.bar_joke_random, name='bar_joke_random'),
    # path('bar_joke_by_id/', views.bar_joke_by_id, name='bar_joke_by_id'),
    # # path('bar_joke_by_type/', views.bar_joke_by_type, name='bar_joke_by_type'),
    # path('bar_joke_search/', views.bar_joke_search, name='bar_joke_search'),

    # path('computer_joke_random/', views.computer_joke_random, name='computer_joke_random'),
    # path('computer_joke_by_id/', views.computer_joke_by_id, name='computer_joke_by_id'),
    # # path('computer_joke_by_type/', views.computer_joke_by_type, name='computer_joke_by_type'),
    # path('computer_joke_search/', views.computer_joke_search, name='computer_joke_search'),

    # path('sports_joke_random/', views.sports_joke_random, name='sports_joke_random'),
    # path('sports_joke_by_id/', views.sports_joke_by_id, name='sports_joke_by_id'),
    # # path('sports_joke_by_type/', views.sports_joke_by_type, name='sports_joke_by_type'),
    # path('sports_joke_search/', views.sports_joke_search, name='sports_joke_search'),

    # path('animal_joke_random/', views.animal_joke_random, name='animal_joke_random'),
    # path('animal_joke_by_id/', views.animal_joke_by_id, name='animal_joke_by_id'),
    # # path('animal_joke_by_type/', views.animal_joke_by_type, name='animal_joke_by_type'),
    # path('animal_joke_search/', views.animal_joke_search, name='animal_joke_search'),

    path('accounts/signup/', views.signup, name='signup'),
    path('allJokes', views.allJokes, name='allJokes'),
    path('submitjoke', views.submitjoke, name='submitjoke'),
    path('postsubmit', views.postsubmit, name='postsubmit'),
    path('profile', views.profilePage, name='profilepage'),
    path('myfavoritejokes', views.myfavoritejokes, name='myfavoritejokes'),
]
