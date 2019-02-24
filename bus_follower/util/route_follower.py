import sys, os, django
sys.path.append("d:\\Python\\Django") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
django.setup()

from transport.models import Bus_stop, Bus_route, Route_way

import json
import requests
#from transport.models import Bus_stop, Bus_route, Route_way
from time import sleep

class WriteRoute():
    url = 'http://trans-gps.cv.ua/'
    def __init__(self, route, url, id):
        self.route = route
        self.id = id
        self.url_end = url
    def get_position(self):
        pass

#response = requests.get("http://www.trans-gps.cv.ua/map/trackers/?selectedRoutesStr=")
#todos = json.loads(response.text)
url = "http://www.trans-gps.cv.ua/map/trackers/?selectedRoutesStr=14_"
response = requests.get(url)
imei = '355227045539582'
bus_info = json.loads(response.text)[imei]
print(bus_info)

def get_coord():
    url = "http://www.trans-gps.cv.ua/map/trackers/?selectedRoutesStr=14_"
    try:
        response = requests.get(url)
    except:
        return 0, 0
    imei = '355227045594918'
    bus_info = json.loads(response.text)[imei]
    return bus_info['lat'], bus_info['lng']

def get_new_coord(tmp_lat, tmp_lng):
    cur_lat, cur_lng = get_coord()
    while tmp_lat == cur_lat and tmp_lng == cur_lng:
        sleep(10)
        cur_lat, cur_lng = get_coord()
        #print('loop', get_coord(), cur_lng, tmp_lng)
    return cur_lat, cur_lng

start_lat, start_lng = get_coord()
lat, lng = get_new_coord(start_lat, start_lng)
position = 0

while lat != start_lat or lng != start_lng:
    Route_way.objects.create(route=Bus_route.objects.get(route='9a'), position=position, lat=lat, lng=lng)
    print(position, lat, lng)
    lat, lng = get_new_coord(lat, lng)
    position+=1
    #sleep(15)

print('finish')
'''for t in range(30):
    sleep(20)
    response = requests.get("http://www.trans-gps.cv.ua/map/trackers/?selectedRoutesStr=14_")
    todos = json.loads(response.text)
    print(t, todos[imei]['lat'], todos[imei]['lng'], todos[imei]['speed'])'''