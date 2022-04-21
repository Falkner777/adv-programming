from audioop import add
import json
from badRequest import BadRequest
import requests

from coordController import CoordController


class WeatherController:

    def __init__(self, api_key, units, language=None):
        self._API_KEY = api_key
        self.defaultCall = "https://api.openweathermap.org/data/2.5/"
        self.units = units
        self.language = language
        self.coordsConverter = CoordController()

    def __getAPIKEY(self):
        return self._API_KEY

    def getDefaultCall(self):
        return self.defaultCall

    def getUnits(self):
        return self.units

    def getLanguage(self):
        return self.language
    
    def getWeatherCity(self, cityId):
        print("WeEaTheR")
    
    def getHourlyData(self, address):
        
        lon, lat = self.coordsConverter.getCityLonLat(address)
        
        
        apiCALL = self.getDefaultCall() + \
            f"onecall?lat={lat}&lon={lon}&" + \
                f"exclude=current,minutely,daily,alerts&units={self.getUnits()}&appid={self.__getAPIKEY()}"
        
        data = requests.get(apiCALL)

        if data.status_code in range(400,600):
            raise BadRequest(data.status_code)

        return data 

