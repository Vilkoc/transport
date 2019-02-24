from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_bus_stop', views.add_bus_stop, name='add_bus_stop'),
    path('test', views.test, name='test'),
]
