from tkinter import *
from tkinter import ttk
import ChangeTopLevel
import controller
import logging
import vf_Top_RegisterCard

    
                
                

class AttributeBlockFrame (Frame):
        """Block for visualization of Object class attribute
        
        ===========
        DESCRIPTION
        ===========
        
        AttributeBlockFrame represents a customized widget which realizes Project Class Attribute visualization 
        with explicit link to class and attribute.
        This widget has a functionality to update each attribute value individually with double-click on value textbox
        
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
                #self.configure ('Style1', background = 'white') #,padx=10, pady = 10)
                
                self.AttributeLabel = AttributeLabel(self, attributeLabel, colorCode)
                
                scrollbar = Scrollbar(self)
                scrollbar.grid(row=1, column = 1, sticky=W+E+N+S) #.pack( side = RIGHT, fill = Y )                
                
                
                self.AttributeValue = AttributeValue(self)
                self.AttributeValue.config (yscrollcommand = scrollbar.set)
                scrollbar.config(command=self.AttributeValue.yview)
                
                self.AttributeLabel.grid(row=0, column = 0, sticky=W+E+N+S)
                self.AttributeValue.grid(row=1, column = 0, sticky=W+E+N+S)
        
                
        def valueUpdate (self, newValue):
                #print ('block valueUpdate')
                #help (self.AttributeValue)
                logging.info (f' CUSTOMIZED ELEMENT REFRESH - for {self.objectName} : {self.attributeName}')
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
                #scrollbar = Scrollbar(self)
                #scrollbar.pack( side = RIGHT, fill = Y )
                
                self.config(width = 75, height = 9, state="disabled", wrap=WORD)#, yscrollcommand = scrollbar.set)
                self.bind ("<Double-1>", self.OnDoubleClick2)

        def OnDoubleClick2(self, Event):
                #print ('double click')
                #print (self.master.attributeName)
                #print ('label: ', self.master.AttributeLabel)
                top = ChangeTopLevel.ChangeTopLevel(self, 
                                                    self.master.dbRecordID, 
                                                    self.master.objectName, 
                                                    self.master.attributeName,
                                                    self.master.attributeLabel,
                                                    Event.widget.get (1.0, END+"-1c"),
                                                    self.master.colorCode)
                top.mainloop()
        
        def valueUpdate(self, newValue):
                        
                if newValue != None:
                        self.config(state="normal")
                        self.delete(1.0, END)
                        self.insert(1.0, newValue)
                        self.config (state="disabled") 
                else:
                        #print ('please update Customized Elements for Empty insert')
                        pass




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
                
                self.ProjectID = ProjectID
                self.ObjectName = ObjectName
                self.ArgList = ArgList
                #print ('Arglist: ', self.ArgList)
                self['columns'] = (ArgList)
                self.heading ('#0', text = 'Code', anchor = 'w')
                self.column('#0', width = 30)
                self.config(height = 15)
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
                
                #print ('.......................')
                #print (self.master.__dict__)
                for i in self.get_children():
                        self.delete(i)                 
                
                #print ('Refresh Object', self)
                #print ('Arglist: ', self.ArgList)
                Keys, Data = controller.RefreshBusinessObject(self.ObjectName, self.ProjectID)
                #print ('Object: ', self.ObjectName)
                #print ('\n')
                #print ('Keys: ', Keys) 
                #print ('\n')
                #print ('Data: ', Data)
                #print ('\n')
                #print ('Columns: ', self('column'))

                for item in Data:
                        insert_list = []
                        #print ('item: ', item)
                        
                        for arg in self.ArgList:
                                #print ('Arg ', arg)
                                insert_list.append(item[Keys[arg]])
                        
                        
                        self.insert('',item[0], text=item[0], values=insert_list)

                        #print (insert_list)
                        del insert_list[:]
                #pass

        def OnDoubleClick(self, event):
                item = self.identify('item', event.x, event.y)
                bdRecordID = self.item(item, 'text')      
                #iskRegisterTopWindow = Toplevel()
                #print ('Toplevel Risk: ', self.ObjectName, item)
                registerItemCard = vf_Top_RegisterCard.MainFrame(self, bdRecordID, self.ObjectName,  'gray')
                registerItemCard.mainloop()
                
                pass
        def OnClick(self, event):
                #print ('1 Click')
                item = self.identify('item', event.x, event.y)
                bdRecordID = self.item(item, 'text')                
                #print (self)
                #print (self.master)
                #print (self.master.__dict__)
                self.master.Refresh(bdRecordID)
                pass
        
if __name__ == '__main__':
        help (Label)