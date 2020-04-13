"""GUI Part of Zoogie application

TODO [ ] : Substitute standard Text widgets with new custom AppText
TODO [ ] : Backgroud Colour across Frames


"""

#IMPORT GLOBALS 
from tkinter import * 
from tkinter import ttk
import logging

import controller

_activeProject = None

_BGC = '#abc4e7'
"""Background colour for Frames 
use https://www.color-hex.com/ to find nice colour code"""

# Custom Widgets
class AppText (Text):
        """Custom 1-line Text widget with simplified update method to substiture Delete+Instert + Formatting"""
        def __init__(self, *args, **kwargs):
                super().__init__(*args,**kwargs)
                self.config(width = 60, height = 1)
        
        def TextUpdate(self, NewText):
                self.delete(1.0, END)
                self.insert(1.0, NewText)

class AppTextBox (Text):
        """Custom many lines Text widget with simplified update method to substiture Delete+Instert + Formatting"""
        def __init__(self, *args, **kwargs):
                super().__init__(*args,**kwargs)
                self.config(width = 60, height = 12)
        
        def TextUpdate(self, NewText):
                self.delete(1.0, END)
                self.insert(1.0, NewText)                

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
                
                self.Label_ProjectID.pack(side=LEFT)
                self.Entry_ProjectID.pack(side=LEFT)
                self.Label_ProjectBusinessID.pack(side=LEFT)
                self.Entry_ProjectBusinessID.pack(side=LEFT)
                self.Label_ProjectName.pack(side=LEFT)
                self.Entry_ProjectName.pack(side=LEFT)
                self.Refresh()
                
        def Refresh(self):
                global _activeProject
                logging.info ('VIEW Starting Project Head Refresh')
                
                Keys, Data = controller.RefreshProjectHead(_activeProject)

                
                self.Entry_ProjectID.insert(0,Data[0][Keys['ID']])
                self.Entry_ProjectBusinessID.insert(0,Data[0][Keys['BusinessID']])   
                self.Entry_ProjectName.insert(0,Data[0][Keys['Project']])
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
                frame_Lessons = Frame_Lessons(self)
                frame_Lessons.config(bg = _BGC)
                
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
                #self.heading ('Event', text = 'Event', anchor = 'w')
                #self.heading ('Effect', text = 'Effect', anchor = 'w')
                #self.heading ('Status', text = 'Status', anchor = 'w')
                #self.heading ('Owner', text = 'Owner', anchor = 'w')


                self.column('#0', width = 60)
                #self.column('BusinessCode', width = 100)            
                self.column('Title', width = 250)
                self.column('Category', width = 150)
                #self.column('Event', width = 350)
                #self.column('Effect', width = 350)
                #self.column('ResourseRequirements', width = 200)
                #self.column('Baseline', width = 200)


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
                #print (_activeProject)
                #self.master.master.switch_frame(mainFrame_Project)        
                Keys, Data = controller.RefreshBusinessObject_byID('Lesson', _activeProject)#  - change id to project id    !!!
                #print (Keys) 
                #print (Data)
                
                ModifiedFrame=self.master.master.LessonsRegisterBreakDownFrame
                
                ModifiedFrame.tx_Title.delete(1.0, END)
                #ModifiedFrame.tx_Title.insert (1.0, Data[0][Keys['Title']])
                ModifiedFrame.tx_Title.TextUpdate(Data[0][Keys['Title']])                   #  <---------
                ModifiedFrame.tx_Category.delete(1.0, END)
                ModifiedFrame.tx_Category.insert (1.0, Data[0][Keys['Category']])
                ModifiedFrame.tx_BusinessCode.delete(1.0, END)
                ModifiedFrame.tx_BusinessCode.insert (1.0, Data[0][Keys['BusinessID']])
                ModifiedFrame.tx_Priority.delete(1.0, END)
                ModifiedFrame.tx_Priority.insert (1.0, Data[0][Keys['Priority']])
                #ModifiedFrame.tx_Description.delete(1.0, END)
                #ModifiedFrame.tx_Description.insert (1.0, Data[0][Keys['Description']])
                ModifiedFrame.tx_Description.TextUpdate(Data[0][Keys['Description']])         #  <=========
                ModifiedFrame.tx_Event.delete(1.0, END)
                ModifiedFrame.tx_Event.insert (1.0, Data[0][Keys['Event']])
                ModifiedFrame.tx_Cause.delete(1.0, END)
                ModifiedFrame.tx_Cause.insert (1.0, Data[0][Keys['CauseTrigger']])
                ModifiedFrame.tx_Recommendation.delete(1.0, END)
                ModifiedFrame.tx_Recommendation.insert (1.0, Data[0][Keys['Recommendations']])
                ModifiedFrame.tx_Effect.delete(1.0, END)
                ModifiedFrame.tx_Effect.insert (1.0, Data[0][Keys['Effect']])
                ModifiedFrame.tx_Indicator.delete(1.0, END)
                ModifiedFrame.tx_Indicator.insert (1.0, Data[0][Keys['EarlyWarningIndicator']])
                ModifiedFrame.tx_DateLogged.delete(1.0, END)
                ModifiedFrame.tx_DateLogged.insert (1.0, Data[0][Keys['DateLogged']])
                ModifiedFrame.tx_LoggedBy.delete(1.0, END)
                ModifiedFrame.tx_LoggedBy.insert (1.0, Data[0][Keys['LoggedBy']])



                
        
class Lessons_Register_BreakDown (Frame):
        def __init__(self, master):
                super().__init__(master)
                #lb_LessonsReg_BreakDown = Label(self, text = 'Lesson Details').pack(anchor=W)   
                
                self.lb_Title = Label(self, text = 'Title', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                #self.tx_Title=Text(self, width = 60, height = 1)
                self.tx_Title = AppText(self) #, width = 60, height = 1)   #  <-----
                
                self.lb_Category = Label(self, text = 'Category', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Category = Text(self, width = 60, height = 1)
                
                self.lb_BusinessCode = Label(self, text = 'Business Case', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_BusinessCode = Text(self, width = 60, height = 1)               
                
                self.lb_Priority = Label(self, text = 'Priority', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Priority = Text(self, width = 60, height = 1)               
                
                self.lb_Description = Label(self, text='Description', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                #self.tx_Description = Text(self, width = 60, height = 12)
                self.tx_Description = AppTextBox(self)                    #  <============
                
                self.lb_Event = Label(self, text = 'Event', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Event = Text (self, width = 60, height = 12)               
                
                self.lb_Cause = Label(self, text = 'Cause Trigger', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Cause = Text(self, width = 60, height = 12)             
                
                
                # RIGHT LONGS
                               
                
                self.lb_Recommendation = Label (self, text = 'Recommendation', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Recommendation = Text (self, width = 60, height = 12)
                
                self.lb_Effect = Label(self, text = 'Effect', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Effect = Text(self, width = 60, height = 12)
                
                self.lb_Indicator = Label(self, text = 'Indicator', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Indicator = Text (self, width = 60, height = 12)
                
                # Foots Left
                self.lb_DateLogged = Label(self, text = 'Date Logged', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_DateLogged = Text(self, width = 60, height = 1)
                
                #Foot Right
                self.lb_LoggedBy = Label(self, text = 'Logged by', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_LoggedBy = Text(self, width = 60, height = 1)               
                
                
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
                BusinessCase = subFrame_BusinessCase(self)
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
                #MandateText.insert(1.0, 'HERE IS THE TEXT')               
                self.MandateLabel.pack()
                self.MandateText.pack ()
                self.Refresh()
        
        def Refresh(self):
                global _activeProject
                logging.info ('VIEW Starting Mandate Refresh')
                #logging.info (_activeProject)
                Keys, Data = controller.RefreshBusinessObject('Mandate', _activeProject)#  - change id to project id    !!!
                self.MandateText.insert(1.0, Data[0][1])
                logging.info ('VIEW Finished Mandate Refresh')
                
class subFrame_BusinessCase (Frame):
        def __init__ (self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                #  не работает ширина и выравнивание лейблов ((
                
                self.lb_ExecSummary = Label(self, text = 'Executive Summary:', width = 90, justify = LEFT, anchor = W, bg = _BGC)
                self.lb_Reasons = Label(self, text = 'Reasons:', width = 90, justify = LEFT, anchor = W, bg = _BGC)
                self.lb_Options = Label(self, text = 'BusinessOptions:', width = 90, justify = LEFT, anchor = W, bg = _BGC)
                self.lb_Time = Label(self, text = 'Time Scale:', width = 90, justify = LEFT, anchor = W, bg = _BGC)
                self.lb_Benefits = Label(self, text = 'Expected Benefits:', width = 90, justify = LEFT, anchor = W, bg = _BGC)
                self.lb_DisBenefits = Label(self, text = 'Expected Dis-Benefits:', width = 90, justify = LEFT, anchor = W, bg = _BGC)
                self.lb_DisCosts = Label(self, text = 'Costs:', width = 90, justify = LEFT, anchor = W, bg = _BGC)
                self.lb_Investment = Label(self, text = 'InvestmentAppraisal:', width = 90, justify = LEFT, anchor = W, bg = _BGC)
                
                self.txt_ExecSummary = Text(self, width = 90, height = 12)
                self.txt_Reasons = Text(self, width = 90, height = 12)
                self.txt_Options = Text(self, width = 90, height = 12)
                self.txt_Time = Text(self, width = 90, height = 12)
                self.txt_Benefits = Text(self, width = 90, height = 12)
                self.txt_DisBenefits = Text(self, width = 90, height = 12)
                self.txt_Costs = Text(self, width = 90, height = 12)
                self.txt_Investment = Text(self, width = 90, height = 12)
                
                self.lb_ExecSummary.grid(row = 0, column = 0)
                self.txt_ExecSummary.grid(row=1, column = 0)
                self.lb_Reasons.grid(row=2, column = 0)
                self.txt_Reasons.grid (row=3, column = 0)
                self.lb_Options.grid (row=4, column = 0)
                self.txt_Options.grid (row=5, column = 0)
                self.lb_Time.grid (row=6, column = 0)
                self.txt_Time.grid (row=7, column = 0)
                
                self.lb_Benefits.grid(row = 0, column = 1)
                self.txt_Benefits.grid(row = 1, column = 1)
                self.lb_DisBenefits.grid(row = 2, column = 1)
                self.txt_DisBenefits.grid(row = 3, column = 1)
                self.lb_DisCosts.grid(row = 4, column = 1)
                self.txt_Costs.grid(row = 5, column = 1)
                self.lb_Investment.grid(row = 6, column = 1)
                self.txt_Investment.grid(row = 7, column = 1)
                
                self.Refresh()
                
        def Refresh(self):
                global _activeProject
                logging.info ('VIEW Starting Business Case Refresh')
                Keys, Data = controller.RefreshBusinessObject('BusinessCase', _activeProject)    
                
                self.txt_ExecSummary.insert (1.0, Data[0][Keys['ExecutiveSummary']])
                self.txt_Reasons.insert (1.0, Data[0][Keys['Reasons']])
                self.txt_Options.insert (1.0, Data[0][Keys['Options']])
                self.txt_Time.insert (1.0, Data[0][Keys['Timescale']])
                
                self.txt_Benefits.insert (1.0, Data[0][Keys['ExpectedBenefits']])
                self.txt_DisBenefits.insert (1.0, Data[0][Keys['ExpectedDisBenefits']])
                self.txt_Costs.insert (1.0, Data[0][Keys['Costs']])
                self.txt_Investment.insert (1.0, Data[0][Keys['InvestmentArraisal']])
                logging.info ('VIEW Finished Business Case Refresh')
                
                
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
                #print ('selected ID: ' , _activeProject)
      
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
                
                self.lb_Title = Label(self, text = 'Title', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Title=Text(self, width = 60, height = 1)
                
                self.lb_Description = Label(self, text='Description', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Description = Text(self, width = 60, height = 12)
                
                self.lb_BusinessID = Label(self, text = 'Business Code', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_BusinessID = Text(self, width = 60, height = 1)
                
                self.lb_Purpose = Label (self, text = 'Purpose', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Purpose = Text (self, width = 60, height = 12)                             
                
                self.lb_Composition = Label(self, text = 'Composition', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Composition = Text(self, width = 60, height = 12)               
                
                self.lb_Derivation = Label(self, text = 'Derivation', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_Derivation = Text(self, width = 60, height = 12)
                
                self.lb_FormatPresentation = Label(self, text = 'Format of Presentation', width = 60, justify = LEFT, anchor = W, bg = _BGC)
                self.tx_FormatPresentation = Text (self, width = 60, height = 12)               
        
                self.lb_DevSkills = Label(self, text = 'Development skills', width = 60, justify = LEFT, anchor = W, bg = _BGC)
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
                
                RiskApproach1 = subFrame_RiskApproach1(self)
                RiskApproach2 = subFrame_RiskApproach2(self)
                RiskRegister = subFrame_RiskRegister(self)
                #ProjectProduct = subFrame_ProjectProduct(self)
                
                self.add(RiskApproach1, text = 'Risk Approach (1)')
                self.add(RiskApproach2, text = 'Risk Approach (2)')
                self.add(RiskRegister, text = 'Risk Register')
                #self.add(ProjectProduct, text = 'Project Product')
                #pass

class subFrame_RiskApproach1(Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                self.lb_Introduction = Label(self, text = 'Introduction:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Procedure = Label(self, text = 'Procedure:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Techniques = Label(self, text = 'Techniques:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Records = Label(self, text = 'Records:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Reporting = Label(self, text = 'Reporting:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Timing = Label(self, text = 'Timing:', width = 90, justify = LEFT, bg = _BGC)
                                                                                                
                
                self.txt_Introduction = Text(self, width = 90, height = 12)
                self.txt_Procedure = Text(self, width = 90, height = 12)
                self.txt_Techniques = Text(self, width = 90, height = 12)
                self.txt_Records = Text(self, width = 90, height = 12)
                self.txt_Reporting = Text(self, width = 90, height = 12)
                self.txt_Timing = Text(self, width = 90, height = 12)
                
                self.lb_Introduction.grid(row = 0, column = 0)
                self.txt_Introduction.grid(row = 1, column = 0)
                self.lb_Procedure.grid(row = 2, column = 0)
                self.txt_Procedure.grid(row = 3, column = 0)
                self.lb_Techniques.grid(row = 4, column = 0)
                self.txt_Techniques.grid(row = 5, column = 0)
                
                self.lb_Records.grid(row = 0, column = 1)
                self.txt_Records.grid(row = 1, column = 1)
                self.lb_Reporting.grid(row = 2, column = 1)
                self.txt_Reporting.grid(row = 3, column = 1)
                self.lb_Timing.grid(row = 4, column = 1)
                self.txt_Timing.grid(row = 5, column = 1)
                
                self.Refresh()
                      
        def Refresh(self):
                global _activeProject
                
                logging.info('VIEW Starting Risk Approach Refresh')
                
                Keys, Data = controller.RefreshBusinessObject('RiskApproach', _activeProject)#  - change id to project id    !!!
                
                self.txt_Introduction.insert (1.0, Data[0][Keys['Introduction']])
                self.txt_Procedure.insert (1.0, Data[0][Keys['Procedure']])
                self.txt_Techniques.insert (1.0, Data[0][Keys['Techniques']])
                self.txt_Records.insert (1.0, Data[0][Keys['Records']])
                self.txt_Reporting.insert (1.0, Data[0][Keys['Reporting']])
                self.txt_Timing.insert (1.0, Data[0][Keys['Timing']])
                logging.info ('VIEW Finished Risk Approach Refresh')
                
                
                #print ('BusinessCase: ', Keys)
                
class subFrame_RiskApproach2(Frame):
        def __init__(self, master):  
                super().__init__(master)
                self.config (bg = _BGC)
                self.lb_RolesResponsibilities = Label(self, text = 'Roles and Responsibilities:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Scales = Label(self, text = 'Scales:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Proxomity = Label(self, text = 'Proxomity:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_RiskCategory = Label(self, text = 'Risk Category:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_ResponseCategory = Label(self, text = 'Response Category:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_EarlyWarningIndicator = Label(self, text = 'Early Warning Indicator:', width = 90, justify = LEFT, bg = _BGC)
                
                self.txt_RolesResponsibilities = Text(self, width = 90, height = 12)
                self.txt_Scales = Text(self, width = 90, height = 12)
                self.txt_Proxomity = Text(self, width = 90, height = 12)
                self.txt_RiskCategory = Text(self, width = 90, height = 12)
                self.txt_ResponseCategory = Text(self, width = 90, height = 12)
                self.txt_EarlyWarningIndicator = Text(self, width = 90, height = 12)                
                
                self.lb_RolesResponsibilities.grid(row = 0, column = 0)
                self.txt_RolesResponsibilities.grid(row = 1, column = 0)
                self.lb_Scales.grid(row = 2, column = 0)
                self.txt_Scales.grid(row = 3, column = 0)
                self.lb_Proxomity.grid(row = 4, column = 0)
                self.txt_Proxomity.grid(row = 5, column = 0)
                
                self.lb_RiskCategory.grid(row = 0, column = 1)
                self.txt_RiskCategory.grid(row = 1, column = 1)
                self.lb_ResponseCategory.grid(row = 2, column = 1)
                self.txt_ResponseCategory.grid(row = 3, column = 1)
                self.lb_EarlyWarningIndicator.grid(row = 4, column = 1)
                self.txt_EarlyWarningIndicator.grid(row = 5, column = 1)  
                
                self.Refresh()
        
        def Refresh(self):  # Correct risk and response categories in model and in db
                global _activeProject
                
                logging.info ('VIEW Starting Risk Approach Refresh')
                
                Keys, Data = controller.RefreshBusinessObject('RiskApproach', _activeProject)#  - change id to project id    !!!
                #self.txt_ExecSummary.insert (1.0, Data[0][Keys['ExecutiveSummary']])
                
                self.txt_RolesResponsibilities.insert (1.0, Data[0][Keys['RolesResponsibilities']])
                self.txt_Scales.insert (1.0, Data[0][Keys['Scales']])
                self.txt_Proxomity.insert (1.0, Data[0][Keys['Proxomity']])
                #self.txt_RiskCategory.insert (1.0, Data[0][Keys['Records']])
                #self.txt_ResponseCategory.insert (1.0, Data[0][Keys['Reporting']])
                self.txt_EarlyWarningIndicator.insert (1.0, Data[0][Keys['EarlyWarningIndicator']])  
                
                logging.info ('VIEW Finished Risk Approach Refresh')
                
class subFrame_RiskRegister (Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                RiskRegisterTreeFrame = Risk_Register_TreeFrame(self)
                RiskRegisterBreakDownFrame = Risk_Register_Breakdown(self)
                RiskRegisterTreeFrame.pack()
                RiskRegisterBreakDownFrame.pack()                   
                
                
                
        #Risk - Register - Tree
        
class Risk_Register_TreeFrame (Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                lb_RiskReg_Tree = Label(self, text = 'Risk Register', bg = _BGC).pack()        
        
        
        #Risk - Register - BreakdownFrame
class Risk_Register_Breakdown (Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                lb_RiskReg_BreakDown = Label(self, text = 'Risk Details', bg = _BGC).pack()                
                tr_RiskTree = RisksTree(self).pack()
        
class RisksTree (ttk.Treeview):
        def __init__ (self, master):
                super().__init__(master)
                self['columns'] = ('BusinessCode', 'Title', 'Category', 'Impact', 'ResponseCategory', 'Status', 'Owner')
                #self.width = 100
                #self.height = 200
                #self.master=master
                self.heading ('#0', text = 'Code', anchor = 'w')
                self.heading ('BusinessCode', text = 'Business Code', anchor = 'w')
                self.heading ('Title', text = 'Title', anchor = 'w')
                self.heading ('Category', text = 'Category', anchor = 'w')
                self.heading ('Impact', text = 'Impact', anchor = 'w')
                self.heading ('ResponseCategory', text = 'ResponseCategory', anchor = 'w')
                self.heading ('Status', text = 'Status', anchor = 'w')
                self.heading ('Owner', text = 'Owner', anchor = 'w')




                #self.column('#0', width = 60)
                #self.column('BusinessCode', width = 100)            
                #self.column('Title', width = 250)
                #self.column('Category', width = 250)
                #self.column('Measurement', width = 350)
                #self.column('Responsibility', width = 350)
                #self.column('ResourseRequirements', width = 200)
                #self.column('Baseline', width = 200)





                self.pack()
                self.Refresh()
                #self.bind("<Double-1>", self.OnDoubleClick)
        
                #Business Case - ProjectProduct - BreakdownFrame        
        def Refresh (self):
                #print ('Portfolio tree method refresh')
                global _activeProject
                
                logging.info ('VIEW Starting Risk Register Refresh')
                
                Keys, Data = controller.RefreshBusinessObject('RiskRegister', _activeProject)#  - change id to project id    !!!
                #print (Keys) 
                #print (Data)

                for item in Data:
                        self.insert('',item[0], text=item[0], values=[
                                item[Keys['BusinessID']],
                                item[Keys['Title']],
                                item[Keys['Category']],
                                item[Keys['Impact']],
                                item[Keys['ResponseCategory']],
                                item[Keys['Status']],
                                item[Keys['Owner']]
                        ]) 
                logging.info ('VIEW Finished Risk Register Refresh')


# TAB   :   Change
class ChangeTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                ChangeApproach = subFrame_ChangeApproach(self)
                ChangeRegister = subFrameChangeRegister(self)
                self.add(ChangeApproach, text = 'Change Approach')
                self.add(ChangeRegister, text = 'Issue Register')
                
                
class subFrame_ChangeApproach(Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
             
                
                self.lb_Introduction = Label(self, text = 'Introduction:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Procedure = Label(self, text = 'Procedure:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Techniques = Label(self, text = 'Techniques:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Records = Label(self, text = 'Records:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Reporting = Label(self, text = 'Reporting:', width = 90, justify = LEFT, bg = _BGC)
                                
                
                self.txt_Introduction = Text(self, width = 90, height = 12)
                self.txt_Procedure = Text(self, width = 90, height = 12)
                self.txt_Techniques = Text(self, width = 90, height = 12)
                self.txt_Records = Text(self, width = 90, height = 12)
                self.txt_Reporting = Text(self, width = 90, height = 12)
                
                self.lb_Introduction.grid(row = 0, column = 0)
                self.txt_Introduction.grid(row = 1, column = 0)
                self.lb_Procedure.grid(row = 2, column = 0)
                self.txt_Procedure.grid(row = 3, column = 0)
                self.lb_Techniques.grid(row = 4, column = 0)
                self.txt_Techniques.grid(row = 5, column = 0)
                
                self.lb_Records.grid(row = 0, column = 1)
                self.txt_Records.grid(row = 1, column = 1)
                self.lb_Reporting.grid(row = 2, column = 1)
                self.txt_Reporting.grid(row = 3, column = 1)     
                
                self.Refresh()
                
        def Refresh(self):
                global _activeProject
                logging.info ('VIEW Starting Change Approach Refresh')
                Keys, Data = controller.RefreshBusinessObject('ChangeApproach', _activeProject)#  - change id to project id    !!!
                
                self.txt_Introduction.insert (1.0, Data[0][Keys['Introduction']])
                self.txt_Procedure.insert (1.0, Data[0][Keys['Procedure']])
                self.txt_Techniques.insert (1.0, Data[0][Keys['Techniques']])
                self.txt_Records.insert (1.0, Data[0][Keys['Records']])
                self.txt_Reporting.insert (1.0, Data[0][Keys['Reporting']])
                #self.txt_Timing.insert (1.0, Data[0][Keys['Timing']])
                logging.info ('VIEW Finished Change Approach Refresh')
                
class subFrameChangeRegister(Frame):
        def __init__(self, master):
                super().__init__(master) 
                self.config (bg = _BGC)
                ChangeRegisterTreeFrame = Change_Register_TreeFrame(self)
                ChangeRegisterBreakDownFrame = Change_Register_BreakDown(self)
                ChangeRegisterTreeFrame.pack()
                ChangeRegisterBreakDownFrame.pack()                            
                
        #Change - Register - Tree
class Change_Register_TreeFrame (Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                lb_ChangeReg_Tree = Label(self, text = 'Issue Register').pack()   
                tr_IssuesTree = IssuesTree(self).pack()
                
class IssuesTree (ttk.Treeview):
        def __init__ (self, master):
                super().__init__(master)
                self['columns'] = ('BusinessCode', 'Title', 'Category', 'Status')
                #self.width = 100
                #self.height = 200
                #self.master=master
                self.heading ('#0', text = 'Code', anchor = 'w')
                self.heading ('BusinessCode', text = 'Business Code', anchor = 'w')
                self.heading ('Title', text = 'Title', anchor = 'w')
                self.heading ('Category', text = 'Category', anchor = 'w')
                self.heading ('Status', text = 'Status', anchor = 'w')
                #self.heading ('Responsibility', text = 'Responsibility', anchor = 'w')
                #self.heading ('ResourseRequirements', text = 'Resourse Requirements', anchor = 'w')
                #self.heading ('Baseline', text = 'Baseline', anchor = 'w')
                
                
                
                
                #self.column('#0', width = 60)
                #self.column('BusinessCode', width = 100)            
                #self.column('Title', width = 250)
                #self.column('Category', width = 250)
                #self.column('Measurement', width = 350)
                #self.column('Responsibility', width = 350)
                #self.column('ResourseRequirements', width = 200)
                #self.column('Baseline', width = 200)
                
                
                
                
                
                self.pack()
                self.Refresh()
                #self.bind("<Double-1>", self.OnDoubleClick)

        #Business Case - ProjectProduct - BreakdownFrame        
        def Refresh (self):
                logging.info ('VIEW Starting Issue tree refresh')
                global _activeProject
                Keys, Data = controller.RefreshBusinessObject('Issue', _activeProject)#  - change id to project id    !!!
                #logging.debug ('Refresh Issue Keys: ', Keys) 
                #logging.debug ('Refresh Issue Data: ', Data)
                
                for item in Data:
                        self.insert('',item[0], text=item[0], values=[
                                item[Keys['BusinessID']],
                                item[Keys['Title']],
                                item[Keys['Category']],
                                item[Keys['Status']]
                                #Data[0][Keys['Measurement']],
                                #Data[0][Keys['Responsibility']]
                        ])   
                logging.info ('VIEW Finished Issue tree Refresh')
                
        #Change - Register - BreakdownFrame
class Change_Register_BreakDown (Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                lb_ChangeReg_BreakDown = Label(self, text = 'Issue Details').pack()    
                
                
# TAB   :   Communication
class CommunicationTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                CommunicationApproach = subFrame_CommunicationApproach(self)
                self.add(CommunicationApproach, text = 'Communication Approach')
                #pass
                
class subFrame_CommunicationApproach(Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                self.lb_Introduction = Label(self, text = 'Introduction:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Procedure = Label(self, text = 'Procedure:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Techniques = Label(self, text = 'Techniques:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Records = Label(self, text = 'Records:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Reporting = Label(self, text = 'Reporting:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Timing = Label(self, text = 'Timing:', width = 90, justify = LEFT, bg = _BGC)
                                                                                                
                
                self.txt_Introduction = Text(self, width = 90, height = 12)
                self.txt_Procedure = Text(self, width = 90, height = 12)
                self.txt_Techniques = Text(self, width = 90, height = 12)
                self.txt_Records = Text(self, width = 90, height = 12)
                self.txt_Reporting = Text(self, width = 90, height = 12)
                self.txt_Timing = Text(self, width = 90, height = 12)
                
                self.lb_Introduction.grid(row = 0, column = 0)
                self.txt_Introduction.grid(row = 1, column = 0)
                self.lb_Procedure.grid(row = 2, column = 0)
                self.txt_Procedure.grid(row = 3, column = 0)
                self.lb_Techniques.grid(row = 4, column = 0)
                self.txt_Techniques.grid(row = 5, column = 0)
                
                self.lb_Records.grid(row = 0, column = 1)
                self.txt_Records.grid(row = 1, column = 1)
                self.lb_Reporting.grid(row = 2, column = 1)
                self.txt_Reporting.grid(row = 3, column = 1)
                self.lb_Timing.grid(row = 4, column = 1)
                self.txt_Timing.grid(row = 5, column = 1)
                
                self.Refresh()
                      
        def Refresh(self):
                global _activeProject
                logging.info ('VIEW Starting Communication Approach Refresh')
                Keys, Data = controller.RefreshBusinessObject('CommunicationApproach', _activeProject)#  - change id to project id    !!!
                #logging.debug ('Refreshing 
                self.txt_Introduction.insert (1.0, Data[0][Keys['Introduction']])
                self.txt_Procedure.insert (1.0, Data[0][Keys['Procedure']])
                self.txt_Techniques.insert (1.0, Data[0][Keys['Techniques']])
                self.txt_Records.insert (1.0, Data[0][Keys['Records']])
                self.txt_Reporting.insert (1.0, Data[0][Keys['Reporting']])
                self.txt_Timing.insert (1.0, Data[0][Keys['Timing']])
                logging.info ('VIEW Finished Communication Approach Refresh')
                
                
                
# TAB   :   DailyLog

# TAB   :   Quality
class QualityTabControl (ttk.Notebook):
        def __init__(self, master):
                super().__init__(master)
                QualityApproach = subFrame_QualityApproach(self)
                self.add(QualityApproach, text = 'Quality Approach')
                #pass
                
class subFrame_QualityApproach(Frame):
        def __init__(self, master):
                super().__init__(master)
                self.config (bg = _BGC)
                
                self.lb_Introduction = Label(self, text = 'Introduction:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Procedure = Label(self, text = 'Procedure:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_ProjectQuality = Label(self, text = 'Project Quality:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Techniques = Label(self, text = 'Techniques:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Records = Label(self, text = 'Records:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Reporting = Label(self, text = 'Reporting:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_Timing = Label(self, text = 'Timing:', width = 90, justify = LEFT, bg = _BGC)
                self.lb_RolesResponsibilities = Label(self, text = 'Roles and Responsibilities:', width = 90, justify = LEFT, bg = _BGC)
                                                                                                
                
                self.txt_Introduction = Text(self, width = 90, height = 12)
                self.txt_Procedure = Text(self, width = 90, height = 12)
                self.txt_ProjectQuality = Text(self, width = 90, height = 12)
                self.txt_Techniques = Text(self, width = 90, height = 12)
                self.txt_Records = Text(self, width = 90, height = 12)
                self.txt_Reporting = Text(self, width = 90, height = 12)
                self.txt_Timing = Text(self, width = 90, height = 12)
                self.txt_RolesResponsibilities = Text(self, width = 90, height = 12)
                
                self.lb_Introduction.grid(row = 0, column = 0)
                self.txt_Introduction.grid(row = 1, column = 0)
                self.lb_Procedure.grid(row = 2, column = 0)
                self.txt_Procedure.grid(row = 3, column = 0)
                self.lb_ProjectQuality.grid(row = 4, column = 0)
                self.txt_ProjectQuality.grid(row = 5, column = 0)
                self.lb_Techniques.grid(row = 6, column = 0)
                self.txt_Techniques.grid(row = 7, column = 0)
                
                self.lb_Records.grid(row = 0, column = 1)
                self.txt_Records.grid(row = 1, column = 1)
                self.lb_Reporting.grid(row = 2, column = 1)
                self.txt_Reporting.grid(row = 3, column = 1)
                self.lb_Timing.grid(row = 4, column = 1)
                self.txt_Timing.grid(row = 5, column = 1)
                self.lb_RolesResponsibilities.grid(row = 6, column = 1)
                self.txt_RolesResponsibilities.grid(row = 7, column = 1)
                
                
                self.Refresh()
                      
        def Refresh(self):
                global _activeProject
                logging.info ('VIEW Starting Quality Approach Refresh')
                Keys, Data = controller.RefreshBusinessObject('QualityApproach', _activeProject)#  - change id to project id    !!!
                #logging.debug ('Refresh Quality Approach Keys:', Keys)
                #logging.debug ('Refresh Quality Approach Data:', Data)
                self.txt_Introduction.insert (1.0, Data[0][Keys['Introduction']])
                self.txt_Procedure.insert (1.0, Data[0][Keys['Procedure']])
                self.txt_ProjectQuality.insert (1.0, Data[0][Keys['ProjectQuality']])
                self.txt_Techniques.insert (1.0, Data[0][Keys['Techniques']])
                self.txt_Records.insert (1.0, Data[0][Keys['Records']])
                self.txt_Reporting.insert (1.0, Data[0][Keys['Reporting']])
                self.txt_Timing.insert (1.0, Data[0][Keys['Timing']])
                self.txt_RolesResponsibilities.insert (1.0, Data[0][Keys['RolesResponsibilities']])
                logging.info ('VIEW Finished Quality Approach Refresh')
                
                
def Main ():
        logging.basicConfig(filename='logging.txt',level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M', filemode='w')
        X = ProjectApp()
        X.mainloop()


if __name__ == '__main__':
        Main()
        
