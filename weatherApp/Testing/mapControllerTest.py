import unittest
import os,sys


path = os.getcwd()
parentPath = os.path.dirname(path) + "/weatherApp"
sys.path.insert(0,parentPath)
print(parentPath)
from Exceptions.badRequest import BadRequest
from Exceptions.emptyRequestException import EmptyRequestException
import keys
from Controllers.mapController import MapController

mapp = MapController(keys.API_KEY)

class TestMapControl(unittest.TestCase):

    def test_setMap(self):
        self.assertRaises(TypeError,mapp.setMap,1,"CL")
        self.assertRaises(TypeError,mapp.setMap,1,2)
        self.assertRaises(EmptyRequestException,mapp.setMap,"asdf","asdf")
        self.assertEqual(None,mapp.setMap("Lefkada","CL"))
        self.assertEqual(None,mapp.setMap("Peristeri","PAC0"))
        self.assertEqual(None,mapp.setMap("New Delhi","TD2"))
        self.assertRaises(BadRequest,mapp.setMap,"Lefkada","asdf")
        self.assertRaises(BadRequest,mapp.setMap,"Patras","asdf")
        self.assertRaises(BadRequest,mapp.setMap,"Athens","asdf")
        self.assertRaises(BadRequest,mapp.setMap,"Lefkada","asdf")

if __name__ == '__main__':
    unittest.main()
