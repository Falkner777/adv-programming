
from re import S
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from weatherController import WeatherController
import weatherGUI
import keys

API_KEY = keys.API_KEY

default_call = "https://api.openweathermap.org/data/2.5/"
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
        
        
        
        self.GUI.stackedWidget.setCurrentIndex(1)

    def goBack(self):
        self.GUI.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = WeatherApp()
    app.exec_()