
from re import S
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from dataManager import DataManager
from weatherController import WeatherController
import weatherGUI
import keys

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
        self.GUI.tempLabel.setText("12°")
        self.show()

    def search(self):
        cityName = self.GUI.searchEdit.text()
        data = self.WeatherCaller.getWeatherCity(cityName)
        info = DataManager.returnCurrentInfo(data)
        self.GUI.humidityValue.setText(str(info["humidity"]))
        self.GUI.tempLabelBig.setText(str(info["temp"])+ '°')
        self.GUI.tempLabel.setText(str(info["temp"])+ '°')
        self.GUI.feelsLlikeValue.setText(str(info["feels_like"])+ '°')
        self.GUI.pressureValue.setText(str(info["pressure"]))
        self.GUI.windspeedValue.setText(str(info["wind"]))
        self.GUI.weatherDescription.setText(info["description"])
        self.GUI.stackedWidget.setCurrentIndex(1)

    def goBack(self):
        self.GUI.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = WeatherApp()
    app.exec_()