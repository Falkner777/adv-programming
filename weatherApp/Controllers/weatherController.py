from audioop import add
import json
from Exceptions.badRequest import BadRequest
import requests

from Controllers.coordController import CoordController


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
    
    def getWeatherCity(self, CityName):
        apiCALL = self.getDefaultCall() + \
            f"weather?q={CityName}&" + \
                f"exclude=minutely,daily,alerts,hourly&units={self.getUnits()}&appid={self.__getAPIKEY()}"    
        data = requests.get(apiCALL)
        if data.status_code in range(400,600):
            raise BadRequest(data.status_code)
        datap=data.json()
        return datap
    
    def getHourlyData(self, address):
        """
        It takes an address, converts it to coordinates, and then uses those coordinates to make a call
        to the OpenWeatherMap API to get the hourly weather data for the next 24 hours.
        
        :param address: The address of the city you want to get the weather for
        :return: A list of dictionaries.
        """
        
        lon, lat = self.coordsConverter.getCityLonLat(address)
        apiCALL = self.getDefaultCall() + \
            f"onecall?lat={lat}&lon={lon}&" + \
                f"exclude=current,minutely,daily,alerts&units={self.getUnits()}&appid={self.__getAPIKEY()}"
        
        data = requests.get(apiCALL)
        if data.status_code in range(400,600):
            raise BadRequest(data.status_code)

        dataJson = data.json()["hourly"][:24]
        return dataJson

    def getDailyData(self, address):
        """
        It takes an address, converts it to coordinates, and then makes a call to the API to get the
        daily weather data for the next 7 days
        
        :param address: The address of the city you want to get the weather for
        :return: A list of dictionaries.
        """
        
        lon, lat = self.coordsConverter.getCityLonLat(address)
        apiCALL = self.getDefaultCall() + \
            f"onecall?lat={lat}&lon={lon}&" + \
                f"exclude=current,minutely,hourly,alerts&units={self.getUnits()}&appid={self.__getAPIKEY()}"
        
        data = requests.get(apiCALL)
        if data.status_code in range(400,600):
            raise BadRequest(data.status_code)

        dataJson = data.json()["daily"][:7]
        return dataJson

