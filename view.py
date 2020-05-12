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
import vf_RegisterLessons

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
                #frame_Lessons = Frame_Lessons(self)
                frame_Lessons = vf_RegisterLessons.MainFrame(self, _BGC)
                #frame_Lessons.config(bg = _BGC)
                
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

class Frame_Plan (Frame):
        def __init__ (self, master):
                super().__init__(master)

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
# TAB LESSONS
class Frame_Lessons (Frame):
        def __init__ (self, master):
                super().__init__(master)
                self.afterLessonsRegisterTreeFrame = Lessons_Register_TreeFrame(self)
                self.afterLessonsRegisterTreeFrame.config (bg = _BGC)
                self.LessonsRegisterBreakDownFrame = Lessons_Register_BreakDown(self)
                self.LessonsRegisterBreakDownFrame.config(bg = _BGC)
                
                self.afterLessonsRegisterTreeFrame.pack(side=LEFT, anchor=NW)
                self.LessonsRegisterBreakDownFrame.pack(side=LEFT, anchor=NW)                            
                
        #Change - Register - Tree
class Lessons_Register_TreeFrame (Frame):
        def __init__(self, master):
                super().__init__(master)
                self.lb_LessonsReg_Tree = Label(self, text = 'Lessons Register', bg = _BGC).pack(anchor=W)   
                self.tr_LessonsTree = LessonsTree(self).pack(anchor=W)
        
class LessonsTree (ttk.Treeview):
        def __init__ (self, master):
                super().__init__(master)
                
                
                self['columns'] = ('Title', 'Category')#, 'Event', 'Effect')
                
                #self.width = 100
                #self.height = 200
                #self.master=master
                self.heading ('#0', text = 'Code', anchor = 'w')
                #self.heading ('BusinessCode', text = 'Business Code', anchor = 'w')
                self.heading ('Title', text = 'Title', anchor = 'w')
                self.heading ('Category', text = 'Category', anchor = 'w')



                self.column('#0', width = 60)
                #self.column('BusinessCode', width = 100)            
                self.column('Title', width = 250)
                self.column('Category', width = 150)



                self.pack(anchor=W)
                self.Refresh()
                self.bind("<Double-1>", self.OnDoubleClick)
        
                #Business Case - ProjectProduct - BreakdownFrame        
        def Refresh (self):
                logging.info ('VIEW Starting Lesson tree Refresh')
                global _activeProject
                Keys, Data = controller.RefreshBusinessObject('Lesson', _activeProject)
                #logging.debug ('Refresh Lesson Keys:', Keys) 
                #logging.debug ('Refresh Lesson Data:', Data)

                for item in Data:
                        self.insert('',item[0], text=item[0], values=[
                                #item[Keys['BusinessID']],
                                item[Keys['Title']],
                                item[Keys['Category']],
                                #item[Keys['Event']],
                                #item[Keys['Effect']]
                        ]) 
                logging.info ('VIEW Finished Lesson tree Refresh')
                        
                        
        def OnDoubleClick(self, event):
                global _activeProject
                item = self.identify('item', event.x, event.y)
                _activeProject = self.item(item, 'text')
       
                Keys, Data = controller.RefreshBusinessObject_byID('Lesson', _activeProject)#  - change id to project id    !!!
                #print (Keys) 
                #print (Data)
                
                ModifiedFrame=self.master.master.LessonsRegisterBreakDownFrame
                

                ModifiedFrame.tx_Title.TextUpdate(Data[0][Keys['Title']])                   

                ModifiedFrame.tx_Category.TextUpdate (Data[0][Keys['Category']])

                ModifiedFrame.tx_BusinessCode.TextUpdate (Data[0][Keys['BusinessID']])

                ModifiedFrame.tx_Priority.TextUpdate (Data[0][Keys['Priority']])

                ModifiedFrame.tx_Description.TextUpdate(Data[0][Keys['Description']])         

                ModifiedFrame.tx_Event.TextUpdate (Data[0][Keys['Event']])

                ModifiedFrame.tx_Cause.TextUpdate (1.0, Data[0][Keys['CauseTrigger']])

                ModifiedFrame.tx_Recommendation.TextUpdate (Data[0][Keys['Recommendations']])

                ModifiedFrame.tx_Effect.TextUpdate (Data[0][Keys['Effect']])

                ModifiedFrame.tx_Indicator.TextUpdate (Data[0][Keys['EarlyWarningIndicator']])

                ModifiedFrame.tx_DateLogged.TextUpdate (Data[0][Keys['DateLogged']])

                ModifiedFrame.tx_LoggedBy.TextUpdate (Data[0][Keys['LoggedBy']])



                
        
class Lessons_Register_BreakDown (Frame):
        
        
        def __init__(self, master):
                super().__init__(master)
                #lb_LessonsReg_BreakDown = Label(self, text = 'Lesson Details').pack(anchor=W)   
                
                self.lb_Title = Label(self, text = 'Title', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                
                self.tx_Title = AppText(self) 
                
                self.lb_Category = Label(self, text = 'Category', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Category = AppText(self)
                
                self.lb_BusinessCode = Label(self, text = 'Business Case', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_BusinessCode = AppText(self)               
                
                self.lb_Priority = Label(self, text = 'Priority', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Priority = AppText(self)               
                
                self.lb_Description = Label(self, text='Description', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                
                self.tx_Description = AppTextBox(self,'Lesson','Description')                    
                
                self.lb_Event = Label(self, text = 'Event', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Event = AppTextBox (self,'Lesson','Event')              
                
                self.lb_Cause = Label(self, text = 'Cause Trigger', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Cause = AppTextBox(self,'Lesson','CauseTrigger')             
                
                
                # RIGHT LONGS
                               
                
                self.lb_Recommendation = Label (self, text = 'Recommendation', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Recommendation = AppTextBox (self,'Lesson','Description')
                
                self.lb_Effect = Label(self, text = 'Effect', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Effect = AppTextBox(self,'Lesson','Effect')
                
                self.lb_Indicator = Label(self, text = 'Indicator', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Indicator = AppTextBox (self,'Lesson','EarlyWarningIndicator')
                
                # Foots Left
                self.lb_DateLogged = Label(self, text = 'Date Logged', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_DateLogged = AppText(self)
                
                #Foot Right
                self.lb_LoggedBy = Label(self, text = 'Logged by', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_LoggedBy = AppText(self)             
                
                
                #---------
                #LEFT SHORTS (ROWS 0 - 3)
                
                self.lb_Title.grid(row = 0, column = 0)
                self.tx_Title.grid(row = 1, column = 0)
                
                self.lb_Category.grid(row = 2, column = 0)
                self.tx_Category.grid(row = 3, column = 0) 
                
                
                #RIGHT SHORTS  (ROWS 0 - 3)
                
                self.lb_BusinessCode.grid(row = 0, column = 1)
                self.tx_BusinessCode.grid(row = 1, column = 1)                 
                
                self.lb_Priority.grid(row = 2, column = 1)
                self.tx_Priority.grid(row = 3, column = 1)                
                
                
                # LEFT LONGS
                
                self.lb_Description.grid(row = 4, column = 0)
                self.tx_Description.grid(row = 5, column = 0)
                
                self.lb_Event.grid(row = 6, column = 0)
                self.tx_Event.grid(row = 7, column = 0)                
                
                self.lb_Cause.grid(row = 8, column = 0)
                self.tx_Cause.grid(row = 9, column = 0)                

                
                # RIGHT LONGS
                               
                
                self.lb_Recommendation.grid(row = 4, column = 1)
                self.tx_Recommendation.grid(row = 5, column = 1)
                
                self.lb_Effect.grid(row = 6, column = 1)
                self.tx_Effect.grid(row = 7, column = 1)
                
                self.lb_Indicator.grid(row = 8, column = 1)
                self.tx_Indicator.grid(row = 9, column = 1)
                
                # Foots Left
                self.lb_DateLogged.grid(row = 10, column = 0)
                self.tx_DateLogged.grid(row = 11, column = 0)
                
                #Foot Right
                self.lb_LoggedBy.grid(row = 10, column = 1)
                self.tx_LoggedBy.grid(row = 11, column = 1)
                



# TAB   :  Business Case             
class BusinessCaseTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                
                Mandate = subFrame_Mandate(self)
                
                BusinessCase = vf_BusinessCase.MainFrame(self, self.master.master.master.ProjectPack.BusinessCase.ID)
                BusinessCase.Refresh()
                
                Benefits = subFrame_Benefits(self)
                ProjectProduct = subFrame_ProjectProduct(self)
                
                self.add(Mandate, text = 'Mandate')
                self.add(BusinessCase, text = 'Business Case')
                self.add(Benefits, text = 'Benefits')
                self.add(ProjectProduct, text = 'Project Product')
        

class subFrame_Mandate(Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                self.MandateLabel = Label(self, text = 'Mandate provided by Sponsor:')
                self.MandateText = Text (self, width = 150, height = 50)
                self.MandateText.config(state="disabled" )
                #MandateText.insert(1.0, 'HERE IS THE TEXT')               
                self.MandateLabel.pack()
                self.MandateText.pack ()
                self.Refresh()
        
        def Refresh(self):
                global _activeProject
                logging.info ('VIEW Starting Mandate Refresh')
                #logging.info (_activeProject)
                Keys, Data = controller.RefreshBusinessObject('Mandate', _activeProject)#  - change id to project id    !!!
                if (len(Data)) != 0:
                        self.MandateText.config(state="normal" )
                        self.MandateText.insert(1.0, Data[0][1])
                        self.MandateText.config(state="disabled" )
                logging.info ('VIEW Finished Mandate Refresh')
                
                
class subFrame_Benefits(Frame):
        def __init__ (self, master):
                super().__init__(master)   
                self.config (bg = _BGC)
                BenefitsTreeFrame = BusinessCase_Benefits_TreeFrame(self)
                BenefitsBreakDownFrame = BusinessCase_Benefits_BreakdownFrame(self)
                BenefitsTreeFrame.pack()
                BenefitsBreakDownFrame.pack()
        #Business Case - Benefits - TreeFrame
class BusinessCase_Benefits_TreeFrame (Frame):
        def __init__(self, master):
                super().__init__(master)
                lb_Benefits_Tree = Label(self, text = 'Project Benefit List', bg = _BGC).pack()
                tr_Benefits_Tree = BenefitsTree(self)
                
                
class BenefitsTree (ttk.Treeview):
        def __init__ (self, master):
                super().__init__(master)
                self['columns'] = ('BusinessCode', 'Title', 'Category', 'Measurement', 'Responsibility') #, 'ResourseRequirements', 'Baseline')
                #self.width = 100
                #self.height = 200
                self.master=master
                self.heading ('#0', text = 'Code', anchor = 'w')
                self.heading ('BusinessCode', text = 'Business Code', anchor = 'w')
                self.heading ('Title', text = 'Title', anchor = 'w')
                self.heading ('Category', text = 'Category', anchor = 'w')
                self.heading ('Measurement', text = 'Measurement', anchor = 'w')
                self.heading ('Responsibility', text = 'Responsibility', anchor = 'w')
                #self.heading ('ResourseRequirements', text = 'Resourse Requirements', anchor = 'w')
                #self.heading ('Baseline', text = 'Baseline', anchor = 'w')
                
                
                
                
                self.column('#0', width = 60)
                self.column('BusinessCode', width = 100)            
                self.column('Title', width = 250)
                self.column('Category', width = 250)
                self.column('Measurement', width = 350)
                self.column('Responsibility', width = 350)
                #self.column('ResourseRequirements', width = 200)
                #self.column('Baseline', width = 200)
                
                
                
                
                
                self.pack()
                self.Refresh()
                #self.bind("<Double-1>", self.OnDoubleClick)

                
        def Refresh (self):
                #print ('Portfolio tree method refresh')
                global _activeProject
                logging.info ('VIEW Starting Benefit tree Refresh')
                Keys, Data = controller.RefreshBusinessObject('Benefit', _activeProject)#  - change id to project id    !!!
                #print (Keys) 
                #print (Data)
                
                for item in Data:
                        self.insert('',item[0], text=item[0], values=[

                                item[Keys['BusinessID']],
                                item[Keys['Title']],
                                item[Keys['Category']],
                                item[Keys['Measurement']],
                                item[Keys['Responsibility']]                                
                        ])
                logging.info ('VIEW Finished Benefit tree Refresh')
        
                
        #Business Case - Benefits - BreakdownFrame
class BusinessCase_Benefits_BreakdownFrame (Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                lb_BenefitBreakDown = Label(self, text = 'Benefit Details').pack()
        
class subFrame_ProjectProduct(Frame):
        def __init__ (self, master):
                super().__init__(master)  
                self.config (bg = _BGC)
                self.ProjectProductTreeFrame = BusinessCase_ProjectProduct_TreeFrame(self)
                self.ProjectProductBreakDownFrame = BusinessCase_ProjectProduct_BreakdownFrame(self)
                self.ProjectProductTreeFrame.pack(side= LEFT, anchor = NW)
                self.ProjectProductBreakDownFrame.pack(side= LEFT, anchor = NW)                
               

        #Business Case - ProjectProduct - TreeFrame

class BusinessCase_ProjectProduct_TreeFrame (Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                lb_ProjectProduct_Tree = Label(self, text = 'Project Product List', bg = _BGC).pack()
                tr_ProductTree = ProjectProductTree(self).pack()
                
class ProjectProductTree (ttk.Treeview):
        def __init__ (self, master):
                super().__init__(master)
                self['columns'] = ('BusinessCode', 'Title')#, 'Purpose')

                self.heading ('#0', text = 'Code', anchor = 'w')
                self.heading ('BusinessCode', text = 'Business Code', anchor = 'w')
                self.heading ('Title', text = 'Product Name', anchor = 'w')

                
                self.column('#0', width = 60)
                self.column('BusinessCode', width = 100)            
                self.column('Title', width = 250)

                
                self.pack()
                self.Refresh()
                self.bind("<Double-1>", self.OnDoubleClick)
                
        def OnDoubleClick(self, event):
                global _activeProject
                item = self.identify('item', event.x, event.y)
                _activeProject = self.item(item, 'text')
                
      
                Keys, Data = controller.RefreshBusinessObject_byID('Product', _activeProject)    
                #print (Keys) 
                #print (Data)
                
                ModifiedFrame = self.master.master.ProjectProductBreakDownFrame
                
                ModifiedFrame.tx_Title.delete(1.0, END)
                ModifiedFrame.tx_Title.insert (1.0, Data[0][Keys['Title']])
                ModifiedFrame.tx_Description.delete(1.0, END)
                ModifiedFrame.tx_Description.insert (1.0, Data[0][Keys['Description']])
                ModifiedFrame.tx_BusinessID.delete(1.0, END)
                ModifiedFrame.tx_BusinessID.insert (1.0, Data[0][Keys['BusinessID']])
                ModifiedFrame.tx_Purpose.delete(1.0, END)
                ModifiedFrame.tx_Purpose.insert (1.0, Data[0][Keys['Purpose']])
                ModifiedFrame.tx_Composition.delete(1.0, END)
                ModifiedFrame.tx_Composition.insert (1.0, Data[0][Keys['Composition']])
                ModifiedFrame.tx_Derivation.delete(1.0, END)
                ModifiedFrame.tx_Derivation.insert (1.0, Data[0][Keys['Derivation']])
                ModifiedFrame.tx_FormatPresentation.delete(1.0, END)
                ModifiedFrame.tx_FormatPresentation.insert (1.0, Data[0][Keys['FormatPresentation']])
                ModifiedFrame.tx_DevSkills.delete(1.0, END)
                ModifiedFrame.tx_DevSkills.insert (1.0, Data[0][Keys['DevSkills']])

        

                
        def Refresh (self):
                #print ('Portfolio tree method refresh')
                global _activeProject
                logging.info ('VIEW Starting Product Refresh')
                Keys, Data = controller.RefreshBusinessObject('Product', _activeProject)#  - change id to project id    !!!
                #logging.debug ('Refresh Product Keys: ', Keys) 
                #logging.debug ('Refresh Product Data: ', Data)
                
                for item in Data:
                        self.insert('',item[0], text=item[0], values=[
                                item[Keys['BusinessID']],
                                item[Keys['Title']],
                                #item[Keys['Purpose']],
                                #Data[0][Keys['Measurement']],
                                #Data[0][Keys['Responsibility']]
                        ]) 
                logging.info ('VIEW Finished Product Refresh')
        
class BusinessCase_ProjectProduct_BreakdownFrame (Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                #lb_ProjectProductBreakDown = Label(self, text = 'Project Product Details').pack()
                
                self.lb_Title = Label(self, text = 'Title', width = 40, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Title=Text(self, width = 60, height = 1)
                
                self.lb_Description = Label(self, text='Description', width = 40, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Description = Text(self, width = 60, height = 12)
                
                self.lb_BusinessID = Label(self, text = 'Business Code', width = 40, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_BusinessID = Text(self, width = 60, height = 1)
                
                self.lb_Purpose = Label (self, text = 'Purpose', width = 40, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Purpose = Text (self, width = 60, height = 12)                             
                
                self.lb_Composition = Label(self, text = 'Composition', width = 40, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Composition = Text(self, width = 60, height = 12)               
                
                self.lb_Derivation = Label(self, text = 'Derivation', width = 40, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Derivation = Text(self, width = 60, height = 12)
                
                self.lb_FormatPresentation = Label(self, text = 'Format of Presentation', width = 40, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_FormatPresentation = Text (self, width = 60, height = 12)               
        
                self.lb_DevSkills = Label(self, text = 'Development skills', width = 40, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_DevSkills = Text (self, width = 60, height = 12)
                            
                
                
                #---------

                
                self.lb_Title.grid(row = 0, column = 0)
                self.tx_Title.grid(row = 1, column = 0)
                
                self.lb_BusinessID.grid(row = 0, column = 1)
                self.tx_BusinessID.grid(row = 1, column = 1)                 
                
                self.lb_Description.grid(row = 2, column = 0)
                self.tx_Description.grid(row = 3, column = 0)                
                
                
                self.lb_Purpose.grid(row = 2, column = 1)
                self.tx_Purpose.grid(row = 3, column = 1)                   
                
                self.lb_Composition.grid(row = 4, column = 0)
                self.tx_Composition.grid(row = 5, column = 0)                 
                
                self.lb_Derivation.grid(row = 4, column = 1)
                self.tx_Derivation.grid(row = 5, column = 1)                
                
                self.lb_FormatPresentation.grid(row = 6, column = 0)
                self.tx_FormatPresentation.grid(row = 7, column = 0)                
   
                self.lb_DevSkills.grid(row = 6, column = 1)
                self.tx_DevSkills.grid(row = 7, column = 1)
                
                
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
                print (self.master.master.master)
                #RiskApproach1 = subFrame_RiskApproach1(self)
                RiskApproach1 = vf_RiskApproach1.MainFrame(self)
                RiskApproach1.Refresh(self.master.master.master.ProjectPack.RiskApproach.ID)
                #RiskApproach2 = subFrame_RiskApproach2(self)
                
                RiskApproach2 = vf_RiskApproach2.MainFrame(self)
                RiskApproach2.Refresh(self.master.master.master.ProjectPack.RiskApproach.ID)
                
                
                RiskRegister = vf_RegisterRisk.MainFrame(self, _BGC)
                
                
                self.add(RiskApproach1, text = 'Risk Approach (1)')
                self.add(RiskApproach2, text = 'Risk Approach (2)')
                self.add(RiskRegister, text = 'Risk Register')
                



# TAB   :   Change
class ChangeTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                
                #print ('change approach: ', self.master.master.master) # LOOKUP
                #print(self.master.master.master.__dict__)
                
                
                ChangeApproach = vf_ChangeApproach.MainFrame(self)
                
                #print (self.master.master.master.ProjectPack.ChangeApproach.ID)
                #print (self.master.master.master.ProjectPack.ChangeApproach.Introduction)
                
                ChangeApproach.Refresh(self.master.master.master.ProjectPack.ChangeApproach.ID)
                
                #ChangeRegister = subFrameChangeRegister(self)
                ChangeRegister = vf_RegisterChange.MainFrame (self, _BGC)
                self.add(ChangeApproach, text = 'Change Approach')
                self.add(ChangeRegister, text = 'Issue Register')
                
              
# TAB   :   Communication
class CommunicationTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                #CommunicationApproach = subFrame_CommunicationApproach(self)
                CommunicationApproach = vf_CommunicationApproach.MainFrame(self)
                CommunicationApproach.Refresh(self.master.master.master.ProjectPack.CommunicationApproach.ID)
                
                
                self.add(CommunicationApproach, text = 'Communication Approach')
                #pass
                

# TAB   :   Quality
class QualityTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                #QualityApproach = subFrame_QualityApproach(self)
                QualityApproach = vf_QualityApproach.MainFrame(self)
                self.add(QualityApproach, text = 'Quality Approach')
                #pass
                
                
                
def Main ():
        logging.basicConfig(filename='logging.txt',level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M', filemode='w')
        X = ProjectApp()
        X.mainloop()


if __name__ == '__main__':
        Main()
        
