from email.policy import default
from coordController import CoordController
from weatherController import  WeatherController
import json
import datetime 

API_KEY = "40532d33f39f395622bd004abeb82179"
apiKey = "7de5c22554fb5aef3c62e8f8234a93e7"
default_call = "https://api.openweathermap.org/data/2.5/"
units = "metric"

app = CoordController(API_KEY)
lon =23.727539
lat =  37.983810 
data = app.getCityLonLat("London",5)
print(data)


