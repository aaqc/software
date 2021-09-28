#!/usr/bin/python

from token_handler import get_token
import requests
import math

params = (
    ('locations', f'{latitude},{longitude}'),
    ('key', f'get_token("google_maps")') 
)

def get_elevation(latitude: float, longitude: float):

    response = requests.get('https://maps.googleapis.com/maps/api/elevation/json', params=params)

    return response

def get_path_distance(start_coords: tuple, end_coords: tuple):
    lat1, lng1 = start_coords
    lat2, lng2 = end_coords

    #Earth Radius
    earth_radius = 6371
  
    lat_diffrance = math.radians(lat2 - lat1)
    lng_diffrance = math.radians(lng2 - lng1)

    lat1_radian = math.radians(lat1)
    lat2_radian = math.radians(lat2)
 
    haversine_formula = (pow(math.sin(lat_diffrance / 2), 2) + pow(math.sin(lng_diffrance / 2), 2) * math.cos(lat1_radian) * math.cos(lat2_radian))

    c = 2 * math.asin(math.sqrt(haversine_formula))

    return {"km": earth_radius * c, "m" :earth_radius * c * 1000 }

def calculate_mid_point(start_coords: tuple, end_coords: tuple):
    lat1, lng1 = start_coords
    lat2, lng2 = end_coords

    lngDiff = math.radians(lng2 - lng1)

    latA = math.radians(lat1)
    latB = math.radians(lat2)
    lngA = math.radians(lng1)

    bx = math.cos(latB) * math.cos(lngDiff)
    by = math.cos(latB) * math.sin(lngDiff)

    latMidway = math.degrees( 
        math.atan2(math.sin(latA) +
        math.sin(latB),math.sqrt((math.cos(latA) + bx) *
        (math.cos(latA) + bx)
         + by * by)))

    lngMidway = math.degrees(lngA + math.atan2(by, math.cos(latA) + bx))


    return (latMidway,lngMidway)

if __name__ == "__main__":
    start_coords = (57.690341, 11.974507)
    end_coords = (57.693616, 11.973180)
    # print(get_path_distance(start_coords, end_coords))
    print(calculate_mid_point(start_coords, end_coords))
    # print(get_elevation(57.708870,11.974560).text)
    pass
