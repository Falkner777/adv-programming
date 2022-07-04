import sqlite3 as sql
import os,sys
from statistics import mode

path = os.getcwd()
parentPath = os.path.dirname(path) + "/weatherApp"
sys.path.insert(0,parentPath)

class ModelDB():

    def __init__(self, dbName):
        self.dbName = dbName
        try:
            self.con = sql.connect(dbName)
            self.cursor = self.con.cursor()
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        except sql.Error as e:
            print(e)

    def selectData(self, query):
        """
        It takes a query as an argument, executes it, and returns the results
        
        :param query: The query to be executed
        :return: The results of the query.
        """
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except sql.Error as e:
            print(e)
            return False

    def storeData(self,query):
        """
        It takes a query as an argument and executes it
        
        :param query: The query to be executed
        :return: a boolean value.
        """
        try:
            self.cursor.execute(query)
            self.con.commit()
            return True
        except sql.Error as e:
            print(e)
            return  False


def updateData(model,cityName,data,units):
    """
    It takes in a model, city name, data, and units. It then queries the database for the dates of the
    city and the city's ID. It then iterates through the data and checks if the date is already in the
    database. If it is, it skips it. If it isn't, it converts the temperature and feels like temperature
    to the correct units and then inserts the data into the database
    
    :param model: the model object
    :param cityName: The name of the city you want to update
    :param data: the data returned from the API call
    :param units: 
    """
    dateQuery = f'select date from AREA,DAY where Name == "{cityName}" and area_id == AREA.Id'
    idQuery = f'select Id from AREA where Name == "{cityName}"'
    cityID = model.selectData(idQuery)[0][0]
    dates = model.selectData(dateQuery)
    for day in data:
        if day['dt'] in dates:
            continue
        match units:
            case 'metric':
                temp = day["temp"]
                feels_like = day["feel_like"]
            case 'imperial':
                temp = {k:round((v - 32)/1.8, 2) for k, v in day['temp'].items()}
                feels_like = {k:round((v - 32)/1.8,2) for k, v in day['feels_like'].items()}
            case 'standard': 
                temp = {k:round((v -273.15),2) for k, v in day['temp'].items()}
                feels_like = {k:round((v -273.15),2) for k, v in day['feels_like'].items()}

        dataTuple = (day["dt"],cityID,temp['max'],temp['min'],temp['day'],temp['morn'],temp['eve'],temp['night'],
                day['pressure'],day['humidity'],day['wind_speed'],feels_like['morn'],
                feels_like['day'],feels_like['eve'],feels_like['night'],day["clouds"],day["uvi"],day['pop'],day['dew_point'])
       
        dailyQuery = f"INSERT INTO DAY (date,area_id,temp_max,temp_min,temp_day,temp_morn,temp_eve,temp_night,\
            pressure,humidity,wind_speed,feel_morn,feel_day,feel_eve,feel_night,\
                clouds,uvi,pop,dew_point)\
                    VALUES{dataTuple}"
        model.storeData(dailyQuery)    

from Controllers.weatherController import WeatherController
import keys
contr = WeatherController(keys.API_KEY,"imperial")

model = ModelDB("/home/dimitris/Desktop/weatherapp.sqlite3")
updateData(model,"Patras",contr.getDailyData("Patras"),contr.getUnits())

