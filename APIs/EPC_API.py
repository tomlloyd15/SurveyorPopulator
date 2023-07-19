import json.decoder

import requests


def get_epc_report(auth_token, postcode, building_name=None, address=None):
    """Takes EPC Certificates from a postcode and returns EPC Data for Specified Area
    Will Return Domestic and Non-Domestic Data Separately"""

    domestic_base_url = "https://epc.opendatacommunities.org/api/v1/domestic/search"
    non_domestic_base_url = "https://epc.opendatacommunities.org/api/v1/non-domestic/search"

    params = {
        "postcode": postcode,
    }

    if building_name:
        params["buildingname"] = building_name
    if address:
        params["address"] = address

    headers = {
        "Authorization": f"Basic {auth_token}",
        "Accept": "application/json"
    }

    domestic_response = requests.get(domestic_base_url, params=params, headers=headers)
    non_domestic_response = requests.get(non_domestic_base_url, params=params, headers=headers)

    print(f"Domestic Response Status Code: {domestic_response.status_code}")
    print(f"Non-Domestic Response Status Code: {non_domestic_response.status_code}")

    """Convert To Dictionary"""
    try:
        domestic_response_dict = domestic_response.json()
    except json.decoder.JSONDecodeError:
        print("No domestic Data")
        domestic_response_dict = {}

    try:
        non_domestic_response_dict = non_domestic_response.json()
    except json.decoder.JSONDecodeError:
        print("No non-domestic Data")
        non_domestic_response_dict = {}

    return domestic_response_dict, non_domestic_response_dict
