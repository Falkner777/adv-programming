import json
from badRequest import BadRequest
import requests


class WeatherController:

    def __init__(self, api_key, units, language=None):
        self._API_KEY = api_key
        self.defaultCall = "https://api.openweathermap.org/data/2.5/"
        self.units = units
        self.language = language
    
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
    
    def getHourlyData(self, latitude, longitude):
        try:
            lon = float(longitude)
        except:
            raise TypeError(f"Longitude but be of type float.{type(lon)} given")

        try:
            lat = float(latitude)
        except:
            raise TypeError(f"Latitude but be of type float.{type(lat)} given")

        apiCALL = self.getDefaultCall() + \
            f"onecall?lat={lat}&lon={lon}&" + \
                f"exclude=current,minutely,daily,alerts&units={self.getUnits()}&appid={self.__getAPIKEY()}"
        
        data = requests.get(apiCALL)

        if data.status_code == 400:
            raise BadRequest(data.reason)

        return data 

