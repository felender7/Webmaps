import folium as f

# Create  Map object
map =  f.Map(location = [-28.29148236287175, 23.549727933663252], zoom_start = 6, tiles= "cartodb positron")

# Adding Elements to the map
fg = f.FeatureGroup(name="My Map")
fg.add_child(f.Marker(location=[-29.60848569170139, 28.345260248070595], popup="Lesotho", icon=f.Icon(color="green")))
fg.add_child(f.Marker(location=[-23.852348170408053, 28.85612449250099], popup="Limpopo", icon=f.Icon(color="red")))

map.add_child(fg)

#Save the Map
map.save("south_africa_map.html")
print("Map saved")
