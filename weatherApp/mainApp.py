from email.policy import default
from weatherController import  WeatherController
import json
import datetime 

API_KEY = "40532d33f39f395622bd004abeb82179"
default_call = "https://api.openweathermap.org/data/2.5/"
units = "metric"

app = WeatherController(API_KEY,default_call, units)
lon =23.727539
lat =  37.983810 
data = app.getHourlyData(lat, lon).json()


# print(datetime.datetime.fromtimestamp(objectdate))

print(data)

