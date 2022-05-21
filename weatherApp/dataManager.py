from cmath import e
import datetime
from sre_constants import RANGE_UNI_IGNORE

from emptyRequestException import EmptyRequestException 
class DataManager():

    def __init__(self):
        pass

    @staticmethod 
    def returnTimestamps(data, typeTime):
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
        if not isinstance(data,list):
            raise TypeError(f"Data type not acceptable: expected <class 'list'>, <{type(data)}> found")
        temperatures = []
        feels_like = []

        for temp in data["temp"]:
            temperatures.append(temp)

        if feels_like:
            for feels in data["feels_like"]:
                feels_like.append(feels)
            return temperatures,feels_like
        
        else:
            return temperatures

    @staticmethod
        
    def returnTemperaturesDaily(data, morn=1, day=0, eve=0, night=0, minn=0, maxx=0, feels_like=0):
        """
        It takes a list of dictionaries, each dictionary containing a temperature key with a dictionary
        of temperatures for the day, and returns a dictionary of lists of temperatures for the day, with
        the keys being the time of day
        
        :param data: list of dictionaries, each dictionary contains the weather data for a day
        :param morn: morning temperature, defaults to 1 (optional)
        :param day: day temperature, defaults to 0 (optional)
        :param eve: evening temperature, defaults to 0 (optional)
        :param night: The minimum temperature at night time. This is the lowest temperature that is
        forecasted to occur between sunset and sunrise the next day, defaults to 0 (optional)
        :param minn: minimum temperature, defaults to 0 (optional)
        :param maxx: returns the maximum temperature of the day, defaults to 0 (optional)
        :param feels_like: if you want to return the feels_like temperatures, defaults to 0 (optional)
        :return: A dictionary with the temperatures for the day, night, morning, evening, min and max.
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
        if morn + day + eve + night + minn + maxx + feels_like == 0:
            raise Exception("EmptyRequest. You haven't choosen any temperature to return.")

        for daytime in data:
            if feels_like:
                if morn:
                    temperatures["morn"].append(daytime['temp']["morn"])
                    feels_like["morn"].append(daytime['feels_like']["morn"])
                if day:
                    temperatures['day'].append(daytime['temp']['day'])
                    feels_like["day"].append(daytime['feels_like']["day"])
                if eve:
                    temperatures['eve'].append(daytime['temp']['eve'])
                    feels_like["eve"].append(daytime['feels_like']["eve"])
                if night:
                    temperatures['night'].append(daytime['temp']['night'])
                    feels_like["night"].append(daytime['feels_like']["night"])
                if minn:
                    temperatures['min'].append(daytime['temp']['min'])
                    feels_like["min"].append(daytime['feels_like']["mminorn"])
                if maxx:
                    temperatures['max'].append(daytime['temp']['max'])
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
        for key in temperatures.keys():
            if len(temperatures[key]) == 0:
                keysToRemove.append(key)
        for key in keysToRemove: 
            del temperatures[key]
            if feels_like:
                del feels_like[key]

        if feels_like:
            return temperatures, feels_like
        else:
            return temperatures

    @staticmethod
    def returnData(data, dataName):
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
        