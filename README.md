# mapa.github.io

README - Interactive Mapping Application with Python
This repository contains a Python code that allows you to retrieve location data and types of complaints from an Excel file, represent them on an interactive map, and save that map to an HTML file. Below is a brief description of the key components of the code and how to use it.

Code Description
The code is divided into the following sections:

Libraries: Necessary libraries are imported to run the program, including Folium, Geopandas, Webbrowser, Pandas, and others.

Spatial Points: An Excel file containing location data and types of complaints is loaded.

Map Development: An interactive map is created with Folium, centered on a specific location, and the zoom level is configured.

Strikes Layer: Iterate through the data in the Excel file and create a group of markers on the map to represent complaints. Each marker includes information such as the date, type of complaint, and a description.

Provinces Layer: Load a GeoJSON file containing geographical data of provinces and create a layer of provinces on the map. A style is configured, and popup information is added to each province.

Choropleth Map Layer: Use Folium to create a choropleth map that allows you to visualize specific data about provinces or areas. Choropleth data is read from an Excel file, and fill color and opacity are assigned.

Adding Layers to the Base Map: Base map layers are added to the map, allowing you to switch between different map styles.

Saving and Viewing the Map: The resulting map is saved to an HTML file named "index.html," and this file is automatically opened in the web browser for viewing.

How to Use the Code
To use this code, follow these steps:

Ensure that you have all the required libraries installed in your Python environment.

Modify the file paths for the Excel and GeoJSON files in the "Spatial Points" and "Provinces Layer" sections to match the location of your own data files.

If you want to add a choropleth layer, make sure you have an appropriate data file and modify the path in the "Choropleth Map Layer" section.

Run the Python code. An HTML file named "index.html" will be generated and automatically opened in your web browser.
