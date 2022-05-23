
from datetime import datetime

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
from matplotlib import pyplot as plt
from plotWindow import Ui_MainWindow as PlotGuiDaily
from plotWindowHourly import Ui_MainWindow as PlotGuiHourly
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
        self.GUI.sevenDaysButton.clicked.connect(self.sevenDayPlot)
        self.GUI.hourlyButton.clicked.connect(self.hourlyPlot)
        self.show()


    def search(self):
        """
        It takes the city name from the search bar, checks if it's empty, if it's not, it calls the API
        and gets the data, then it displays it on the GUI
        :return: the icon that is mapped to the icon code.
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

    def sevenDayPlot(self):
        self.plotWindow = qtw.QMainWindow()
        self.windowGUI = PlotGuiDaily()
        self.windowGUI.setupUi(self.plotWindow)
        
        plotMap = {"Temperature":"temp", "Feels-Like": "feels_like", "Pressure": "pressure", "Humidity": "humidity", \
            "Atmospheric Temperature":"dew_point", "Wind speed": "wind_speed", "Cloudiness":"clouds", \
                "UV":"uvi" , "Precipitation":"pop"}
        self.checkBoxes = [self.windowGUI.mornBox,self.windowGUI.dayBox,self.windowGUI.eveBox,\
            self.windowGUI.nightBox,self.windowGUI.minBox,self.windowGUI.maxBox]
        self.windowGUI.comboBox.addItems(list(plotMap.keys()))
        self.windowGUI.comboBox.currentIndexChanged.connect(self.hideComboBoxes)
        self.windowGUI.plotButton.clicked.connect(lambda :self.plotGraphDaily(plotMap[self.windowGUI.comboBox.currentText()]))
        self.plotWindow.show()
        
    def hideComboBoxes(self):
        if self.windowGUI.comboBox.currentText() == "Temperature" or self.windowGUI.comboBox.currentText() =="Feels-Like":
            for box in self.checkBoxes:
                box.setVisible(True)
        else:
            for box in self.checkBoxes:
                box.setVisible(False)

    def hourlyPlot(self):
        self.plotWindowHourly = qtw.QMainWindow()
        self.windowGUIHourly = PlotGuiHourly()
        self.windowGUIHourly.setupUi(self.plotWindowHourly)
        
        plotMap = {"Temperature":"temp", "Feels-Like": "feels_like", "Pressure": "pressure", "Humidity": "humidity", \
            "Atmospheric Temperature":"dew_point", "Wind speed": "wind_speed", "Cloudiness":"clouds", \
                "UV":"uvi" , "Precipitation":"pop"}
        self.windowGUIHourly.comboBox.addItems(list(plotMap.keys()))
        key = self.windowGUIHourly.comboBox.currentText()
        value = plotMap[key]

        self.windowGUIHourly.plotButton.clicked.connect(lambda: self.plotGraphHourly(value))
        self.plotWindowHourly.show()

    def plotGraphHourly(self, value):
        data = self.WeatherCaller.getHourlyData(self.cityName)
        plotUnits = {"temp":'Temperature(°C)', "feels_like": 'Temperature(°C)', "pressure":"Pressure (hPa)", "wind_speed":"Wind speed(m/s)",\
            "dew_point": "Temperature(°C)", "uvi":"UV Index", "clouds": "Cloudiness(%)", "pop":"Probability of precipitation","humidity": "Humidity (%)"}
        timeAxis = DataManager.returnTimestamps(data,"hour")
        plotValues = DataManager.returnData(data,value)
        plt.figure(facecolor="#C2C4FA",figsize=(10,6))
        plt.plot(timeAxis, plotValues,color="#484DD5")
        plt.title("24 Hour Forecast",fontweight='bold',fontfamily="Roboto")
        plt.xticks(rotation = 22, ha='right')
        plt.ylabel(plotUnits[value],fontfamily="Roboto")
        plt.xlabel("",fontfamily="Roboto")
        plt.show()

    def plotGraphDaily(self, value):
        data = self.WeatherCaller.getDailyData(self.cityName)
        plotUnits = {"temp":'Temperature(°C)', "feels_like": 'Temperature(°C)', "pressure":"Pressure (hPa)", "wind_speed":"Wind speed(m/s)",\
            "dew_point": "Temperature(°C)", "uvi":"UV Index", "clouds": "Cloudiness(%)", "pop":"Probability of precipitation","humidity": "Humidity (%)"}
        timeAxis = DataManager.returnTimestamps(data,"day")

        if value == "temp" or value == "feels_like":
            boxValues =[]
            for box in self.checkBoxes:
                boxValues.append(box.isChecked()) 
            
            morn,day,eve,night,minn,maxx = tuple(boxValues)
            if value == "temp":
                feels = 0
            if value =="feels_like":
                feels = 1 
            tempDict = DataManager.returnTemperaturesDaily(data,morn,day,eve,night,minn,maxx, feels)
            plt.figure(facecolor="#C2C4FA")
            for key in tempDict.keys():
                plt.plot(timeAxis,tempDict[key])
            plt.legend(tempDict.keys())
            plt.title("Seven Day Forecast",fontweight='bold',fontfamily="Roboto")
            plt.xticks(rotation = 15, ha='right')
            plt.ylabel(plotUnits[value],fontfamily="Roboto")
            plt.xlabel("",fontfamily="Roboto")
            
        else:

        
            plotValues = DataManager.returnData(data,value)
            plt.figure(facecolor="#C2C4FA")
            plt.plot(timeAxis, plotValues,color="#484DD5")
            plt.title("Seven Day Forecast",fontweight='bold',fontfamily="Roboto")
            plt.xticks(rotation = 15, ha='right')
            plt.ylabel(plotUnits[value],fontfamily="Roboto")
            plt.xlabel("",fontfamily="Roboto")
        plt.show()

    def goBack(self):
        self.GUI.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = WeatherApp()
    app.exec_()