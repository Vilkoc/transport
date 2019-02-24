from django.shortcuts import render
from .models import *
from .forms import BusStop, GeoData
from .util.calc import *
from .util.funct import *

def index(request):
    return render(request, 'index.html', {'form': GeoData, 'result': result})

def my_places(request):
    return render(request, 'my_places.html', {'form': GeoData, 'result': result})

def test(request):
    if request.method == 'POST':
        form = GeoData(request.POST)
        if form.is_valid():
            my_lat = form.cleaned_data['my_lat']
            my_lng = form.cleaned_data['my_lng']
            fin_lat = form.cleaned_data['fin_lat']
            fin_lng = form.cleaned_data['fin_lng']

            my_stop = nearest_bus_stop(lat, lng, 5)
            fin_stop = nearest_bus_stop(lat, lng, 5)

            return render(request, 'test.html', {'form': GeoData, 'result': result})
    return render(request, 'test.html', {'form':GeoData})

def add_bus_stop(request):
    if request.method == 'POST':
        form = Bus_stop(request.POST)
        if form.is_valid():
            add_stop_and_else(form)
            return render(request, 'test.html', {'form': BusStop})
    result = 'Enter data'
    return render(request, 'add_bus_stop.html', {'form': BusStop})

def index(request):
    return render(request, 'index.html', {'form': GeoData, 'result': result})

