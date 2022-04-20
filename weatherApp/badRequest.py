class BadRequest(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"\n{self.message}. Not acceptable longitude or latitude."
        
