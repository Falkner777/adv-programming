from email.policy import default
from controller import Controller


API_KEY = "40532d33f39f395622bd004abeb82179"
default_call = "https://api.openweathermap.org/data/2.5/"

app = Controller(1234,12314)
app.getWeatherCity(123)
