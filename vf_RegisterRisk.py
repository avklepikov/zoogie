from tkinter import *
import CustomizedElements
import controller

class MainFrame (Frame):
        def __init__ (self, master, dbProjectRecordID ,colorCode):
                super().__init__(master)
                self.config (bg = colorCode)
                self.dbProjectRecordID = dbProjectRecordID
                #self.label = Label(self, text = 'label')
                #self.label.pack()
                
                self.Register = CustomizedElements.RegisterList(self, 
                                                                self.dbProjectRecordID,
                                                                'RiskRegister', 
                                                                ['BusinessID', 'Title', 'Category', 'Probability', 'RaisedDate', 'ResponseCategory', 'Owner', 'Actionee', 'Status'],
                                                                [80, 250, 120,120, 120, 120, 120, 120, 80])
                
                self.Register.pack()
                
                self.BD = Breakdown(self, colorCode)
                self.BD.pack()
                
        def Refresh (self, dbRecordID):
                self.BD.Refresh(dbRecordID)


class Breakdown (Frame):
        def __init__ (self, master, colorCode):
                super().__init__(master)
                self.className = 'RiskRegister'
                #dbRecordID = '1'
                #colorCode = 'gray'
                
                self.Attr1 = CustomizedElements.AttributeBlockFrame(self, -1, self.className, 'Title', 'Title', colorCode)
                self.Attr2 = CustomizedElements.AttributeBlockFrame(self, -1, self.className, 'Description', 'Description', colorCode)
                self.Attr3 = CustomizedElements.AttributeBlockFrame(self, -1, self.className, 'Impact', 'Impact', colorCode)
                self.Attr4 = CustomizedElements.AttributeBlockFrame(self, -1, self.className, 'Response', 'Response', colorCode)

                
        
                self.Attr1.grid(row=0, column = 0)
                self.Attr2.grid(row=1, column = 0)
                self.Attr3.grid(row=0, column = 1)
                self.Attr4.grid(row=1, column = 1)

                
                self.attributesObjects = (self.Attr1, 
                                          self.Attr2, 
                                          self.Attr3, 
                                          self.Attr4)
                
                #self.BreakDownAttrList = [self.Attr1, self.Attr2, self.Attr3, self.Attr4]
                #self.Button = Button(self, text = 'Refresh', command = self.Refresh)
                #self.Button.grid (row=4, column = 0)          
        
        def Refresh (self, dbRecordID):

                Keys, Data = controller.RefreshBusinessObject_byID(self.className, dbRecordID)

                
                for item in self.attributesObjects:
                        #print (item.attributeName)
                        item.valueUpdate(Data[0][Keys[item.attributeName]])
                        item.dbRecordID = Data[0][Keys['ID']]
        
                
def Main():
        app = Tk()
        block = MainFrame(app)
        block.pack()
        app.mainloop()
        
if __name__=='__main__':
        Main()