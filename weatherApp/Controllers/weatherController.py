import os,sys

path = os.getcwd()

sys.path.insert(0, path)

from Exceptions.badRequest import BadRequest
from Exceptions.noConnection import ConnectionChecker as netChecker
import requests

from Controllers.coordController import CoordController


class WeatherController:

    def __init__(self, api_key, units, language=None):
        self.__API_KEY = api_key
        self.defaultCall = "https://api.openweathermap.org/data/2.5/"
        self.units = units
        self.language = language
        self.coordsConverter = CoordController(api_key)

    @property
    def __APIKEY(self):
        return self.__API_KEY

    @__APIKEY.setter
    def __APIKEY(self, key):
        if not isinstance(key,str):
            raise TypeError(f"key must be of <class 'str'> , {type(key)} given")
        self.__API_KEY = key

    def getDefaultCall(self):
        return self.defaultCall

    def getUnits(self):
        return self.units

    def getLanguage(self):
        return self.language
    
    def getWeatherCity(self, CityName):
        if not isinstance(CityName,str):
            raise TypeError(f"CityName must be of <class 'str'> , {type(CityName)} given")
        apiCALL = self.getDefaultCall() + \
            f"weather?q={CityName}&" + \
                f"exclude=minutely,daily,alerts,hourly&units={self.getUnits()}&appid={self.__APIKEY}"    
        
        netChecker.checkConnection()
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
        if not isinstance(address,str):
            raise TypeError(f"address must be of <class 'str'> , {type(address)} given")

        lon, lat = self.coordsConverter.getCityLonLat(address)
        apiCALL = self.getDefaultCall() + \
            f"onecall?lat={lat}&lon={lon}&" + \
                f"exclude=current,minutely,daily,alerts&units={self.getUnits()}&appid={self.__APIKEY}"
        
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
        if not isinstance(address,str):
            raise TypeError(f"address must be of <class 'str'> , {type(address)} given")
        lon, lat = self.coordsConverter.getCityLonLat(address)
        apiCALL = self.getDefaultCall() + \
            f"onecall?lat={lat}&lon={lon}&" + \
                f"exclude=current,minutely,hourly,alerts&units={self.getUnits()}&appid={self.__APIKEY}"
        
        data = requests.get(apiCALL)
        if data.status_code in range(400,600):
            raise BadRequest(data.status_code)

        dataJson = data.json()["daily"][:7]
        return dataJson


