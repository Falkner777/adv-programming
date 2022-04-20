class BadRequest(Exception):

    def __init__(self, code):
        self.code = code
        
    def getCode(self):
        return self.code
   
    def __str__(self):
        if 400 <= self.getCode() < 500:
            return f"{self.getCode()} Client Error. Check your call."
        if 500 <= self.getCode() < 600:
            return f"{self.getCode()} Server Error. Try again later"

        
