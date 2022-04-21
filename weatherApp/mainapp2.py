
from weatherController2 import WeatherController2
from pprint import pprint

API_KEY = "40532d33f39f395622bd004abeb82179"
default_call = "https://api.openweathermap.org/data/2.5/"
units = "metric"
app = WeatherController2(API_KEY,default_call, units)
Cityname="Lefkada"
data = app.gethumidityCity(Cityname)
pprint(data)