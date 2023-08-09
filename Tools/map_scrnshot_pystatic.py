import staticmaps
from PIL import Image

def save_to_image(latitude, longitude):
    print("Saving Map as .png ...")
    context = staticmaps.Context()
    context.set_tile_provider(staticmaps.tile_provider_OSM)

    point = staticmaps.create_latlng(latitude, longitude)

    context.add_object(staticmaps.Marker(point, size=10))

    image = context.render_pillow(800, 500)
    image.save("Tools/Map_Images/map.png")

    print("Map Saved as map.png")

