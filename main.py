from APIs.planit_API import planit_API
from Docx_Populators.planit_populator import planit_document_creator
from Tools.geocode_tool import get_coordinates

from APIs.EPC_API import get_epc_report
from Docx_Populators.EPC_populator import EPC_document_creator

from Tools.map_scrnshot_tool import save_to_image

from Docx_Populators.combined_populator import combined_document_creator

"""Main Parameters"""
search_radius = 0.1  # Search Radius in KM
address = "12 Eaton Crescent, Clifton, Bristol"  # Address as a string


"""Geocode"""
lat, lng, postcodeReceived = get_coordinates(address)
print(f"Postcode: {postcodeReceived}")


"""Save map to image"""
save_to_image(lat, lng)


"""Planit Data"""
print("Processing Planit Document...")
planit_data = planit_API(search_radius, lat, lng)


"""EPC Data"""
print("Processing EPC Document...")
auth_token = "dG9ieXdpbGtpbnMxQGdtYWlsLmNvbTo0ZTc5OGNkY2U3ZjdjN2Q0ZTY2ZWVlZjdmMGQxNzI4YTNlZjc4YThk"
postcode = postcodeReceived
building_name = None
EPC_address = None

EPC_data = get_epc_report(auth_token, postcode, building_name, EPC_address)[0]


"""Populate Combined Document"""
print("Compiling Document...")
combined_document_creator(address, planit_data, EPC_data)

