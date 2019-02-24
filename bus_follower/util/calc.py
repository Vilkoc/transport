from .funct import *


def find_nearest_stop(coord):
    pass

def find_routes(begin, end):
    # search which routes curses between 2 stops
    pass

def nearest_buses(stop, route):
    for bus in get_buses_coord_tg(route):
        pass

def calc_time(bus, stop):
    pass

#sql='SELECT * FROM bus_stop ORDER BY ABS(ABS(lat - arg_lat) - ABS(lit - arg_lit))'