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
                
                self.config(width = 70, height = 8, state="disabled", wrap=WORD)#, yscrollcommand = scrollbar.set)
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
        """Plain/tree register """
        def __init__ (self, master, ProjectID: int, ObjectName: str, ArgList, ArgSizeList, treeType = False ):
                """Can be of 2 types: plain and tree. Controled by treeType attribute with default False (plain) value"""
                super().__init__(master)
                #print ("***********************", ObjectName, "treeType: ", treeType)
                
                # Defining own instance attributes
                self.ProjectID = ProjectID
                self.ObjectName = ObjectName
                self.ArgList = ArgList
                #print ('Arglist: ', self.ArgList)
                
                # Setting the TreeView 
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
                
                # Pop-Up Menu settings
                self.popup_menu = Menu (self, tearoff=0)
                self.popup_menu.add_command(label='Add new register item', command = self._addNewRegisterItem)
                self.popup_menu.add_command(label='Delete selected item', command = self._deleteRegisterItem)
                self.bind ('<Button-2>', self._do_popup)
                self.Refresh()
        
        def Refresh (self):
                
                print ('........REFRESH...............')
                print (self.master.__dict__)
                
                # Cleaning the tree from the data 
                for i in self.get_children():
                        self.delete(i)                 
                
                print ('Refresh Object', self)
                print ('Arglist: ', self.ArgList)
                
                # Retrieve the data
                Keys, Data = controller.RefreshBusinessObject(self.ObjectName, self.ProjectID)
                
                
                print ('Object: ', self.ObjectName)
                print ('\n')
                print ('Keys: ', Keys) 
                print ('\n')
                print ('Data: ', Data)
                print ('\n')
                #print ('Columns: ', self('column'))
                
                if 'ParentID' in Keys:
                        isNested = True
                else:
                        isNested = False
                

                
                if isNested == False:
                        # Algorythm without ParentID
                        # Inserting data values one by one (Algorythm for replacement for new nested views)
                        self.column('#0', width = 30)
                        
                        for item in Data:
                                insert_list = []
                                #print ('item: ', item)
                                
                                for arg in self.ArgList:
                                        #print ('Arg ', arg)
                                        insert_list.append(item[Keys[arg]])
                                        #print ('Parent ID index: ', Keys['ParentID'])
                                        
        
                                self.insert('',item[0], text=item[0], values=insert_list)
        
                                #print (insert_list)
                                del insert_list[:]
                else:
                        print ('is Nested')
                        print ('Data initial: \n', Data)
                        self.column('#0', width = 70)
                        self.column('ID', minwidth = 0)
                        self.column('ParentID', minwidth = 0)
                        
                        #Population of core level items
                        remove_list = []
                        for item in Data:
                                insert_list = []
                                
                                print ('\ncheck item:', item)
                                if item[Keys['ParentID']] == 0:
                                        for arg in self.ArgList:
                                                #print (arg, item[Keys[arg]])
                                                insert_list.append(item[Keys[arg]])
                                                
                                                
                                                
                                                
                                        remove_list.append(item)
                                        self.insert('',item[0], iid=item[0], text=item[0], values=insert_list)
                                        
                                        
                                del insert_list[:]
                        
                        print ('\nData from which to remove: \n', Data)
                        print ('\nList for removal\n', remove_list)   
                        
                        for item in remove_list:
                                print ('\nitem from Data to remove: \n', item)
                                Data.remove(item)
                                
                        
                                
                        print ('data after base level has been completed : \n', Data)
                        
                        #Population of nested items
                        #1st loop. Go through remaining Data list
                        print (Keys['ParentID'])
                        indexParentID=Keys['ParentID']
                        print ('Parent ID index:', indexParentID)
                        while len(Data) > 0:
                                print ('Data Len:', len(Data))
                                for item in Data:
                                        insert_list = []
                                        #Parent is retrieved with index 13 in item 
                                        
                                        print (item[indexParentID], 'DataItem Parent------>')
                                        print ('search index:', item[indexParentID], ':', self.exists(item[indexParentID]))
                                        #for child in self.get_children():
                                                #print ('get children:', self.get_children())
                                                #print('tree item:', self.item(child)["values"][0])
                                        if self.exists(item[indexParentID]):
                                                #When match is found
                                                for arg in self.ArgList:
                                                        #print (arg, item[Keys[arg]])
                                                        insert_list.append(item[Keys[arg]])       
                                                #print ('item from Data to remove: ', item)        
                                                self.insert(item[indexParentID] ,item[0], iid=item[0], text=item[0], values=insert_list)
                                                Data.remove(item)                                                
                                                        
                                                
                                        #print ('------<')
                                        
                                        del insert_list[:]
                                        #print ('Data after cycle:', Data)
                                        #print ()
                                
                                
                        
                        
                                        
                        
                
                
                
                """
                insert(parent, index, iid=None, **kw)
                Creates a new item and returns the item identifier of the newly created item.
                
                parent is the item ID of the parent item, or the empty string to create a new top-level item. index is an integer, or the value “end”, 
                specifying where in the list of parent’s children to insert the new item. If index is less than or equal to zero, the new node is inserted at the beginning; 
                if index is greater than or equal to the current number of children, it is inserted at the end. If iid is specified, it is used as the item identifier; 
                iid must not already exist in the tree. Otherwise, a new unique identifier is generated.
                """

        def OnDoubleClick(self, event):
                item = self.identify('item', event.x, event.y)
                bdRecordID = self.item(item, 'text')  
                
                if item!="":
                        registerItemCard = vf_Top_RegisterCard.MainFrame(self, bdRecordID, self.ObjectName,  'gray')
                        registerItemCard.mainloop()
                
                
        def OnClick(self, event):
                #print ('1 Click')
                item = self.identify('item', event.x, event.y)
                bdRecordID = self.item(item, 'text')                
                #print (self)
                #print (self.master)
                #print (self.master.__dict__)
                if item!="":
                        self.master.Refresh(bdRecordID)
                
        
        def _addNewRegisterItem (self):
                
                controller.appendProjectObject(self.ObjectName, self.ProjectID)
                self._registerRefresh()
                
        def _deleteRegisterItem(self):

                curItem = self.focus()
                dbRecordID = self.item(curItem, 'text') 
                if dbRecordID != '':
                        controller.deleteProjectObject(self.ObjectName, dbRecordID)
                        self.Refresh()
                
                
        def _do_popup (self, event):
                try:
                        self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
                finally:
                        # make sure to release the grab (Tk 8.0a1 only)
                        self.popup_menu.grab_release()   
        
        def _registerRefresh (self):
                self.Refresh()           
        
if __name__ == '__main__':
        help (Label)