import datetime 
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
    def returnTemperatures(data, tempType = 0):
        """
        This function takes in a list of dictionaries and returns a list of temperatures
        
        :param data: the data you want to get the temperatures from
        :param tempType: 0 for actual temperature, 1 for actual and feels like temperature, defaults to
        0 (optional)
        :return: A list of temperatures
        """
        temperatures = []
        if tempType == 0:
            for temp in data:
                temperatures.append(temp["temp"])
        else:
            for temp in data:
                temperatures.append((temp["temp"], temp["feels_like"]))
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

        
        