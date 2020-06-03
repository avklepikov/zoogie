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
        
        X.BusinessCase.Timescale="""
July 2020"""        
        
        
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
        
        X.ChangeApproach.Records = """Issue register is to be maintained in Zoogie PM
Steering committee reviews and approves issue report which is then saved in pdf format"""
        
        
        X.QualityApproach.Introduction = """Quality control is applied to current Project.
All key quality creterias related to Project delivery should be registered and approved by Steering.
Acceptance of project deliveries is based on these defined criterias.
In case all defined criterias are met project can be considered to be ready for closure procedure"""
        
        X.QualityApproach.ProjectQuality = """Project quality is controlled by Head of Project office and Corporate QA by means of presence at steering or project documentation audit"""

        X.QualityApproach.Records = """Acceptance criteria is described in project Brief and Product description
Quality acceptance reviews are scheduled and tracked through Quality register in Zoogie """
        
        X.QualityApproach.Procedure = """Quality criterias initially defined in Project Brief, then developed in details within Product Definitions
Creterias are verified during acceptance events""" 
        
        X.BenefitApproach.Introduction ="""This policy describes scope and actions related to Benefits management related to current Project:
- Target Benefits should be defined at the project Initiation
- Benefits from each project product should be determinez by Senior User and described in Product Description
- Baseline benefits esitmation is responsibility of Senior User
- Realized benefits estimations is responsibility of Senior User
- Control of utilization of Project deliveries to realize Benefits - responsibility of sSenior User and is out of current Project scope"""
        
        #print (X)
        
        X.CommunicationApproach.Introduction = """Communication approach states the rules and procedure applied to project communication. PM is responsible for monitoring that policy is executed."""
        
        X.CommunicationApproach.Procedure = """Reports are prepared by Project Support distributed based on schedule 
Format PDF slide"""

        
        X.CommunicationApproach.Reporting = """Monthly
Exception report
Risk report
Issue Report"""
        
        X.CommunicationApproach.Timing = """Highlight report is to be distributed Monthly"""
        
        
        X.CommunicationApproach.RolesResponsibilities = """PM is responsible for control that reports are produced by Project support"""
        
        X.CommunicationApproach.Records = """All reporting is registered, documentation is stored in Zoogie (next releases)"""
        
        X.RiskApproach.Introduction = """Risk Approach describes methods and procedures how current project manages the risk. Project has a predefined risk-budget which can not be used without approval of Committee for the purposes of risk responses"""
        
        X.RiskApproach.Records = """All identified Risks are to recorded in Risk register for the further processing"""
        
        X.RiskApproach.Reporting = """Risk Report is to be produced by PM in case of High-impact risks
        Risk register is produced for each Steering Committee"""
        
        X.RiskApproach.Procedure = """Risk should be reported by any project participant for further analysis and action. Once a month project manager collects key participants to analyze current register to review new records and to get status on already registered risks"""
        
        X.RiskApproach.Techniques = """Risk budget is calculated based on expected value of the risk expressed in $"""
        
        X.RiskApproach.Category = """Current project approach considers the following risk categories:
- Time
- Cost
- Quality"""
        
        
        
        
        
        
