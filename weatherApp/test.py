

import numpy as np
import keys
import requests
from matplotlib import pyplot as plt
from weatherController import WeatherController
from dataManager import DataManager as dm

weatherCaller = WeatherController(keys.API_KEY, 'metric')

data = weatherCaller.getDailyData("Athens")

test = dm.returnTemperaturesDaily(data,morn=0)
print(test)
