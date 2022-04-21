
from pprint import pprint
from weatherController import  WeatherController
import json
import datetime 
from matplotlib import pyplot as plt

API_KEY = "40532d33f39f395622bd004abeb82179"
geoKEY = "f7abd3f018df76b5c983da7768b7cf2a"
default_call = "https://api.openweathermap.org/data/2.5/"
units = "metric"


app = WeatherController(API_KEY,units)

city = "Tsoukalades"
data = app.getHourlyData(city).json()
pprint(data)
temps = []
time = []
for temp in data["hourly"]:
    temps.append(temp["temp"])
    time.append(datetime.datetime.fromtimestamp(temp["dt"]).strftime("%H:%m"))


plt.plot(time[:24],temps[:24])

plt.stem(time[:24],temps[:24])
plt.xticks(rotation=40,ha="right")

plt.title(f"24-Hour temperature forecast for {city}")
plt.xlabel("Time",weight="bold")
plt.ylabel("Temperature ",weight="bold")
plt.show()