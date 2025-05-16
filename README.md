# College Map 

This project uses the [Folium](https://python-visualization.github.io/folium/) library to create an interactive map of a college campus. The map includes markers for various departments, roads, lawns, gates, and a visual boundary for the campus.

## 🗺️ Features

- **Interactive Map** centered at the college location.
- **Department Markers**: Each major department/building is marked with a popup showing its name and an image.
- **Roads and Paths**: Main roads and walkways are illustrated using white polylines.
- **Lawns**: Green lawn areas between buildings are drawn using polygons.
- **Campus Boundary**: The overall college campus is enclosed with a transparent boundary polygon.

## 📍 Departments and Landmarks Included

- Admin Block  
- Botany, Physics, Chemistry, Zoology, HPE, Islamiyat  
- BS Block, Computer Science, Library, FSC Classes, Economy  
- Masjid, Secrecy, Hostel  
- Girls Gate & Boys Gate  

## 🛠️ Technologies Used

- Python 3
- Folium Library
- HTML Popups for image embedding

## 📁 File Structure

CampusMap/
│
├── images/ # Folder for all referenced images
│ ├── Admin Block.png
│ ├── Botany.png
│ ├── ...
│
├── map.html # The generated interactive map
├── campus_map.py # Main Python script to create the map
└── README.md # Project documentation
## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/CampusMap.git
   cd CampusMap
2. Install required package:
   ```bash
   pip install folium
3. Run the script:
    ```bash
    python campus_map.py
> ⚠️ **Note:** Ensure all image paths used in the code are correctly linked to your local or hosted image files. Otherwise, image popups may not render.
