
import os,sys
path = os.getcwd()
parentPath = os.path.dirname(path) + "/weatherApp"
sys.path.insert(0,parentPath)
from Controllers.coordController import CoordController
import keys
import requests
import folium
import folium.plugins as plugins
from PIL import Image
import io

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
        self.zoomLevel = 6
    
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
        """
        It takes a city name and a layer name as input, gets the coordinates of the city, gets the tile
        coordinates of the city, makes a call to the API, gets the image data, saves the image data as a
        png file, loads the png file, creates a tile object, gets the bounding polygon of the tile, gets
        the coordinates of the bounding polygon, gets the minimum and maximum longitude and latitude,
        creates a folium map, creates an image overlay, adds the image overlay to the map, adds the tile
        layers to the map, adds the layer control to the map, adds the minimap to the map, adds a marker
        to the map, and saves the map as an html file
        
        :param cityName: The name of the city you want to get the map for
        :param layerName: The name of the map layer you want to use
        """
        
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

        layers = ["Open Street Map","Stamen Terrain", "Stamen Toner", "Stamen Watercolor", "CartoDB Positron", "CartoDB Dark_Matter"]
        for layer in layers:
            folium.raster_layers.TileLayer(layer).add_to(weathermap)

        folium.LayerControl().add_to(weathermap)
        minimap = plugins.MiniMap(toggle_display=True)
        weathermap.add_child(minimap)


        folium.Marker([lat,lon],popup=cityName,tooltip='Open').add_to(weathermap)

        weathermap.save("./Controllers/map.html")


