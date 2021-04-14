import folium as f
import pandas as pd
# Create  Map object
map =  f.Map(location = [-28.29148236287175, 23.549727933663252], zoom_start = 6, tiles= "cartodb positron")


# Load data from csv
data = pd.read_csv("za.csv")

#get lat, lng, City, population
lat = list(data["lat"])
lng = list(data["lng"])
popups = list(data["city"])
populations = list(data["population"])

# Add Colours
colors = ['black', 'red', 'green', 'lightgreen', 'darkblue', 'cadetblue', 'darkgreen', 'lightgray', 'darkpurple', 'lightblue', 'blue', 'beige', 'red', 'orange', 'gray', 'pink', 'darkred', 'lightred', 'purple'] * 6

# Adding Elements to the map
fgv = f.FeatureGroup(name="City Markers")
for latitude, longitude,popup, color,population in zip(lat,lng, popups, colors, populations) :
    fgv.add_child(f.Marker(location=[latitude, longitude], popup=popup + "\nPopulation: " + str(population) , icon=f.Icon(color=color)))

#Adding a GeoJson Polygon

fgp = f.FeatureGroup(name="Population")

fgp.add_child(f.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(f.LayerControl())


#Save the Map
map.save("templates/index.html")
print("Map saved")
