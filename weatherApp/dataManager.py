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

        
        