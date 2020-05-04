from tkinter import *
from tkinter import ttk
import BC_Frame



class Application (Tk):
        def __init__(self):
                super().__init__()
                self.title ('Application')

                Frame1 = BC_Frame.MainFrame (self) 
                Frame1.pack()


App = Application()
#print (App.__dict__)
App.mainloop()


        
