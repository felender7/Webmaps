import folium as f
import pandas as pd
# Create  Map object
map =  f.Map(location = [-28.29148236287175, 23.549727933663252], zoom_start = 6, tiles= "cartodb positron")

# Adding Elements to the map
# Load data from csv
data = pd.read_csv("za.csv")

#get lat and lng
lat = list(data["lat"])
lng = list(data["lng"])
popups = list(data["city"])
colors = ['black', 'red', 'green', 'lightgreen', 'darkblue', 'cadetblue', 'darkgreen', 'lightgray', 'darkpurple', 'lightblue', 'blue', 'beige', 'red', 'orange', 'gray', 'pink', 'darkred', 'lightred', 'purple'] * 6
fg = f.FeatureGroup(name="My Map")
for latitude, longitude,popup, color in zip(lat,lng, popups, colors) :
    fg.add_child(f.Marker(location=[latitude, longitude], popup=popup, icon=f.Icon(color=color)))

map.add_child(fg)


#Save the Map
map.save("south_africa_map.html")
print("Map saved")
