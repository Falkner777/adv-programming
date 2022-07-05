
import unittest
import os,sys
path = os.getcwd()

sys.path.insert(0, path)
from dataManager import DataManager
from Controllers.weatherController import WeatherController
import keys

class TestDataManager(unittest.TestCase):
    
    def setUp(self) -> None:
        self.weatherContr = WeatherController(keys.API_KEY,"metric")
        self.dataHour = self.weatherContr.getHourlyData("Patras")
        self.dataWeek = self.weatherContr.getDailyData("Patras")
        self.dataNow = self.weatherContr.getWeatherCity("Patras")

    def test_returnTimestamps(self):
        self.assertRaises(Exception,DataManager.returnTimestamps,self.dataHour,"asd")
        self.assertEqual(len(DataManager.returnTimestamps(self.dataHour,"hour")),24)
        self.assertEqual(len(DataManager.returnTimestamps(self.dataWeek,"day")),7)
        self.assertEqual(type(DataManager.returnTimestamps(self.dataHour,"hour")),list)
        self.assertEqual(type(DataManager.returnTimestamps(self.dataWeek,"day")),list)

    def test_TemperatureDaily(self):
        self.assertRaises(TypeError,DataManager.returnTemperaturesDaily,1)
        self.assertEqual(type(DataManager.returnTemperaturesDaily(self.dataWeek)),dict)
        lenOfLists = len(DataManager.returnTemperaturesDaily(self.dataWeek,1,1,1).keys())
        self.assertEqual(lenOfLists,3)
        self.assertRaises(Exception,DataManager.returnTemperaturesDaily,self.dataWeek,0)

    def test_returnData(self):
        self.assertEqual(len(DataManager.returnData(self.dataHour,"temp")),24)
        self.assertEqual(len(DataManager.returnData(self.dataHour,"uvi")),24)
        self.assertEqual(len(DataManager.returnData(self.dataHour,"pop")),24)
        self.assertEqual(len(DataManager.returnData(self.dataHour,"feels_like")),24)
        self.assertRaises(TypeError,DataManager.returnData,1,"temp")
        self.assertRaises(Exception,DataManager.returnData,self.dataHour,"as")

    def test_returnCurrentInfo(self):
        self.assertEqual(type(DataManager.returnCurrentInfo(self.dataNow)),dict)
        self.assertEqual(len(DataManager.returnCurrentInfo(self.dataNow).keys()),7)
        self.assertRaises(TypeError,DataManager.returnCurrentInfo,1)

if __name__=="__main__":
    unittest.main()