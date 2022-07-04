from ast import match_case
import math
import os,sys

from pip import main
path = os.getcwd()
parentPath = os.path.dirname(path) + "/weatherApp"
sys.path.insert(0,parentPath)
from Exceptions.badRequest import BadRequest
import datetime
import requests
from dateutil.tz import tzoffset
from Controllers.coordController import CoordController
import keys
from dataManager import DataManager
from Controllers.weatherController import WeatherController
units = "metric"
API_KEY = keys.API_KEY
WeatherCaller = WeatherController(API_KEY, units)

def printBasicData(data,cityname,currentTime):
    print(f"------------------{cityname}------------------")
    print(f"----------------{currentTime}------------------")
    print(f"Description: {data['weather'][0]['description'].title()}")
    print(f"Temperature:{data['main']['temp']}")
    print(f"Feels_Like: {data['main']['feels_like']}")
    print(f"Pressure: {data['main']['pressure']}")
    print(f"Humidity: {data['main']['humidity']}")
    print(f"Wind-Speed:{data['wind']['speed']}")
    print()
    # print(f"------------------------------------------")
def printhourly(data,cityname,currentTime):
    for hour in hourlyData:
        dt = datetime.datetime.fromtimestamp(hour["dt"],tz= tzinfo).strftime('%H:%M')
        print(f"{dt}-{hour[choiceMapper[data]]}")
def printdaily(data,cityname,currentTime):
    for day in dailyData:
        dt = datetime.datetime.fromtimestamp(day["dt"],tz= tzinfo).strftime('%D')
        print(f"{dt} - {day[DailyMapper[data]]}")        
if __name__ == '__main__':
    while True:
        print("----------------------------------------------------------------")
        print("-------------------Welcome to the WeatherApp!-------------------")
        print("----------------------------------------------------------------")
        print("Enter your desired location(type 0 for exit):")
        
        try:
            cityName = input()
            if cityName == '0':
                exit()
            data = WeatherCaller.getWeatherCity(cityName)
            tzinfo = tzoffset(None, data["timezone"])  
            currTime = datetime.datetime.now(tzinfo).strftime("%H:%M:%S")
            printBasicData(data,cityName,currTime)
        except BadRequest:
            print("You have entered an invalid city name!!\n\n")

        while True:
            print("Please enter if you would like to get extra information:\n\
                1.Get hourly data\n\
                2.Get weekly data\n\
                3.Get history data\n\
                4.Search for another location\n\
                5.Exit")

            choice = input()
            match choice:
                case '1':
                    hourlyData = WeatherCaller.getHourlyData(cityName)
                    print("Choose between: Temperature, Feels-Like, Pressurem Humidity, Soil Temperature, Wind speed, Cloudiness, UV, Precipitation")
                    choiceMapper = {"Temperature": "temp", "Feels-Like": "feels_like", "Pressure": "pressure", "Humidity": "humidity",
                    "Soil Temperature": "dew_point", "Wind speed":"wind_speed", "Cloudiness": "clouds",
                    "UV": "uvi", "Precipitation": "pop"}
                    hourlyChoice=input()
                    if hourlyChoice in choiceMapper.keys():
                        printhourly(hourlyChoice,cityName,currTime)
                    else:       
                        print("You have entered an invalid city name!!\n\n")
        
                    # for hour in hourlyData:
                    #     dt = datetime.datetime.fromtimestamp(hour["dt"],tz= tzinfo).strftime('%H:%M')
                    #     print(f"{dt}-{hour['temp']}")
                    
                
                    continue
                case '2':
                    dailyData = WeatherCaller.getDailyData(cityName)
                    print("Choose between: Temperature, Feels-Like, Pressurem Humidity, Soil Temperature, Wind speed, Cloudiness, UV, Precipitation")
                    DailyMapper = {"Temperature":"temp","Feels-Like":"feels_like","Pressure":"pressure","Humidity":"patrashumidity","Soil TEmperature":"dew_point","Cloudiness": "clouds",
                    "UV": "uvi", "Precipitation": "pop" }
                    dailyChoice=input()
                    if dailyChoice in DailyMapper.keys():
                        printdaily(dailyChoice,cityName,currTime)
                    continue
                case '3':
                    continue
                case '4':
                    break
                case '5':
                    exit()
                case _:
                    print("\n\nPlease choose an integer value between 1 and 5\n\n")
                    continue

        # input("\n\nPress Enter to continue...")
  


        # if choice==2:
        #     print("Insert the name of the city")
        #     cityName=input()   

        # if choice==3:
        #     print("Insert the name of the city")
        #     cityName=input()       
        #     WeatherCaller = WeatherController(API_KEY, units)
        #     data = WeatherCaller.getDailyData(cityName)
        #     today=datetime.date.today()
        #     for i in range (7):
        #         print(today + datetime.timedelta(days=i),data[i]['temp'])
            