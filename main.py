from APIs.planit_API import planit_API
from Docx_Populators.planit_populator import planit_document_creator
from Tools.geocode_tool import get_coordinates

"""Main Function"""

search_radius = 0.1  # Search Radius in KM
address = "46 Cloford Close, Trowbridge, Wiltshire"  # Address as a string

lat, lng = get_coordinates(address)
planit_document_creator(planit_API(search_radius, lat, lng))
