"""Module contains InitiateDB() method which creates SQLite database from Scratch
"""


import sqlite3

from Database import db_constants
from Database import db 
from Model import model
import pathlib

PROJECT_OBJECTS = (model.ProjectObject.__subclasses__())
"""List of Class objects from the Model which should be transformed into Tables in database
"""


def get_classes():
        """Method returns list of Classes used in Project
        """
        class_list = []
        for _class in PROJECT_OBJECTS:
                class_list.append (_class.__name__)
        return class_list



def initiateDB():
        """creation of ProjectApp from scratch (even if there is no database file
        Method takes all Project Classes and usins db_constants identifies required database structure"""
        for _class in get_classes():
                print (f'--> {_class}')
                db.executeSQL (db.compile_CREATE_TABLE_script(_class))
                print (f'... created table for {_class}')
        print ('done')
        

def checkDBExists():
        """verification that database exists. if not creating new empty database"""
        path = pathlib.Path(db_constants.DB_DATABASE['filename'])
        #print ('DB verification:', path.is_file())
        if path.is_file() == False:
                print ('.... creating SQLite Database ', db_constants.DB_DATABASE['filename'])
                initiateDB()
        

def Main():
        
        checkDBExists()
        

if __name__ == '__main__':
        Main()