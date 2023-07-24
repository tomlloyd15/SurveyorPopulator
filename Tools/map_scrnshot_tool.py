import folium
import io
import matplotlib.pyplot as plt
from PIL import Image


def plot_point_on_map(latitude, longitude):
    folium_map = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude]).add_to(folium_map)
    return folium_map


def save_to_image(latitude, longitude):
    # Example usage
    cur_map = plot_point_on_map(latitude, longitude)
    cur_map.save("Tools/Map_Images/map.html")
    print("Map Saved as map.html.")
    print("Saving Map as .png ...")
    img_data = cur_map._to_png()
    img = Image.open(io.BytesIO(img_data))
    img.save('Tools/Map_Images/map.png')
    print("Map Saved as map.png")
