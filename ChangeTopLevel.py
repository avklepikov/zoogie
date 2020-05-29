from tkinter import *
from tkinter import ttk
import controller

class ChangeTopLevel (Toplevel):
        def __init__(self, master: object, dbRecordID: int, objectName: str, attributeName: str, attributeLabel: str, attributeValue: str, colorCode: str):
                #print ('toplevel module:')
                super().__init__(master)
                self.config (bg = colorCode)
                self.title ('Zoogie - edit window')
                
                # Set attributes
                self.dbRecordID = dbRecordID
                self.objectName = objectName
                self.attributeName = attributeName
                self.colorCode = colorCode
                
                #Visualization
                
                
                
                
                self.Label_ObjectName_Label = Label (self, text = 'Artifact Name:', bg = colorCode, justify = LEFT, anchor = W).grid(row = 1, column = 0, sticky = W+E)
                self.Label_ObjectName_Value = Label (self, text = self.objectName, bg = colorCode, justify = LEFT, anchor = W).grid(row = 1, column = 1, sticky = W+E)  
                self.Label_ObjectName_Label = Label (self, text = 'Artifact Field:', bg = colorCode, justify = LEFT, anchor = W).grid(row = 2, column = 0, sticky = W+E)
                self.Label_ObjectName_Value = Label (self, text = self.attributeName, bg = colorCode, justify = LEFT, anchor = W).grid(row = 2, column = 1, sticky = W+E)                  
                self.Label_dbRecordID_Label = Label (self, text = 'Database Record ID:', bg = colorCode, justify = LEFT, anchor = W).grid(row = 3, column = 0, sticky = W+E)
                self.Label_dbRecordID_Value = Label (self, text = self.dbRecordID, bg = colorCode, justify = LEFT, anchor = W).grid(row = 3, column = 1, sticky = W+E)                
                
                
                
                self.ChangeLabel = Label(self)
                self.ChangeLabel.config (text = attributeLabel, bg = colorCode)
                self.ChangeLabel.grid(row = 0, column = 2)
                
                self.ChangeText = Text(self)
                self.ChangeText.insert (1.0, attributeValue)
                self.ChangeText.config (width = 150, height = 35, state="disabled", wrap=WORD)
                self.ChangeText.grid(row = 1, column =2, rowspan = 35)
                
                
                self.EditButton = Button(self, text = 'Edit', command = self.attributeEdit)
                self.EditButton.grid(row = 5, column = 0, columnspan = 2, sticky = W+E)
        
        def attributeEdit(self):
                print ('AttributeEdit method')
                self.EditButton.destroy()
                self.Label_Commentary = Label(self, text = 'Edit commentary', bg = self.colorCode, anchor = W).grid(row = 6, column = 0, sticky = W+E)
                self.Text_Commentary = Text (self,  width = 30, height = 6).grid(row=7, column = 0, columnspan=2, rowspan = 6)#,sticky = W+E)
                self.ChangeText.config(state='normal')
                SaveButton = Button(self, text = 'Save changes', command = self.saveChanges).grid(row=14,column = 0, columnspan = 2, sticky = W+E)
                
        def saveChanges(self):
                #print ('saveChanges method')
                #print(self.ChangeText.get(1.0, END))
                controller.UpdateAttribute(self.objectName, self.attributeName, self.dbRecordID, self.ChangeText.get(1.0, END+"-1c"))
                #self.master.master.Refresh()
                
                self.destroy()
                
                # pass
                
                #print (self.dbRecordID, self.objectName, self.attributeName, attributeLabel, attributeValue)
        
if __name__ == '__main__':
        _App = Tk()
        _Window = ChangeTopLevel(_App, 1,'Obj Name', 'attr name', 'Label', 'This is a text', 'gray')
        _App.mainloop()