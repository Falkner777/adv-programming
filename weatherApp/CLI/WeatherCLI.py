import argparse
import sys
import keys
from Controllers.weatherController import WeatherController
from dataManager import DataManager
units = "metric"
API_KEY = keys.API_KEY
cityName=input()
WeatherCaller = WeatherController(API_KEY, units)
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
# parser_getweathercity = subparsers.add_parser('getweathercity')
# parser_getweathercity.set_defaults(func=WeatherCaller.getWeatherCity)
data = WeatherCaller.getWeatherCity(cityName)
info = DataManager.returnCurrentInfo(data)
print(info)
