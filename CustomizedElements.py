from tkinter import *
from tkinter import ttk
import ChangeTopLevel
import controller

class AttributeBlockFrame (Frame):
        """Block for visualization of Object class attribute
        
        ===========
        DESCRIPTION
        ===========
        
        AttributeBlockFrame represents a customized widget which realizes Project Class Attribute visualization 
        with explicit link to class and attribute.
        
        ===========
        ATTRIBUTES:
        ===========
        
            :master: (obj) master widget 
            :dbRecordID: (int) database table record ID 
            :objectName: (str) Model Project Class name
            :attributeName: (str) ProjectClass Atribute
            :attributeLabel: (str) Viewable name of the attribute
            :colorCode: (str) color schema code
            
        ===========
        METHODS
        ===========
        
            :valueUpdate (newValue): updates visualized value of the attribute
            
                passes new attribute value to underlying text box
            
        """
        def __init__(self, master: object, dbRecordID: int, objectName: str, attributeName: str, attributeLabel: str, colorCode: str):  

                super().__init__(master)
                self.dbRecordID = dbRecordID
                self.objectName = objectName
                self.attributeName = attributeName
                self.attributeLabel = attributeLabel
                self.colorCode = colorCode
                self.config (bg = colorCode,padx=10, pady = 10)
                self.AttributeLabel = AttributeLabel(self, attributeLabel, colorCode)
                self.AttributeValue = AttributeValue(self)
                
                self.AttributeLabel.grid(row=0, column = 0, sticky=W+E+N+S)
                self.AttributeValue.grid(row=1, column = 0, sticky=W+E+N+S)
        
                
        def valueUpdate (self, newValue):
                #print ('block valueUpdate')
                #help (self.AttributeValue)
                self.AttributeValue.valueUpdate (newValue)
        
    

class AttributeLabel (Label):
        def __init__(self, master, attributeLabel, colorCode):
                super().__init__(master)
                self.config (text = attributeLabel, justify = LEFT, bg = colorCode, anchor = W)
        
                
        

class AttributeValue (Text):
        """Text widget to visualize attribute value
        
        ==============
        METHODS
        ==============
        
        :valueUpdate (new value: str): fast method to update attribute value in the widget 
        
        """
        def __init__(self, master):
                super().__init__(master)
                #self.insert (1.0, 'Long text')
                self.config(width = 85, height = 10, state="disabled")
                self.bind ("<Double-1>", self.OnDoubleClick2)

        def OnDoubleClick2(self, Event):
                print ('double click')
                print (self.master.attributeName)
                #print ('label: ', self.master.AttributeLabel)
                top = ChangeTopLevel.ChangeTopLevel(self, 
                                                    self.master.dbRecordID, 
                                                    self.master.objectName, 
                                                    self.master.attributeName,
                                                    self.master.attributeLabel,
                                                    Event.widget.get (1.0, END),
                                                    self.master.colorCode)
                top.mainloop()
        
        def valueUpdate(self, newValue):
                        
                self.config(state="normal")
                self.delete(1.0, END)
                self.insert(1.0, newValue)
                self.config (state="disabled")        




#class ListFrame(Frame):
        #def __init__ (self):
                #super().__init__(master)
                #pass
        
        
#class ListTree (ttk.Treeview):
        #def __init__ (self):
                #super().__init__(master)
                #pass
        





class RegisterList (ttk.Treeview):
        def __init__ (self, master, ProjectID: int, ObjectName: str, ArgList, ArgSizeList ):
                super().__init__(master)
                #print (ArgList)
                self.ProjectID = ProjectID
                self.ObjectName = ObjectName
                self.ArgList = ArgList
                self['columns'] = (ArgList)
                self.heading ('#0', text = 'Code', anchor = 'w')
                self.column('#0', width = 30)
                self.config(height = 20)
                self.bind("<Button-1>", self.OnClick)
                self.bind("<Double-1>", self.OnDoubleClick)
                i=0
                for Arg in ArgList:
                        
                        self.heading (ArgList[i], text = ArgList[i], anchor = 'w')
                        self.column(ArgList[i], width = ArgSizeList[i])
                        i+=1
                
                self.pack()
                self.Refresh()
        
        def Refresh (self):
                
                print ('.......................')
                #print (self.master.__dict__)
                
                Keys, Data = controller.RefreshBusinessObject(self.ObjectName, self.ProjectID)
                #print ('Object: ', self.ObjectName)
                #print ('\n')
                #print ('Keys:', Keys) 
                #print ('\n')
                #print ('Data:', Data)
                #print ('\n')
                #print (self('columns'))

                for item in Data:
                        insert_list = []
                        print ('item: ', item)
                        
                        for arg in self.ArgList:
                                print ('Arg ', arg)
                                insert_list.append(item[Keys[arg]])
                        
                        
                        self.insert('',item[0], text=item[0], values=insert_list)

                        print (insert_list)
                        del insert_list[:]
                #pass

        def OnDoubleClick(self, event):
                print ('2-click')
                
                pass
        def OnClick(self, event):
                print ('1 Click')
                item = self.identify('item', event.x, event.y)
                bdRecordID = self.item(item, 'text')                
                print (self)
                print (self.master)
                print (self.master.__dict__)
                self.master.Refresh(bdRecordID)
                pass
        
if __name__ == '__main__':
        help (Label)