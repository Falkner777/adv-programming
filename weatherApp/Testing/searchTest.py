import unittest
import os,sys

path = os.getcwd()

sys.path.insert(0, path)


from mainApp import WeatherApp
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from PyQt5.QtTest import QTest
from Exceptions.badRequest import BadRequest
app = qtw.QApplication(sys.argv)
class TestSearchWindow(unittest.TestCase):
  

    def setUp(self) :
        self.mainapp = WeatherApp()

    def setDefaults(self):
        self.mainapp.GUI.stackedWidget.setCurrentIndex(0)


    def test_defaults(self):
        self.assertEqual(self.mainapp.GUI.standardRadio.isChecked(),True)
        self.assertEqual(self.mainapp.GUI.searchEdit.text(),"")

    def test_SearchEditKelvin(self):
        self.setDefaults()
        QTest.keyClicks(self.mainapp.GUI.searchEdit,"Lefkada")
        searchButton = self.mainapp.GUI.searchButton
        QTest.mouseClick(searchButton,qtc.Qt.LeftButton)
        self.assertEqual(self.mainapp.GUI.cityLabel.text(),"Lefkada")
        self.assertIn("K",self.mainapp.GUI.tempLabelBig.text())
    
    def test_SearchEditCelsius(self):
        self.setDefaults()
        QTest.mouseClick(self.mainapp.GUI.metricRadio,qtc.Qt.LeftButton)
        QTest.keyClicks(self.mainapp.GUI.searchEdit,"Patras")
        searchButton = self.mainapp.GUI.searchButton
        QTest.mouseClick(searchButton,qtc.Qt.LeftButton)
        self.assertEqual(self.mainapp.GUI.cityLabel.text(),"Patras")
        self.assertIn("C",self.mainapp.GUI.tempLabelBig.text())

    def test_SearchEditFahrenheit(self):
        self.setDefaults()
        QTest.mouseClick(self.mainapp.GUI.imperialRadio,qtc.Qt.LeftButton)
        QTest.keyClicks(self.mainapp.GUI.searchEdit,"Athens")
        searchButton = self.mainapp.GUI.searchButton
        QTest.mouseClick(searchButton,qtc.Qt.LeftButton)
        self.assertEqual(self.mainapp.GUI.cityLabel.text(),"Athens")
        self.assertIn("F",self.mainapp.GUI.tempLabelBig.text())


if __name__ == '__main__':
    unittest.main()
