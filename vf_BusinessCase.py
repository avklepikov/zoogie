"""Business Case Frame module

===========
DESCRIPTION
===========

Is used to

- visualize all Business Case Project Object attributes on the screen.

- update any attribute with double-click on any attribute value


TODO [ ] Link object ID with the overall Project

"""


from tkinter import *
from tkinter import ttk
import CustomizedElements as CE
import controller

colorCode = '#abc4e7'

class MainFrame (Frame):
        def __init__ (self, master, dbProjectRecordID):
                super().__init__(master)
                self.dbProjectRecordID=dbProjectRecordID
                #self.dbRecordID = -1
                self.className = 'BusinessCase'
                
                self.Attr1 = CE.AttributeBlockFrame(self, -1, self.className, 'ExecutiveSummary', 'Executive Summary', colorCode)
                self.Attr2 = CE.AttributeBlockFrame(self, -1, self.className, 'Reasons', 'Reasons', colorCode)
                self.Attr3 = CE.AttributeBlockFrame(self, -1, self.className, 'Options', 'BusinessOptions', colorCode)
                self.Attr4 = CE.AttributeBlockFrame(self, -1, self.className, 'Timescale', 'Time Scale', colorCode)
                self.Attr5 = CE.AttributeBlockFrame(self, -1, self.className, 'ExpectedBenefits', 'Expected Benefits', colorCode)
                self.Attr6 = CE.AttributeBlockFrame(self, -1, self.className, 'ExpectedDisBenefits', 'Expected Dis-benefits', colorCode)
                self.Attr7 = CE.AttributeBlockFrame(self, -1, self.className, 'Costs', 'Costs', colorCode)
                self.Attr8 = CE.AttributeBlockFrame(self, -1, self.className, 'InvestmentArraisal', 'Investment Appriasal', colorCode)
                
        
                self.Attr1.grid(row=0, column = 0)
                self.Attr2.grid(row=1, column = 0)
                self.Attr3.grid(row=2, column = 0)
                self.Attr4.grid(row=3, column = 0)
                self.Attr5.grid(row=0, column = 1)
                self.Attr6.grid(row=1, column = 1)
                self.Attr7.grid(row=2, column = 1)
                self.Attr8.grid(row=3, column = 1)
                
                self.attributesObjects = (self.Attr1, 
                                          self.Attr2, 
                                          self.Attr3, 
                                          self.Attr4, 
                                          self.Attr5, 
                                          self.Attr6,
                                          self.Attr7,
                                          self.Attr8)
                
                self.Button = Button(self, text = 'Refresh', command = self.Refresh)
                self.Button.grid (row=4, column = 0)
                
                        
        def Refresh (self):        # ? move to separate superclass
                
                #_activeProject = 1
                Keys, Data = controller.RefreshBusinessObject(self.className, self.dbProjectRecordID)
                #print (Keys, Data)
                for eachAttributeObject in self.attributesObjects:
                        eachAttributeObject.valueUpdate (Data[0][Keys[eachAttributeObject.attributeName]])
                        eachAttributeObject.dbRecordID = Data[0][Keys['ID']]
        

