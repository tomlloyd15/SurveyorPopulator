from geopy.geocoders import Nominatim


def get_coordinates(address=""):
    """Function that returns coordinates of an address"""

    geolocator = Nominatim(user_agent="tobywilkins1@gmail.com")
    location = geolocator.geocode(address)

    return location.latitude, location.longitude  # returns longitude and latitude
