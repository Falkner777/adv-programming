
import math

import os,sys
from pprint import pprint
from re import M

path = os.getcwd()
sys.path.insert(0, path)

from Exceptions.badRequest import BadRequest
import datetime

from dateutil.tz import tzoffset
from Controllers.coordController import CoordController
import keys
from dataManager import DataManager
from Controllers.weatherController import WeatherController
from Controllers.modelDB import ModelDB,updateCity,updateDailyData,getCityID

API_KEY = keys.API_KEY

def loadData(dbConnector,cityName):
    """
    It takes a database connector and a city name as input, and returns a list of tuples containing the
    data for the last 50 days for that city
    
    :param dbConnector: The database connector object
    :param cityName: The name of the city you want to get data for
    """
   
    dataQuery = f"SELECT  date, temp_max,humidity,pressure,wind_speed,uvi,clouds,pop from DAY \
        where area_id == {getCityID(dbConnector,cityName)} LIMIT 50"

    res = dbConnector.selectData(dataQuery)
    colNames = ("Date","Temperature","Humidity","Pressure","Wind Speed","UVI","Clouds","Precipitation")
    print(colNames)
    for row in res:
        pprint(row)

def printBasicData(data,cityname,currentTime):
    """
    This function takes in the data, city name, and current time and prints out the basic weather data
    for the city
    
    :param data: The data that we got from the API
    :param cityname: The name of the city you want to get the weather for
    :param currentTime: The current time in the city
    """
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
    
def printhourly(data):
    """
    It takes in a string, and prints out the hourly data for that string
    
    :param data: The data you want to print
    """
    for hour in hourlyData:
        dt = datetime.datetime.fromtimestamp(hour["dt"],tz= tzinfo).strftime('%H:%M')
        print(f"{dt}-{hour[choiceMapper[data]]}")

def printdaily(data):
    """
    It takes a data type (e.g. "temp") and prints the date and the value of that data type for each day
    in the forecast
    
    :param data: The data you want to print
    """
    for day in dailyData:
        dt = datetime.datetime.fromtimestamp(day["dt"],tz= tzinfo).strftime('%D')
        print(f"{dt} - {day[DailyMapper[data]]}")        

if __name__ == '__main__':
    
    dbConnector = ModelDB("./Data/weatherapp.sqlite3")
   
    coordController = CoordController(API_KEY)
    print(path)
    print("----------------------------------------------------------------")
    print("-------------------Welcome to the WeatherApp!-------------------")
    print("----------------------------------------------------------------")
    
    while True:
        
        print("Enter your desired location(type 0 for exit):")
        try:
            cityName = input()
            if cityName == '0':
                exit()
            
            print("Please enter your desired type of units.")
            units=input()
            WeatherCaller = WeatherController(API_KEY, units)
            data = WeatherCaller.getWeatherCity(cityName)
            updateCity(dbConnector,cityName,coordController)
            updateDailyData(dbConnector,cityName,WeatherCaller.getDailyData(cityName),units)
            
            tzinfo = tzoffset(None, data["timezone"])  
            currTime = datetime.datetime.now(tzinfo).strftime("%H:%M:%S")
            printBasicData(data,cityName,currTime)
        except BadRequest:
            print("You have entered an invalid city name!!\n\n")
        input("Press any key to continue...")
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
                        printhourly(hourlyChoice)
                    else:       
                        print("You have entered an invalid city name!!\n\n")

               
                    input("Press any key to continue...")
                    continue
                case '2':
                    dailyData = WeatherCaller.getDailyData(cityName)
                    print("Choose between: Temperature, Feels-Like, Pressurem Humidity, Soil Temperature, Wind speed, Cloudiness, UV, Precipitation")
                    DailyMapper = {"Temperature":"temp","Feels-Like":"feels_like","Pressure":"pressure","Wind speed": "wind_speed","Humidity":"humidity","Soil Temperature":"dew_point","Cloudiness": "clouds",
                    "UV": "uvi", "Precipitation": "pop" }
                    dailyChoice=input()
                    if dailyChoice in DailyMapper.keys():
                        printdaily(dailyChoice)
                    else:
                        print("\n!Invalid Input!\n")
                    input("Press any key to continue...")
                    continue
                case '3':
                    loadData(dbConnector,cityName)
                    input("Press any key to continue...")
                    continue
                case '4':
                    break
                case '5':
                    exit()
                case _:
                    print("\n\nPlease choose an integer value between 1 and 5\n\n")
                    continue
            
            

