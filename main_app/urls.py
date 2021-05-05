from django.urls import path
from . import views

# Paths/Routes
urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profilePage, name='profilepage'),
    path('allJokes/', views.allJokes, name='allJokes'),
    path('submitjoke/', views.submitjoke, name='submitjoke'),
    path('myfavoritejokes/', views.myfavoritejokes, name='myfavoritejokes'),
    path('accounts/signup/', views.signup, name='signup'),
    path('postsubmit/', views.postsubmit, name='postsubmit'),
    path('joke_random/', views.joke_random, name='joke_random'),
    path('joke_random/<str:category_name>/', views.joke_random, name='joke_random'),
    path('<str:category>_joke_by_id/', views.joke_by_id, name='joke_by_id'),
    path('<str:category>_joke_search/', views.joke_search, name='joke_search'),
    path('jokes/<int:joke_id>/', views.joke_details, name='joke_details'),
    path('jokes/<int:joke_id>/add_comment/', views.add_comment, name='add_comment'),
    path('jokes/<int:joke_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('jokes/<int:joke_id>/comments/<int:pk>/update/', views.Update_comment.as_view(), name='update_comment'),
    path('<str:category>/', views.joke_category, name='joke_category'),
    path('jokes/<int:joke_id>/assoc_favorite/', views.assoc_favorite, name='assoc_favorite'),
    path('jokes/<int:joke_id>/assoc_dislike/', views.assoc_dislike, name='assoc_dislike'),
    path('editprofile', views.editprofile, name='editprofile')

]
