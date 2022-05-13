
from re import S
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from badRequest import BadRequest
from dataManager import DataManager
from weatherController import WeatherController
import weatherGUI
import keys
import string
import resources
API_KEY = keys.API_KEY


units = "metric"

class WeatherApp(qtw.QWidget):

    def __init__(self):
        
        super().__init__()
        self.WeatherCaller = WeatherController(API_KEY, units)
        self.GUI = weatherGUI.Ui_Form()
        self.GUI.setupUi(self)
        self.GUI.stackedWidget.setCurrentIndex(0)

        self.GUI.searchButton.clicked.connect(self.search)
        self.GUI.goBackButton.clicked.connect(self.goBack)
        
        self.show()

    def search(self):
        """
        It takes the text from the search bar, checks if it's empty, if it's not, it calls the API and
        gets the data, then it displays it on the GUI
        :return: the current weather information for the city that was searched.
        """
        self.cityName = self.GUI.searchEdit.text()
        if self.cityName == "":
            messageDdialog = qtw.QMessageBox()
            messageDdialog.setWindowTitle("Empty Request")
            messageDdialog.setIcon(qtw.QMessageBox.Critical)
            messageDdialog.setText("Please search for a location!")
            messageDdialog.exec_()
            return    
        try:
            data = self.WeatherCaller.getWeatherCity(self.cityName)
            info = DataManager.returnCurrentInfo(data)
            self.GUI.humidityValue.setText(str(info["humidity"]) + "%")
            self.GUI.tempLabelBig.setText(str(round(info["temp"]))+ '°C')
            self.GUI.tempValue.setText(str(info["temp"])+ '°C')
            self.GUI.feelsLlikeValue.setText(str(info["feels_like"])+ '°C')
            self.GUI.pressureValue.setText(str(info["pressure"]) + "hPa")
            self.GUI.windspeedValue.setText(str(info["wind"])+ "m/s")
            self.GUI.weatherDescription.setText(string.capwords(info["description"]))
            self.GUI.cityLabel.setText(string.capwords(self.cityName))
            self.GUI.weatherIcon.setPixmap(self.iconMapper(info["icon"]))
            self.GUI.stackedWidget.setCurrentIndex(1)
            self.GUI.searchEdit.setText("")
        except BadRequest as e:
            errorDdialog = qtw.QMessageBox()
            errorDdialog.setWindowTitle("Error on search!")
            errorDdialog.setIcon(qtw.QMessageBox.Critical)
            errorDdialog.setText(e.__str__())
            errorDdialog.exec_()
            self.GUI.searchEdit.setText("")

    def iconMapper(self,icon):
        """
        It takes the icon code from the API and returns the corresponding icon from the `icons` folder
        
        :param icon: The icon code for the current weather condition
        :return: A QPixmap object.
        """
        icons = {
            "01d":"wi_day-sunny","01n":"wi_moon-alt-new",
            "02d":"wi_day-cloudy","02n":"wi_night-alt-cloudy",
            "03d":"wi_cloud","03n":"wi_cloud",
            "04d":"wi_cloudy.png","04n":"wi_cloudy.png",
            "09d":"wi_showers.png","09n":"wi_showers.png",
            "10d":"wi_rain","10n":"wi_rain",
            "11d":"wi_storm-showers","11n":"wi_storm-showers",
            "13d":"wi_snowflake-cold","13n":"wi_snowflake-cold",
            "50d":"wi_windy","50n":"wi_windy",
        }
        
        return qtg.QPixmap(":/icons/icons/"+icons[icon].strip())

  

    def goBack(self):
        self.GUI.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = WeatherApp()
    app.exec_()