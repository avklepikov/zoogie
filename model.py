"""Model.py introduces Project Management related conceptes and artifacts 

Superclass ProjectObject is used to manage general methods:
    append   : to create new item with related data
    update   : update item's data
    delete   : delete item
    viewItem (_id) : to retrieve item's data based on its primary key _id
    viewProjectRelatedItems (_Project_id): to retrieve list of items related to the Project based on its primary key _Project_id
    viewList :
    
Classes: Business name is Project Objects
    ProjectObject    : Superclass with common attributes and methods
    Benefit          : List of benefits which are expected from the Project
    BenefitApproach  : Applied policy by which benefits delivery is managed
    BusinessCase     : Justification to run the project
    DailyLog         : Daily informal records of Project Manager
    ErrorRegister    : List of errors identified during the product acceptance test
    Issue            : Identified problem or change request
    Lesson           : Lesson learned to be taked into account in future
    Mandate          : Mandate from senior management to start the project
    Product          : Project product or subproduct or interim product that is produced by the Project
    ProjectBrief     : Brief formal justification of the Project during Initiation Stage
    QualityApproach  : Applied policy to manage project quality
    QualityRegister  : List of quality acceptance events and their status
    RiskApproach     : Applied policy to manage Project risks
    RiskRegister     : List of identified risks
    Stakeholder      : List of Project stakeholders
    WorkPackage      : Specified amount of work and its output authorized during a stage
    Stage            : Defined time horizont or project phase with a specified delivery
    CommunicationApproach : Applied policy to manage Project communications
    Team             : List of project members
    ChangeApproach   : Applied approach to manage Project changes
    QualityCriteria  : Quality requirement to be met by the project's product
    Project          : Project class around which all other Project object are organized
    
    
"""

import logging
import db        #database connector to run the model on SQLLite DB


PREDEFINED_LISTS_OF_VALUES = {
        'RiskRegister' : {
                'Status' : ['Open', 'Canceled', 'Realised', 'Closed'],
                'Probability': ['High', 'Medium', 'Low'],
                'ResponseCategory' : ['Avoid', 'Expolot', 'Reduce', 'Enhance',  'Share', 'Accept', 'Plan'],
                'Impact': ['High', 'Medium', 'Low'],
                'Category': ['Time', 'Cost', 'Quality', 'Benefits', 'Scope']},
        'Issue': {
                'Category' : ['change request (CR)', 'problem', 'Off-spec'],
                'Priority': ['High', 'Medium', 'Low'],
                'Status': ['Open problem', 'Solved problem', 'CR Awaiting Approval', 'CR Approved by Board', 'CR Approved by PM', 'Open Off-spec', 'Solved Off-Spec', 'Canceled']
        }}       

class ProjectPack():
        def __init__(self):
                self.Project = Project()
                self.Mandate = Mandate()
                self.ProjectBrief = ProjectBrief()
                self.BusinessCase = BusinessCase()
                self.BenefitApproach = BenefitApproach()
                self.QualityApproach = QualityApproach()
                self.RiskApproach = RiskApproach()
                self.CommunicationApproach = CommunicationApproach()
                self.ChangeApproach = ChangeApproach()
                #print ('ProjectPack')
                
        def Refresh (self, _ProjectID: int):
                
                ProjectObjectList = [self.Mandate, 
                                     self.ProjectBrief, 
                                     self.BusinessCase, 
                                     self.BenefitApproach, 
                                     self.QualityApproach, 
                                     self.RiskApproach, 
                                     self.CommunicationApproach, 
                                     self.ChangeApproach
                                     ]
                
                
                dict_sql_result = self.Project.viewItem(_ProjectID)
                #print (dict_project_data)
                for item in self.Project.__dict__:
                        _index = dict_sql_result[0][item]
                        _value = dict_sql_result[1][0][_index]
                        setattr (self.Project, item, _value)
                
                for ProjectObjectListItem in ProjectObjectList:
                        dict_sql_result = ProjectObjectListItem.viewProjectRelatedItems(_ProjectID)
                        ProjectObjectListItem
                        
                        #print ('Object:' , help(ProjectObjectListItem))
                        #print (dict_sql_result[0])
                        #print (dict_sql_result[1])
                        #print ('dict: ', ProjectObjectListItem.__dict__)
                        for item in ProjectObjectListItem.__dict__:
                                #print (item)
                                _index = dict_sql_result[0][item]
                
                                _value = dict_sql_result[1][0][_index]
                
                                setattr (ProjectObjectListItem, item, _value)
                                
                        
        def Create (self, ProjectName: str):
                self.Project.Project=ProjectName
                self.Project.TechStatus='Active'
                success = self._createProjectRecord()
                if success == 1:
                        self._createProjectParts()
                else:
                        pass
                
        
        def _createProjectRecord(self):        
                SQL = db.compile_SELECT_BY_ATTR_VAL('Project', ['ID'], 'Project', self.Project.Project)
                SQL_return = db.executeSQLget(SQL)

                if  len(SQL_return) == 0:
                        
                        self.Project.append()
                        SQL_return = db.executeSQLget(SQL)

                        self.Project.ID = SQL_return[0][0]
                        self.BenefitApproach.RelatedProject = self.Project.ID
                        self.BusinessCase.RelatedProject = self.Project.ID
                        self.ChangeApproach.RelatedProject = self.Project.ID
                        self.CommunicationApproach.RelatedProject = self.Project.ID
                        self.Mandate.RelatedProject = self.Project.ID
                        self.ProjectBrief.RelatedProject = self.Project.ID
                        self.QualityApproach.RelatedProject = self.Project.ID
                        self.RiskApproach.RelatedProject = self.Project.ID
                        return 1
                        
                else:
                        print ('There is an Existing Project with provided Name')
                        return 0
        
        def _createProjectParts(self):
                
                PartsList = [self.BenefitApproach, 
                             self.BusinessCase, 
                             self.ChangeApproach, 
                             self.CommunicationApproach, 
                             self.Mandate, 
                             self.ProjectBrief, 
                             self.QualityApproach,
                             self.RiskApproach
                             ]
                
                for item in PartsList:
                        
                        SQL = db.compile_SELECT_BY_ATTR_VAL(item.__class__.__name__, ['ID'], 'RelatedProject', self.Project.ID)
                        SQL_return = db.executeSQLget(SQL)
                        #print (item.__class__.__name__, SQL_return)
                        if  len(SQL_return) == 0:
                                
                                print (item.__class__.__name__)
                                
                                item.RelatedProject= self.Project.ID
                                item.append()
                                SQL_return = db.executeSQLget(SQL)
                                item.ID = SQL_return[0][0]
                                
                
                
                        
                
        
        def __str__(self):
                print ('=============================')
                print ('     PROJECT DESCRIPTION     ')
                print ('=============================')
                
                print ('\n==========GENERAL===========\n')
                print (self.Project)
                
                print ('\n--------Mandate--------')
                print (self.Mandate)
                
                print ('\n-----Project Brief-----')
                print(self.ProjectBrief)                
                
                print ('\n-----Business Case-----')
                print (self.BusinessCase)
                
                
                
                print ('\n========APPROACHES=========\n')
                print ('-----Benefits Approach-----')
                print (self.BenefitApproach)
                
                
                print ('\n-----Quality Approach-----')
                print(self.QualityApproach)
                
                print ('\n-----Change Approach-----')
                print(self.ChangeApproach)
                
                print ('\n-----Communication Approach-----')
                print (self.CommunicationApproach)  
                
                print ('\n-----Risk Approach-----')
                print (self.RiskApproach)    
                print ('----------')                
                return ('===================================')
        
        

class ProjectObject():   # Unified methods are set in this SuperClass
        """Provides each Project Class with unified methods to read and update the database
        
        Attributes:
        -none-
        
        Methods:
            append
            update
            delete
            viewItem -> List of Tuples
            viewList -> List of Tuples
        """
        def __str__(self):
                #return (str(self.__dict__))
                _Return =""
                for _attr in self.__dict__:
                        _st_attr = _attr + " "*(20 - len(_attr))
                        if self.__dict__[_attr] != None:
                                _Return = _Return + _st_attr + ' : ' +str(self.__dict__[_attr]) + '\n'# + '\n'
                        else:
                                _Return = _Return + _st_attr + ' : .....\n'# + '\n'
                return _Return
        
        def __init__(self):
                #print('done')
                
                pass
        
        
        def append (self):
                """Created a Database record and writes all Project Object attributes into it
                """
                #print ('append: ', self.__class__.__name__, self.__dict__)
                _sql = db.compile_INSERT_script(self.__class__.__name__, self.__dict__)
                db.executeSQL(_sql)


        def update (self):
                """Finds related Project Object record and overwrites all Project Object attributes into it
                """
                print ('update', self.__class__.__name__, self.__dict__)
                _sql = db.compile_UPDATE_script (self.__class__.__name__, self.__dict__)
                db.executeSQL(_sql)
                
        def update_attr (self, _class, _attr, _id, _attr_value):   # NOT COMPLETED
                #logging.info (f'    MODEL Starting update_attr (_class = {_class}, _attr = {_attr}, _id = {_id}, _attr_value = {_attr_value})')
                _sql  = db.compile_SET_ATTR_VALUE_BY_ITEM_ID (_class, _attr, _id, _attr_value)
                db.executeSQL(_sql)
                
                
        def delete (self):
                """Finds related Project Object record and delete it from database
                """                
                logging.info ('delete: ', self.__class__.__name__, self.__dict__)
                
                
        def viewItem (self, _id):
                """Retrieves Project Object item from database based on its ID
                
                Args:
                    _id  (str)  : Record id
                
                Returns:
                    _dict   : attibute names
                    _data   : values
                """
                logging.info (f'    MODEL Starting viewItem (_id = {_id})')
                
                _sql = db.complile_SELECT_BY_ITEM_ID(self.__class__.__name__, self.__dict__,_id)
                _data = db.executeSQLget(_sql)
                _dict = {}
                x = 0
                for key in self.__dict__.keys():
                        _dict[key] = x
                        x = x + 1
                
                return _dict, _data                

        def viewProjectRelatedItems (self, _Project_id):
                """Retrieves Project related Object items from database based on its Project ID
                
                Args:
                    _Project_id  (str)  : Project id
                
                Returns:
                    _dict   : attibute names
                    _data   : values
                """                
                logging.info (f'    MODEL Starting viewProjectRelatedItems (_Project_id = {_Project_id})')
                #print ('viewitem: ', self.__class__.__name__, self.__dict__)
                _sql = db.complile_SELECT_BY_PROJECT_ID(self.__class__.__name__, self.__dict__,_Project_id)
                _data = db.executeSQLget(_sql)
                _dict = {}
                x = 0
                for key in self.__dict__.keys():
                        _dict[key] = x
                        x = x + 1
                
                return _dict, _data                   


        def viewList (self):
                """Returns: Dictionary (attr: index in Datatable); DataTable
                """
                logging.info (f'    MODEL Starting viewList ()')
                #print ('viewlist: ', self.__class__.__name__, self.__dict__)
                _sql = db.complile_SELECT_ALL(self.__class__.__name__, self.__dict__)
                _data = db.executeSQLget(_sql)
                _dict = {}
                x = 0
                for key in self.__dict__.keys():
                        _dict[key] = x
                        x = x + 1
                
                return _dict, _data



class Benefit (ProjectObject):          # OK
        """Superclass object to manage general attributes and methods for all Project Objects (classes)
        
        ===========
        ATTRIBUTES:
        ===========
        
            :ID:                   (int) Item technical ID in database
            :BusinessID:           (str) BusinessID in format accepted by Project Office
            :RelatedProject:       (str) Related Project primary key
            :Title:                (str) Short name of the Benefit
            :Description:          (str) Benefit description
            :Category:             (str) Benefit category
            :Measurement:          (str) How Benefit is measured: technics and units of measure
            :Responsibility:       (str) Who is responsibles of Benefit measurement
            :ResourceRequirements: (str) Resouce required to perform benefit measurement
            :Baseline:             (str) Benefit baseline value defined in the begining of the project
            
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      BusinessID: str = None,
                      RelatedProject: int = None,
                      Title: str = None,
                      Description: str = None,
                      Category:str = None,
                      Measurement: str = None,
                      Responsibility: str = None,
                      ResourceRequirements: str = None,
                      Baseline: str = None,
                      ID: int = None):
                super().__init__()
                self.ID = ID
                self.BusinessID = BusinessID
                self.RelatedProject = RelatedProject
                self.Title = Title
                self.Description = Description
                self.Category = Category
                self.Measurement = Measurement
                self.Responsibility = Responsibility
                self.ResourceRequirements = ResourceRequirements
                self.Baseline = Baseline  
                
                
class BenefitApproach (ProjectObject):  # OK +ProjectPack
        """BenefitApproach  : Applied policy by which benefits delivery is managed
        
        Attributes:
            ID                (int): Item technical ID in database
            RelatedProject    (str): Related Project primary key
            Introduction      (str): Policy text
            ManagementActions (str): Management actions to support execution of stated policy
            Review            (str): 
           
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes   
        """
        def __init__ (self,
                      RelatedProject: int = None,
                      Introduction: str = None,
                      ManagementActions: str = None,
                      Review: str = None,
                      ID: int = None):
                super().__init__()
                self.ID = ID
                self.RelatedProject = RelatedProject
                self.Introduction = Introduction
                self.Review = Review
        

class BusinessCase (ProjectObject):     # OK +ProjectPack
        """Justification to run the project
        
        Attributes:
            ID                    (int): Item technical ID in database 
            RelatedProject        (int): Related Project primary key
            ExecutiveSummary      (str): Few lines explaining project ideas and purpose  
            Reasons               (str): Explained reasons to start the project
            Options               (str): Analysis of available options including running the project and doing nothing
            ExpectedBenefits      (str): Expected Benefits from Project and its products
            ExpectedDisBenefits   (str): Expected DisBenefits from Project and its products
            Timescale             (str): Explanation related to key time line expectations
            Costs                 (str): Explanation of Project costs
            InvestmentArraisal    (str): Who and how approves the investments and based on what criteria 
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        
        def __init__(self,
                     RelatedProject: int = None,
                     ExecutiveSummary: str = None,
                     Reasons: str = None,
                     Options: str = None,
                     ExpectedBenefits: str = None,
                     ExpectedDisBenefits: str = None,
                     Timescale: str = None,
                     Costs: str = None,
                     InvestmentArraisal: str = None,
                     ID: int = None):
                super().__init__()
                self.ID=ID
                self.RelatedProject=RelatedProject
                self.ExecutiveSummary=ExecutiveSummary
                self.Reasons=Reasons
                self.Options=Options
                self.ExpectedBenefits=ExpectedBenefits
                self.ExpectedDisBenefits=ExpectedDisBenefits
                self.Timescale=Timescale
                self.Costs=Costs
                self.InvestmentArraisal=InvestmentArraisal                

class DailyLog (ProjectObject):         # OK
        """Daily informal records of Project Manager
        
        Attributes:
            ID              (int): Item technical ID in database
            BusinessID      (int): BusinessID in format accepted by Project Office
            RelatedProject  (int): Related Project primary key
            RaisedDate      (str): Date of recording
            Category        (str): Category of Record {Event; Problem; Action}
            Description     (str): Description
            Responsible     (str): Responsible for action
            TargetDate      (str): Target date for Actions
            Status          (str): Problem or Action status - {Closed; Canceled}
            Results         (str): Extra explanation of results for problems or events or actions
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      BusinessID: int = None,
                      RelatedProject: int = None,
                      RaisedDate: str = None,
                      Category: str = None,
                      Description: str = None,
                      Responsible: str = None,
                      TargetDate: str = None,
                      Status: str = None,
                      Results: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.BusinessID=BusinessID
                self.RelatedProject=RelatedProject
                self.RaisedDate=RaisedDate
                self.Category=Category
                self.Description=Description
                self.Responsible=Responsible
                self.TargetDate=TargetDate
                self.Status=Status
                self.Results=Results                

class ErrorRegister (ProjectObject):    # OK
        """List of errors identified during the product acceptance test
        
        Attributes:
            ID              (int): Item technical ID in database
            BusinessID      (str): BusinessID in format accepted by Project Office
            RelatedProject  (int): Related Project primary key
            RelatedProduct  (int): Related Product primary key for which error was registered
            Title           (str): Short description
            Description     (str): Long description
            RaisedBy        (str): Person name who found/registered an error
            RaisedDate      (str): Date when error was identified and registered
            ClosedDate      (str): Date when error was solved 
            Status          (str): Current Status {Open, Solved, Closed, Canceled}
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      BusinessID: str = None,
                      RelatedProject: int = None,
                      RelatedProduct: int = None,
                      Title: str = None,
                      Description: str = None,
                      RaisedBy: str = None,
                      RaisedDate: str = None,
                      ClosedDate: str = None,
                      Status: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.BusinessID=BusinessID
                self.RelatedProject=RelatedProject
                self.RelatedProduct=RelatedProduct
                self.Title=Title
                self.Description=Description
                self.RaisedBy=RaisedBy
                self.RaisedDate=RaisedDate
                self.ClosedDate=ClosedDate
                self.Status=Status                

class Issue (ProjectObject):            # OK
        """Identified problem or change request
        
        Attributes:
            ID              (int): Item technical ID in database
            BusinessID      (str): BusinessID in format accepted by Project Office
            RelatedProject  (int): Related Project primary key
            Title           (str): Short description
            Category        (str): Category from {Off-spec, change request, problem}
            DateRaised      (str): Date when error was identified and registered
            RaisedBy        (str):  Person name who found/registered an error
            IssueAuthor     (str): ?
            Description     (str): Long description
            Priority        (str): Priority from {high, medium, low}
            Severity        (str): ?
            Status          (str): Status from {Open, Closed, Canceled}
            ClosureDate     (str): Date of issue closure
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes     
        """
        def __init__ (self,
                      BusinessID: str = None,
                      RelatedProject: int = None,
                      Title: str = None,
                      Category: str = None,
                      DateRaised: str = None,
                      RaisedBy: str = None,
                      IssueAuthor: str = None,
                      Description: str = None,
                      Priority: str = None,
                      Severity: str = None,
                      Status: str = None,
                      ClosureDate: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.BusinessID=BusinessID
                self.RelatedProject=RelatedProject
                self.Title = Title
                self.Category=Category
                self.DateRaised=DateRaised
                self.RaisedBy=RaisedBy
                self.IssueAuthor=IssueAuthor
                self.Description=Description
                self.Priority=Priority
                self.Severity=Severity
                self.Status=Status
                self.ClosureDate=ClosureDate                

class Lesson (ProjectObject):           # OK
        """Lesson learned to be taked into account in other Projects
        
        Attributes:
            ID              (int): Item technical ID in database
            BusinessID      (str): BusinessID in format accepted by Project Office
            RelatedProject  (int): Related Project primary key
            Title           (str): Short description
            Description     (str): Long description
            Category        (str): Category from custom reference table (not-predefined)
            Event           (str): Description of event occurred
            Effect          (str): What effect event had on the project
            CauseTrigger    (str): What what the reason for the event
            EarlyWarningIndicator     (str): Is there any early indicator that event will occurr?
            Recommendations (str): Reccommendations for future projects
            DateLogged      (str): Date when Lesson was logged
            LoggedBy        (str): Person name logged the lesson
            Priority        (str): Priority from {High, Medium, Low}
            
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes
            
        """
        
        def __init__ (self,
                      BusinessID: str = None,
                      RelatedProject: int = None,
                      Title: str = None,
                      Description: str = None,
                      Category: str = None,
                      Event: str = None,
                      Effect: str = None,
                      CauseTrigger: str = None,
                      EarlyWarningIndicator: str = None,
                      Recommendations: str = None,
                      DateLogged: str = None,
                      LoggedBy: str = None,
                      Priority: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.BusinessID=BusinessID
                self.RelatedProject=RelatedProject
                self.Title = Title,
                self.Description = Description
                self.Category=Category
                self.Event=Event
                self.Effect=Effect
                self.CauseTrigger=CauseTrigger
                self.EarlyWarningIndicator=EarlyWarningIndicator
                self.Recommendations=Recommendations
                self.DateLogged=DateLogged
                self.LoggedBy=LoggedBy
                self.Priority=Priority                

class Mandate (ProjectObject):          # OK +ProjectPack
        """Mandate from senior management to start the project
        
        Attributes:
            ID              (int): Item technical ID in database
            RelatedProject  (int): Related Project primary key
            Mandate         (str): Text of mandate email, meeting minutes or other document)
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
            
        """
        def __init__ (self,
                      Mandate: str = None,
                      RelatedProject: int = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.Mandate=Mandate
                self.RelatedProject=RelatedProject                

class Product (ProjectObject):          # OK
        """Project product or subproduct or interim product that is produced by the Project
        Can be Product or related Subproducts
        
        Attributes:
            ID              (int): Item technical ID in database. 
            ParentID        (int): Technical ID of subproduct's parent product in database.
            BusinessID      (str): BusinessID in format accepted by Project Office.
            RelatedProject  (int): Related Project primary key.
            Title           (str): Short product name.
            Description     (str): Product/subproduct detailed description.
            Purpose         (str): What is the purpose of produced product or subproduct.
            Composition     (str): From which parts product consists.
            Derivation      (str): From what raw materials or other artifacts project should be produced.
            FormatPresentation      (str): How product looks like, format, material etc.
            DevSkills       (str): What skills are needed to develop the product. 
            
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes
        """
        
        def __init__ (self,  
                      BusinessID: str = None, 
                      RelatedProject: int = None, 
                      Title: str = None, 
                      Description: str = None,
                      Purpose: str = None, 
                      Composition: str = None, 
                      Derivation: str = None, 
                      FormatPresentation: str = None, 
                      DevSkills: str = None, 
                      ID: int = None,
                      ParentID: int = None):
                
                super().__init__()
                self.ID = ID
                self.BusinessID = BusinessID
                self.RelatedProject=RelatedProject
                self.Title = Title
                self.Description = Description
                self.Purpose = Purpose
                self.Composition = Composition
                self.Derivation = Derivation
                self.FormatPresentation = FormatPresentation
                self.DevSkills = DevSkills
                self.ParentID = ParentID
                
                
        

class ProjectBrief (ProjectObject):     # OK +ProjectPack
        """Brief formal justification of the Project during Initiation Stage
        
        Attributes:
            ID                      (int): Item technical ID in database.
            RelatedProject          (int): Related Project primary key.
            Background              (str): ?
            ObjectiveTime           (str): Target time constrains set for the project
            ObjectiveCost           (str): Target cost/budget constrains set for the project
            ObjectiveQuality        (str): Target quality constrains set for the project
            ObjectiveScope          (str): Target scope constrains set for the project
            ObjectiveBenefits       (str): Target benefits constrains set for the project
            ObjectiveRisks          (str): Target risks constrains set for the project
            Outcomes                (str): Descriptions of project outcomes that will realize stated benefits
            Scope                   (str): Agreed scope under change control
            ConstrainsAssumptions   (str): Assumptions 
            ToleranceTime           (str): Defined tolerance for time constrains delegated to Project Manager
            ToleranceCost           (str): Defined tolerance for cost/buget constrains delegated to Project Manager
            ToleranceQuality        (str): Defined tolerance for quality constrains delegated to Project Manager
            ToleranceScope          (str): Defined tolerance for scope constrains delegated to Project Manager
            ToleranceBenefits       (str): Defined tolerance for benefits constrains delegated to Project Manager
            ToleranceRisks          (str): Defined tolerance for risks constrains delegated to Project Manager
            Stakeholders            (str): Description of major stakeholders for the Project
            ProjectApproach         (str): General rules and concepts defining how the project will be organized and managed
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        
        def __init__ (self,
                      RelatedProject: int = None,
                      Background: str = None,
                      ObjectiveTime: str = None,
                      ObjectiveCost: str = None,
                      ObjectiveQuality: str = None,
                      ObjectiveScope: str = None,
                      ObjectiveBenefits: str = None,
                      ObjectiveRisks: str = None,
                      Outcomes: str = None,
                      Scope: str = None,
                      ConstrainsAssumptions: str = None,
                      ToleranceTime: str = None,
                      ToleranceCost: str = None,
                      ToleranceQuality: str = None,
                      ToleranceScope: str = None,
                      ToleranceBenefits: str = None,
                      ToleranceRisks: str = None,
                      Stakeholders: str = None,
                      ProjectApproach: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.RelatedProject=RelatedProject
                self.Background=Background
                self.ObjectiveTime=ObjectiveTime
                self.ObjectiveCost=ObjectiveCost
                self.ObjectiveQuality=ObjectiveQuality
                self.ObjectiveScope=ObjectiveScope
                self.ObjectiveBenefits=ObjectiveBenefits
                self.ObjectiveRisks=ObjectiveRisks
                self.Outcomes=Outcomes
                self.Scope=Scope
                self.ConstrainsAssumptions=ConstrainsAssumptions
                self.ToleranceTime=ToleranceTime
                self.ToleranceCost=ToleranceCost
                self.ToleranceQuality=ToleranceQuality
                self.ToleranceScope=ToleranceScope
                self.ToleranceBenefits=ToleranceBenefits
                self.ToleranceRisks=ToleranceRisks
                self.Stakeholders=Stakeholders
                self.ProjectApproach=ProjectApproach
               

class QualityApproach (ProjectObject):  # OK +ProjectPack
        """Applied policy to manage project quality
        
        Attributes:
            ID              (int): Item technical ID in database.
            RelatedProject  (int): Related Project primary key.
            Introduction    (str): General introduction to Quality approach related to the Project
            Procedure       (str): Procedure / Policy
            ProjectQuality  (str): How quality of Project management is monitored and contrled. Responsibilities, events, controls
            Techniques      (str): Quality check technics applied in the project
            Records         (str): Records and Registers used to register Quality events, checks and issues
            Reporting       (str): Organization of reporting related to Quality theme. Forms, schedule, responsibility
            Timing          (str): Defined schedule for quality check events
            RolesResponsibilities   (str): Defined responsibilities of Project team to perform Quality checks
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      RelatedProject: int = None,
                      Introduction: str = None,
                      Procedure: str = None,
                      ProjectQuality: str = None,
                      Techniques: str = None,
                      Records: str = None,
                      Reporting: str = None,
                      Timing: str = None,
                      RolesResponsibilities: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.RelatedProject=RelatedProject
                self.Introduction=Introduction
                self.Procedure=Procedure
                self.ProjectQuality=ProjectQuality
                self.Techniques=Techniques
                self.Records=Records
                self.Reporting=Reporting
                self.Timing=Timing
                self.RolesResponsibilities=RolesResponsibilities                

class QualityRegister (ProjectObject):  # OK
        """List of quality acceptance event and its status
        
        Attributes:
            ID                      (int): Item technical ID in database.
            BusinessID              (str): BusinessID in format accepted by Project Office.
            RelatedProject          (int): Related Project primary key.
            RelatedProduct          (str): Which product or subproduct is verified
            Method                  (str): How Quality check will be performed
            RolesResponsibilities   (str): Who will perform quality check
            Dates                   (str): Date of acceptance test
            Result                  (str): Result of acceptance test
            
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      BusinessID: str = None,
                      RelatedProject: int = None,
                      RelatedProduct: str = None,
                      Method: str = None,
                      RolesResponsibilities: str = None,
                      Dates: str = None,
                      Result: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.BusinessID=BusinessID
                self.RelatedProject=RelatedProject
                self.RelatedProduct=RelatedProduct
                self.Method=Method
                self.RolesResponsibilities=RolesResponsibilities
                self.Dates=Dates
                self.Result=Result                

class RiskApproach (ProjectObject):     # -- +ProjectPack             -> correct Attribute Proximity
        """Applied policy to manage Project risks
        
        Attributes:
            ID                      (int): Item technical ID in database.
            RelatedProject          (int): Related Project primary key.
            Introduction            (str): General introduction to the Policy
            Procedure               (str): Organizational procedures to be followed 
            Techniques              (str): What technics should be applied to follow the policy
            Records                 (str): What records are to be set to register identified risks
            Reporting               (str): What reporting should be established with regard to identified / processed risks
            Timing                  (str): Schedule on communication regarding identified risks and related reporting
            RolesResponsibilities   (str): Who is responsible to capture, record, monitor risks nd process actions
            Scales                  (str): Risk Scale applied
            Proxomity               (str): How risk proximity is calculated
            Category                (str): Applied risk categories
            EarlyWarningIndicator   (str): Are there any early indicator that will predict risk event
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes     
        """
        def __init__ (self,
                      RelatedProject: int = None,
                      Introduction: str = None,
                      Procedure: str = None,
                      Techniques: str = None,
                      Records: str = None,
                      Reporting: str = None,
                      Timing: str = None,
                      RolesResponsibilities: str = None,
                      Scales: str = None,
                      Proxomity: str = None,
                      Category: str = None,
                      ResponseCategory: str = None,
                      EarlyWarningIndicator: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.RelatedProject=RelatedProject
                self.Introduction=Introduction
                self.Procedure=Procedure
                self.Techniques=Techniques
                self.Records=Records
                self.Reporting=Reporting
                self.Timing=Timing
                self.RolesResponsibilities=RolesResponsibilities
                self.Scales=Scales
                self.Proxomity=Proxomity
                self.Category=Category
                self.ResponseCategory=ResponseCategory
                self.EarlyWarningIndicator=EarlyWarningIndicator                

class RiskRegister (ProjectObject):     # --                          -> add attr explanation
        """List of identified risks
        
        ===========
        Attributes:
        ===========
        
            :ID:                      (int) Item technical ID in database.
            :BusinessID:              (str) BusinessID in format accepted by Project Office.
            :RelatedProject:          (int) Related Project primary key.
            :Title:                   (str) Short name for identified risk
            :RiskEvent:               (str) Risk Event  <--
            :RiskEffect:              (str) Risk Effect <--
            :Author:                  (str) Name of person who raised the risk
            :RaisedDate:              (str) Date when risk was raised
            :Category:                (str) Risk category from the categories set in Risk Approach
            :Description:             (str) Detailed description of risk
            :Probability:             (str) Probability of risk event
            :Impact:                  (str) Impact on project 
            :ExpectedValue:           (str) ?
            :Proximity:               (str) ?
            :ResponseCategory:        (str) Response to the risk defined in Risk approach
            :Response:                (str) Description of response
            :Status:                  (str) Status {open, canceled, realised, closed}
            :Owner:                   (str) Name of person responsible for the risk item monitoring 
            :Actionee:                (str) Name of person responsible for mitigation action
        
        ========
        Methods:
        ========
        
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      BusinessID: str = None,
                      RelatedProject: int = None,
                      Title: str = None,
                      RiskEvent: str = None,
                      RiskEffect: str = None,
                      Author: str = None,
                      RaisedDate: str = None,
                      Category: str = None,
                      Description: str = None,
                      Probability: str = None,
                      Impact: str = None,
                      ExpectedValue: str = None,
                      Proximity: str = None,
                      ResponseCategory: str = None,
                      Response: str = None,
                      Status: str = None,
                      Owner: str = None,
                      Actionee: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.BusinessID=BusinessID
                self.RelatedProject=RelatedProject
                self.Title = Title
                self.RiskEvent = RiskEvent
                self.RiskEffect = RiskEffect
                self.Author=Author
                self.RaisedDate=RaisedDate
                self.Category=Category
                self.Description=Description
                self.Probability=Probability
                self.Impact=Impact
                self.ExpectedValue=ExpectedValue
                self.Proximity=Proximity
                self.ResponseCategory=Category
                self.Response=Response
                self.Status=Status
                self.Owner=Owner
                self.Actionee=Actionee    
                #self.ShortListAttributes =[self.ID, self.BusinessID, self.Title, self.Category, self.RaisedDate, self.ResponseCategory, self.Owner, self.Status]
                #"""List of attributes shown as lines in the Treeview register"""

class Stakeholder (ProjectObject):      # OK
        """List of Project stakeholders
        
        Attributes:
            ID                      (int): Item technical ID in database.
            RelatedProject          (int): Related Project primary key.
            CurrentRel              (str): Description of current relations with the stakeholder
            Interfaces              (str): What points of joint interest is known, areas of interaction
            KeyMessages             (str): Key messages to deliver to the Stakeholder
            InfoToProject           (str): What kind of information is requered from the Stakeholder to the Project
            InfoFromProject         (str): What kind of information Stakeholder requires from the Project
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __self__ (self,
                      RelatedProject: int = None,
                      CurrentRel: str = None,
                      Interfaces: str = None,
                      KeyMessages: str = None,
                      InfoToProject: str = None,
                      InfoFromProject: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.RelatedProject=RelatedProject
                self.CurrentRel=CurrentRel
                self.Interfaces=Interfaces
                self.KeyMessages=KeyMessages
                self.InfoToProject=InfoToProject
                self.InfoFromProject=InfoFromProject                

class WorkPackage (ProjectObject):      # OK
        """Specified amount of work and its output authorized during a stage
        
        Attributes:
            ID                      (int): Item technical ID in database.
            BusinessID              (str): BusinessID in format accepted by Project Office.
            RelatedProject          (int): Related Project primary key.
            DateAgreement           (str): Date when approval for work delivery was received
            TeamManager             (str): Name of supplier team manager responsible for delivery
            WP                      (str): ?
            DevInterfaces           (str): ?
            OpsInterfaces           (str): ?
            ChangeControl           (str): ?
            JointAgreements         (str): ?
            Tolerances              (str): Agreed accepted tolerances
            Constrains              (str): Constrains to be followed
            ReportingRequirements   (str): How reporting regarding delivery should be organized 
            ProblemHandlingEscalation      (str): Ways of escalation
            ApprovalMethod                 (str): How workpackage should be / was approved
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      BusinessID: str = None,
                      RelatedProject: int = None,
                      DateAgreement: str = None,
                      TeamManager: str = None,
                      WP: str = None,
                      DevInterfaces: str = None,
                      OpsInterfaces: str = None,
                      ChangeControl: str = None,
                      JointAgreements: str = None,
                      Tolerances: str = None,
                      Constrains: str = None,
                      ReportingRequirements: str = None,
                      ProblemHandlingEscalation: str = None,
                      ApprovalMethod: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.BusinessID=BusinessID
                self.RelatedProject=RelatedProject
                self.DateAgreement=DateAgreement
                self.TeamManager=TeamManager
                self.WP=WP
                self.DevInterfaces=DevInterfaces
                self.OpsInterfaces=OpsInterfaces
                self.ChangeControl=ChangeControl
                self.JointAgreements=JointAgreements
                self.Tolerances=Tolerances
                self.Constrains=Constrains
                self.ReportingRequirements=ReportingRequirements
                self.ProblemHandlingEscalation=ProblemHandlingEscalation
                self.ApprovalMethod=ApprovalMethod                
             

class Stage (ProjectObject):            # OK
        """Defined time horizont or project phase with a specified delivery
        
        Attributes:
            
            ID                      (int): Item technical ID in database.
            RelatedProject          (int): Related Project primary key.
            StartDate               (str): Start date of the Project Stage
            EndDate                 (str): End date of the project stage
            Status                  (str): Status of the stage {Scheduled, Active, Replaced, Closed}
            Title                   (str): Short name for the stage
            Category                (str): Stage category from {Initiation, Delivery}
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      RelatedProject: int = None,
                      StartDate: str = None,
                      EndDate: str = None,
                      Status: str = None,
                      Title: str = None,
                      Category: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.RelatedProject=RelatedProject
                self.StartDate=StartDate
                self.EndDate=EndDate
                self.Status=Status
                self.Title=Title
                self.Category=Category                

class CommunicationApproach (ProjectObject):   # OK +ProjectPack
        """Applied policy to manage Project communications
        
        Attributes:
        
            ID                      (int): Item technical ID in database.
            RelatedProject          (int): Related Project primary key.
            Introduction            (str): Introduction to the Policy
            Procedure               (str): Organizational procedure to be followed 
            Techniques              (str): Thechnics used to communicate including communicational channels
            Records                 (str): Records used to register major communication including reporting
            Reporting               (str): What kind of reporting is produced by the project
            Timing                  (str): Reporting schedule
            RolesResponsibilities   (str): Who is responsible for the reporting production
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      RelatedProject: int = None,
                      Introduction: str = None,
                      Procedure: str = None,
                      Techniques: str = None,
                      Records: str = None,
                      Reporting: str = None,
                      Timing: str = None,
                      RolesResponsibilities: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.RelatedProject=RelatedProject
                self.Introduction=Introduction
                self.Procedure=Procedure
                self.Techniques=Techniques
                self.Records=Records
                self.Reporting=Reporting
                self.Timing=Timing
                self.RolesResponsibilities=RolesResponsibilities                

class Team (ProjectObject):             # OK
        """List of project members
        
        Attributes:
            
            ID                      (int): Item technical ID in database.
            RelatedProject          (int): Related Project primary key.
            Person                  (str): Name of the person
            Role                    (str): One of the Roles {Executive, Senior User, Senior Supplier, Project Manager, 
                                                             User, Supplier, Sponsor, Quality Assurance, Project Office}
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      RelatedProject: int = None,
                      Person: str = None,
                      Role: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.RelatedProject=RelatedProject
                self.Person=Person
                self.Role=Role                

class ChangeApproach (ProjectObject):   # OK +ProjectPack
        """Applied approach to manage Project changes
        
        Attributes:
            
            ID                      (int): Item technical ID in database.
            Introduction            (str): General introduction to the policy
            RelatedProject          (int): Related Project primary key.
            Procedure               (str): Organizational procedure followed to control changes
            Techniques              (str): Applied technics to control changes
            Records                 (str): Project records where changes are registered
            Reporting               (str): What kind of reporting used to inform about requested and approved changes
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      Introduction: str = None,
                      RelatedProject: int = None,
                      Procedure: str = None,
                      Techniques: str = None,
                      Records: str = None,
                      Reporting: str = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.Introduction=Introduction
                self.RelatedProject=RelatedProject
                self.Procedure=Procedure
                self.Techniques=Techniques
                self.Records=Records
                self.Reporting=Reporting  
                
class QualityCriteria (ProjectObject):  # --                          -> add attr explanation
        """Quality requirement to be met by the project's product
        
        Attributes:
        
            ID                      (int): Item technical ID in database.
            BusinessID              (str): BusinessID in format accepted by Project Office.
            RelatedProject          (int): Related Project primary key.
            RelatedProduct          (int): ?
            Expectation             (str): Description of expectations from the User / Customer
            Description             (str): ?
            AcceptCriteria          (str): Expectations in terms of criteria
            Tolerance               (str): Possible accepted tollerance around criteria
            Method                  (str): Mthod of estimation of criteria compliance
            Responsibility          (str): Who is responsible to verify criteria
        
        Methods:
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      BusinessID: str = None,
                      RelatedProject: int = None,
                      RelatedProduct: int = None,
                      Expectation: str = None,
                      Description: str = None,
                      AcceptCriteria: str = None,
                      Tolerance: str = None,
                      Method: str = None,
                      Responsibility  : str = None,  
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.BusinessID=BusinessID
                self.RelatedProject=RelatedProject
                self.RelatedProduct=RelatedProduct
                self.Expectation=Expectation
                self.Description=Description
                self.AcceptCriteria=AcceptCriteria
                self.Tolerance=Tolerance
                self.Method=Method
                self.Responsibility=Responsibility
        
class Project (ProjectObject):          # OK +ProjectPack
        """Project class around which all other Project object are organized
        
        ===========
        Attributes:
        ===========
        
            :ID:         (int) Item technical ID in database.
            :Project:    (str) Short name
            :BusinessID: (str) BusinessID in format accepted by Project Office.
            :TechStatus: (str) Technical status tp indicate archived, active, draft and deleted versions of the Project
            
            TechStatus Values:
            
            - Active
            - Draft
            - Deleted
            - Archived
            
        ========
        Methods:
        ========
        
            Please refer to Superclass Methods for standard methods applied across all Project Classes    
        """
        def __init__ (self,
                      Project: str = None,
                      BusinessID: str = None,
                      ID: int = None,
                      TechStatus: str = None):
                super().__init__()
                self.ID = ID
                self.Project = Project
                self.BusinessID = BusinessID
                self.TechStatus = TechStatus
                
                #self.ProjectBrief = ProjectBrief()
                
                #self.BenefitApproach = BenefitApproach()
                #self.BusinessCase = BusinessCase()
                #self.QualityApproach=QualityApproach()
                #self.RiskApproach=RiskApproach()
                #self.CommunicationApproach = CommunicationApproach()
                #self.ChangeApproach = ChangeApproach()
                
                
                


def Main ():
        
        logging.basicConfig(filename='logging.txt',level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M', filemode='w')
        
        X = ProjectPack()
        #X.Refresh(1)
        X.Create('KISPL PROJECT XX4')
        
        #X.ID = 1
        #X.update()
        
        #Y = Mandate()
        #print ('I am alive')
        #print (X)
        #print ('BenefitAppr: ', X.BenefitApproach)
        print (X)

if __name__ == '__main__':
        Main()