from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# import requests
import datetime
import random
from .models import Joke, CATEGORIES, Comment, Profile
from .forms import JokeForm, CommentForm, ProfileForm, UserUpdateForm


# API_KEY = '4967ac58d9msh8e3af7a90bbc99dp19e443jsnc0ddfc3ec16a'

# Create your views here.
def home(request):
    db_jokes = Joke.objects.all()
    random_joke = db_jokes[(random.randint(0,(len(db_jokes)) - 1 ))]
    print(random_joke)
    return render(request, 'home.html', {'random_joke': random_joke})


def allJokes(request):
    # jokes = Joke.objects.order_by('id')
    categories = CATEGORIES

    joke_list = []
    for category in categories:
        joke_in_category = Joke.objects.filter(category=category[0]).order_by("?").first()
        category_joke = {
            'category': category,
            'joke': joke_in_category,
            }
        joke_list.append(category_joke)

    # print('\033[30;206;48;2;255;255;0m', 'jokes =', jokes, '\033[0m')
    context = {
        'categories': categories,
        'jokes': joke_list,
        }

    return render(request, 'allJokes.html', context)



def submitjoke(request):
    j_form = JokeForm(request.GET)
    if request.method == "POST":
        j_form = JokeForm(request.POST)
        if j_form.is_valid():
            new_joke = j_form.save(commit = False)
            new_joke.createdBy = request.user
            new_joke.save()
        return redirect('/submitjoke/postsubmit')
    else:
        j_form = JokeForm()

    context={'j_form': j_form}
    return render(request, 'submitjoke.html',context )

@login_required
def postsubmit(request):
    return render(request, 'postsubmit.html')

@login_required
def submittedjokes(request):
    return render(request, 'user/submittedjokes.html')


@login_required
def profilePage(request):
    return render(request, 'user/profilepage.html')

@login_required
def editprofile(request):
    u_form = UserUpdateForm(request.GET, initial={'value' : 'Peter'})
    if request.method == 'POST':
        p_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            print(p_form)
            return redirect('/jokes/profile/')
    else:
        p_form = ProfileForm(instance=request.user, initial={'bio' : request.user.profile.bio, 'facebook_url': request.user.profile.facebook_url, 'twitter_url': request.user.profile.twitter_url,'instagram_url': request.user.profile.instagram_url, 'website_url': request.user.profile.website_url})
        u_form = UserUpdateForm(instance=request.user.profile, initial={'username' : request.user})

    context={'p_form': p_form, 'u_form': u_form}
    return render(request, 'user/editprofile.html',context )


@login_required
def myfavoritejokes(request):
    return render(request, 'user/myfavoritejokes.html')

    # path('<str:category>_joke_random/', views.joke_random, name='joke_random'),
    # path('<str:category>_joke_by_id/', views.joke_by_id, name='joke_by_id'),
    # path('<str:category>_joke_search/', views.joke_search, name='joke_search'),

@login_required
def assoc_favorite(request, joke_id):
    Joke.objects.get(id=joke_id).favorites.add(request.user.id)
    return redirect('allJokes')

@login_required
def assoc_dislike(request, joke_id):
    Joke.objects.get(id=joke_id).dislikes.add(request.user.id)
    return redirect('allJokes')

def joke_category(request, category):

    user = User.objects.get(id=request.user.id)

    if category == 'dad':
        category_code = 'D'
    elif category == 'yomama':
        category_code = 'Y'
    elif category == 'chucknorris':
        category_code = 'H'
    elif category == 'random':
        category_code = 'R'
    elif category == 'pun':
        category_code = 'P'
    elif category == 'knockknock':
        category_code = 'K'
    elif category == 'bar':
        category_code = 'B'
    elif category == 'computer':
        category_code = 'C'
    elif category == 'sports':
        category_code = 'S'
    elif category == 'animal':
        category_code = 'A'
 


    db_jokes = Joke.objects.filter(category = category_code)

    jokes_without_action = Joke.objects.exclude(id__in = user.favorites.all().values_list('id'))

    return render(request, 'joke_category.html', {'all': db_jokes, 'category': category, 'jokes_without_action': jokes_without_action})
    print(db_jokes)
    return render(request, 'joke_category.html', {'all': db_jokes, 'category': category})

def joke_random(request, category_name):
    import requests
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'My Library (https://github.com/sean-yates/Auto-Jokester)'
    }

    if category_name == 'dad':
        url = 'https://icanhazdadjoke.com'
        arg_cat = 'D'
    elif category_name == 'yomama':
        url = 'https://api.yomomma.info'
        arg_cat = 'Y'
    elif category_name == 'chucknorris':
        url = 'http://api.icndb.com/jokes/random'
        arg_cat = 'H'
        # url = 'https://api.chucknorris.io/jokes/random'
    elif category_name == 'pun':
        url = 'https://v2.jokeapi.dev/joke/Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit'
        # types: single (joke), twopart (setup, delivery)
        arg_cat = 'P'
    elif category_name == 'knockknock':
        print('\033[30;206;48;2;255;255;0m', 'category_name =', category_name, '\033[0m')
    elif category_name == 'bar':
        print('\033[30;206;48;2;255;255;0m', 'category_name =', category_name, '\033[0m')
    elif category_name == 'computer':
        url = 'https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit'
        print('\033[30;206;48;2;255;255;0m', 'category_name =', category_name, '\033[0m')
        arg_cat = 'C'
    elif category_name == 'sports':
        print('\033[30;206;48;2;255;255;0m', 'category_name =', category_name, '\033[0m')
    elif category_name == 'animal':
        print('\033[30;206;48;2;255;255;0m', 'category_name =', category_name, '\033[0m')
    else:
        print("\033[30;206;48;2;255;255;0mI don't know how you ended up here.\033[0m")

    response = requests.request("GET", url, headers=headers)

    context = { 'response': response }

    response_data = response.json()


    if category_name == 'dad' or category_name == 'yomama':
        pass
        print('\033[30;206;48;2;255;255;0m', 'response_data["joke"] =', response_data['joke'], '\033[0m')
    elif category_name == 'chucknorris':
        pass
        print('\033[30;206;48;2;255;255;0m', 'response_data["value"]["joke"] =', response_data['value']['joke'], '\033[0m')

    save_joke_to_db(response_data['joke'], url, arg_cat)

    return render(request, 'joke_random.html', context)

def random_dad_joke(request):
    # From icanhazdadjoke.com
    import requests
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'My Library (https://github.com/sean-yates/Auto-Jokester)'
    }
    response = requests.request("GET", 'https://icanhazdadjoke.com', headers=headers)
    context = { 'response': response }

    response_data = response.json()

    print('\033[30;206;48;2;255;255;0m', response_data['joke'], '\033[0m')

    save_joke_to_db(response_data['joke'])

    return render(request, 'joke_random.html', context)

def searchJoke(request):
    # From icanhazdadjoke.com
    import requests
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'My Library (https://github.com/sean-yates/Auto-Jokester)'
    }
    response = requests.request("GET", 'https://icanhazdadjoke.com/search?term=computer', headers=headers)
    context = { 'response': response }

    response_data = response.json()

    print('\033[30;206;48;2;255;255;0m', response_data['results'][0], '\033[0m')
    
    save_joke_to_db(response_data['results'][0]['joke'])

    return render(request, 'joke_search.html', context)

def save_joke_to_db(incoming_joke, source, category):
    existing_joke = Joke.objects.filter(joke__contains=incoming_joke)
    print('\033[30;206;48;2;255;0;0m', len(existing_joke))
    if len(existing_joke) == 0:
        newJoke = {
            'joke':incoming_joke, 
            'source':source,
            'category':category,
            'createdBy':None,
            }

        form = JokeForm(newJoke)
        if form.is_valid():
            new_joke = form.save(commit=False)
            new_joke.save()
    else:
        print('Joke already exists.')

def joke_by_id(request):
    pass

def jokeByType(request):
    pass

def joke_search(request):
    pass


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



def joke_details(request, joke_id):
    joke = Joke.objects.get(id=joke_id)
    comment_form = CommentForm()
    context = {
        'joke': joke,
        'comment_form': comment_form
    }
    return render(request, 'comments.html', context)

@login_required
def add_comment(request, joke_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.user = request.user
        new_comment.joke_id = joke_id
        new_comment.save()
    return redirect('joke_details', joke_id=joke_id)


@login_required
def delete_comment(request, joke_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
        comment.delete()
    return redirect('joke_details',joke_id=joke_id)

class Update_comment(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['text']


@login_required
def unapproved_jokes(request):
    jokes_for_review = Joke.objects.filter(approved=False, reviewed=False)
    context = {
        'jokes': jokes_for_review
    }
    
    return render(request, 'unapproved_jokes.html', context)

@login_required
def approve_joke(request,joke_id):
    joke = Joke.objects.get(id=joke_id)
    joke.reviewed = True
    joke.approved = True
    joke.save()
    return redirect('unapproved_jokes')

@login_required
def reject_joke(request,joke_id):
    joke = Joke.objects.get(id=joke_id)
    joke.reviewed = True
    joke.save()
    return redirect('unapproved_jokes')