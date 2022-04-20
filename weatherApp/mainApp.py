from email.policy import default
from coordController import CoordController
from weatherController import  WeatherController
import json
import datetime 
from pprint import pprint
API_KEY = "40532d33f39f395622bd004abeb82179"
geoKEY = "f7abd3f018df76b5c983da7768b7cf2a"
default_call = "https://api.openweathermap.org/data/2.5/"
units = "metric"


app = WeatherController(API_KEY,units)

data = app.getHourlyData("Lefkada")
pprint(data.json())


