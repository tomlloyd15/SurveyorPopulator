from geopy.geocoders import Nominatim


def get_coordinates(address=""):
    """Function that returns coordinates of an address"""
    geolocator = Nominatim(user_agent="tobywilkins1@gmail.com")
    location = geolocator.geocode(address)
    postcode = location.raw['display_name'].split(',')[-2]
    postcode = postcode.lstrip()  # removes blank space at start of string

    return location.latitude, location.longitude, postcode  # returns longitude, latitude, and postcode

