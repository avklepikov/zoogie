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
                }}
        
                
class MainFrame (Frame):
        def __init__ (self, master, dbProjectRecordID, objectName, colorCode):
                super().__init__(master)
                self.config (bg = colorCode)
                self.dbProjectRecordID = dbProjectRecordID
                self.objectName = objectName
                #self.label = Label(self, text = 'label')
                #self.label.pack()
                print (self.objectName)
                argList = []
                argLabelList = []
                argSizeList = []
                
                #print (REGISTER_BLOCKS['QualityRegister']['Register'])
                for item in REGISTER_BLOCKS[self.objectName]['Register']:
                        print (item)
                        argList.append (item)
                        argLabelList.append (REGISTER_BLOCKS[self.objectName]['Register'][item][0])
                        argSizeList.append (REGISTER_BLOCKS[self.objectName]['Register'][item][1])
                        #print (REGISTER_BLOCKS['QualityRegister']['Register'][item][1])
                
                print (argList)
                print (argLabelList)
                print (argSizeList)
                
                self.Register = CustomizedElements.RegisterList(self, 
                                                                self.dbProjectRecordID,
                                                                self.objectName, 
                                                                argList,
                                                                argSizeList)
                
                self.Register.pack()
                
                
                argList.clear()
                argLabelList.clear()
                argSizeList.clear()
                argRowList = []
                argColumnList = []
                
                #print (REGISTER_BLOCKS['QualityRegister']['Register'])
                for item in REGISTER_BLOCKS[self.objectName]['Breakdown']:
                        print (item)
                        argList.append (item)
                        argLabelList.append (REGISTER_BLOCKS[self.objectName]['Breakdown'][item][0])
                        argRowList.append (REGISTER_BLOCKS[self.objectName]['Breakdown'][item][1])
                        argColumnList.append (REGISTER_BLOCKS[self.objectName]['Breakdown'][item][2])
                        #argSizeList.append (REGISTER_BLOCKS[self.objectName]['Breakdown'][item][1])
                        #print (REGISTER_BLOCKS['QualityRegister']['Register'][item][1])
                
                print (argList)
                print (argLabelList)
                print (argSizeList)                
                
                
                self.BD = Breakdown(self, self.objectName, argList, argLabelList, argRowList, argColumnList, colorCode)
                self.BD.pack()
                
        def Refresh (self, dbRecordID):
                self.BD.Refresh(dbRecordID)     

class Breakdown (Frame):
        def __init__ (self, master, objectName, argList, argLabelList, argRowList, argColumnList, colorCode):
                super().__init__(master)
                self.objectName = objectName
                self.config (bg = colorCode)
                #dbRecordID = '1'
                #colorCode = 'gray'
                
                ObjectsList = []
                
                print ('len = ', len(argList), ' --> ', range(len(argList)))
                for item in range(len(argList)):
                        print (item, argList[item], argLabelList[item])
                        ObjectsList.append(CustomizedElements.AttributeBlockFrame(self, -1, self.objectName, argList[item], argLabelList[item], colorCode))
                        ObjectsList[-1].grid(row = argRowList[item], column = argColumnList[item],)
                
                #self.Attr1 = CustomizedElements.AttributeBlockFrame(self, -1, self.objectName, 'Title', 'Title', colorCode)
                #self.Attr2 = CustomizedElements.AttributeBlockFrame(self, -1, self.objectName, 'RolesResponsibilities', 'RolesResponsibilities', colorCode)
                #self.Attr2 = CustomizedElements.AttributeBlockFrame(self, -1, self.objectName, 'Result', 'Result', colorCode)


                
        
                #self.Attr1.grid(row=0, column = 0)
                #self.Attr2.grid(row=0, column = 1)


                self.attributesObjects = ObjectsList
                #self.attributesObjects = (self.Attr1, 
                                          #self.Attr2)
                
                #self.Button = Button(self, text = 'Refresh', command = self.Refresh)
                #self.Button.grid (row=4, column = 0)          
        def Refresh (self, dbRecordID):

                Keys, Data = controller.RefreshBusinessObject_byID(self.objectName, dbRecordID)

                
                for item in self.attributesObjects:
                        #print (item.attributeName)
                        item.valueUpdate(Data[0][Keys[item.attributeName]])
                        item.dbRecordID = Data[0][Keys['ID']]
                        


def Main():
        
        logging.basicConfig(filename='logging.txt',level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M', filemode='w')
        app = Tk()
        block = MainFrame(app,29, 'Team' ,'gray')
        #block = MainFrame(app,1, 'Stakeholder' ,'gray')
        #block = MainFrame(app,1, 'QualityRegister' ,'gray')
        #QualityRegister
        block.pack()
        app.mainloop()
        
if __name__=='__main__':
        Main()