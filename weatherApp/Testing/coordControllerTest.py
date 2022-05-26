import unittest
import os,sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parentDir = os.path.dirname(currentDir)
sys.path.append(parentDir)

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