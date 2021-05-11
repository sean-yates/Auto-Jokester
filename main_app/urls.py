from django.urls import path
from . import views

# Paths/Routes
urlpatterns = [
    path('', views.home, name='home'),

    path('about_us/', views.about_us, name='about_us'),

    path('profile/', views.profilePage, name='profilepage'),
    path('profiles/<int:user_id>/', views.anotheruserprofilepage, name='profiles'),

    path('allJokes/', views.allJokes, name='allJokes'),

    path('submitjoke/', views.submitjoke, name='submitjoke'),
    path('submitjoke/postsubmit/', views.postsubmit, name='postsubmit'),

    
    path('myfavoritejokes/', views.myfavoritejokes, name='myfavoritejokes'),
    path('accounts/signup/', views.signup, name='signup'),
    
    path('joke_random/', views.joke_random, name='joke_random'),
    path('joke_random/<str:category_name>/', views.joke_random, name='joke_random'),
    path('<str:category>_joke_by_id/', views.joke_by_id, name='joke_by_id'),
    path('<str:category>_joke_search/', views.joke_search, name='joke_search'),
    path('jokes/<int:joke_id>/', views.joke_details, name='joke_details'),
    path('jokes/<int:joke_id>/add_comment/', views.add_comment, name='add_comment'),
    path('jokes/<int:joke_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('jokes/<int:joke_id>/comments/<int:pk>/update/', views.Update_comment.as_view(), name='update_comment'),
    
    path('jokes/<int:pk>/update/', views.Update_joke.as_view(), name='update_joke'),
    # path('jokes/<int:pk>/delete/', views.delete_joke, name='delete_joke'),
    path('jokes/<int:pk>/delete/', views.JokeDelete.as_view(), name='delete_joke'),

    path('<str:category>/', views.joke_category, name='joke_category'),
    path('editprofile', views.editprofile, name='editprofile'),

    path('jokes/unapproved/', views.unapproved_jokes, name='unapproved_jokes'),
    path('jokes/<int:joke_id>/approve', views.approve_joke, name='approve_joke'),
    path('jokes/<int:joke_id>/reject', views.reject_joke, name='reject_joke'),

    path('jokes/<int:joke_id>/assoc_favorite/', views.assoc_favorite, name='assoc_favorite'),
    path('jokes/<int:joke_id>/assoc_dislike/', views.assoc_dislike, name='assoc_dislike'),
    path('jokes/<int:joke_id>/disassoc_favorite/', views.disassoc_favorite, name='disassoc_favorite'),

    path('editprofile', views.editprofile, name='editprofile'),
    path('jokes/submittedjokes', views.submittedjokes, name='submittedjokes'),
    path('search', views.search, name='search'),
    
 
]