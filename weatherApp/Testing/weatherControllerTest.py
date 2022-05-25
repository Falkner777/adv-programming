from typing import Type
import unittest
import os,sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)
from Controllers.weatherController import WeatherController
from Exceptions.badRequest import BadRequest
from Exceptions.emptyRequestException import EmptyRequestException
import keys
import requests

weathCont = WeatherController(keys.API_KEY, "metric")


class TestWeatherControll(unittest.TestCase):

    def test_getWeatherCity(self):
        self.assertRaises(BadRequest,weathCont.getWeatherCity,"asdf")
        self.assertRaises(TypeError,weathCont.getWeatherCity,12)
        self.assertEqual(dict,type(weathCont.getWeatherCity("Lefkada")))
    
    def test_getHourlyData(self):
        self.assertRaises(EmptyRequestException,weathCont.getHourlyData,"asdfasd")
        self.assertRaises(TypeError,weathCont.getHourlyData,123)
        self.assertEqual(list,type(weathCont.getHourlyData("Lefkada")))
        self.assertEqual(24,len(weathCont.getHourlyData("Lefkada")))
    
    def test_getDailyData(self):
        self.assertRaises(EmptyRequestException,weathCont.getDailyData,"asdfasd")
        self.assertRaises(TypeError,weathCont.getDailyData,123)
        self.assertEqual(list,type(weathCont.getDailyData("Lefkada")))
        self.assertEqual(7,len(weathCont.getDailyData("Lefkada")))