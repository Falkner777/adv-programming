
from datetime import datetime
from sqlite3 import Timestamp

import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import numpy as np
from Exceptions.badRequest import BadRequest
from dataManager import DataManager
from Controllers.weatherController import WeatherController
from Controllers.mapController import MapController
import GUISnResources.weatherGUI as weatherGUI
from GUISnResources.messageBox import MessageBox
import keys
import string
from Exceptions.noConnection import ConnectionChecker as conChecker
from matplotlib import pyplot as plt
from GUISnResources.plotWindow import Ui_MainWindow as PlotGuiDaily
from GUISnResources.plotWindowHourly import Ui_MainWindow as PlotGuiHourly
from GUISnResources.mapPlotGUI import Ui_MainWindow as MapPlotGui
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
API_KEY = keys.API_KEY

sys.argv.append("--disable-web-security")
class WeatherApp(qtw.QWidget):

    def __init__(self):

        super().__init__()

        self.GUI = weatherGUI.Ui_Form()
        self.GUI.setupUi(self)
        self.GUI.stackedWidget.setCurrentIndex(0)

        self.GUI.searchButton.clicked.connect(self.search)
        self.mapControl = MapController(API_KEY)
        self.GUI.goBackButton.clicked.connect(self.goBack)
        self.GUI.sevenDaysButton.clicked.connect(self.sevenDayPlot)
        self.GUI.hourlyButton.clicked.connect(self.hourlyPlot)
        self.GUI.mapsButton.clicked.connect(self.mapPlot)
        self.show()

    def search(self):
        """
        It takes the city name from the search bar, checks if it's empty, if it's not, it calls the API
        and gets the data, then it displays it on the GUI
        :return: the icon that is mapped to the icon code.
        """

        self.tempUnits = {"standard": "°K", "metric": "°C", "imperial": "°F"}
        if self.GUI.standardRadio.isChecked():
            self.units = "standard"
        if self.GUI.metricRadio.isChecked():
            self.units = "metric"
        if self.GUI.imperialRadio.isChecked():
            self.units = "imperial"
        self.WeatherCaller = WeatherController(API_KEY, self.units)

        self.cityName = self.GUI.searchEdit.text()
        if self.cityName == "":
            popMessage = MessageBox(
                "Please search for a location!", "Empty Request")
            popMessage.createMessage()
            return
        try:
            data = self.WeatherCaller.getWeatherCity(self.cityName)
            info = DataManager.returnCurrentInfo(data)
            self.GUI.humidityValue.setText(str(info["humidity"]) + "%")
            self.GUI.tempLabelBig.setText(
                str(round(info["temp"])) + self.tempUnits[self.units])
            self.GUI.tempValue.setText(
                str(info["temp"]) + self.tempUnits[self.units])
            self.GUI.feelsLlikeValue.setText(
                str(info["feels_like"]) + self.tempUnits[self.units])
            self.GUI.pressureValue.setText(str(info["pressure"]) + "hPa")
            self.GUI.windspeedValue.setText(str(info["wind"]) + "m/s")
            self.GUI.weatherDescription.setText(
                string.capwords(info["description"]))
            self.GUI.cityLabel.setText(string.capwords(self.cityName))
            self.GUI.weatherIcon.setPixmap(self.iconMapper(info["icon"]))
            self.GUI.stackedWidget.setCurrentIndex(1)
            self.GUI.searchEdit.setText("")
        except BadRequest as e:
            popMessage = MessageBox(e.__str__(), "Error on search")
            popMessage.createMessage()
            self.GUI.searchEdit.setText("")

    def iconMapper(self, icon):
        """
        It takes the icon code from the API and returns the corresponding icon from the `icons` folder

        :param icon: The icon code for the current weather condition
        :return: A QPixmap object.
        """
        icons = {
            "01d": "wi_day-sunny", "01n": "wi_moon-alt-new",
            "02d": "wi_day-cloudy", "02n": "wi_night-alt-cloudy",
            "03d": "wi_cloud", "03n": "wi_cloud",
            "04d": "wi_cloudy.png", "04n": "wi_cloudy.png",
            "09d": "wi_showers.png", "09n": "wi_showers.png",
            "10d": "wi_rain", "10n": "wi_rain",
            "11d": "wi_storm-showers", "11n": "wi_storm-showers",
            "13d": "wi_snowflake-cold", "13n": "wi_snowflake-cold",
            "50d": "wi_windy", "50n": "wi_windy",
        }

        return qtg.QPixmap(":/icons/icons/"+icons[icon].strip())

    def sevenDayPlot(self):
        self.plotWindow = qtw.QMainWindow()
        self.windowGUI = PlotGuiDaily()
        self.windowGUI.setupUi(self.plotWindow)

        plotMap = {"Temperature": "temp", "Feels-Like": "feels_like", "Pressure": "pressure", "Humidity": "humidity",
                   "Soil Temperature": "dew_point", "Wind speed": "wind_speed", "Cloudiness": "clouds",
                   "UV": "uvi", "Precipitation": "pop"}
        self.checkBoxes = [self.windowGUI.mornBox, self.windowGUI.dayBox, self.windowGUI.eveBox,
                           self.windowGUI.nightBox, self.windowGUI.minBox, self.windowGUI.maxBox]
        self.windowGUI.comboBox.addItems(list(plotMap.keys()))
        self.windowGUI.comboBox.currentIndexChanged.connect(
            self.hideComboBoxes)
        self.windowGUI.plotButton.clicked.connect(
            lambda: self.plotGraphDaily(plotMap[self.windowGUI.comboBox.currentText()]))
        self.plotWindow.show()

    def hideComboBoxes(self):
        if self.windowGUI.comboBox.currentText() == "Temperature" or self.windowGUI.comboBox.currentText() == "Feels-Like":
            for box in self.checkBoxes:
                box.setVisible(True)
        else:
            for box in self.checkBoxes:
                box.setVisible(False)

    def hourlyPlot(self):
        self.plotWindowHourly = qtw.QMainWindow()
        self.windowGUIHourly = PlotGuiHourly()
        self.windowGUIHourly.setupUi(self.plotWindowHourly)

        plotMap = {"Temperature": "temp", "Feels-Like": "feels_like", "Pressure": "pressure", "Humidity": "humidity",
                   "Soil Temperature": "dew_point", "Wind speed": "wind_speed", "Cloudiness": "clouds",
                   "UV": "uvi", "Precipitation": "pop"}
        self.windowGUIHourly.comboBox.addItems(list(plotMap.keys()))

        self.windowGUIHourly.plotButton.clicked.connect(lambda: self.plotGraphHourly(
            plotMap[self.windowGUIHourly.comboBox.currentText()]))
        self.plotWindowHourly.show()

    def plotGraphHourly(self, value):
        data = self.WeatherCaller.getHourlyData(self.cityName)
        plotUnits = {"temp": f'Temperature({self.tempUnits[self.units]})', "feels_like": f'Temperature({self.tempUnits[self.units]})',
                     "pressure": "Pressure (hPa)", "wind_speed": "Wind speed(m/s)",
                     "dew_point": f"Soil Temperature(°K)", "uvi": "UV Index", "clouds": "Cloudiness(%)",
                     "pop": "Probability of precipitation", "humidity": "Humidity (%)"}

        timeAxis = DataManager.returnTimestamps(data, "hour")
        plotValues = DataManager.returnData(data, value)
        plt.figure(facecolor="#C2C4FA", figsize=(10, 6))
        plt.plot(timeAxis, plotValues, color="#484DD5")
        plt.plot(timeAxis, plotValues, color="#484DD5", marker=".")
        plt.title("24 Hour Forecast", fontweight='bold',
                  fontfamily="Roboto", fontsize=18)
        ticks = [timeAxis[x*4] for x in range(len(timeAxis)//4)]
        ticks.append(timeAxis[-1])
        plt.xticks(ticks)
        plt.ylabel(plotUnits[value], fontfamily="Roboto", fontsize=16)
        plt.xlabel("", fontfamily="Roboto")
        plt.show()

    def plotGraphDaily(self, value):
        data = self.WeatherCaller.getDailyData(self.cityName)
        plotUnits = {"temp": f'Temperature({self.tempUnits[self.units]})', "feels_like": f'Temperature({self.tempUnits[self.units]})',
                     "pressure": "Pressure (hPa)", "wind_speed": "Wind speed(m/s)",
                     "dew_point": f"Soil Temperature(°K)", "uvi": "UV Index",
                     "clouds": "Cloudiness(%)", "pop": "Probability of precipitation", "humidity": "Humidity (%)"}
        timeAxis = DataManager.returnTimestamps(data, "day")

        if value == "temp" or value == "feels_like":
            boxValues = []
            for box in self.checkBoxes:
                boxValues.append(box.isChecked())

            morn, day, eve, night, minn, maxx = tuple(boxValues)
            if value == "temp":
                feels = 0
            if value == "feels_like":
                feels = 1

            try:
                tempDict = DataManager.returnTemperaturesDaily(
                    data, morn, day, eve, night, minn, maxx, feels)
            except Exception as e:
                popMessage = MessageBox(e.__str__, "Error fetching data")
                popMessage.createMessage()
                return

            plt.figure(facecolor="#C2C4FA")
            for key in tempDict.keys():
                plt.plot(timeAxis, tempDict[key])
            plt.legend(tempDict.keys())
            plt.title("Seven Day Forecast", fontweight='bold',
                      fontfamily="Roboto", fontsize=18)
            plt.xticks(rotation=15, ha='right')
            plt.ylabel(plotUnits[value], fontfamily="Roboto", fontsize=16)
            plt.xlabel("", fontfamily="Roboto")

        else:

            plotValues = DataManager.returnData(data, value)
            plt.figure(facecolor="#C2C4FA")
            plt.plot(timeAxis, plotValues, color="#484DD5")
            plt.title("Seven Day Forecast", fontweight='bold',
                      fontfamily="Roboto", fontsize=18)
            plt.xticks(rotation=15, ha='right')
            plt.ylabel(plotUnits[value], fontfamily="Roboto", fontsize=16)
            plt.xlabel("", fontfamily="Roboto")
        plt.show()

    def mapPlot(self):
        mapLayers = {"Convective precipitation":"PAC0","Precipitation intensity":"PR0","Accumulated precipitation":"PA0",\
            "Accumulated precipitation - rain":"PAR0","Accumulated precipitation - snow":"PAS0","Depth of snow":"SD0",\
                "Wind speed at an altitude of 10 meters":"WS10","Joint display of speed wind  and  direction":"WND"\
                    ,"Atmospheric pressure on mean sea level":"APM","Air temperature at a height of 2 meters":"TA2",\
                        "Temperature of a dew point":"TD2","Soil temperature 0-10":"TS0","Soil temperature >10":"TS10",\
                            "Relative humidity":"HRD0","Cloudiness":"CL"}

        self.mapLayerWindow = qtw.QMainWindow()
        self.mapWindowGui = MapPlotGui()
        self.mapWindowGui.setupUi(self.mapLayerWindow)
        self.mapWindowGui.comboBox.addItems(list(mapLayers.keys()))
        self.mapWindowGui.pushButton.clicked.connect(lambda:self.showMap(mapLayers[self.mapWindowGui.comboBox.currentText()]))
        self.mapLayerWindow.show()

    def showMap(self,layer):

        self.mapControl.setMap(self.cityName,layer)
        self.mapWindow = QWebEngineView()
        self.mapWindow.load(qtc.QUrl.fromLocalFile("/home/dimitris/adv_programming/adv-programming/weatherApp/Controllers/map.html"))
        self.mapWindow.show()

        

    def goBack(self):
        self.GUI.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = WeatherApp()
    app.exec_()
