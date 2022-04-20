from email.policy import default
from weatherController2 import WeatherController2


API_KEY = "40532d33f39f395622bd004abeb82179"
default_call = "https://api.openweathermap.org/data/2.5/"
units = "metric"
app = WeatherController2(API_KEY,default_call, units)
City_id=833
data = app.getWeatherCity(City_id).json()
print(data)