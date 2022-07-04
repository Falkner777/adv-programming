# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(376, 714)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.0899545, x2:0, y2:1, stop:0 rgba(70, 76, 212, 255), stop:1 rgba(255, 255, 255, 116))")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Search = QtWidgets.QWidget()
        self.Search.setObjectName("Search")
        self.cloudIcon = QtWidgets.QLabel(self.Search)
        self.cloudIcon.setGeometry(QtCore.QRect(138, 242, 141, 91))
        self.cloudIcon.setStyleSheet("background-color: transparent;")
        self.cloudIcon.setText("")
        self.cloudIcon.setPixmap(QtGui.QPixmap(":/icons/icons/clouds.png"))
        self.cloudIcon.setObjectName("cloudIcon")
        self.titleLabel = QtWidgets.QLabel(self.Search)
        self.titleLabel.setGeometry(QtCore.QRect(98, 104, 181, 31))
        self.titleLabel.setStyleSheet("font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 32px;\n"
"line-height: 38px;\n"
"text-align: center;\n"
"letter-spacing: 0.04em;\n"
"\n"
"color: #FFFFFF;\n"
"background-color: transparent;\n"
""
"")
        self.titleLabel.setObjectName("titleLabel")
        self.searchButton = QtWidgets.QPushButton(self.Search)
        self.searchButton.setGeometry(QtCore.QRect(127, 480, 137, 51))
        self.searchButton.setStyleSheet("\n"
"background: #484DD5;\n"
"border-radius: 25px;\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"text-align: center;\n"
"letter-spacing: 0.04em;\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.searchButton.setText("Search")
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.searchEdit = QtWidgets.QLineEdit(self.Search)
        self.searchEdit.setGeometry(QtCore.QRect(65, 370, 251, 41))
        self.searchEdit.setStyleSheet("\n"
"font-family: 'Roboto';\
font-style: normal;\
font-weight: 300;\
font-size: 18px;\
line-height: 21px;\
letter-spacing: 0.04em;\
color: rgba(0, 0, 0, 0.53);\
padding:10px;"

"background: #FFFFFF;\n"
"\n"
"\n"
"border-radius: 20px;\n"
"")
        self.searchEdit.setObjectName("searchEdit")
        self.blobIcon_3 = QtWidgets.QLabel(self.Search)
        self.blobIcon_3.setGeometry(QtCore.QRect(70, -10, 421, 211))
        self.blobIcon_3.setStyleSheet("background-color: transparent;")
        self.blobIcon_3.setText("")
        self.blobIcon_3.setPixmap(QtGui.QPixmap(":/icons/icons/vector.png"))
        self.blobIcon_3.setObjectName("blobIcon_3")
        self.standardRadio = QtWidgets.QRadioButton(self.Search)
        self.standardRadio.setGeometry(QtCore.QRect(33, 434, 103, 27))
        self.standardRadio.setStyleSheet("font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 26px;\n"
"text-align: center;\n"
"letter-spacing: 0.04em;\n"
"background:none;\n"
"color: #FFFFFF;\n"
"")
        self.standardRadio.setChecked(True)
        self.standardRadio.setObjectName("standardRadio")
        self.metricRadio = QtWidgets.QRadioButton(self.Search)
        self.metricRadio.setGeometry(QtCore.QRect(161, 434, 81, 27))
        self.metricRadio.setStyleSheet("font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 26px;\n"
"text-align: center;\n"
"letter-spacing: 0.04em;\n"
"background:none;\n"
"color: #FFFFFF;\n"
"")
        self.metricRadio.setObjectName("metricRadio")
        self.imperialRadio = QtWidgets.QRadioButton(self.Search)
        self.imperialRadio.setGeometry(QtCore.QRect(268, 434, 90, 27))
        self.imperialRadio.setStyleSheet("font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 26px;\n"
"text-align: center;\n"
"letter-spacing: 0.04em;\n"
"background:none;\n"
"color: #FFFFFF;\n"
"")
        self.imperialRadio.setObjectName("imperialRadio")
        self.cloudIcon.raise_()
        self.searchButton.raise_()
        self.searchEdit.raise_()
        self.blobIcon_3.raise_()
        self.titleLabel.raise_()
        self.standardRadio.raise_()
        self.metricRadio.raise_()
        self.imperialRadio.raise_()
        self.stackedWidget.addWidget(self.Search)
        self.Main = QtWidgets.QWidget()
        self.Main.setObjectName("Main")
        self.humidityIcon = QtWidgets.QLabel(self.Main)
        self.humidityIcon.setGeometry(QtCore.QRect(32, 473, 20, 20))
        self.humidityIcon.setMinimumSize(QtCore.QSize(20, 20))
        self.humidityIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.humidityIcon.setStyleSheet("background-color:transparent;")
        self.humidityIcon.setText("")
        self.humidityIcon.setPixmap(QtGui.QPixmap(":/icons/icons/carbon_humidity.png"))
        self.humidityIcon.setObjectName("humidityIcon")
        self.weatherIcon = QtWidgets.QLabel(self.Main)
        self.weatherIcon.setGeometry(QtCore.QRect(147, 318, 80, 80))
        self.weatherIcon.setStyleSheet("background-color:transparent;\n"
"")
        self.weatherIcon.setText("")
        self.weatherIcon.setPixmap(QtGui.QPixmap(":/icons/icons/arcticons_hyperlocal-weather.png"))
        self.weatherIcon.setObjectName("weatherIcon")
        self.windspeedValue = QtWidgets.QLabel(self.Main)
        self.windspeedValue.setGeometry(QtCore.QRect(170, 564, 81, 23))
        self.windspeedValue.setStyleSheet("\n"
"\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"letter-spacing: 0.04em;\n"
"background-color:transparent;\n"
"color: rgb(46, 54, 213);\n"
"\n"
"")
        self.windspeedValue.setObjectName("windspeedValue")
        self.blobIcon_2 = QtWidgets.QLabel(self.Main)
        self.blobIcon_2.setGeometry(QtCore.QRect(70, -20, 421, 211))
        self.blobIcon_2.setStyleSheet("background-color: transparent;")
        self.blobIcon_2.setText("")
        self.blobIcon_2.setPixmap(QtGui.QPixmap(":/icons/icons/vector.png"))
        self.blobIcon_2.setObjectName("blobIcon_2")
        self.feelsLlikeValue = QtWidgets.QLabel(self.Main)
        self.feelsLlikeValue.setGeometry(QtCore.QRect(170, 533, 81, 22))
        self.feelsLlikeValue.setStyleSheet("\n"
"\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"letter-spacing: 0.04em;\n"
"background-color:transparent;\n"
"color: rgb(46, 54, 213);\n"
"")
        self.feelsLlikeValue.setObjectName("feelsLlikeValue")
        self.pressureValue = QtWidgets.QLabel(self.Main)
        self.pressureValue.setGeometry(QtCore.QRect(170, 595, 81, 23))
        self.pressureValue.setStyleSheet("\n"
"\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"letter-spacing: 0.04em;\n"
"background-color:transparent;\n"
"color: rgb(46, 54, 213);\n"
"\n"
"")
        self.pressureValue.setObjectName("pressureValue")
        self.tempLabel = QtWidgets.QLabel(self.Main)
        self.tempLabel.setGeometry(QtCore.QRect(58, 503, 74, 22))
        self.tempLabel.setStyleSheet("\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"letter-spacing: 0.04em;\n"
"background-color:transparent;\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.tempLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tempLabel.setObjectName("tempLabel")
        self.pressureLabel = QtWidgets.QLabel(self.Main)
        self.pressureLabel.setGeometry(QtCore.QRect(58, 596, 76, 22))
        self.pressureLabel.setStyleSheet("\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"letter-spacing: 0.04em;\n"
"background-color:transparent;\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.pressureLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pressureLabel.setObjectName("pressureLabel")
        self.windspeedIcon = QtWidgets.QLabel(self.Main)
        self.windspeedIcon.setGeometry(QtCore.QRect(32, 566, 20, 20))
        self.windspeedIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.windspeedIcon.setStyleSheet("background-color:transparent;")
        self.windspeedIcon.setText("")
        self.windspeedIcon.setPixmap(QtGui.QPixmap(":/icons/icons/carbon_windy.png"))
        self.windspeedIcon.setObjectName("windspeedIcon")
        self.windspeedLabel = QtWidgets.QLabel(self.Main)
        self.windspeedLabel.setGeometry(QtCore.QRect(58, 565, 99, 22))
        self.windspeedLabel.setStyleSheet("\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"letter-spacing: 0.04em;\n"
"background-color:transparent;\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.windspeedLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.windspeedLabel.setObjectName("windspeedLabel")
        self.tempLabelBig = QtWidgets.QLabel(self.Main)
        self.tempLabelBig.setGeometry(QtCore.QRect(-9, 204, 391, 114))
        self.tempLabelBig.setStyleSheet("\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 96px;\n"
"line-height: 112px;\n"
"text-align: center;\n"
"letter-spacing: 0.04em;\n"
"background-color:transparent;\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.tempLabelBig.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLabelBig.setObjectName("tempLabelBig")
        self.feelslikeIcon = QtWidgets.QLabel(self.Main)
        self.feelslikeIcon.setGeometry(QtCore.QRect(32, 535, 20, 20))
        self.feelslikeIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.feelslikeIcon.setStyleSheet("background-color:transparent;")
        self.feelslikeIcon.setText("")
        self.feelslikeIcon.setPixmap(QtGui.QPixmap(":/icons/icons/carbon_temperature-feels-like.png"))
        self.feelslikeIcon.setObjectName("feelslikeIcon")
        self.pressureIcon = QtWidgets.QLabel(self.Main)
        self.pressureIcon.setGeometry(QtCore.QRect(32, 597, 20, 20))
        self.pressureIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.pressureIcon.setStyleSheet("background-color:transparent;")
        self.pressureIcon.setText("")
        self.pressureIcon.setPixmap(QtGui.QPixmap(":/icons/icons/carbon_pressure.png"))
        self.pressureIcon.setObjectName("pressureIcon")
        self.sevenDaysButton = QtWidgets.QPushButton(self.Main)
        self.sevenDaysButton.setGeometry(QtCore.QRect(251, 522, 101, 41))
        self.sevenDaysButton.setStyleSheet("\n"
"\n"
"background: #484DD5;\n"
"border-radius: 20px;\n"
"\n"
"\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"text-align: center;\n"
"letter-spacing: 0.04em;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.sevenDaysButton.setObjectName("sevenDaysButton")
        self.humidityLabel = QtWidgets.QLabel(self.Main)
        self.humidityLabel.setEnabled(True)
        self.humidityLabel.setGeometry(QtCore.QRect(58, 472, 77, 22))
        self.humidityLabel.setStyleSheet("\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"letter-spacing: 0.04em;\n"
"background-color:transparent;\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.humidityLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.humidityLabel.setObjectName("humidityLabel")
        self.mapsButton = QtWidgets.QPushButton(self.Main)
        self.mapsButton.setGeometry(QtCore.QRect(251, 578, 101, 41))
        self.mapsButton.setStyleSheet("\n"
"\n"
"background: #484DD5;\n"
"border-radius: 20px;\n"
"\n"
"\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"text-align: center;\n"
"letter-spacing: 0.04em;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"\n"
"background: #484DD5;\n"
"border-radius: 20px;\n"
"")
        self.mapsButton.setObjectName("mapsButton")
        self.cityLabel = QtWidgets.QLabel(self.Main)
        self.cityLabel.setGeometry(QtCore.QRect(103, 92, 181, 31))
        self.cityLabel.setStyleSheet("font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 32px;\n"
"line-height: 38px;\n"
"text-align: center;\n"
"letter-spacing: 0.04em;\n"
"\n"
"color: #FFFFFF;\n"
"background-color: transparent;\n"
""
"")
        self.cityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cityLabel.setObjectName("cityLabel")
        self.humidityValue = QtWidgets.QLabel(self.Main)
        self.humidityValue.setGeometry(QtCore.QRect(170, 471, 71, 23))
        self.humidityValue.setStyleSheet("\n"
"\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"letter-spacing: 0.04em;\n"
"background-color:transparent;\n"
"color: rgb(46, 54, 213);\n"
"\n"
"")
        self.humidityValue.setObjectName("humidityValue")
        self.tempIcon = QtWidgets.QLabel(self.Main)
        self.tempIcon.setGeometry(QtCore.QRect(32, 504, 20, 20))
        self.tempIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.tempIcon.setStyleSheet("background-color:transparent;")
        self.tempIcon.setText("")
        self.tempIcon.setPixmap(QtGui.QPixmap(":/icons/icons/carbon_temperature.png"))
        self.tempIcon.setObjectName("tempIcon")
        self.tempValue = QtWidgets.QLabel(self.Main)
        self.tempValue.setGeometry(QtCore.QRect(170, 502, 81, 22))
        self.tempValue.setStyleSheet("\n"
"\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"letter-spacing: 0.04em;\n"
"background-color:transparent;\n"
"color:rgb(46, 54, 213);\n"
"\n"
"")
        self.tempValue.setObjectName("tempValue")
        self.weatherDescription = QtWidgets.QLabel(self.Main)
        self.weatherDescription.setGeometry(QtCore.QRect(90, 420, 198, 26))
        self.weatherDescription.setStyleSheet("\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 16px;\n"
"line-height: 19px;\n"
"text-align: center;\n"
"letter-spacing: 0.12em;\n"
"background-color:transparent;\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.weatherDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherDescription.setObjectName("weatherDescription")
        self.feelsLikeLabel = QtWidgets.QLabel(self.Main)
        self.feelsLikeLabel.setGeometry(QtCore.QRect(58, 534, 85, 22))
        self.feelsLikeLabel.setStyleSheet("\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"letter-spacing: 0.04em;\n"
"background-color:transparent;\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.feelsLikeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.feelsLikeLabel.setObjectName("feelsLikeLabel")
        self.hourlyButton = QtWidgets.QPushButton(self.Main)
        self.hourlyButton.setGeometry(QtCore.QRect(251, 466, 101, 41))
        self.hourlyButton.setStyleSheet("\n"
"\n"
"background: #484DD5;\n"
"border-radius: 20px;\n"
"\n"
"\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"text-align: center;\n"
"letter-spacing: 0.04em;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.hourlyButton.setObjectName("hourlyButton")
        self.goBackButton = QtWidgets.QPushButton(self.Main)
        self.goBackButton.setGeometry(QtCore.QRect(11, 11, 31, 31))
        self.goBackButton.setStyleSheet("border-color:transparent")
        self.goBackButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Vector.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goBackButton.setIcon(icon)
        self.goBackButton.setIconSize(QtCore.QSize(21, 21))
        self.goBackButton.setAutoDefault(False)
        self.goBackButton.setDefault(False)
        self.goBackButton.setFlat(True)
        self.goBackButton.setObjectName("goBackButton")
        self.historyButton = QtWidgets.QPushButton(self.Main)
        self.historyButton.setGeometry(QtCore.QRect(80, 640, 211, 41))
        self.historyButton.setStyleSheet("\n"
"\n"
"background: #484DD5;\n"
"border-radius: 20px;\n"
"\n"
"\n"
"font-family: \'Roboto\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"text-align: center;\n"
"letter-spacing: 0.04em;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"\n"
"background: #484DD5;\n"
"border-radius: 20px;\n"
"")
        self.historyButton.setObjectName("historyButton")
        self.stackedWidget.addWidget(self.Main)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.titleLabel.setText(_translate("Form", "WeatherApp"))
        self.standardRadio.setText(_translate("Form", "Standard"))
        self.metricRadio.setText(_translate("Form", "Metric"))
        self.imperialRadio.setText(_translate("Form", "Imperial"))
        self.windspeedValue.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">45</span><span style=\" font-size:10pt;\">m/s</span></p></body></html>"))
        self.feelsLlikeValue.setText(_translate("Form", "25°"))
        self.pressureValue.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">23</span><span style=\" font-size:10pt;\">hPa</span></p></body></html>"))
        self.tempLabel.setText(_translate("Form", "Temper. :"))
        self.pressureLabel.setText(_translate("Form", "Pressure:"))
        self.windspeedLabel.setText(_translate("Form", "Wind-speed:"))
        self.tempLabelBig.setText(_translate("Form", "26°"))
        self.sevenDaysButton.setText(_translate("Form", "7-Days"))
        self.humidityLabel.setText(_translate("Form", "Humidity:"))
        self.mapsButton.setText(_translate("Form", "Maps"))
        self.cityLabel.setText(_translate("Form", "Lefkada"))
        self.humidityValue.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">56</span><span style=\" font-size:10pt;\">%</span></p></body></html>"))
        self.tempValue.setText(_translate("Form", "26°"))
        self.weatherDescription.setText(_translate("Form", "Light Drizzle"))
        self.feelsLikeLabel.setText(_translate("Form", "Feels-Like:"))
        self.hourlyButton.setText(_translate("Form", "Hourly"))
        self.historyButton.setText(_translate("Form", "History Data"))
import GUISnResources.resources