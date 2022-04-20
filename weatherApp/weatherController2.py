import json


import requests


class WeatherController2:

    def __init__(self, api_key, default_call, units, language=None):
        self._API_KEY = api_key
        self.defaultCall = default_call
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

class BadRequest(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"\n{self.message}. Not acceptable longitude or latitude."
        
