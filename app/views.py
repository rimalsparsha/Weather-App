from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')



import datetime

def result(request):
    city = request.GET.get('city')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c20cd9f2f51e82c49b2d917f96002e05'
    data = requests.get(url).json()

    payload = {
        'city' : data['name'],
        'weather' : data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'],
        'kelvin_temperature' : data['main']['temp'],
        'celcius_temperature' : int(data['main']['temp'] - 273),
        'pressure' : data['main']['pressure'],
        'humidity' : data['main']['humidity'],
        'date_time' : datetime.datetime.now(),
    }

    context = {'data' : payload}

    return render(request, 'result.html', context)
