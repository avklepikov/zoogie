from tkinter import *
import CustomizedElements

class MainFrame (Frame):
        def __init__ (self, master, colorCode):
                super().__init__(master)
                self.config (bg = colorCode)
                self.ProjectID = 1
                #self.label = Label(self, text = 'label')
                #self.label.pack()
                
                self.Register = CustomizedElements.RegisterList(self, 
                                                                self.ProjectID,
                                                                'Issue', 
                                                                ['BusinessID', 'Title', 'Category', 'Priority', 'DateRaised', 'RaisedBy', 'Severity', 'ClosureDate', 'Status'],
                                                                [80, 250, 120, 120, 120, 120, 120, 120, 80])
                
                self.Register.pack()
                
                self.BD = Breakdown(self, colorCode)
                self.BD.pack()
                
                


class Breakdown (Frame):
        def __init__ (self, master, colorCode):
                super().__init__(master)
                self.className = 'RiskRegister'
                dbRecordID = '1'
                #colorCode = 'gray'
                
                self.Attr1 = CustomizedElements.AttributeBlockFrame(self, dbRecordID, self.className, 'Title', 'Title', colorCode)
                self.Attr2 = CustomizedElements.AttributeBlockFrame(self, dbRecordID, self.className, 'Description', 'Description', colorCode)


                
        
                self.Attr1.grid(row=0, column = 0)
                self.Attr2.grid(row=0, column = 1)


                
                self.attributesObjects = (self.Attr1, 
                                          self.Attr2)
                
                #self.Button = Button(self, text = 'Refresh', command = self.Refresh)
                #self.Button.grid (row=4, column = 0)          
                
def Main():
        app = Tk()
        block = MainFrame(app)
        block.pack()
        app.mainloop()
        
if __name__=='__main__':
        Main()