from cmath import e
import datetime
from sre_constants import RANGE_UNI_IGNORE

from emptyRequestException import EmptyRequestException 
class DataManager():

    def __init__(self):
        pass

    @staticmethod 
    def returnTimestamps(data, typeTime):
        """
        It takes in a list of dictionaries and a string, and returns a list of strings
        
        :param data: The data that we're going to be using to create the graph
        :param typeTime: This is the type of time you want to return. You can choose between 'day' or
        'hour'
        :return: A list of timestamps in the format specified by the typeTime parameter.
        """
        timeString = ''
        match typeTime:
            case 'hour':
                timeString = "%I %M %p"
            case 'day':
                timeString = "%a %d %b"
            case _:
                raise Exception("Please specify between 'day' or 'hour'")
        timestamps = []
        for dt in data:
            timestamps.append(datetime.datetime.fromtimestamp(dt["dt"]).strftime(timeString))

        return timestamps
    

    @staticmethod
    def returnTemperaturesHourly(data, feels_like =0):
        """
        It takes in a list of dictionaries and returns a list of temperatures or feels_like temperatures
        
        :param data: This is the data that is returned from the API
        :param feels_like: if set to 1, returns the feels_like temperatures, else returns the actual
        temperatures, defaults to 0 (optional)
        :return: a list of temperatures or feels_like temperatures.
        """
        if not isinstance(data,list):
            raise TypeError(f"Data type not acceptable: expected <class 'list'>, <{type(data)}> found")
        temperatures = []
        feels_like = []

    
        if feels_like:
            for feels in data["feels_like"]:
                feels_like.append(feels)
            return feels_like
        else:
            for temp in data["temp"]:
                temperatures.append(temp)
            return temperatures

    @staticmethod
    def returnTemperaturesDaily(data, morn=1, day=0, eve=0, night=0, minn=0, maxx=0, feels=0):
        """
        It takes a list of dictionaries, each dictionary containing a 'temp' key and a 'feels_like' key,
        and returns a dictionary of lists, each list containing the temperatures for a given time of day
        
        :param data: the data you want to extract the temperatures from
        :param morn: morning temperature, defaults to 1 (optional)
        :param day: day temperature, as a string, defaults to 0 (optional)
        :param eve: evening temperature, defaults to 0 (optional)
        :param night: Night temperature. This is minimum temperature (usually happens around midnight),
        defaults to 0 (optional)
        :param minn: minimum temperature, defaults to 0 (optional)
        :param maxx: returns the maximum temperature of the day, defaults to 0 (optional)
        :param feels: if True, returns the feels like temperatures, else returns the actual
        temperatures, defaults to 0 (optional)
        :return: A dictionary with the temperatures for each day.
        """
       
        if not isinstance(data,list):
            raise TypeError(f"Data type not acceptable: expected <class 'list'>, <{type(data)}> found")
        temperatures={  "morn":[],
                        "day": [],
                        "eve": [],
                      "night": [],
                        "min": [],
                        "max": [],
        }
        feels_like ={"morn":[],
                        "day": [],
                        "eve": [],
                      "night": [],
                        "min": [],
                        "max": [],

        }
        if morn + day + eve + night + minn + maxx + feels == 0:
            raise Exception("EmptyRequest. You haven't choosen any temperature to return.")

        for daytime in data:
            if feels:
                if morn:
                    feels_like["morn"].append(daytime['feels_like']["morn"])
                if day:
                    feels_like["day"].append(daytime['feels_like']["day"])
                if eve:
                    feels_like["eve"].append(daytime['feels_like']["eve"])
                if night:
                    feels_like["night"].append(daytime['feels_like']["night"])
                if minn:
                    feels_like["min"].append(daytime['feels_like']["min"])
                if maxx:
                    feels_like["max"].append(daytime['feels_like']["max"])
            else:
                if morn:
                    temperatures["morn"].append(daytime['temp']["morn"])
                if day:
                    temperatures['day'].append(daytime['temp']['day'])
                if eve:
                    temperatures['eve'].append(daytime['temp']['eve'])
                if night:
                    temperatures['night'].append(daytime['temp']['night'])
                if minn:
                    temperatures['min'].append(daytime['temp']['min'])
                if maxx:
                    temperatures['max'].append(daytime['temp']['max'])

        keysToRemove = []
        if feels:
            for key in feels_like.keys():
                if len(feels_like[key]) == 0:
                    keysToRemove.append(key)
        else:
            for key in temperatures.keys():
                if len(temperatures[key]) == 0:
                    keysToRemove.append(key)
                    
        for key in keysToRemove: 
            if feels:
                del feels_like[key]
            else:
                del temperatures[key]

        if feels:
            return feels_like
        else:
            return temperatures

    @staticmethod
    def returnData(data, dataName):
        """
        > This function takes in a list of dictionaries and a string, and returns a list of values from
        the dictionaries that correspond to the string
        
        :param data: the data to be returned
        :param dataName: The name of the data you want to return
        :return: A list of the values of the dataName key in the data dictionary.
        """
        toReturn = []
        if dataName in data[0].keys():
            for dataSlice in data:
                toReturn.append(dataSlice[dataName])
        else:
            raise Exception(f"{dataName} not in available data")
        
        return toReturn

    @staticmethod
    def returnCurrentInfo(data):
        """
        It takes in a dictionary of weather data and returns a dictionary of the current weather
        information
        
        :param data: the data that is returned from the API call
        :return: A dictionary with the current weather information.
        """
        if not isinstance(data,dict):
            raise TypeError(f"Data type not acceptable: expected <class 'dict'>, <{type(data)}> found")
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        icon = data["weather"][0]["icon"]
        toReturn = {"description":description, "temp":temp, "feels_like": feels_like, "pressure": pressure, "humidity":humidity,\
            "wind": wind, "icon": icon}
        
        return toReturn
        