import gmaps
import os
import googlemaps
import pandas as pd
import time
from geopy.geocoders import GoogleV3
import geopy.distance



def miles_to_meters(miles):
    try:
        return miles*1609.34
    except:
        return 0

API_KEY= os.environ.get('API_KEY')
map_client=googlemaps.Client(API_KEY)

def convert_lat_long(zipcode):
    coordinates=[]
    geolocator = GoogleV3(api_key=API_KEY)
    name = zipcode
    location = geolocator.geocode(name)

    coordinates.append(location.latitude)
    coordinates.append(location.longitude)
    tuple(coordinates)
    return tuple(coordinates)

def get_places_from_coordinates(latitude_longitude):
    location=latitude_longitude
    search_string='veterinary clinics'

    distance= miles_to_meters(5)
    result_list=[]

    response=map_client.places_nearby(
        location=location,
        keyword=search_string,
        name='veterinary',
        radius=distance
    )

    result_list.extend(response.get('results'))
    next_page_token=response.get('next_page_token')

    while next_page_token:
        time.sleep(2)
        response=map_client.places_nearby(
        location=location,
        keyword=search_string,
        name='veterinary',
        radius=distance,
        page_token=next_page_token
        )

        result_list.extend(response.get('results'))
        next_page_token=response.get('next_page_token')
        places_dict={}
        for a in response['results']:
            place_id= a['place_id']
            place_name=a['name']
            place_lat= a['geometry']['location']['lat']
            place_long= a['geometry']['location']['lng']
            places_dict[place_id]={'lat':place_lat,'long':place_long, 'name':place_name}
       
    return places_dict

        
