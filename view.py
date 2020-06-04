"""GUI Part of Zoogie application


"""

#IMPORT GLOBALS 
from tkinter import * 
from tkinter import ttk
import logging

#IMPORT OWN MODULES:
import controller
import vf_RiskApproach1  # I do not know how to split them in vf_Register
import vf_RiskApproach2  # I do not know how to split them in vf_Register 


import vf_Register
import CustomizedElements

_activeProject = None

_BGC = '#abc4e7'
"""Background colour for Frames 
use https://www.color-hex.com/ to find nice colour code"""

#_TextBoxSizes = {'small' : 1,
                 #'medium' : 12,
                 #'big' : 36}
"""Parameters for Heights of customized text boxes AppTextBox
To delete as unused?"""




# Custom Widgets
#class AppText (Text):
        #"""Custom 1-line Text widget with simplified update method to substiture Delete+Instert + Formatting"""
        #def __init__(self, *args, **kwargs):
                #super().__init__(*args,**kwargs)
                #self.config(width = 60, height = 1, state="disabled")
                
        
        #def TextUpdate(self, NewText):
                
                #self.config(state="normal")
                #self.delete(1.0, END)
                #self.insert(1.0, NewText)
                #self.config (state="disabled")
                
        
   


#class AppTextBox (Text):
        #"""Custom Text widget with simplified update method to substiture Delete+Instert + Formatting + mapping to Class name and Attributes"""
        #def __init__(self, master, __class, __attribute, *args, **kwargs):
            
                #super().__init__(master, *args,**kwargs)

                #self._class = __class
                #self._attribute = __attribute
                #self.config(width = 60, height = 12,state="disabled")
                #self.bind ("<Double-1>", self.OnDoubleClick2)

        
        #def TextUpdate(self, NewText):
                #self.config(state="normal")
                #self.delete(1.0, END)
                #self.insert(1.0, NewText)  
                #self.config (state="disabled")
                
        #def OnDoubleClick2 (self, Event):
                #logging.info ('OnDoubleClick2 is aptured')
                #global _activeProject

                #top = Toplevel(self)
                #top.config(bg = _BGC)
                ##relatedProjectID = Label (top, text = _activeProject, bg = _BGC).grid(row=0, column = 0)
                
                #self.relatedClass = Label(top, text = Event.widget._class, bg = _BGC).grid(row=0, column = 0, sticky=W+E+N+S)
                #self.relatedAttribute = Label(top, text = Event.widget._attribute, bg = _BGC).grid(row = 1, column = 0, sticky=W+E+N+S)
                #self.editableTextBox = Text(top, height = 30)
                #self.editableTextBox.insert (1.0, Event.widget.get (1.0, END))
                #self.editableTextBox.grid(row=2, column =0, columnspan=2)
                
                #self.CommentaryLabel = Label(top, text = 'Change related commentaries:', bg = _BGC).grid(row=3, column =0)
                #self.CommentaryText = Text(top, height = 3).grid(row=4, column =0)
                
                #self.buttonEdit = Button(top, text = 'Edit', command = abc).grid(row=5, column =0, sticky=W+E+N+S)
                #self.buttonEdit = Button(top, text = 'Save Changes', command = self.SaveChangaes).grid(row=6, column =0, sticky=W+E+N+S)
                #self.buttonEdit = Button(top, text = 'Close without changes', command = abc).grid(row=7, column =0, sticky=W+E+N+S)
                
                
                
                #top.mainloop()
                
        #def SaveChangaes (self):
                ##logging.info ('VIEW SAVING NEW ATTR VALUE')
                #__class =  self._class
                #__attr = self._attribute
                #__value = self.editableTextBox.get (1.0, END)
                #controller.UpdateAttribute(__class, __attr, _activeProject, __value)



def abc():  #NOT USED TextBox Click event General. To accept TextBox Value, class and attribute names to run SQL
        print ("ABC")

class Application(Tk):
        def __init__ (self):
                super().__init__()
                #application = Tk()
                projectsList = PortfoliosTree(self)
                projectsList.pack()
                #application.mainloop()

#class PortfoliosTree (Frame):
        #def __init__(self, master):
                #super().__init__(master)
                #portfolioTree = PortfoliosTree (self)
                #portfolioTree.pack()
                
                
                
class PortfoliosTree (ttk.Treeview):
        def __init__(self, master):
                super().__init__(master)
                self['columns'] = (['Title', 'Version', 'SnapshotAsOfDate', 'SnapshotBoardConfirmed', 'SnapshotCommentary'])
                
                self.heading ('#0', text = 'Code', anchor = 'w')
                self.heading ('Title', text = 'Title', anchor = 'w')
                self.heading ('Version', text = 'Version', anchor = 'w')
                self.heading ('SnapshotAsOfDate', text = 'As Of Date', anchor = 'w')
                self.heading ('SnapshotBoardConfirmed', text = 'Agreed by Steering', anchor = 'w')
                self.heading ('SnapshotCommentary', text = 'Commentary', anchor = 'w')
                
                
                self.column('#0', width = 70)
                
                
                
                self.config(height = 15)        
                self.pack()
                self.projectsList = controller.getProjectsList()
                
                self.bind("<Double-1>", self.OnDoubleClick)
                
                
                self.popup_menu = Menu (self, tearoff=0)
                self.popup_menu.add_command(label='Add new project', command = self._addNewProject)
                self.popup_menu.add_command(label='Add new Sample project', command = self._addNewSampleProject)
                self.popup_menu.add_command(label='Export selected project (csv)', command = self._CSVexportProject)
                #self.popup_menu.add_command(label='Snapshot selected project', command = self._snapshotProject)  
                
                #self.popup_menu.add_command(label='Delete selected project', command = self._deleteProject)  
                self.bind ('<Button-2>', self._do_popup)
                
                self.Refresh()
                
                
        def OnDoubleClick(self, event):
                item = self.identify('item', event.x, event.y)
                bdRecordID = self.item(item, 'text')     
                if (len(self.item(item, 'values'))) != 1:
                        #print ('Selected', bdRecordID)
                        projectwindow = ProjectApp(bdRecordID)
                        projectwindow.mainloop()
                        #registerItemCard = vf_Top_RegisterCard.MainFrame(self, bdRecordID, self.ObjectName,  'gray')
                        #registerItemCard.mainloop()     

        
        def Refresh (self):
                print ('Refresh tree')
                for i in self.get_children():
                        self.delete(i)
                        
                self.projectsList.Refresh()
                #print (self.projectsList)
                
                
                # CREATE FOLDERS
                folderIndex = {}
                for item in self.projectsList.HeadList:
                        
                        #print(self.projectsList.HeadList.index(item))
                        folderIndex[item[0]] = self.projectsList.HeadList.index(item)
                        self.insert('', self.projectsList.HeadList.index(item), iid = self.projectsList.HeadList.index(item), text = item[0], values=[item[1]])
                
                #print ('Folder Index')
                #print (folderIndex)
                
                for item in self.projectsList.DetailList:
                        #print (folderIndex[item[1]])
                        self.insert(folderIndex[item[1]], item[0], text = item[0], values=[item[2],item[3],item[4],item[5],item[6]])
                        pass
                        
        def _do_popup (self, event):
                try:
                        self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
                        
                finally:
                        # make sure to release the grab (Tk 8.0a1 only)
                        self.popup_menu.grab_release()  
                        pass

        def _addNewProject(self):
                newProjectRequest = NewProjectRequest(self)
                newProjectRequest.mainloop()
                
        def _addNewSampleProject(self):
                newProjectRequest = NewSampleProjectRequest(self)
                newProjectRequest.mainloop()                
        
        def _snapshotProject(self):
                pass
        
        def _deleteProject(self):
                pass
        
        def _CSVexportProject(self):
                #print (self)
                curItem = self.focus()
                bdRecordID = self.item(curItem, 'text') 
                if (len(self.item(curItem, 'values'))) != 1:
                        print ('ID', bdRecordID)
                        #self.item(
                        projectPack = controller.GetProjectPack(bdRecordID)
                        projectPack.exportCSV()
                        #print (projectPack)
                

class NewProjectRequest (Toplevel):
        def __init__(self, master):
                super().__init__(master)
                self.title('Creation of a new Project')
                self.myLabel = Label(self, text='Enter Business Code for a new Project')
                self.myLabel.pack()
                self.myEntryBox = Entry(self) 
                self.myEntryBox.focus_set()
                self.myEntryBox.pack()  
                
                self.myLabel2 = Label(self, text='Enter Title for a new Project')
                self.myLabel2.pack()
                self.myEntryBox2 = Entry(self) 
                self.myEntryBox2.focus_set()
                self.myEntryBox2.pack()  
                
                self.mySubmitButton = Button(self, text='Create', command=self._creationOfProject)
                self.mySubmitButton.pack()   
                
        def _creationOfProject (self):
                projectBID = self.myEntryBox.get()
                projectTitle = self.myEntryBox2.get()
                controller.appendProjectPack(projectTitle, projectBID)
                #print ('careta')
                self.master.Refresh()
                self.destroy()

class NewSampleProjectRequest (Toplevel):
        def __init__(self, master):
                super().__init__(master)
                self.title('Creation of a new Project')
                self.myLabel = Label(self, text='Enter Business Code for a new Project')
                self.myLabel.pack()
                self.myEntryBox = Entry(self) 
                self.myEntryBox.focus_set()
                self.myEntryBox.pack()  
                
                self.myLabel2 = Label(self, text='Enter Title for a new Project')
                self.myLabel2.pack()
                self.myEntryBox2 = Entry(self) 
                self.myEntryBox2.focus_set()
                self.myEntryBox2.pack()  
                
                self.mySubmitButton = Button(self, text='Create', command=self._creationOfProject)
                self.mySubmitButton.pack()   
                
        def _creationOfProject (self):
                projectBID = self.myEntryBox.get()
                projectTitle = self.myEntryBox2.get()
                controller.appendProjectPack(projectTitle, projectBID, 'Yes')
                #print ('careta')
                self.master.Refresh()
                self.destroy()
                
# Building GUI                
class ProjectApp (Toplevel):
        def __init__ (self, _activeProject):
                super().__init__()
                self._frame = mainFrame_Project(self, _activeProject)
                
                #self.switch_frame(mainFrame_Portfolio)
               
                
        #def switch_frame(self, frame_class):
                #new_frame = frame_class(self)
                #if self._frame is not None:
                        #self._frame.destroy()
                #self._frame = new_frame
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
        def __init__ (self, master, _activeProject):
                super().__init__(master)
                self.ProjectPack = controller.GetProjectPack(_activeProject)
                #print(self.ProjectPack)
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
                
                self.master.master.title('Project # : ' + str (self.master.ProjectPack.Project.ID) + ' ' + self.master.ProjectPack.Project.Project)
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
                
                
                BusinessCase = vf_Register.MainFrameWIthoutRegister(self, self.master.master.master.ProjectPack.BusinessCase.ID, 'BusinessCase', _BGC)
                
                
                Benefits = vf_Register.MainFrame(self,self.master.master.master.ProjectPack.Project.ID, 'Benefit', _BGC)
                
                ProjectProduct = vf_Register.MainFrame(self, self.master.master.master.ProjectPack.Project.ID, 'Product', _BGC)             
                
                
                ProjectApproach = vf_Register.MainFrameWIthoutRegister(self, self.master.master.master.ProjectPack.ProjectApproach.ID, 'ProjectApproach', _BGC)
                
                self.add(Mandate, text = 'Mandate')
                self.add(BusinessCase, text = 'Business Case')
                self.add(ProjectApproach, text = 'Project Approach')
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
                
                
                RiskRegister = vf_Register.MainFrame(self, self.master.master.master.ProjectPack.Project.ID, 'RiskRegister', _BGC)
                
                
                
                self.add(RiskApproach1, text = 'Risk Approach (1)')
                self.add(RiskApproach2, text = 'Risk Approach (2)')
                self.add(RiskRegister, text = 'Risk Register')
                



# TAB   :   Change
class ChangeTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)

                ChangeApproach = vf_Register.MainFrameWIthoutRegister(self, self.master.master.master.ProjectPack.ChangeApproach.ID, 'ChangeApproach', _BGC)
                ChangeRegister = vf_Register.MainFrame(self, self.master.master.master.ProjectPack.Project.ID, 'Issue', _BGC)
                self.add(ChangeApproach, text = 'Change Approach')
                self.add(ChangeRegister, text = 'Issue Register')
                
              
# TAB   :   Communication
class CommunicationTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                
                CommunicationApproach = vf_Register.MainFrameWIthoutRegister(self,self.master.master.master.ProjectPack.CommunicationApproach.ID, 'CommunicationApproach', _BGC)

                self.add(CommunicationApproach, text = 'Communication Approach')
                
                stakeholders = vf_Register.MainFrame(self, self.master.master.master.ProjectPack.Project.ID, 'Stakeholder', _BGC)
                self.add(stakeholders, text = 'Stakeholders')
                
                

# TAB   :   Quality
class QualityTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                QualityApproach = vf_Register.MainFrameWIthoutRegister(self, self.master.master.master.ProjectPack.QualityApproach.ID, 'QualityApproach', _BGC)

                self.add(QualityApproach, text = 'Quality Approach')
                
                QualityRegister = vf_Register.MainFrame(self, self.master.master.master.ProjectPack.Project.ID, 'QualityRegister', _BGC)
                self.add(QualityRegister, text = 'Quality Register')
                
                
                
                
def Main ():
        logging.basicConfig(filename='logging.txt',level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M', filemode='w')
        
        #X = ProjectApp()
        X = Application()
        X.title ('Zoogie Project')
        X.mainloop()


if __name__ == '__main__':
        Main()
        
