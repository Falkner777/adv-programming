import json
import requests
from Exceptions.badRequest import BadRequest
from Exceptions.emptyRequestException import EmptyRequestException
import keys


class CoordController():

    def __init__(self):
        self._API_KEY = keys.API_KEY
        self.defaultCall = "http://api.openweathermap.org/geo/1.0/"
    
    def __getAPIKEY(self):
        return self._API_KEY

    def getDefaultCall(self):
        return self.defaultCall
        
    
    def getCityLonLat(self, cityName, resultLimit=1):
        
        apiCall = self.getDefaultCall() + f"direct?q={cityName}" +\
            f"&limit{resultLimit}&appid={self.__getAPIKEY()}"

        data = requests.get(apiCall)

        if data.status_code in range(400,600):
            raise BadRequest(data.status_code)

        dataJson = data.json()

        if len(dataJson) == 0:
            raise EmptyRequestException()

        dataJson = dataJson[0]

        return dataJson["lon"], dataJson["lat"] 
