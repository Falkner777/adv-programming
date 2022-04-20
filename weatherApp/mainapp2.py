from email.policy import default
from controller import Controller


API_KEY = "40532d33f39f395622bd004abeb82179"
default_call = "https://api.openweathermap.org/data/2.5/"
units = "metric"
app = WeatherController(API_KEY,default_call, units)