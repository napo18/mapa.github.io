""" Este código básicamente toma los datos de ubicación y tipos de reclamo desde el archivo Excel, los coloca en un mapa interactivo y guarda ese mapa en un archivo HTML. 
Luego, abre el archivo HTML en el navegador para que puedas ver el mapa resultante."""
#Librerias
import folium # se obtienen las caracteristicas html y opciones para la creacion del mapa
import geopandas as gpd
import webbrowser # para revisar en la web el documento programado
import pandas as pd #se utiliza para leer los volumenes de datos
import matplotlib as mlp
from folium import Choropleth

from folium.plugins import MarkerCluster #sirve para agrupar los puntos espaciales o huelgas



#Puntos Espaciales

huelgas = pd.read_excel("/Users/edwinalmanzarpena/Documents/Proyectos/Mapa2/Georeferenciacion.xlsx") #definir la ubicacion del archivo xls a utilizar



#Desarrollo de mapa
mapa = folium.Map(location=[18.498608379132104, -69.86607496153842], #Objeto utilizado como modulo con el metodo map para generar el mapa y la location para la region que se busca focalizar 
                  zoom_start=9) # se utiliza para generar el zoom necesario para el mapa


#Capa de huelgas

#eleccion de variables dentro de las columnas del .xlsx o DateFrame
fecha = list(huelgas["Fecha"])
reclamo = list(huelgas["Reclamo"])
latitud = list(huelgas["Latitud"])
longitud = list(huelgas["Longitud"])
color = list(huelgas["Color"])
prefix = list(huelgas["Prefix"])
icon = list(huelgas["Icon"])
descripcion = list(huelgas["descripcion"])
mc_h = MarkerCluster()

for fc,re,la,lo,cl,pr,ic,dc in zip(fecha,reclamo,latitud,longitud,color,prefix,icon,descripcion): #Se itera a través de los datos usando zip para combinar los elementos correspondientes de las listas.
    mc_h.add_child(folium.Marker(location=[la,lo],
    popup="<b>Fecha: </b>"+str(fc)+ "<br> <b> Reclamo: <b> "+re+"</br>" +"<br> <b> Descripción: <b>"+str(dc)+"</br>", max_width=4000, min=4000,
    icon=folium.Icon(color=cl,
    icon=ic,
    prefix=pr)))

capa_huelgas = folium.FeatureGroup(name="Huelgas")
mc_h.add_to(capa_huelgas)

mapa.add_child(capa_huelgas)

"""for index, row in huelgas.iterrows(): #
    folium.Marker([row["Latitud"], row["longitud"]], #utilizacion de la funcion importada que permite la selecion de los encabezados del documento (excel)
                 popup=row["Tipo de Reclamo"], # Indica la etiqueta a colocar a los iconos y coordenadas
                 icon=folium.Icon(color="Red", icon="fire", prefix="fa")).add_to(mapa) # identificador y creador de iconos por medio de folium"""
 
#Capa de provincias--------------------------------------
prov= gpd.read_file("/Users/edwinalmanzarpena/Documents/Proyectos/Mapa2/PRO.geojson") #Este código utiliza geopandas para leer un archivo GeoJSON ubicado en la ruta especificada.
style= {"fillcolor": "#808080", "lineColor": "#0FFFFF"} #Aquí se define un estilo para las provincias en el mapa

#Creación de una capa GeoJSON en Folium
prov_layer=folium.GeoJson(  #metodo de folium llamado GeoJason
    prov,
    name= "Provincias",
    style_function= lambda x: style,
    tooltip= folium.GeoJsonTooltip(
        fields=["PROV", "TOPONIMIA"],
        aliases=["NO.: ", "Nombre: "],
        localize=True
    )).add_to(mapa)

""" Aquí se utiliza folium para crear una capa GeoJSON en el mapa interactivo. La capa prov_layer se crea a partir de los datos del DataFrame prov. Se le asigna el nombre "Provincias" y se aplica el estilo definido anteriormente.

Además, se agrega una información emergente (tooltip) que muestra dos campos del GeoJSON: "PROV" y "TOPONOMIA". Estos campos se mostrarán como "NO." y "Nombre" en el tooltip respectivamente. """

# Capa de mapa coroplético (Agrega esto)
choropleth_data = pd.read_excel("/Users/edwinalmanzarpena/Documents/Proyectos/Mapa2/Coropletico.xlsx")  # Reemplaza esto con la ubicación de tus datos coropléticos
# Asegúrate de que tus datos contengan un campo con nombres de provincias o áreas y un campo con valores para cada área

choropleth = folium.Choropleth(
    geo_data= prov,  # Reemplaza esto con la ubicación de tus datos geoespaciales
    data=choropleth_data,
    columns=["TOPONIMIA", "Valor"],  # Reemplaza con tus columnas adecuadas
    key_on="feature.properties.TOPONIMIA",
    fill_color="OrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    ine_color='black',
    highlight=True,
    legend_name="Título del Mapa Coroplético"
 ).add_to(mapa)




#Forma de agregar Capas a mapa base
folium.TileLayer("CartoDB positron").add_to(mapa) #se utiliza para agregar capas extra al mapa
folium.TileLayer("Stamen Terrain").add_to(mapa) #se utiliza para agregar capas extra al mapa
folium.TileLayer("OpenStreetMap").add_to(mapa) #se utiliza para agregar capas extra al mapa
folium.TileLayer("Stamen Toner").add_to(mapa) #se utiliza para agregar capas extra al mapa

folium.LayerControl().add_to(mapa)

mapa.save("index.html") #crea y guarda el archivo html, generado por las funciones
webbrowser.open("index.html")