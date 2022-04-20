import json
import requests
from badRequest import BadRequest

class CoordController():

    def __init__(self, api_key):
        self._API_KEY = api_key
        self.defaultCall = "f7abd3f018df76b5c983da7768b7cf2a"
    
    def __getAPIKEY(self):
        return self._API_KEY

    def getDefaultCall(self):
        return self.defaultCall

    def getCityLonLat(self, cityName, resultLimit):
        
        apiCall = self.getDefaultCall() + f"direct?q={cityName}" +\
            f"&limit{resultLimit}&appid={self.__getAPIKEY}"

        data = requests.get(apiCall)

        if data.status_code in [400,401,402,404]:
            raise BadRequest(data.reason)

        return data 
