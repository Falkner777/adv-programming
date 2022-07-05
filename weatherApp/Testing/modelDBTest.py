import sqlite3 as sql
import os,sys
import unittest

path = os.getcwd()

sys.path.insert(0, path)
from Controllers.modelDB import ModelDB

class TestModelDB(unittest.TestCase):

    def setUp(self) -> None:
        self.connector = ModelDB(f'.{os.path.sep}sample.sqlite3') 
    
    def test_selectData(self):
        self.assertFalse(self.connector.selectData("NOT A VALID QUERY"))
        self.assertFalse(self.connector.selectData("SELECT * FROM PLACES"))
        self.assertEqual(type(self.connector.selectData("SELECT name FROM sqlite_master WHERE type='table';")),list)
    
    def test_storeDate(self):
        self.assertTrue(self.connector.storeData(f'CREATE TABLE IF NOT EXISTS "AREA" (\
	"lon"	TEXT NOT NULL,\
	"lat"	TEXT NOT NULL,\
	"Name"	TEXT NOT NULL,\
	"Id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT\
)'))
        self.assertTrue(self.connector.storeData(f"INSERT INTO AREA (lon,lat,Name)\
        VALUES ({123},{123},'Patras')"))
        self.assertFalse(self.connector.storeData("Not a valid query"))
    


if __name__=="__main__":
    unittest.main()