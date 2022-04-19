import requests
import json

class Controller:

    def __init__(self, api_key, units):
        self.API_KEY = api_key
        self.units = units
    
    def getWeatherCity(self, cityId):
        print("WeEaTheR")


