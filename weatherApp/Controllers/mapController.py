import os,sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)
from weatherController import WeatherController
from coordController import CoordController
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
from Exceptions.noConnection import ConnectionChecker as netChecker
from Exceptions.badRequest import BadRequest

class MapController():

    def __init__(self,api_key):
        self.__API_KEY = api_key
        self.defaultCall = "http://maps.openweathermap.org/maps/2.0/weather/"
        self.coordController = CoordController(api_key)
        self.zoomLevel = 4
    
    @property
    def __APIKEY(self):
        return self.__API_KEY
    
    @__APIKEY.setter
    def __APIKEY(self,key):
        if not isinstance(key,str):
            raise TypeError(f"key must be of <class 'str'> , {type(key)} given")
        self.__API_KEY = key

    @property
    def defaultcall(self):
        return self.defaultCall

    @property
    def zoom(self):
        return self.zoomLevel
    
    def setMap(self,cityName, layerName):
        
        if not isinstance(cityName,str):
            raise TypeError(f"cityName must be of <class 'str'> , {type(cityName)} given")

        if not isinstance(layerName,str):
            raise TypeError(f"layerName must be of <class 'str'> , {type(layerName)} given")


        lon,lat = self.coordController.getCityLonLat(cityName)
        geopoint = Point(lon, lat)
        x_tile,y_tile = Tile.tile_coords_for_point(geopoint,self.zoom)

        call = self.defaultCall + \
            f"{layerName}/{self.zoom}/{x_tile}/{y_tile}?appid={self.__APIKEY}"
        netChecker.checkConnection()
        data = requests.get(call)

        if data.status_code in range(400,600):
            raise BadRequest(data.status_code)
        
        imageData = data.content
        image = Image.open(io.BytesIO(imageData))
        
        imagePath = "./Controllers/mapLayer.png"
        image.save(imagePath)

        imgForMap = IMAGE.load(imagePath)
        
        tile = Tile(x_tile, y_tile,self.zoom, 0, imgForMap)
        polygon = tile.bounding_polygon()
        geopoints = polygon.points
        geocoordinates = [(p.lon, p.lat) for p in geopoints]
        lon_min,lon_max = geocoordinates[0][0],geocoordinates[1][0]
        lat_min,lat_max = geocoordinates[-2][1], geocoordinates[-1][1]
        weathermap = folium.Map(location=[lat,lon],\
        zoom_start=10, parse_html=True)
        img_overlay = folium.raster_layers.ImageOverlay(name="map", image = imagePath,bounds=[[lat_min,lon_min],[lat_max,lon_max]])
        img_overlay.add_to(weathermap)
        weathermap.save("./Controllers/map.html")


test = MapController(keys.API_KEY)
test.setMap("Lefkada","CL")