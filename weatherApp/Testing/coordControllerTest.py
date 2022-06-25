import unittest
import os,sys
path = os.getcwd()
parentPath = os.path.dirname(path) + "/weatherApp"
sys.path.insert(0,parentPath)

from Exceptions.emptyRequestException import EmptyRequestException
import keys
from Controllers.coordController import CoordController

cord = CoordController(keys.API_KEY)

class TestCoordControll(unittest.TestCase):

    def test_getCityLonLat(self):
        self.assertRaises(TypeError,cord.getCityLonLat,123)
        self.assertRaises(TypeError,cord.getCityLonLat,["Lefkada"])
        self.assertRaises(TypeError,cord.getCityLonLat,{"lef":"Lefkada"})
        self.assertRaises(TypeError,cord.getCityLonLat,12.4)
        self.assertRaises(EmptyRequestException,cord.getCityLonLat,"Lqweraasdass")
        self.assertEqual(tuple,type(cord.getCityLonLat("Lefkada")))
        self.assertEqual(tuple,type(cord.getCityLonLat("Peru")))
        self.assertEqual(tuple,type(cord.getCityLonLat("Sydney")))
        self.assertEqual(tuple,type(cord.getCityLonLat("New York")))