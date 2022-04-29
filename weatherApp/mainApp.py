
from re import S
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import weatherGUI
API_KEY = "40532d33f39f395622bd004abeb82179"
geoKEY = "f7abd3f018df76b5c983da7768b7cf2a"
default_call = "https://api.openweathermap.org/data/2.5/"
units = "metric"

class WeatherApp(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.GUI = weatherGUI.Ui_Form()
        self.GUI.setupUi(self)
        self.GUI.stackedWidget.setCurrentIndex(0)

        self.GUI.searchButton.clicked.connect(self.search)
        self.GUI.goBackButton.clicked.connect(self.goBack)
        self.show()

    def search(self):
        self.GUI.stackedWidget.setCurrentIndex(1)

    def goBack(self):
        self.GUI.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = WeatherApp()
    app.exec_()