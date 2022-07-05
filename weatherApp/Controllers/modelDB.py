import sqlite3 as sql
import os,sys,time
from datetime import datetime

path = os.getcwd()

sys.path.insert(0, path)



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

def getCityID(connector,cityName):
    """
    It takes a connector and a city name as input, and returns the city ID.
    
    :param connector: the connector object that you created in the previous step
    :param cityName: The name of the city you want to get the ID for
    :return: The cityID is being returned.
    """

    idQuery = f'select Id from AREA where Name == "{cityName}"'
    cityID = connector.selectData(idQuery)[0][0]

    return cityID

def updateCity(connector,cityName,controller):
    """
    It takes in a city name, and if it's not already in the database, it adds it
    
    :param connector: the connector object
    :param cityName: The name of the city you want to add to the database
    :param controller: the controller object
    :return: A list of tuples containing the name of the city and the number of stores in that city.
    """
    cityQuery = "SELECT Name from AREA"
    cities = connector.selectData(cityQuery)
    cityName = (cityName.title(),)
    print(cityName)
    if cityName in cities:
        return
    
    lon,lat = controller.getCityLonLat(cityName[0])
    storeQuery = f"INSERT INTO AREA (lon,lat,Name)\
        VALUES ({lon},{lat},'{cityName[0]}')"
    connector.storeData(storeQuery)

def updateDailyData(connector,cityName,data,units):
    """
    It takes in the connector, city name, data and units and updates the database with the new data
    
    :param connector: the connector object
    :param cityName: The name of the city you want to update
    :param data: the data from the API call
    :param units: 
    """

    dateQuery = f'select date from AREA,DAY where Name == "{cityName}" and area_id == AREA.Id'
    cityID = getCityID(connector,cityName)
    dates = connector.selectData(dateQuery)
    for day in data:
        convertedDate = datetime.fromtimestamp(day['dt']).strftime("%d/%m/%Y")
        convertedDate = (convertedDate,)
        if convertedDate in dates:
            continue
        match units:
            case 'metric':
                temp = day["temp"]
                feels_like = day["feels_like"]
            case 'imperial':
                temp = {k:round((v - 32)/1.8, 2) for k, v in day['temp'].items()}
                feels_like = {k:round((v - 32)/1.8,2) for k, v in day['feels_like'].items()}
            case 'standard': 
                temp = {k:round((v -273.15),2) for k, v in day['temp'].items()}
                feels_like = {k:round((v -273.15),2) for k, v in day['feels_like'].items()}
        dt = datetime.fromtimestamp(day["dt"]).strftime("%d/%m/%Y")
        dataTuple = (dt,cityID,temp['max'],temp['min'],temp['day'],temp['morn'],temp['eve'],temp['night'],
                day['pressure'],day['humidity'],day['wind_speed'],feels_like['morn'],
                feels_like['day'],feels_like['eve'],feels_like['night'],day["clouds"],day["uvi"],day['pop'],day['dew_point'])
       
        dailyQuery = f"INSERT INTO DAY (date,area_id,temp_max,temp_min,temp_day,temp_morn,temp_eve,temp_night,\
            pressure,humidity,wind_speed,feel_morn,feel_day,feel_eve,feel_night,\
                clouds,uvi,pop,dew_point)\
                    VALUES{dataTuple}"
        connector.storeData(dailyQuery)    



