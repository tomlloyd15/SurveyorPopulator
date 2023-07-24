from APIs.planit_API import planit_API
from Docx_Populators.planit_populator import planit_document_creator
from Tools.geocode_tool import get_coordinates

from APIs.EPC_API import get_epc_report
from Docx_Populators.EPC_populator import EPC_document_creator

from Tools.map_scrnshot_tool import save_to_image

"""Main Parameters"""
search_radius = 0.1  # Search Radius in KM
address = "46 Cloford Close, Trowbridge, Wiltshire"  # Address as a string


"""Geocode"""
lat, lng, postcodeReceived = get_coordinates(address)
print(f"Postcode: {postcodeReceived}")


"""Save map to image"""
save_to_image(lat, lng)


"""Planit Document Populate"""
print("Processing Planit Document...")
planit_document_creator(planit_API(search_radius, lat, lng))


"""EPC Document Populate"""
print("Processing EPC Document...")
auth_token = "dG9ieXdpbGtpbnMxQGdtYWlsLmNvbTo0ZTc5OGNkY2U3ZjdjN2Q0ZTY2ZWVlZjdmMGQxNzI4YTNlZjc4YThk"
postcode = postcodeReceived
building_name = None
address = None

EPC_document_creator(get_epc_report(auth_token, postcode, building_name, address)[0])


