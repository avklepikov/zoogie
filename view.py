"""GUI Part of Zoogie application

TODO [ ] : Substitute standard Text widgets with new custom AppText
TODO [x] : Backgroud Colour across Frames
TODO [ ] : Reduce space to the left from text widgets 
TODO [ ] : Change from _ActiveProject to _ID in OnDoubleClick methods - cosmetics of the code
TODO [ ] : Implement _TextBoxSizes


"""

#IMPORT GLOBALS 
from tkinter import * 
from tkinter import ttk
import logging

import controller

import vf_BusinessCase
import vf_QualityApproach
import vf_RiskApproach1
import vf_RiskApproach2
import vf_ChangeApproach
import vf_CommunicationApproach
import vf_RegisterRisk
import vf_RegisterChange
import vf_RegisterProjectProduct
import vf_Register
import CustomizedElements

_activeProject = None

_BGC = '#abc4e7'
"""Background colour for Frames 
use https://www.color-hex.com/ to find nice colour code"""

_TextBoxSizes = {'small' : 1,
                 'medium' : 12,
                 'big' : 36}
"""Parameters for Heights of customized text boxes AppTextBox"""




# Custom Widgets
class AppText (Text):
        """Custom 1-line Text widget with simplified update method to substiture Delete+Instert + Formatting"""
        def __init__(self, *args, **kwargs):
                super().__init__(*args,**kwargs)
                self.config(width = 60, height = 1, state="disabled")
                #self.bind ("<Double-1>", self.OnDoubleClick2)
        
        def TextUpdate(self, NewText):
                
                self.config(state="normal")
                self.delete(1.0, END)
                self.insert(1.0, NewText)
                self.config (state="disabled")
                
        #def OnDoubleClick2 (self, Event):
   


class AppTextBox (Text):
        """Custom Text widget with simplified update method to substiture Delete+Instert + Formatting + mapping to Class name and Attributes"""
        def __init__(self, master, __class, __attribute, *args, **kwargs):
            
                super().__init__(master, *args,**kwargs)

                self._class = __class
                self._attribute = __attribute
                self.config(width = 60, height = 12,state="disabled")
                self.bind ("<Double-1>", self.OnDoubleClick2)

        
        def TextUpdate(self, NewText):
                self.config(state="normal")
                self.delete(1.0, END)
                self.insert(1.0, NewText)  
                self.config (state="disabled")
                
        def OnDoubleClick2 (self, Event):
                logging.info ('OnDoubleClick2 is aptured')
                global _activeProject

                top = Toplevel(self)
                top.config(bg = _BGC)
                #relatedProjectID = Label (top, text = _activeProject, bg = _BGC).grid(row=0, column = 0)
                
                self.relatedClass = Label(top, text = Event.widget._class, bg = _BGC).grid(row=0, column = 0, sticky=W+E+N+S)
                self.relatedAttribute = Label(top, text = Event.widget._attribute, bg = _BGC).grid(row = 1, column = 0, sticky=W+E+N+S)
                self.editableTextBox = Text(top, height = 30)
                self.editableTextBox.insert (1.0, Event.widget.get (1.0, END))
                self.editableTextBox.grid(row=2, column =0, columnspan=2)
                
                self.CommentaryLabel = Label(top, text = 'Change related commentaries:', bg = _BGC).grid(row=3, column =0)
                self.CommentaryText = Text(top, height = 3).grid(row=4, column =0)
                
                self.buttonEdit = Button(top, text = 'Edit', command = abc).grid(row=5, column =0, sticky=W+E+N+S)
                self.buttonEdit = Button(top, text = 'Save Changes', command = self.SaveChangaes).grid(row=6, column =0, sticky=W+E+N+S)
                self.buttonEdit = Button(top, text = 'Close without changes', command = abc).grid(row=7, column =0, sticky=W+E+N+S)
                
                
                
                top.mainloop()
                
        def SaveChangaes (self):
                #logging.info ('VIEW SAVING NEW ATTR VALUE')
                __class =  self._class
                __attr = self._attribute
                __value = self.editableTextBox.get (1.0, END)
                controller.UpdateAttribute(__class, __attr, _activeProject, __value)



def abc():  #NOT USED TextBox Click event General. To accept TextBox Value, class and attribute names to run SQL
        print ("ABC")

# Building GUI                
class ProjectApp (Tk):
        def __init__ (self):
                super().__init__()
                self._frame = None
                self.switch_frame(mainFrame_Portfolio)
               
                
        def switch_frame(self, frame_class):
                new_frame = frame_class(self)
                if self._frame is not None:
                        self._frame.destroy()
                self._frame = new_frame
                self._frame.pack()
                
             
                
                
#  ---------------- PORTFOLIO MAIN FRAME -------------------                
class mainFrame_Portfolio(Frame):
        def __init__ (self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                self.master=master
                portfolio = PortfolioTree(self)
                portfolio.pack()

                
class PortfolioTree (ttk.Treeview):
        def __init__ (self, master):
                super().__init__(master)
                self['columns'] = ('BusinessCode', 'ProjectName')
                #self.width = 100
                #self.height = 200
                self.master=master
                self.heading ('#0', text = 'Code', anchor = 'w')
                self.heading ('BusinessCode', text = 'Business Code', anchor = 'w')
                self.heading ('ProjectName', text = 'Project Name', anchor = 'w')
                self.column('#0', width = 60)
                self.column('BusinessCode', width = 100)            
                self.column('ProjectName', width = 250)
                
                self.pack()
                self.Refresh()
                self.bind("<Double-1>", self.OnDoubleClick)

                
        def Refresh (self):
                logging.info('VIEW PortfolioTree.Refresh has been activated')
                Data = controller.RefreshPortfolioList()
                for item in Data:
                        #print (item[1:2])
                        self.insert('',item[0], text=item[0], values=[item[2],item[1]])
                        
        def OnDoubleClick(self, event):
                global _activeProject
                item = self.identify('item', event.x, event.y)
                _activeProject = self.item(item, 'text')
                #print (_activeProject)
                self.master.master.switch_frame(mainFrame_Project)
                

                
                
#  -----------------PROJECT MAIN FRAME ---------------------                
class mainFrame_Project(Frame):
        def __init__ (self, master):
                super().__init__(master)
                self.ProjectPack = controller.GetProjectPack(_activeProject)
                print(self.ProjectPack)
                self.config (bg = _BGC)
                project_head = ProjectHead(self)
                tab_control = ProjectTabControl(self)
                project_head.pack()
                tab_control.pack()
                
                
class ProjectHead(Frame):
        def __init__ (self, master):
                super().__init__(master)
                
        
                self.Label_ProjectID = Label(self, text = 'Project ID:')
                self.Entry_ProjectID = Entry(self)
                
                self.Label_ProjectBusinessID = Label(self, text = 'Project Business ID:')
                self.Entry_ProjectBusinessID = Entry(self)                
                
                self.Label_ProjectName = Label(self, text = 'Project Name:')
                self.Entry_ProjectName = Entry(self)   
                
                self.Label_ProjectStatus = Label(self, text = 'Status:')
                self.Entry_ProjectStatus = Entry(self)                   
                
                
                
                self.Label_ProjectID.pack(side=LEFT)
                self.Entry_ProjectID.pack(side=LEFT)
                self.Label_ProjectBusinessID.pack(side=LEFT)
                self.Entry_ProjectBusinessID.pack(side=LEFT)
                self.Label_ProjectName.pack(side=LEFT)
                self.Entry_ProjectName.pack(side=LEFT)
                self.Label_ProjectStatus.pack(side=LEFT)
                self.Entry_ProjectStatus.pack(side=LEFT)
                
                self.Refresh()
                
        def Refresh(self):
                global _activeProject
                logging.info ('VIEW Starting Project Head Refresh')
                


                self.Entry_ProjectID.insert(0, self.master.ProjectPack.Project.ID)
                if self.master.ProjectPack.Project.BusinessID != None:
                        self.Entry_ProjectBusinessID.insert(0, self.master.ProjectPack.Project.BusinessID)   
                self.Entry_ProjectName.insert(0, self.master.ProjectPack.Project.Project)
                self.Entry_ProjectStatus.insert(0,self.master.ProjectPack.Project.TechStatus )
                
                logging.info ('VIEW Finished Project Head Refresh')
                
class ProjectTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                frame_BusinessCase = Frame_BusinessCase(self)
                frame_BusinessCase.config(bg = _BGC)
                frame_Organization = Frame_Organization(self)
                frame_Organization.config(bg = _BGC)
                frame_Plan = Frame_Plan(self)
                frame_Plan.config(bg = _BGC)
                frame_Quality = Frame_Quality(self)
                frame_Quality.config(bg = _BGC)
                frame_Risk = Frame_Risk(self)
                frame_Risk.config(bg = _BGC)
                frame_Change = Frame_Change(self)
                frame_Change.config(bg = _BGC)
                frame_Communication = Frame_Communication(self)
                frame_Communication.config(bg = _BGC)
                frame_Lessons = vf_Register.MainFrame(self, self.master.ProjectPack.Project.ID, 'Lesson', _BGC)

                
                frame_DailyLog = Frame_DailyLog(self)
                frame_DailyLog.config(bg = _BGC)
                frame_Dashboard = Frame_DashBoard(self)
                frame_Dashboard.config(bg = _BGC)
                frame_Meetings = Frame_Meetings(self)
                frame_Meetings.config(bg = _BGC)
                
                self.add (frame_BusinessCase, text = 'Business Case')
                self.add (frame_Organization, text = 'Organization')
                self.add (frame_Plan, text = 'Plan')
                self.add (frame_Quality, text = 'Quality')
                self.add (frame_Risk, text = 'Risk')
                self.add (frame_Change, text = 'Change')
                self.add (frame_Communication, text = 'Communication')
                self.add (frame_Lessons, text = 'Lessons')
                self.add (frame_DailyLog, text = 'Daily Log')
                self.add (frame_Dashboard, text = 'DashBoard')
                self.add (frame_Meetings, text = 'Meetings')
                

class Frame_BusinessCase (Frame):
        def __init__ (self, master):
                super().__init__(master)
                self.config (bg = _BGC)                           # no effect
                tab_control = BusinessCaseTabControl(self)
                tab_control.pack()

class Frame_Organization (Frame):
        def __init__ (self, master):
                super().__init__(master)
                teamRegister = vf_Register.MainFrame(self, self.master.master.ProjectPack.Project.ID, 'Team', _BGC)
                teamRegister.pack()
                

class Frame_Plan (Frame):
        def __init__ (self, master):
                super().__init__(master)
                tab_control = PlanTabControl(self)
                tab_control.pack()

class Frame_Quality (Frame):
        def __init__ (self, master):
                super().__init__(master)
                tab_control = QualityTabControl(self)
                tab_control.pack()                

class Frame_Risk (Frame):
        def __init__ (self, master):
                super().__init__(master)
                tab_control = RiskTabControl(self)
                tab_control.pack()
                
class Frame_Change (Frame):
        def __init__ (self, master):
                super().__init__(master)
                tab_control = ChangeTabControl(self)
                tab_control.pack()                

class Frame_Communication (Frame):
        def __init__ (self, master):
                super().__init__(master)
                tab_control = CommunicationTabControl(self)
                tab_control.pack()                

class Frame_DailyLog (Frame):
        def __init__ (self, master):
                super().__init__(master)

class Frame_DashBoard (Frame):
        def __init__ (self, master):
                super().__init__(master)

class Frame_Meetings (Frame):
        def __init__ (self, master):
                super().__init__(master)

class PlanTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                stages = vf_Register.MainFrame(self,self.master.master.master.ProjectPack.Project.ID, 'Stage', _BGC)
                self.add(stages, text = 'Project Stages')
                
# TAB   :  Business Case             
class BusinessCaseTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                
                Mandate = subFrame_Mandate(self)
                
                BusinessCase = vf_BusinessCase.MainFrame(self, self.master.master.master.ProjectPack.BusinessCase.ID)
                BusinessCase.Refresh()
                
                #Benefits = subFrame_Benefits(self)
                Benefits = vf_Register.MainFrame(self,self.master.master.master.ProjectPack.Project.ID, 'Benefit', _BGC)
                              
                ProjectProduct = vf_RegisterProjectProduct.MainFrame (self, self.master.master.master.ProjectPack.Project.ID, _BGC)
                
                
                self.add(Mandate, text = 'Mandate')
                self.add(BusinessCase, text = 'Business Case')
                self.add(Benefits, text = 'Benefits')
                self.add(ProjectProduct, text = 'Project Product')
        

class subFrame_Mandate(Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                
                
                mandate = CustomizedElements.AttributeBlockFrame(self, self.master.master.master.master.ProjectPack.Mandate.ID, 'Mandate', 'Mandate', 'Mandate text', _BGC)
                
                mandate.AttributeValue.config(width = 130, height = 30)
                mandate.pack()
                mandate.valueUpdate(self.master.master.master.master.ProjectPack.Mandate.Mandate)
                
                
                
# TAB   :   Organization
class subFrame_Team(Frame):
        def __init__ (self, master):
                super().__init__(master)  
                self.config (bg = _BGC)
                
class subFrame_Roles(Frame):
        def __init__ (self, master):
                super().__init__(master) 
                self.config (bg = _BGC)

# TAB   :   Plan
class subFrame_Products(Frame):
        def __init__ (self, master):
                super().__init__(master)  
                self.config (bg = _BGC)
                
class subFrame_WBS(Frame):
        def __init__ (self, master):
                super().__init__(master)  
                self.config (bg = _BGC)
# TAB   :   Risk
class RiskTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                
                RiskApproach1 = vf_RiskApproach1.MainFrame(self, self.master.master.master.ProjectPack.RiskApproach.ID)
                RiskApproach1.Refresh()
                
                
                RiskApproach2 = vf_RiskApproach2.MainFrame(self, self.master.master.master.ProjectPack.RiskApproach.ID)
                RiskApproach2.Refresh()
                
                
                RiskRegister = vf_RegisterRisk.MainFrame(self, self.master.master.master.ProjectPack.Project.ID, _BGC)  #<--- TODO CHECK
                
                
                self.add(RiskApproach1, text = 'Risk Approach (1)')
                self.add(RiskApproach2, text = 'Risk Approach (2)')
                self.add(RiskRegister, text = 'Risk Register')
                



# TAB   :   Change
class ChangeTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                
                
                
                
                ChangeApproach = vf_ChangeApproach.MainFrame(self, self.master.master.master.ProjectPack.ChangeApproach.ID)
                
                
                
                ChangeApproach.Refresh()
                
                
                ChangeRegister = vf_RegisterChange.MainFrame (self, self.master.master.master.ProjectPack.Project.ID, _BGC) # <- TODO Check
                self.add(ChangeApproach, text = 'Change Approach')
                self.add(ChangeRegister, text = 'Issue Register')
                
              
# TAB   :   Communication
class CommunicationTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                
                CommunicationApproach = vf_CommunicationApproach.MainFrame(self, self.master.master.master.ProjectPack.CommunicationApproach.ID)
                CommunicationApproach.Refresh()
                self.add(CommunicationApproach, text = 'Communication Approach')
                
                stakeholders = vf_Register.MainFrame(self, self.master.master.master.ProjectPack.Project.ID, 'Stakeholder', _BGC)
                self.add(stakeholders, text = 'Stakeholders')
                
                

# TAB   :   Quality
class QualityTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                
                QualityApproach = vf_QualityApproach.MainFrame(self, self.master.master.master.ProjectPack.QualityApproach.ID)
                QualityApproach.Refresh()
                self.add(QualityApproach, text = 'Quality Approach')
                
                QualityRegister = vf_Register.MainFrame(self, self.master.master.master.ProjectPack.Project.ID, 'QualityRegister', _BGC)
                self.add(QualityRegister, text = 'Quality Register')
                
                
                
                
def Main ():
        logging.basicConfig(filename='logging.txt',level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M', filemode='w')
        X = ProjectApp()
        X.mainloop()


if __name__ == '__main__':
        Main()
        
