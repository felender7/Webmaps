import folium as f

# Create  Map object
map =  f.Map(location = [-28.29148236287175, 23.549727933663252], zoom_start = 6, tiles= "cartodb positron")

# Adding Elements to the map
coordinates = [[-29.60848569170139, 28.345260248070595], [-23.852348170408053, 28.85612449250099] , [-26.47871416756294, 28.87755514305355]]
popups = ["Lesotho", "Limpop", "Gauteng"]
colors = ["red","green", "blue"]

fg = f.FeatureGroup(name="My Map")
for coordinate,popup,color in zip(coordinates, popups, colors) :
    fg.add_child(f.Marker(location=coordinate, popup=popup, icon=f.Icon(color=color)))

map.add_child(fg)


#Save the Map
map.save("south_africa_map.html")
print("Map saved")
