
from pprint import pprint
from weatherController import  WeatherController
import json
import datetime 
from matplotlib import pyplot as plt
from dataManager import DataManager as dm

API_KEY = "40532d33f39f395622bd004abeb82179"
geoKEY = "f7abd3f018df76b5c983da7768b7cf2a"
default_call = "https://api.openweathermap.org/data/2.5/"
units = "metric"


app = WeatherController(API_KEY,units)

city = "Athens"
data = app.getHourlyData(city)

temps = dm.returnTemperatures(data, 1)
test = dm.returnData(data, "uvi")
print(test)
timestamps = dm.returnTimestamps(data, "hour")

plt.plot(timestamps,temps)
plt.show()
