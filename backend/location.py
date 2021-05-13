import geocoder
from geopy.geocoders import Nominatim

def location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    g = geocoder.ip('me')
    coordinates=g.latlng
    latitude=str(coordinates[0])
    longitude=str(coordinates[1])
    location = geolocator.geocode(latitude+","+longitude)
    return location