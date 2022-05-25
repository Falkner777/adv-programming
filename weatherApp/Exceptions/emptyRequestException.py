class EmptyRequestException(Exception):
    
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return f"The city you have searched for does not exist."