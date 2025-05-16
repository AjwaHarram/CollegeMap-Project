import folium 
from folium import IFrame 

# Create the base map centered at a specific location
map = folium.Map(location=(31.8175, 70.9078), zoom_start=17)

# Dictionary containing department names, coordinates, and image paths
Departments = {
    "Admin Block": ((31.817530900978024, 70.90772164891065), "Admin Block.png"),
    "Girls Gate": ((31.81785, 70.9075), "CampusMap Project/gate.JPG"),
    "Boys Gate": ((31.81765, 70.90805), "Bgate.jpg"),
    "Botany": ((31.8177, 70.90715), "Botany.png"),
    "Islamiyat": ((31.8175718, 70.9071313), "Islamiyat.png"),
    "Physics": ((31.817443623428048, 70.90711271422474), "Physics.png"),
    "HPE": ((31.81700, 70.90710), "HPE.png"),
    "Chemistry": ((31.81715, 70.90705), "Chemistry.png"),
    "Zoology": ((31.81720, 70.90710), "Zoology.png"),
    "BS Block": ((31.816965673477505, 70.9083134649508), "BS Block.png"),
    "Computer Science": ((31.816580606711895, 70.90843724385537), "cs.JPEG"),
    "Library": ((31.8164874, 70.9084071), "Library.png"),
    "FSC classes": ((31.8161, 70.9080), "Fsc.png"),
    "Economy": ((31.816394208322258, 70.90837704849551), "Economy.png"),
    "Masjid": ((31.8165, 70.9072), "Masjid.png"),
    "Secrecy": ((31.8161, 70.9075), "Secrecy.png"),
    "Hostel": ((31.8160, 70.9074), "Hostel.png")
}

# Add markers for each department with image popup
for name, (coords, image) in Departments.items():
    html = f"""
    <h4>{name}</h4>
    <img src="{image}" width="200px">
    """
    iframe = IFrame(html, width=220, height=250)
    popup = folium.Popup(iframe, max_width=300)
    
    # Create a blue marker with popup
    folium.Marker(  
        location=coords,
        popup=popup,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(map) 


# Draw the main road from the Girls Gate
main_road = [
    (31.81785, 70.9075),  
    (31.8174, 70.9075)   
]
folium.PolyLine(  
    locations=main_road,
    color='white',
    weight=15,
    opacity=0.9,
    tooltip='Main Road from Girls Gate'
).add_to(map)

# Draw the road from the Boys Gate
gate2_road = [
    (31.8174, 70.90805),       
    (31.8163, 70.90805),       
    (31.81765, 70.90805)        
]
folium.PolyLine(
    locations=gate2_road,
    color='white',
    weight=15,
    opacity=0.9,
    tooltip='Main road from Boys Gate'
).add_to(map)

# Road turning west
west_road = [
    (31.8163, 70.90805),      
    (31.8163, 70.9073)        
]
folium.PolyLine(
    locations=west_road,
    color='white',
    weight=15,
    opacity=0.9,
    tooltip='Road turning west'
).add_to(map)

# New road moving straight down
straight_road = [
    (31.8174, 70.90805),        
    (31.8174, 70.9073)          
]
folium.PolyLine(
    locations=straight_road,
    color='white',  
    weight=15,
    opacity=0.9,
    tooltip='New road moving straight'
).add_to(map)

# New road heading south from straight road
new_road_south = [
    (31.8174, 70.9073),         
    (31.8163, 70.9073)        
]
folium.PolyLine(
    locations=new_road_south,
    color='white', 
    weight=15,
    opacity=0.9,
    tooltip='New road moving south'
).add_to(map)

# Short path to Admin Block
admin_block_road = [
    (31.8175309, 70.9077216),  
    (31.8174, 70.9077216)     
]        
folium.Polygon(
    locations=admin_block_road,
    color='white',
    weight=15,
    opacity=1,
    tooltip='Admin Block Road'
).add_to(map)

# Green lawn west of Admin Block
West_lawn = [
    (31.8175309, 70.90771),     
    (31.8175309, 70.90751),    
    (31.8174, 70.90751),        
    (31.8174, 70.90771)        
]
folium.Polygon(
    locations=West_lawn,
    color='green',
    fill=True,
    fill_color='green',
    fill_opacity=0.5,
    tooltip='West Lawn Area'
).add_to(map)

# Green lawn east of Admin Block
East_lawn = [  
    (31.8175309, 70.90774),      
    (31.8175309, 70.90805),      
    (31.8174, 70.90805),        
    (31.8174, 70.90774)       
]
folium.Polygon(
    locations=East_lawn,
    color='green',
    fill=True,
    fill_color='green',
    fill_opacity=0.5,
    tooltip='East Lawn Area'
).add_to(map)

# Lawn area from BS Block to Economy
bs_to_economy_lawn = [
    (31.81733, 70.90795),
    (31.81733, 70.90805),
    (31.81639, 70.90805),
    (31.81639, 70.90795)
]
folium.Polygon(
    locations=bs_to_economy_lawn,
    color='green',
    fill=True,
    fill_color='green',
    fill_opacity=0.5,
    tooltip='Lawn in front of BS Block to Economy'
).add_to(map)

# Campus boundary polygon
college_boundary = [
    (31.8160, 70.9073),   
    (31.8165, 70.9070),   
    (31.81715, 70.9070),  
    (31.8177, 70.9070),   
    (31.8180, 70.9073),   
    (31.8180, 70.9081),  
    (31.8177, 70.90845),  
    (31.8164, 70.90845), 
    (31.8160, 70.9080)    
]
folium.Polygon(
    locations=college_boundary,
    color='black',
    fill=True,
    fill_color='lightblue',
    fill_opacity=0.2,
    weight=3,
    tooltip='College Campus Boundary'
).add_to(map)

# Save the map to an HTML file
map.save("map.html") 