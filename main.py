from APIs.planit_API import planit_API
from Docx_Populators.planit_populator import planit_document_creator
from Tools.geocode_tool import get_coordinates

from APIs.EPC_API import get_epc_report
from Docx_Populators.EPC_populator import EPC_document_creator

"""Main Function"""


search_radius = 0.1  # Search Radius in KM
address = "46 Cloford Close, Trowbridge, Wiltshire"  # Address as a string
lat, lng, postcodeRecieved = get_coordinates(address)
print(postcodeRecieved)
"""Planit Document Populate"""
print("Processing Planit Document...")
#lat, lng = get_coordinates(address)
planit_document_creator(planit_API(search_radius, lat, lng))


"""EPC Document Populate"""
print("Processing EPC Document...")
auth_token = "dG9ieXdpbGtpbnMxQGdtYWlsLmNvbTo0ZTc5OGNkY2U3ZjdjN2Q0ZTY2ZWVlZjdmMGQxNzI4YTNlZjc4YThk"
postcode = postcodeRecieved
building_name = None
address = None

EPC_document_creator(get_epc_report(auth_token, postcode, building_name, address)[0])



