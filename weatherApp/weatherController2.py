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
    
    def getWeatherCity(self, CityName):
        apiCALL = self.getDefaultCall() + \
            f"weather?q={CityName}&" + \
                f"exclude=minutely,daily,alerts,hourly&units={self.getUnits()}&appid={self.__getAPIKEY()}"    
        data = requests.get(apiCALL)
        if data.status_code in range(400,600):
            raise BadRequest(data.status_code)
        return data

    
    def getHourlyData(self, latitude, longitude):
        return self.hourly

        
