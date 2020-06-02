def generate(X: object):
        #X = ProjectPack()
        
        X.Project.Project='Sample: New CRM'
        X.Project.BusinessID='SMP-000'
        X.Project.TechStatus='Published (Current)'
        X.Project.SnapshotBoardConfirmed = 'Yes'
        X.Project.SnapshotAsOfDate = '31-03-2020'
        X.Project.SnapshotCommentary = 'Approved by Steering on 01-04-2020'
        
        X.Mandate.Mandate = """Dear Mr Frankenstein,
        
Kindly initiate a project to create new CRM system
we expect an increase in client base up to 10k by end of next year
        
Project to be opened by end of July, funding from Sales budget
        
Regards
Head of Sales Department, VP

"""
        X.BusinessCase.ExecutiveSummary="""Purchase and installation of new SMART CRM to enable onboarding up to 10k new clients by end of 2021.
Tagret date for project delivery - july 2021"""
        
        X.BusinessCase.ExpectedBenefits="""Keep high standards in communcation with clients
Prevent increase in Sales FTE"""
        
        X.BusinessCase.ExpectedDisBenefits="""
Not identified"""
        
        X.BusinessCase.Costs="""To be covered by Sales Budget
   $1.1 m capital Expenses
   $0.3 k consulting service
        """
        
        X.BusinessCase.Options="""1. Keep working with locally developed DB
Free of charge
High IT risks IT does not support the system
High Business risks in case of system fails

2. CRM BCM Solutions:
$2.0 mio"""
        
        X.ProjectApproach.IndustrySolutions ="""Two widely used systems with positive references:
- SMART CRM (selected)
- BCM Solutions"""
        
        X.ProjectApproach.DeliveryApproach="""Waterfall framework:
- scope of work clearly defined
- implementation time is 3 mo (suits our purpose)"""
        
        X.ProjectApproach.TrainingNeeds="""Local IT needs Hadoop training to efficiently incorporate and support SMART CRM"""
        
        X.ProjectApproach.ExternalDependency="""None"""
        
        X.ProjectBrief.Background = """Our company XYZ in planing expansion to the new markets which will per our estimates incerase client base by 10k by end of 2020.
Current technology applied in Sales Department can not be used for such increase in clients base
In order to meet targets Sales Deaprtment initiates a project to purchase and install new CRM system"""
        
        X.ProjectBrief.ObjectiveQuality="""Currect client based is fully transferred
Target - July 2021"""
        
        X.ProjectBrief.ObjectiveTime = """Target - July 2021
"""
        
        X.ProjectBrief.ObjectiveRisks = """Maximum delay: Oct 2021
Costs not to exceed 120% from initial budjet"""
        
        X.ChangeApproach.Introduction = """Change control is applied for current project.
All events potentially leading to changes in Project are to be registered, reviewed by Steering to make decision"""
        
        X.ChangeApproach.Procedure = """Project Manager, Seniour User or Senior Supplier may raise an issue which is recordeded by Project Manager in Issue Register"""
        
        X.ChangeApproach.Techniques = """Golder version of Issue Register is kept in Zoogie Project application and is used to prepare materioals for Steering"""
        
        X.QualityApproach.Introduction = """Quality control is applied to current Project.
All key quality creterias related to Project delivery should be registered and approved by Steering.
Acceptance of project deliveries is based on these defined criterias.
In case all defined criterias are met project can be considered to be ready for closure procedure"""
        
        X.QualityApproach.Procedure = """Quality criterias initially defined in Project Brief, then developed in details within Product Definitions
Creterias are verified during acceptance events""" 
        
        #print (X)
        
        