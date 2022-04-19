import requests
import json

class Controller:

    def __init__(self, api_key, default_call, units):
        self.API_KEY = api_key
        self.defaultCall = default_call
        self.units = units
    
    def getWeatherCity(self, cityId):
        print("WeEaTheR")


