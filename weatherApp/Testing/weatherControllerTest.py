
import unittest
import os,sys
path = os.getcwd()
parentPath = os.path.dirname(path) + "/weatherApp"
sys.path.insert(0,parentPath)
from Controllers.weatherController import WeatherController
from Exceptions.badRequest import BadRequest
from Exceptions.emptyRequestException import EmptyRequestException
import keys


weathCont = WeatherController(keys.API_KEY, "metric")


class TestWeatherControll(unittest.TestCase):

    def test_getWeatherCity(self):
        self.assertRaises(BadRequest,weathCont.getWeatherCity,"asdf")
        self.assertRaises(TypeError,weathCont.getWeatherCity,12)
        self.assertEqual(dict,type(weathCont.getWeatherCity("Lefkada")))
        self.assertEqual(dict, type(weathCont.getWeatherCity("Melbourne")))
        self.assertEqual(dict, type(weathCont.getWeatherCity("Patras")))
        self.assertEqual(dict, type(weathCont.getWeatherCity("Paris")))
        self.assertEqual(dict, type(weathCont.getWeatherCity("Berlin")))
        self.assertEqual(dict, type(weathCont.getWeatherCity("Dresden")))
    
    def test_getHourlyData(self):
        self.assertRaises(EmptyRequestException,weathCont.getHourlyData,"asdfasd")
        self.assertRaises(TypeError,weathCont.getHourlyData,123)
        self.assertEqual(list,type(weathCont.getHourlyData("Lefkada")))
        self.assertEqual(24,len(weathCont.getHourlyData("Peru")))
        self.assertEqual(24,len(weathCont.getHourlyData("Thessaloniki")))
        self.assertEqual(24,len(weathCont.getHourlyData("Rome")))
        self.assertEqual(24,len(weathCont.getHourlyData("Peristeri")))
    
    def test_getDailyData(self):
        self.assertRaises(EmptyRequestException,weathCont.getDailyData,"asdfasd")
        self.assertRaises(TypeError,weathCont.getDailyData,123)
        self.assertEqual(list,type(weathCont.getDailyData("Lefkada")))
        self.assertEqual(7,len(weathCont.getDailyData("Lefkada")))
        self.assertEqual(7,len(weathCont.getDailyData("Bangok")))
        self.assertEqual(7,len(weathCont.getDailyData("Munich")))
        self.assertEqual(7,len(weathCont.getDailyData("Vienna")))
        self.assertEqual(7,len(weathCont.getDailyData("Madrid")))