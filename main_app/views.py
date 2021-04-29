from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# import requests
import datetime

API_KEY = '4967ac58d9msh8e3af7a90bbc99dp19e443jsnc0ddfc3ec16a'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def allJokes(request):
    return render(request, 'allJokes.html')

def submitjoke(request):
    return render(request, 'submitjoke.html')

def randomJoke(request):
    # Ref. https://rapidapi.com/KegenGuyll/api/dad-jokes/endpoints
    # On left-hand side, click "Random" ==> select "GET Random Jokes"
    # On right-hand side, click "Code Snippets" --> select "Python" ==> "Requests" from dropdown menu
    import requests
    url = "https://dad-jokes.p.rapidapi.com/random/joke"
    headers = {
        'x-rapidapi-key': "4967ac58d9msh8e3af7a90bbc99dp19e443jsnc0ddfc3ec16a",
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers = headers)
    context = { 'response': response }
    print(response.text)
    return render(request, 'randomJoke.html', context)

def jokeById(request):
    # Ref. https://rapidapi.com/KegenGuyll/api/dad-jokes/endpoints ==> select "GET JokeByID"
    # On left-hand side, click "Random" ==> select "GET JokeByID"
    # On right-hand side, click "Code Snippets" --> select "Python" ==> "Requests" from dropdown menu
    import requests
    url = "https://dad-jokes.p.rapidapi.com/joke/5f80ccd641785ba7c7d27b4b"
    headers = {
        'x-rapidapi-key': "4967ac58d9msh8e3af7a90bbc99dp19e443jsnc0ddfc3ec16a",
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers = headers)
    context = { 'response': response }
    print(response.text)
    return render(request, 'jokeById.html', context)

def jokeByType(request):
    # Ref. https://rapidapi.com/KegenGuyll/api/dad-jokes/endpoints ==> select "GET JokeByType"
    # On left-hand side, click "Random" ==> select "GET JokeByType"
    # On right-hand side, click "Code Snippets" --> select "Python" ==> "Requests" from dropdown menu
    import requests
    url = "https://dad-jokes.p.rapidapi.com/joke/type/general"
    headers = {
        'x-rapidapi-key': "4967ac58d9msh8e3af7a90bbc99dp19e443jsnc0ddfc3ec16a",
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers = headers)
    context = { 'response': response }
    print(response.text)
    return render(request, 'jokeByType.html', context)

def jokeSearch(request):
    # Ref. https://rapidapi.com/KegenGuyll/api/dad-jokes/endpoints ==> select "GET Search"
    # On left-hand side, click "Random" ==> select "GET Search"
    # On right-hand side, click "Code Snippets" --> select "Python" ==> "Requests" from dropdown menu
    import requests
    url = "https://dad-jokes.p.rapidapi.com/joke/search"
    querystring = {"term":"cow"}
    headers = {
        'x-rapidapi-key': "4967ac58d9msh8e3af7a90bbc99dp19e443jsnc0ddfc3ec16a",
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers = headers, params = querystring)
    context = { 'response': response }
    print(response.text)
    return render(request, 'jokeSearch.html', context)


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