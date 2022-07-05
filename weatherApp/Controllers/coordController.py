import os,sys

path = os.getcwd()

sys.path.insert(0, path)

import requests
from Exceptions.badRequest import BadRequest
from Exceptions.emptyRequestException import EmptyRequestException



class CoordController():

    def __init__(self,api_key):
        self.__API_KEY = api_key
        self.defaultCall = "http://api.openweathermap.org/geo/1.0/"
    
    @property
    def __APIKEY(self):
        return self.__API_KEY
    
    @__APIKEY.setter
    def __APIKEY(self,key):
        if not isinstance(key,str):
            raise TypeError(f"key must be of <class 'str'> , {type(key)} given")
        self.__API_KEY = key

    def getDefaultCall(self):
        return self.defaultCall
        
    def getCityLonLat(self, cityName):

        if not isinstance(cityName,str):
            raise TypeError(f"cityName must be of <class 'str'> , {type(cityName)} given")
       
        apiCall = self.getDefaultCall() + f"direct?q={cityName}" +\
            f"&limit1&appid={self.__APIKEY}"

        data = requests.get(apiCall)
        if data.status_code in range(500,600):
            raise BadRequest(data.status_code)

        dataJson = data.json()

        if len(dataJson) == 0:
            raise EmptyRequestException()
        dataJson = dataJson[0]

        return dataJson["lon"], dataJson["lat"] 

