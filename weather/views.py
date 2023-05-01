from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
import json
import urllib.request




# Create your views here.
def index(request):
    return render (request, 'index.html')


def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3cb3f8d7d49de59473219e833289ba6e").read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+ '' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity'])
        }
    else:
        city=''
        data = {}
    return render (request, 'weather.html', {'city':city, 'data':data})


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
       
            
    context ={'form':form}
    return render(request, 'register.html', context)

    

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')
