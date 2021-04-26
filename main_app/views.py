from django.shortcuts import render
# import requests
API_KEY = '4967ac58d9msh8e3af7a90bbc99dp19e443jsnc0ddfc3ec16a'

# Create your views here.

def home(request):
    return render(request, 'home.html')

def randomJoke(request):
    import requests

    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
        'x-rapidapi-key': "4967ac58d9msh8e3af7a90bbc99dp19e443jsnc0ddfc3ec16a",
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    context = { 'response': response }

    print(response.text)
    return render(request, 'randomJoke.html', context)




