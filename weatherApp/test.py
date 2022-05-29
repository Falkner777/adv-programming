
from Controllers.weatherController import CoordController
import keys
import requests

import folium
from PIL import Image
import io
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys
from pyowm.utils.geo import Point
from pyowm.commons.tile import Tile,Image as IMAGE

op = "CL" 
z=5




coord = CoordController(keys.API_KEY)
lon,lat = coord.getCityLonLat("Los Angeles")

geopoint = Point(lon,lat)
x_tile, y_tile = Tile.tile_coords_for_point(geopoint, z)

call =f"http://maps.openweathermap.org/maps/2.0/weather/{op}/{z}/{x_tile}/{y_tile}?appid={keys.API_KEY}&opacity=0.6"
data = requests.get(call).content
image = Image.open(io.BytesIO(data))
image.save("test.png")
img = IMAGE.load("./test.png")

tile = Tile(x_tile,y_tile,z,0,img)
polygon = tile.bounding_polygon()
geopoints = polygon.points
geocoordinates = [(p.lon, p.lat) for p in geopoints]
print(geocoordinates)
lon_min,lon_max = geocoordinates[0][0],geocoordinates[1][0]
lat_min,lat_max = geocoordinates[-2][1], geocoordinates[-1][1]


myMap = folium.Map(location=[lat,lon],\
    zoom_start=10, parse_html=True)
img_overlay = folium.raster_layers.ImageOverlay(name="map", image ="./test.png",bounds=[[lat_min,lon_min],[lat_max,lon_max]])
img_overlay.add_to(myMap)
myMap.save("test.html")

app = qtw.QApplication(sys.argv)

web = QWebEngineView()
web.load(qtc.QUrl.fromLocalFile("/home/dimitris/adv_programming/adv-programming/weatherApp/test.html"))
web.show()
app.exec_()
