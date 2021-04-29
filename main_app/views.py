from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# import requests
import datetime
from .models import Joke
from .forms import JokeForm

# API_KEY = '4967ac58d9msh8e3af7a90bbc99dp19e443jsnc0ddfc3ec16a'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def allJokes(request):
    return render(request, 'allJokes.html')

def submitjoke(request):
    return render(request, 'submitjoke.html')

def postsubmit(request):
    return render(request, 'postsubmit.html')

def profilePage(request):
    return render(request, 'user/profilepage.html')

def myfavoritejokes(request):
    return render(request, 'user/myfavoritejokes.html')

def randomJoke(request):
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

    return render(request, 'randomJoke.html', context)

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

    return render(request, 'randomJoke.html', context)

def save_joke_to_db(incoming_joke):
    existing_joke = Joke.objects.filter(joke__contains=incoming_joke)
    print('\033[30;206;48;2;255;0;0m', len(existing_joke))
    if len(existing_joke) == 0:
        newJoke = {
            'joke':incoming_joke, 
            'source':'icanhazdadjoke.com',
            'category':'D',
            'createdBy':None,
            }

        form = JokeForm(newJoke)
        if form.is_valid():
            new_joke = form.save(commit=False)
            new_joke.save()
    else:
        print('Joke already exists.')

def jokeById(request):
    pass

def jokeByType(request):
    pass

def jokeSearch(request):
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