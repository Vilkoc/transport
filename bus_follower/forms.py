from django import forms
from . import models

class BusStop(forms.Form):
    url = forms.CharField(label='url', required=True)
    route = forms.CharField(label='Route')
    position = forms.IntegerField(label='Position')
    length = forms.IntegerField(label='Length')

class GeoData(forms.Form):
    my_lat = forms.FloatField(label='My Latitude')
    my_lng = forms.FloatField(label='My Longtitude')
    fin_lat = forms.FloatField(label='fin Latitude')
    fin_lng = forms.FloatField(label='fin Longtitude')
