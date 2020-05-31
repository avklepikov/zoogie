from tkinter import *
import CustomizedElements
import controller

import logging

#TODO Add Title to Qulity Register


REGISTER_BLOCKS = {
        'QualityRegister': {
                'Register': {
                        'BusinessID' : ['Bisiness ID', 80],
                        'Title': ['Title', 250],
                        'Dates': ['Date', 120],
                        'Method': ['Method', 250],
                        'Status': ['Status', 120]},
                'Breakdown': {
                        'RolesResponsibilities': ['Roles and Responsibilities', 0, 0],
                        'Result':['Result', 0, 1]}
                },
        'Stakeholder':{
                'Register':{
                        'Name': ['Name', 250],
                        'EMail': ['EMail', 250],
                        'Phone': ['Phone', 250],
                        'Birthday': ['Birthday', 150],
                        'SupportLevel': ['Level of Support', 250],
                        'InfluenceLevel': ['Level of influence', 250]},
                'Breakdown': {
                        'Interests': ['Interests', 0, 0],
                        'CurrentRel': ['Current Relation', 0, 1],
                        'InfoFromProject': ['Information from Project to Stakeholder', 1, 0],
                        'InfoToProject': ['Information to Project from Stakeholder', 1, 1],
                        'Interfaces': ['Interfaces', 2, 0],
                        'KeyMessages': ['Key Messages', 2, 1]}},
        'Benefit':{
                'Register': {
                        'Title': ['Name', 250],
                        'Category': ['Category', 150]},
                'Breakdown': {
                        'Description': ['Description', 0, 0],
                        'Baseline': ['Baseline', 0, 1],
                        'Measurement': ['Measurement', 1, 0],
                        'ResourceRequirements': ['Resourse Requirements', 1, 1],
                        'Responsibility': ['Responsibilities', 2, 0]}},
        'Team':{
                'Register': {
                        'Person': ['Name', 250],
                        'Role': ['Role', 250],
                        },
                'Breakdown': {
                        'Responsibilities': ['Project Responsibilities', 0, 0]}
                },
        'Lesson':{
                'Register':{
                        'BusinessID' : ['Bisiness ID', 80],
                        'Title': ['Title', 250],
                        'Category': ['Category', 210],
                        'CategoryProcess': ['CategoryProcess', 210],
                        'Priority': ['Priority', 150],
                        'LoggedBy': ['LoggedBy', 120],
                        'DateLogged' :['DateLogged', 120]},
                'Breakdown': {
                        'Title': ['Title', 0, 0],
                        'Description': ['Description', 0, 1],
                        'Recommendations': ['Recommendations', 1, 1],
                        'CauseTrigger': ['Cause Trigger', 1, 0],
                }
                },
        'Change':{
                'Register':{},
                'Breakdown':{}
                },
                
        'Stage':{
                'Register':{
                        'Title': ['Title', 250],
                        'Category': ['Stage Category', 250],
                        'StartDate': ['Start Date', 100],
                        'EndDate': ['End Date', 100],
                        'Status': ['Status', 150]},
                'Breakdown':{}
        }}
        
                
class MainFrame (Frame):
        def __init__ (self, master, dbProjectRecordID, objectName, colorCode):
                super().__init__(master)
                self.config (bg = colorCode)
                self.dbProjectRecordID = dbProjectRecordID
                self.objectName = objectName
                argList = []
                argLabelList = []
                argSizeList = []
                
                #Building the Register based on REGISTER_BLOCKS setup:
                for item in REGISTER_BLOCKS[self.objectName]['Register']:
                        argList.append (item)
                        argLabelList.append (REGISTER_BLOCKS[self.objectName]['Register'][item][0])
                        argSizeList.append (REGISTER_BLOCKS[self.objectName]['Register'][item][1])                
                self.Register = CustomizedElements.RegisterList(self, 
                                                                self.dbProjectRecordID,
                                                                self.objectName, 
                                                                argList,
                                                                argSizeList)
                self.Register.pack()
                
                #Building the Breakdown section
                BD_argList =[]
                BD_argLabelList= []
                argSizeList.clear()
                argRowList = []
                argColumnList = []
                for item in REGISTER_BLOCKS[self.objectName]['Breakdown']:
                        BD_argList.append (item)
                        BD_argLabelList.append (REGISTER_BLOCKS[self.objectName]['Breakdown'][item][0])
                        argRowList.append (REGISTER_BLOCKS[self.objectName]['Breakdown'][item][1])
                        argColumnList.append (REGISTER_BLOCKS[self.objectName]['Breakdown'][item][2])

                
                self.BD = Breakdown(self, self.objectName, BD_argList, BD_argLabelList, argRowList, argColumnList, colorCode)
                self.BD.pack()
                

                
        def Refresh (self, dbRecordID):
                """BreakDown refresh based on item selected in the register"""
                self.BD.Refresh(dbRecordID)    
         
        

class Breakdown (Frame):
        def __init__ (self, master, objectName, argList, argLabelList, argRowList, argColumnList, colorCode):
                super().__init__(master)
                self.objectName = objectName
                self.config (bg = colorCode)

                
                ObjectsList = []
                

                for item in range(len(argList)):
                        
                        ObjectsList.append(CustomizedElements.AttributeBlockFrame(self, -1, self.objectName, argList[item], argLabelList[item], colorCode))
                        ObjectsList[-1].grid(row = argRowList[item], column = argColumnList[item],)


                self.attributesObjects = ObjectsList
         
        def Refresh (self, dbRecordID):

                Keys, Data = controller.RefreshBusinessObject_byID(self.objectName, dbRecordID)

                
                for item in self.attributesObjects:
                        item.valueUpdate(Data[0][Keys[item.attributeName]])
                        item.dbRecordID = Data[0][Keys['ID']]
                        


def Main():
        
        logging.basicConfig(filename='logging.txt',level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M', filemode='w')
        app = Tk()
        block = MainFrame(app,29, 'Lesson' ,'gray')
        #block = MainFrame(app,1, 'Stakeholder' ,'gray')
        #block = MainFrame(app,1, 'QualityRegister' ,'gray')
        #QualityRegister
        block.pack()
        app.mainloop()
        
if __name__=='__main__':
        Main()