#import folium
import pandas as pd
data = pd.read_csv("mapdata.csv")
long =data["Location_Coordinates"]
#lat =data["Location"]
print(long)
'''
m = folium.Map(
    location=[46.3014, -123.7390],
    zoom_start=7,
    tiles='Stamen Terrain'
)

folium.Marker(
    location=[47.3489, -124.708],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(vis1, width=450, height=250))
).add_to(m)

folium.Marker(
    location=[44.639, -124.5339],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(vis2, width=450, height=250))
).add_to(m)

folium.Marker(
    location=[46.216, -124.1280],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(vis3, width=450, height=250))
).add_to(m)
'''