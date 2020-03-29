import logging
import db


class ProjectObject():   # Unified methods are set in this SuperClass
        """Provides each Project Class with unified methods to read and update the database
        
        Accepted methods:
            append
            update
            delete
            viewItem -> List of Tuples
            viewList -> List of Tuples
        """
        def __init__(self):
                print('done')
        
        
        def append (self):
                print ('append: ', self.__class__.__name__, self.__dict__)
                _sql = db.compile_INSERT_script(self.__class__.__name__, self.__dict__)
                db.executeSQL(_sql)


        def update (self):
                print ('update', self.__class__.__name__, self.__dict__)
                _sql = db.compile_UPDATE_script (self.__class__.__name__, self.__dict__)
                db.executeSQL(_sql)
                
        def delete (self):
                logging.info ('delete: ', self.__class__.__name__, self.__dict__)
                
                
        def viewItem (self, _id):
                #print ('viewitem: ', self.__class__.__name__, self.__dict__)
                _sql = db.complile_SELECT_BY_ITEM_ID(self.__class__.__name__, self.__dict__,_id)
                _data = db.executeSQLget(_sql)
                _dict = {}
                x = 0
                for key in self.__dict__.keys():
                        _dict[key] = x
                        x = x + 1
                
                return _dict, _data                

        def viewProjectRelatedItems (self, _Project_id):
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
                #print ('viewlist: ', self.__class__.__name__, self.__dict__)
                _sql = db.complile_SELECT_ALL(self.__class__.__name__, self.__dict__)
                _data = db.executeSQLget(_sql)
                _dict = {}
                x = 0
                for key in self.__dict__.keys():
                        _dict[key] = x
                        x = x + 1
                
                return _dict, _data



class Benefit (ProjectObject): # OK
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
                
class BenefitApproach (ProjectObject): # OK
        def __init__ (self,
                      RelatedProject: int = None,
                      General: str = None,
                      ManagementActions: str = None,
                      Review: str = None,
                      ID: int = None):
                uper().__init__()
                self.ID = ID
                self.RelatedProject = RelatedProject
                self.General = General
                self.Review = Review
        

class BusinessCase (ProjectObject): # OK
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

class DailyLog (ProjectObject):  #OK
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

class ErrorRegister (ProjectObject):   # OK
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

class Issue (ProjectObject):  # OK
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

class Lesson (ProjectObject):   # OK
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

class Mandate (ProjectObject):   # OK
        def __init__ (self,
                      Mandate: str = None,
                      RelatedProject: int = None,
                      ID: int = None):
                super().__init__()
                self.ID=ID
                self.Mandate=Mandate
                self.RelatedProject=RelatedProject                

class Product (ProjectObject): # OK
        """Provides business attributes related to Product
        ATTRIBUTES
        ----------
        BusinessID: str, 
        RelatedProject: int, 
        Title: str, 
        Purpose: str, 
        Composition: str, 
        Derivation: str, 
        FormatPresentation: str, 
        DevSkills: str, 
        ID: int = None (Optional) - Provided only for records that already exist in the database table
        ParentID: int = None (Optional) - Provided only for the records that have parent product
        
        METHODS:
        SUPERCLASS: Please refer to Superclass Methods for standard methods applied across all Project Classes
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
        

class ProjectBrief (ProjectObject):   # OK
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
               

class QualityApproach (ProjectObject):   # OK
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

class QualityRegister (ProjectObject):   # OK
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

class RiskApproach (ProjectObject):    # OK
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
                self.Category=Category
                self.EarlyWarningIndicator=EarlyWarningIndicator                

class RiskRegister (ProjectObject):   # OK
        def __init__ (self,
                      BusinessID: str = None,
                      RelatedProject: int = None,
                      Title: str = None,
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

class Stakeholder (ProjectObject):   # OK
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

class WorkPackage (ProjectObject):  # OK
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
             

class Stage (ProjectObject):   # OK
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

class CommunicationApproach (ProjectObject):
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

class Team (ProjectObject):   # OK
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

class ChangeApproach (ProjectObject):  # OK
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
                
class QualityCriteria (ProjectObject):  # OK
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
        
class Project (ProjectObject):  # OK
        def __init__ (self,
                      Project: str = None,
                      BusinessID: str = None,
                      ID: int = None):
                self.ID = ID
                self.Project = Project
                self.BusinessID = BusinessID


def Main ():
        #X = Product('BusinessID',123,'title-3','purpose','composition','derivation','format','devskill')
        #X.ID = 1
        #X.update()
        
        Y = Mandate()
        print (Y.viewItem(1))

if __name__ == '__main__':
        Main()