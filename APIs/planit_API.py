import requests


def planit_API(search_radius, latitude, longitude):
    """Returns Dictionary of All Planning Applications in a given search area"""

    applic_search_url = f"https://www.planit.org.uk/api/applics/json?krad={str(search_radius)}" \
                        f"&lat={str(latitude)}&lng={str(longitude)}"
    x = requests.get(applic_search_url)

    return x.json()  # Converts data to dictionary


