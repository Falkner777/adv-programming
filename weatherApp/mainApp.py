
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from maingui import Ui_Form
API_KEY = "40532d33f39f395622bd004abeb82179"
geoKEY = "f7abd3f018df76b5c983da7768b7cf2a"
default_call = "https://api.openweathermap.org/data/2.5/"
units = "metric"

class LoginGui(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.loginUI = Ui_Form()
        self.loginUI.setupUi(self)
        self.show()



if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = LoginGui()
    app.exec_()