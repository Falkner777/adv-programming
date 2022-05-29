import urllib.request

class ConnectionError(Exception):

    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return f"It appears you do not have internet access.\n\
                 Please check your connection!"

class ConnectionChecker():

    @staticmethod
    def checkConnection(host="http://google.com"):
        try:
            urllib.request.urlopen(host)
        except:
            raise ConnectionError