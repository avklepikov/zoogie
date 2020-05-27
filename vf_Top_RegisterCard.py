from tkinter import *
from tkinter import ttk

import controller


REGISTER_BLOCKS = {
        'RiskRegister': {
                'ID': ['TEXT_LINE_BLOCKED', 0, 1],
                'RelatedProject': ['TEXT_LINE_BLOCKED', 7, 0],
                'BusinessID': ['TEXT_LINE', 0, 2],
                'Title': ['TEXT_LINE', 0, 0],
                'RiskEvent':['TEXT_LINE', 1, 0],
                'RiskEffect':['TEXT_LINE', 1, 1],
                'Description': ['TEXT_BOX', 4, 0],
                'Impact': ['TEXT_BOX', 4, 1],
                'Owner': ['TEXT_LINE', 5, 1],
                'Category': ['COMBO', 1, 2],
                'Author': ['TEXT_LINE', 3, 0],
                'ExpectedValue': ['TEXT_BOX',4 ,2],
                'Probability': ['COMBO', 2, 1],
                'Proximity': ['TEXT_LINE', 2, 0],
                'RaisedDate': ['TEXT_LINE', 3, 1],
                'Response': ['TEXT_BOX',6 ,0],
                'ResponseCategory': ['COMBO', 5, 0],
                'Status': ['COMBO', 2, 2],
                'Actionee': ['TEXT_LINE', 5, 2],
                'Risk Identification': ['LABEL', 8, 0],
                'Risk Assessment':['LABEL', 8, 1],
                'Risk Evaluation':['LABEL', 8, 2],
                'Risk Planing': ['LABEL', 8, 3]
                },
        'QualityRegister':{
                'ID':['TEXT_LINE_BLOCKED', 0, 0],
                'RelatedProject':['TEXT_LINE_BLOCKED', 7, 0],
                'BusinessID':['TEXT_LINE', 0 , 1],
                'Dates': ['TEXT_LINE', 0, 2],
                'Title':['TEXT_LINE', 1, 0],
                'Result': ['TEXT_BOX', 2, 0],
                'RolesResponsibilities': ['TEXT_BOX', 2, 1],
                'Method': ['TEXT_LINE', 1, 1],
                'RelatedProduct': ['TEXT_LINE', 7, 1],
                'Status': ['COMBO', 1, 2]
                
                },
        'Lesson':{
                'ID': ['TEXT_LINE_BLOCKED', 0, 0],
                'RelatedProject':['TEXT_LINE_BLOCKED', 0, 1],
                'BusinessID': ['TEXT_LINE', 0, 2],
                'Category': ['TEXT_LINE', 1, 0],
                'Event': ['TEXT_LINE', 1, 1],
                'Effect': ['TEXT_LINE', 1, 2],
                'CauseTrigger':['TEXT_LINE', 2, 0],
                'Description': ['TEXT_BOX', 2, 1],
                'DateLogged':['TEXT_LINE', 4, 1],
                'EarlyWarningIndicator':['TEXT_LINE', 2, 2],
                'LoogedBy':['TEXT_LINE', 4, 0],
                'Priority':['TEXT_LINE', 5, 0],
                'Recommendations': ['TEXT_BOX', 5, 1],
                'Title':['TEXT_LINE', 3, 0],
                'Lesson Identification': ['LABEL', 8,0],
                'Lesson Analysis': ['LABEL', 8,1]
                },
        'Product':{
                'ID':['TEXT_LINE_BLOCKED', 0, 0],
                'BusinessID': ['TEXT_LINE_BLOCKED', 0, 1],
                'Title':['TEXT_LINE', 1, 0],
                'Description': ['TEXT_BOX', 2, 0],
                'Derivation': ['TEXT_BOX', 2 , 1],
                'Composition': ['TEXT_BOX', 2, 2],
                'DevSkills':['TEXT_BOX', 3, 0],
                'FormatPresentation': ['TEXT_BOX', 3, 0],
                'Purpose': ['TEXT_BOX', 3, 1],
                'RelatedProject': ['TEXT_LINE_BLOCKED', 0, 2],
                'ParentID': ['TEXT_LINE', 1, 1]
                },
        'Issue':{
                'ID': ['TEXT_LINE_BLOCKED', 0, 0],
                'BusinessID': ['TEXT_LINE_BLOCKED', 0, 1],
                'RelatedProject': ['TEXT_LINE_BLOCKED', 0, 2],
                'Description': ['TEXT_BOX', 1, 0],
                'Category':['COMBO', 2, 0],
                'Priority': ['COMBO', 2, 1],
                'Severity': ['TEXT_LINE', 2, 2],
                'ClosureDate': ['TEXT_LINE', 4, 0],
                'DateRaised': ['TEXT_LINE', 3, 2],
                'IssueAuthor': ['TEXT_LINE', 3, 1],
                'RaisedBy': ['TEXT_LINE', 3, 0],
                'Status': ['COMBO', 5, 0]
                },
        'Benefit':{
                'ID': ['TEXT_LINE_BLOCKED', 0, 0],
                'BusinessID': ['TEXT_BOX', 0, 1],
                'RelatedProject': ['TEXT_LINE_BLOCKED', 0, 2],
                'Title': ['TEXT_LINE', 1, 0],
                'Description': ['TEXT_BOX', 2, 0],
                'Category':['TEXT_LINE', 1, 1],
                'Measurement': ['TEXT_BOX', 2, 1],
                'Baseline': ['TEXT_BOX', 3, 1],
                'ResourseRequirement': ['TEXT_BOX', 2, 2],
                'Responsibility': ['TEXT_BOX', 3, 0]
                },
        'Stakeholder':{
                'ID': ['TEXT_LINE_BLOCKED', 0, 0],
                #'BusinessID': ['TEXT_LINE', 0, 1],
                'RelatedProject': ['TEXT_LINE_BLOCKED', 0, 2],
                'Name': ['TEXT_LINE', 1, 0],
                'Phone': ['TEXT_LINE', 1, 1],
                'EMail': ['TEXT_LINE', 1, 2],
                'Interfaces': ['TEXT_BOX', 2, 1],
                'Interests': ['TEXT_BOX', 2, 1],
                'CurrentRel': ['TEXT_BOX', 2, 1],
                'Birthday': ['TEXT_LINE', 3, 0],
                'InfluenceLevel': ['COMBO', 3, 1],
                'SupportLevel': ['COMBO', 3, 2],
                'InfoFromProject': ['TEXT_BOX', 4, 0],
                'InfoToProject': ['TEXT_BOX', 4, 1],
                'KeyMessages': ['TEXT_BOX', 4, 1]
                }
        }
        


class MainFrame (Toplevel):
        """MainFrame is main callable class for any register"""
        
        
        def __init__ (self, master: object, dbRecordID: int, objectName: str, colorCode: str):
                """MainFrame is main callable class for any register
                
                ==========
                ATTRIBUTES
                ==========
                
                :master: object 
                :dbRecordID: (int) For new item should be -1  
                :objectName: (str) Name of Project Object (register) 

                
                """
                super().__init__(master)
                print ('start toplevel for register card')
                self.config (bg=colorCode)
                self.dbRecordID = dbRecordID
                self.objectName = objectName
                self.colorCode=colorCode
                
                print ('dbRecord:', self.dbRecordID, ' objName:', self.objectName)
                
                self.controlFrame = ControlFrame(self, self.dbRecordID, self.objectName, self.objectName, self.objectName, self.colorCode)
                self.cardFrame = CardFrame(self, self.dbRecordID, self.objectName, self.colorCode)
                self.controlFrame.pack(side = LEFT)
                self.cardFrame.pack(side = LEFT)
                
                if self.dbRecordID!= -1:
                        self.Refresh()
        
        
        def lockFields (self):
                self.cardFrame.lockFields()
                
        
        def unlockFields (self):
                self.cardFrame.unlockFields()
        
        def Refresh (self):
                Keys, Data = controller.RefreshBusinessObject_byID(self.objectName, self.dbRecordID)
                #print ('====')
                #print (Keys)
                #print ('====')
                #print (Data)
                #print ('====')
                self.cardFrame.Refresh(Keys, Data)
        
        def SaveChanges (self):
                _class = controller (self.objectName)
                print (_class)
                pass
        
        
class ControlFrame (Frame):
        """Frame with control elements to switch card to edit mode, edit commentaries, save button"""
        def __init__ (self, master, dbRecordID, objectName, attributeName, attributeLabel, colorCode):
                super().__init__(master)
                self.dbRecordID = dbRecordID
                self.objectName = objectName
                self.attributeName = attributeName
                self.colorCode = colorCode
                self.attributeLabel = attributeLabel
                self.config(bg = colorCode)
                
                self.EditButton = Button(self, text = 'Edit', command = self.attributeEdit)
                self.EditButton.pack()
                #self.EditButton.grid(row = 5, column = 0, columnspan = 2, sticky = W+E)               
                
        def attributeEdit(self):
                print ('AttributeEdit method')
                self.EditButton.destroy()
                self.Label_Commentary = Label(self, text = 'Edit commentary', bg = self.colorCode, anchor = W).grid(row = 6, column = 0, sticky = W+E)
                self.Text_Commentary = Text (self,  width = 30, height = 6).grid(row=7, column = 0, columnspan=2, rowspan = 6)#,sticky = W+E)
                #self.ChangeText.config(state='normal')
                SaveButton = Button(self, text = 'Save changes', command = self.saveChanges).grid(row=14,column = 0, columnspan = 2, sticky = W+E)
                
                self.master.unlockFields()
                
        
                
        def saveChanges(self):
                print ('saveChanges method')
                print(self.ChangeText.get(1.0, END))
                controller.UpdateAttribute(self.objectName, self.attributeName, self.dbRecordID, self.ChangeText.get(1.0, END))
                #self.master.master.Refresh()
                
                self.destroy()                
                
class CardFrame (Frame):
        """Frame with all Register attributes"""
        def __init__ (self, master: object, dbRecordID: int, objectName: str, colorCode: str):
                super().__init__(master)
                self.objectName = objectName
                self.colorCode = colorCode
                self.FrameObjects = []
                self.config (bg=colorCode)
                #LBL = Label (self, text = 'Card').pack()
                print('-->', self.objectName)
                RR_Blocks = REGISTER_BLOCKS[self.objectName]
                self.editableClasses = [AttributeTextBox, AttributeTextLine, AttributeCombo, AttributeTextLineBlocked]
                        
                for item in RR_Blocks:
                        #print (RR_Blocks[item])
                        #print (item)
                        self.FrameObjects.append(AttributeLabel(self, item, colorCode))
                        self.FrameObjects[-1].grid(row = RR_Blocks[item][1]*2, column = RR_Blocks[item][2], sticky=W+E+N+S)
                        if RR_Blocks[item][0] == 'TEXT_BOX':
                                
                                #print (RR_Blocks[item])
                                self.FrameObjects.append(AttributeTextBox(self, self.objectName, item))
                                #print (item, ' grid ', RR_Blocks[item][1], RR_Blocks[item][2])
                                
                                
                        if RR_Blocks[item][0] == 'TEXT_LINE':
                                
                                #print (RR_Blocks[item])
                                self.FrameObjects.append(AttributeTextLine(self, self.objectName, item))                                 
                        
                        if RR_Blocks[item][0] == 'COMBO':
                                
                                #print (RR_Blocks[item])
                                values = controller.GetPredefinedListValues(self.objectName,item)
                                #print (values)
                                self.FrameObjects.append(AttributeCombo(self, 
                                                                   values, 
                                                                   self.objectName, 
                                                                   item))   
                        if RR_Blocks[item][0] == 'TEXT_LINE_BLOCKED':
                                
                                #print (RR_Blocks[item])
                                self.FrameObjects.append(AttributeTextLineBlocked(self, self.objectName, item))
                        
                        if RR_Blocks[item][0] == 'LABEL':
                                self.FrameObjects.append(Label(self, text = item))
                                
                        
                        self.FrameObjects[-1].grid(row = RR_Blocks[item][1]*2+1, column = RR_Blocks[item][2], padx = 14, pady = 3)
                
                self.lockFields()
               
                        
                        
        def lockFields (self):
                for item in self.FrameObjects:
                        if isinstance(item, AttributeTextBox) or isinstance(item, AttributeTextLine) or isinstance(item, AttributeCombo) or isinstance(item, AttributeTextLineBlocked):
                                #print (item, ' is AttributeTextBox')
                                item.lockField() 
                                
                                
        def unlockFields (self):
                for item in self.FrameObjects:
                        if isinstance(item, AttributeTextBox) or isinstance(item, AttributeTextLine) or isinstance(item, AttributeCombo) or isinstance(item, AttributeTextLineBlocked):
                                #print (item, ' is AttributeTextBox')
                                item.unlockField()                                
                
        
        def Refresh (self, Keys, Data):
                for item in self.FrameObjects:
                        if type(item) in self.editableClasses:
                                if Data[0][Keys[item.attributeName]] != None:
                                        item.Refresh(Data[0][Keys[item.attributeName]])
                                else:
                                        pass #item.Refresh('Text')
                                #print (item.attributeName, ' ---> ',Data[0][Keys[item.attributeName]])
        
                
class AttributeLabel (Label):
        
        
        def __init__ (self, master, attributeLabel, colorCode):
                super().__init__(master)
                #print ('label:', attributeLabel)
                self.config (text = attributeLabel, justify = LEFT, bg = colorCode, anchor = W)
                


class AttributeTextBox (Text):
        
        
        def __init__(self, master, objectName, attributeName):
                super().__init__(master)
                self.objectName = objectName
                self.attributeName = attributeName
                self.config(width = 30, height = 9, state="disabled")#, yscrollcommand = scrollbar.set)
                
        def lockField (self):
                self.config(state="disabled")
                
        def unlockField (self):
                self.config(state="normal")          
                
        def Refresh(self, _text):
                #print ('AttributeTextBox refresh:', _text)
                self.unlockField()
                self.delete(1.0 , END)
                self.insert(1.0, _text)
                self.lockField()
        
class AttributeTextLine (Text):
        
        
        def __init__ (self, master, objectName, attributeName):
                super().__init__(master)
                self.objectName = objectName
                self.attributeName = attributeName                
                self.config(width = 30, height = 1, state="disabled")#, yscrollcommand = scrollbar.set)
                
        def lockField (self):
                self.config(state="disabled")
        
        def unlockField (self):
                self.config(state="normal")          
                
        def Refresh (self, _text):
                self.unlockField()
                self.delete(1.0 , END)
                self.insert(1.0, _text)
                self.lockField()
        
class AttributeTextLineBlocked (Text):
        
        
        def __init__ (self, master, objectName, attributeName):
                super().__init__(master)
                self.objectName = objectName
                self.attributeName = attributeName                
                self.config(width = 30, height = 1, state="disabled")#, yscrollcommand = scrollbar.set)    
                
        def lockField (self):
                self.config(state="disabled")
                
        def unlockField (self):
                self.config(state="normal")          
        
        def Refresh (self, _text):
                self.unlockField()
                self.delete(1.0 , END)
                self.insert(1.0, _text)
                self.lockField()              
        
                                
class AttributeCombo (ttk.Combobox):
        
        
        def __init__ (self, master, _values, objectName, attributeName):
                super().__init__(master)
                
                self.config (values = _values)
                self.objectName = objectName
                self.attributeName = attributeName                
                
        def lockField (self):
                self.config(state="disabled")
        
        def unlockField (self):
                self.config(state="normal")                
        
                
        def Refresh (self, _text):
                print ('AttributeCombo refresh')
                self.set(_text)
                
def Main():
        app = Tk()
        MF = MainFrame(app, 2, 'RiskRegister', '#abc4e7')
        MF.Refresh()
        
        #MF = MainFrame(app, -1, 'QualityRegister', '#abc4e7')
        #MF = MainFrame(app, -1, 'Lesson', '#abc4e7')
        
        #MF.pack()
        MF.mainloop()
        


if __name__ == '__main__':
        Main()