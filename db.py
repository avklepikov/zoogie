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
                
def executeSQL (SQL: str):                                        # OK
        """Execution of SQL script which does not provide any RETURN
        """
        logging.info (f'      DB Starting executeSQL (SQL = {SQL})')
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(SQL)
        con.commit()
        con.close() 
        
        
def executeSQLget(SQL:str):                                       # OK
        """Execution of SQL script which provides RETURN
        """   
        logging.info (f'      DB Starting executeSQLget (SQL = {SQL})')
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(SQL)
        rows = cursorObj.fetchall()
        con.close() 
        return rows
        
def get_class_table(_class: list):                                # OK
        """Method returns related database table name related to the Project object class.
        Method uses DB_TABLE_MAPPING dictionary from db_constants file.
        """
        return db_constants.DB_TABLE_MAPPING[_class]

def get_class_attribute_fields(_class: str):                      # OK (not used)
        """Method takes Project Object class name and returns list of its attributes as a list.
        Method uses DB_FIELDS_MAPPING dictionary from db_constants file.
        
        Attributes:
            _class        (str): Name of the Class for any Project object used in the Model
            
        Return:
            _attr_list    (list): List of attributes related to the Class
        """
        logging.info (f'      DB Starting get_class_attribute_fields (_class = {_class})')
        
        attr_list=[]   
        for attr in db_constants.DB_FIELDS_MAPPING[_class]:
                attr_list.append (db_constants.DB_FIELDS_MAPPING[_class][attr][0])
        return attr_list

def get_class_attribute_field_and_type(_class: str):              # OK
        """takes Project Class name and returns list of attributes with its SQLLITE field type.
        Method uses DB_FIELDS_MAPPING dictionary from db_constants file.
        
        Attributes:
            _class        (str): Name of the Class for any Project object used in the Model
            
        Return:
            _attr_list    (list): List of database table fields related to provided class name followed by its SQLite field type 
                                  in the format [field type, field type, field type]
        """
        logging.info (f'      DB Starting get_class_attribute_field_and_type (_class = {_class})')
        attr_list=[]   
        for attr in db_constants.DB_FIELDS_MAPPING[_class]:
                attr_list.append (db_constants.DB_FIELDS_MAPPING[_class][attr][0] + 
                                  " " + 
                                  db_constants.DB_FIELDS_MAPPING[_class][attr][1])
        return attr_list



def get_class_PK(_class: str):                                    # OK
        """Method returns Primary Key of the table related to provided Class name from the Model
        Method uses DB_FIELDS_PK mapping dictionary from db_constants file.
        """
        logging.info (f'      DB Starting get_class_PK (_class = {_class})')
        return db_constants.DB_FIELDS_PK[_class]


def compile_CREATE_TABLE_script (_class: str):                    #OK (used from db initialization codule)
        """based in _class argument (Class from Project related classes) 
        creates SQL script for SQLLite to
        create new table, which structure is defined in db_constants
        
        Method uses the following logic:
        - based on the class name gets related table name with get_class_table()
        - based on the class name gets related field names followed by field types with attr_str_list()
        
        Attributes:
            _class        (str): Name of the Class for any Project object used in the Model
            
        Return:
            SQL           (str): compiled SQL script which can be executed in SQLite
        
        """
        logging.info (f'      DB Starting compile_CREATE_TABLE_script (_class = {_class})')
        
        table = get_class_table(_class) 
        attr_str_list = ', '.join(get_class_attribute_field_and_type(_class))
        PK = get_class_PK(_class)
        SQL = f"CREATE TABLE {table}({attr_str_list})" 
        return SQL


def complile_SELECT_ALL (_class: str, _attr_value_dict: dict):
        logging.info (f'      DB Starting complile_SELECT_ALL (_class = {_class}, _attr_value_dict = {_attr_value_dict})')
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
        logging.info (f'      DB Starting complile_SELECT_BY_PROJECT_ID (_class = {_class}, _attr_value_dict = {_attr_value_dict}, _Project_id = {_Project_id})')
        
        table = get_class_table(_class)
        _fields_list = []
        for attr in _attr_value_dict:
                _fields_list.append ( db_constants.DB_FIELDS_MAPPING[_class][attr][0])
        _fields_list_str = ', '.join(_fields_list)
        _id_field = db_constants.DB_FIELDS_PK[_class]
        SQL = f"SELECT {_fields_list_str} FROM {table} WHERE RelatedProject = {_Project_id}"  
        #logging.debug('Resulting SQL: ', SQL)
        return SQL

def complile_SELECT_BY_ITEM_ID (_class: str, _attr_value_dict: dict, _id: int):    # why we use _attr_value_dict?
        """This method compiles SQL script to get from the database any project class record by its ID
        """
        logging.info (f'      DB Starting complile_SELECT_BY_ITEM_ID (_class = {_class}, _attr_value_dict = {_attr_value_dict}, _id = {_id})')
        
        table = get_class_table(_class)
        _fields_list = []
        for attr in _attr_value_dict:
                _fields_list.append ( db_constants.DB_FIELDS_MAPPING[_class][attr][0])
        _fields_list_str = ', '.join(_fields_list)
        _id_field = db_constants.DB_FIELDS_PK[_class]
        #print ('SELECT_BY_ITEM_ID : _id_field: ', _id_field)
        
        SQL = f"SELECT {_fields_list_str} FROM {table} WHERE {_id_field} = {_id}"  # changed from {_id_field} to RelatedProject
        #logging.debug('Resulting SQL: ', SQL)
        return SQL        

def compile_INSERT_script (_class: str, _attr_value_dict: dict):
        """based in _class argument (Class from Project related classes) 
        creates SQL script for SQLLite that
        creates ......"""
        
        logging.info (f'      DB Starting compile_INSERT_script (_class = {_class}, _attr_value_dict = {_attr_value_dict})')
        
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
        
        logging.info (f'      DB Starting compile_UPDATE_script (_class = {_class}, _attr_value_dict = {_attr_value_dict})')
        
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



def main():
        initiateDB()

if __name__ == '__main__':
        main()