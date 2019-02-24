from bus_follower.models import *
from django.db.models import Func, F
import json, requests
from time import sleep


def test_for_git():
    pass

def add_stop_and_else(form):
    url = form.cleaned_data['url']
    route = form.cleaned_data['route']
    position = form.cleaned_data['position']
    length = form.cleaned_data['length']

    name = url.split('/')[5].replace('+', ' ')
    coords = url[-40:].split('!3d')[1]
    latitude, litititude = coords.split('!4d')
    latitude, litititude = float(latitude), float(litititude[:-6])
    count = 1

    if Bus_stop.objects.filter(name=name).exists():
        if not Bus_stop.objects.filter(lat=latitude, lng=litititude).exists():
            while Bus_stop.objects.filter(name=name + ' ' + str(count)).exists():
                count += 1
            name = name + ' ' + str(count)
            Bus_stop.objects.create(name=name, lat=latitude, lng=litititude)
    else:
        Bus_stop.objects.create(name=name, lat=latitude, lng=litititude)
    if not Bus_route.objects.filter(route=route).exists():
        Bus_route.objects.create(route=route)
        # if not Bus_stop_position.objects.filter(stop=Bus_stop.objects.filter(name=name),
        #                                        route=Bus_route.objects.filter(route=route)).count():
    if Bus_route.objects.filter(route=route).exists() and Bus_stop.objects.filter(name=name).exists():
        if not Bus_stop_position.objects.filter(stop=Bus_stop.objects.get(name=name),
                                                route=Bus_route.objects.get(route=route)).exists():
            Bus_stop_position.objects.create(stop=Bus_stop.objects.get(name=name),
                                             route=Bus_route.objects.get(route=route),
                                             position=position, length=length)

def nearest_bus_stop(lat, lng, quantiti):
    result = Bus_stop.objects.annotate(abs_lat=Func(F('lng') - lng, function='ABS')) \
                 .annotate(abs_lit=Func(F('lat') - lat, function='ABS')) \
                 .annotate(all_diff=F('abs_lat') + F('abs_lit')) \
                 .order_by('all_diff').all()[:quantiti]
    return result

def nearest_plase(table, lat, lng, quantiti):
    result = table.objects.annotate(abs_lat=Func(F('lng') - lng, function='ABS')) \
                 .annotate(abs_lit=Func(F('lat') - lat, function='ABS')) \
                 .annotate(all_diff=F('abs_lat') + F('abs_lit')) \
                 .order_by('all_diff').all()[:quantiti]
    return result

def find_dir(start, stop):
    if (start - stop) > 0:
        return 1
    else:
        return 0
def get_buses_coord_and_dir_tg(route):
    url = "http://www.trans-gps.cv.ua/map/trackers/?selectedRoutesStr="
    try:
        response = requests.get(url)
    except:
        return 1
    bus_info = json.loads(response.text)
    #print(bus_info)
    tmp = bus_info.copy()
    for bus in tmp:
        if bus_info[bus]['routeName'] != route:
            del bus_info[bus]
    route_db = Bus_route.objects.filter(route=route).get()
    sleep(15)
    try:
        response = requests.get(url)
    except:
        return 0
    bus_info1 = json.loads(response.text)
    tmp = bus_info1.copy()
    for bus in tmp:
        if bus_info1[bus]['routeName'] != route:
            del bus_info1[bus]

    tmp = bus_info.copy()
    for bus in tmp:
        if bus_info[bus]['lat'] == bus_info1[bus]['lat'] and bus_info[bus]['lat'] == bus_info1[bus]['lat']:
            del bus_info[bus]
            del bus_info1[bus]
    quantiti = 4
    for bus in bus_info:
        begin_dot = nearest_plase(Route_way, bus_info[bus]['lat'], bus_info[bus]['lng'], quantiti)
        end_dot = nearest_plase(Route_way, bus_info1[bus]['lat'], bus_info1[bus]['lng'], quantiti)
        for dot in range(quantiti):
            if (end_dot[quantiti].position - begin_dot[quantiti]) > 0:
                pass
    result = bus_info
    return result