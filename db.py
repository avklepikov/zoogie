"""This module is used to connect Zoogie model with SQLite database.

"""
import sqlite3
import logging
#import model   # ??? two ways import?
import db_constants

#PROJECT_OBJECTS = (model.ProjectObject.__subclasses__())
#"""List of Class objects from the Model which should be transformed into Tables in database
#"""

#def get_classes():
        #"""Method returns list of Classes used in Project
        #"""
        #class_list = []
        #for _class in PROJECT_OBJECTS:
                #class_list.append (_class.__name__)
        #return class_list

def sql_connection():
        try:
                con = sqlite3.connect('ProjectApp.db')
                return con
        
        except Error:
                print(Error)
                
def executeSQL (SQL: str):
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(SQL)
        con.commit()
        con.close() 
        
        
def executeSQLget(SQL:str):
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(SQL)
        rows = cursorObj.fetchall()
        #con.commit()
        con.close() 
        return rows
        
def get_class_table(_class: list):
        return db_constants.DB_TABLE_MAPPING[_class]

def get_class_attribute_fields(_class: str):
        attr_list=[]   
        for attr in db_constants.DB_FIELDS_MAPPING[_class]:
                attr_list.append (db_constants.DB_FIELDS_MAPPING[_class][attr][0])
        return attr_list

def get_class_attribute_field_and_type(_class: str):
        """takes Project Class as an argument and through mapping thable from db_constants
        returns list of attributes with its SQLLITE field type"""
        attr_list=[]   
        for attr in db_constants.DB_FIELDS_MAPPING[_class]:
                attr_list.append (db_constants.DB_FIELDS_MAPPING[_class][attr][0] + 
                                  " " + 
                                  db_constants.DB_FIELDS_MAPPING[_class][attr][1])
        return attr_list



def get_class_PK(_class: str):
        return db_constants.DB_FIELDS_PK[_class]


def compile_CREATE_TABLE_script (_class: str):
        """based in _class argument (Class from Project related classes) 
        creates SQL script for SQLLite that
        creates new table, which structure is defined in db_constants"""
        
        table = get_class_table(_class)
        attr_str_list = ', '.join(get_class_attribute_field_and_type(_class))
        PK = get_class_PK(_class)
        SQL = f"CREATE TABLE {table}({attr_str_list})" 
        return SQL


def complile_SELECT_ALL (_class: str, _attr_value_dict: dict):
        logging.info('complile_SELECT_ALL has been activated with parameters: ', _class, _attr_value_dict)
        table = get_class_table(_class)
        _fields_list = []
        for attr in _attr_value_dict:
                _fields_list.append ( db_constants.DB_FIELDS_MAPPING[_class][attr][0])
        _fields_list_str = ', '.join(_fields_list)
        SQL = f"SELECT {_fields_list_str} FROM {table}"
        logging.debug('Resulting SQL: ', SQL)
        return SQL

def complile_SELECT_BY_PROJECT_ID (_class: str, _attr_value_dict: dict, _Project_id: int):
        """his is a target function to be used to retrived any Project record by related Project ID"""
        logging.info('complile_SELECT_BY_PROJECT_ID has been activated with parameters: ', _class, _attr_value_dict, _Project_id)
        table = get_class_table(_class)
        _fields_list = []
        for attr in _attr_value_dict:
                _fields_list.append ( db_constants.DB_FIELDS_MAPPING[_class][attr][0])
        _fields_list_str = ', '.join(_fields_list)
        _id_field = db_constants.DB_FIELDS_PK[_class]
        SQL = f"SELECT {_fields_list_str} FROM {table} WHERE RelatedProject = {_Project_id}"  
        logging.debug('Resulting SQL: ', SQL)
        return SQL

def complile_SELECT_BY_ITEM_ID (_class: str, _attr_value_dict: dict, _id: int):
        """This is a target function to be used to retrived any Project record by its ID
        """
        logging.info('complile_SELECT_BY_ITEM_ID has been activated with parameters: ', _class, _attr_value_dict, _id)
        
        table = get_class_table(_class)
        _fields_list = []
        for attr in _attr_value_dict:
                _fields_list.append ( db_constants.DB_FIELDS_MAPPING[_class][attr][0])
        _fields_list_str = ', '.join(_fields_list)
        _id_field = db_constants.DB_FIELDS_PK[_class]
        #print ('SELECT_BY_ITEM_ID : _id_field: ', _id_field)
        
        SQL = f"SELECT {_fields_list_str} FROM {table} WHERE {_id_field} = {_id}"  # changed from {_id_field} to RelatedProject
        logging.debug('Resulting SQL: ', SQL)
        return SQL        

def compile_INSERT_script (_class: str, _attr_value_dict: dict):
        """based in _class argument (Class from Project related classes) 
        creates SQL script for SQLLite that
        creates ......"""
        
        table = get_class_table(_class)
        _fields_list = []
        _values_list = []
        for attr in _attr_value_dict:
                if _attr_value_dict[attr] is not None:
                        
                        _fields_list.append ( db_constants.DB_FIELDS_MAPPING[_class][attr][0])
                        
                        if db_constants.DB_FIELDS_MAPPING[_class][attr][1] == "TEXT":
                                _values_list.append ("'"+_attr_value_dict[attr]+"'")
                        else:
                                _values_list.append ( str(_attr_value_dict[attr]))
                                
                                
                                
        _fields_list_str = ', '.join(_fields_list)
        _values_list_str = ', '.join(_values_list)
        SQL = f"INSERT INTO {table} ({_fields_list_str}) VALUES ({_values_list_str})"    
        
        return SQL

def compile_UPDATE_script (_class: str, _attr_value_dict: dict):
        """based in _class argument (Class from Project related classes) 
        creates SQL script for SQLLite that
        UPDATES table based on the ID = PK (primary Key set in the db_constants)"""
        
        table = get_class_table(_class)
        

        _equation = []
        _PK = get_class_PK(_class)
        for attr in _attr_value_dict:
                if _attr_value_dict[attr] is not None:
                        
                        
                        if db_constants.DB_FIELDS_MAPPING[_class][attr][0] != _PK:
                                if db_constants.DB_FIELDS_MAPPING[_class][attr][1] == "TEXT":
                                        _values_list = "'"+_attr_value_dict[attr]+"'"
                                         
                                        
                                        
                                else:
                                        _values_list =  str(_attr_value_dict[attr])
                                xxx = db_constants.DB_FIELDS_MAPPING[_class][attr][0] + " = " + _values_list       
                                _equation.append (xxx)        
                        
                        else:
                                _PK_str = db_constants.DB_FIELDS_MAPPING[_class][attr][0] + " = " + str(_attr_value_dict[attr])
                                
        _SET_str = ', '.join(_equation)
        
        SQL = f"UPDATE  {table} SET {_SET_str} WHERE {_PK_str}"    
        #print (SQL)
        
        return SQL

#def initiateDB():
        #"""creation of ProjectApp from scratch (even if there is no database file
        #Method takes all Project Classes and usins db_constants identifies required database structure"""
        #for _class in get_classes():
                #executeSQL (compile_CREATE_TABLE_script(_class))
                #print (f'... created table for {_class}')
        #print ('done')



def main():
        initiateDB()

if __name__ == '__main__':
        main()