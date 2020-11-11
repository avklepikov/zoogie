
DB_DATABASE={
        'filename': 'ProjectApp.db'}

DB_FIELDS_MAPPING ={                                #Class attributes -> Db Fields
        'Product': {
                'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                'BusinessID': ['BusinessID', 'TEXT'],
                'RelatedProject': ['RelatedProject', 'INTEGER'],
                'Title': ['Title', 'TEXT'],
                'Description': ['Description', 'TEXT'],
                'Purpose': ['Purpose', 'TEXT'],
                'Composition': ['Composition', 'TEXT'],
                'Derivation': ['Derivation', 'TEXT'],
                'FormatPresentation': ['FormatPresentation', 'TEXT'],
                'DevSkills': ['DevSkills', 'TEXT'],
                'Category': ['Category', 'TEXT'],
                'Status': ['Status', 'TEXT'],
                'AcceptanceCriterias': ['AcceptanceCriterias', 'TEXT'],
                'ParentID':['ParentID', 'INTEGER']},
        
        'Benefit':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                   'BusinessID': ['BusinessID', 'TEXT'],
                   'RelatedProject': ['RelatedProject', 'INTEGER'],
                   'Title': ['Title', 'TEXT'],
                   'Description':['Description', 'TEXT'],
                   'Category': ['Category', 'TEXT'],
                   'Measurement': ['Measurement', 'TEXT'],
                   'Responsibility': ['Responsibility', 'TEXT'],
                   'ResourceRequirements': ['ResourceRequirements', 'TEXT'],
                   'Baseline': ['Baseline', 'TEXT']},
        
        'ProjectApproach':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                     'RelatedProject': ['RelatedProject', 'INTEGER'],
                     'ExternalDependency': ['ExternalDependency', 'TEXT'],
                     'IndustrySolutions': ['IndustrySolutions', 'TEXT'],
                     'OperationalEnvironment': ['OperationalEnvironment', 'TEXT'],
                     'SecurityConstrains': ['SecurityConstrains', 'TEXT'],
                     'DeliveryApproach': ['DeliveryApproach', 'TEXT'],
                     'TrainingNeeds': ['TrainingNeeds', 'TEXT']},
        
        'BusinessCase':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                        'RelatedProject': ['RelatedProject', 'INTEGER'],
                        'ExecutiveSummary': ['ExecutiveSummary', 'TEXT'],
                        'Reasons': ['Reasons', 'TEXT'],
                        'Options':['Options', 'TEXT'],
                        'ExpectedBenefits': ['ExpectedBenefits', 'TEXT'],
                        'ExpectedDisBenefits': ['ExpectedDisBenefits', 'TEXT'],
                        'Timescale': ['Timescale', 'TEXT'],
                        'Costs': ['Costs', 'TEXT'],
                        'InvestmentArraisal': ['InvestmentArraisal', 'TEXT']}, 
        
        'DailyLog':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                    'BusinessID': ['BusinessID', 'TEXT'],
                    'RelatedProject': ['RelatedProject', 'INTEGER'],
                    'RaisedDate': ['RaisedDate', 'TEXT'],
                    'Category': ['Category', 'TEXT'],
                    'Description': ['Description', 'TEXT'],
                    'Responsible': ['Responsible', 'TEXT'],
                    'TargetDate': ['TargetDate', 'TEXT'],
                    'Status': ['Status', 'TEXT'],
                    'Results': ['Results', 'TEXT']}, 
        
        'ErrorRegister':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                         'BusinessID': ['BusinessID', 'TEXT'],
                         'RelatedProject': ['RelatedProject', 'INTEGER'],
                         'RelatedProduct': ['RelatedProduct', 'TEXT'],
                         'Title': ['Title', 'TEXT'],
                         'Description': ['Description', 'TEXT'],
                         'RaisedBy': ['RaisedBy', 'TEXT'],
                         'RaisedDate': ['RaisedDate', 'TEXT'],
                         'ClosedDate': ['ClosedDate', 'TEXT'],
                         'Status': ['Status', 'TEXT']}, 
        
        'Issue':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                 'BusinessID': ['BusinessID', 'TEXT'],
                 'RelatedProject': ['RelatedProject', 'INTEGER'],
                 'Title': ['Title', 'TEXT'],
                 'Category': ['Category', 'TEXT'],
                 'DateRaised': ['DateRaised', 'TEXT'],
                 'RaisedBy': ['RaisedBy', 'TEXT'],
                 'IssueAuthor': ['IssueAuthor', 'TEXT'],
                 'Description': ['Description', 'TEXT'],
                 'Priority': ['Priority', 'TEXT'],
                 'Severity': ['Severity', 'TEXT'],
                 'Status': ['Status', 'TEXT'],
                 'ClosureDate': ['ClosureDate', 'TEXT']}, 
        
        'Lesson':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                  'BusinessID': ['BusinessID', 'TEXT'],
                  'RelatedProject': ['RelatedProject', 'INTEGER'],
                  'Title': ['Title', 'TEXT'],
                  'Description': ['Description', 'TEXT'],
                  'Category': ['Category', 'TEXT'],
                  'CategoryProcess': ['CategoryProcess', 'TEXT'],
                  'Event': ['Event', 'TEXT'],
                  'Effect': ['Effect', 'TEXT'],
                  'CauseTrigger': ['CauseTrigger', 'TEXT'],
                  'EarlyWarningIndicator': ['EarlyWarningIndicator', 'TEXT'],
                  'Recommendations': ['Recommendations', 'TEXT'],
                  'DateLogged': ['DateLogged', 'TEXT'],
                  'LoggedBy': ['LoggedBy', 'TEXT'],
                  'Priority': ['Priority', 'TEXT']}, 
        
        'Mandate':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                   'Mandate': ['Mandate', 'TEXT'],
                   'RelatedProject': ['RelatedProject', 'INTEGER']}, 
        
        
        'ProjectBrief':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                        'RelatedProject': ['RelatedProject', 'INTEGER'],
                        'Background': ['Background', 'TEXT'],
                        'ObjectiveTime': ['ObjectiveTime', 'TEXT'],
                        'ObjectiveCost': ['ObjectiveCost', 'TEXT'],
                        'ObjectiveQuality': ['ObjectiveQuality', 'TEXT'],
                        'ObjectiveScope': ['ObjectiveScope', 'TEXT'],
                        'ObjectiveBenefits': ['ObjectiveBenefits', 'TEXT'],
                        'ObjectiveRisks': ['ObjectiveRisks', 'TEXT'],
                        'Outcomes': ['Outcomes', 'TEXT'],
                        'Scope': ['Scope', 'TEXT'],
                        'ConstrainsAssumptions': ['ConstrainsAssumptions', 'TEXT'],
                        'ToleranceTime': ['ToleranceTime', 'TEXT'],
                        'ToleranceCost': ['ToleranceCost', 'TEXT'],
                        'ToleranceQuality': ['ToleranceQuality', 'TEXT'],
                        'ToleranceScope': ['ToleranceScope', 'TEXT'],
                        'ToleranceBenefits': ['ToleranceBenefits', 'TEXT'],
                        'ToleranceRisks': ['ToleranceRisks', 'TEXT'],
                        'Stakeholders': ['Stakeholders', 'TEXT'],
                        'ProjectApproach': ['ProjectApproach', 'TEXT']}, 
        
        'QualityApproach':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                           'RelatedProject': ['RelatedProject', 'INTEGER'],
                           'Introduction': ['Introduction', 'TEXT'],
                           'Procedure': ['Procedure', 'TEXT'],
                           'ProjectQuality': ['ProjectQuality', 'TEXT'],
                           'Techniques': ['Techniques', 'TEXT'],
                           'Records': ['Records', 'TEXT'],
                           'Reporting': ['Reporting', 'TEXT'],
                           'Timing': ['Timing', 'TEXT'],
                           'RolesResponsibilities': ['RolesResponsibilities', 'TEXT']}, 
        
        'QualityRegister':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                           'BusinessID': ['BusinessID', 'TEXT'],
                           'RelatedProject': ['RelatedProject', 'INTEGER'],
                           'RelatedProduct': ['RelatedProduct', 'INTEGER'],
                           'Title': ['Title', 'TEXT'],
                           'Method': ['Method', 'TEXT'],
                           'RolesResponsibilities': ['RolesResponsibilities', 'TEXT'],
                           'Dates': ['Dates', 'TEXT'],
                           'Result': ['Result', 'TEXT'],
                           'Status': ['Status', 'TEXT']}, 
        
        'RiskApproach':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                        'RelatedProject': ['RelatedProject', 'INTEGER'],
                        'Introduction': ['Introduction', 'TEXT'],
                        'Procedure': ['Procedure', 'TEXT'],
                        'Techniques': ['Techniques', 'TEXT'],
                        'Records': ['Records', 'TEXT'],
                        'Reporting': ['Reporting', 'TEXT'],
                        'Timing': ['Timing', 'TEXT'],
                        'RolesResponsibilities': ['RolesResponsibilities', 'TEXT'],
                        'Scales': ['Scales', 'TEXT'],
                        'Proxomity': ['Proxomity', 'TEXT'],
                        'Category': ['Category', 'TEXT'],
                        'ResponseCategory': ['ResponseCategory', 'TEXT'],
                        'EarlyWarningIndicator': ['EarlyWarningIndicator', 'TEXT']}, 
        
        'RiskRegister':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                        'BusinessID': ['BusinessID', 'TEXT'],
                        'RelatedProject': ['RelatedProject', 'INTEGER'],
                        'Title': ['Title', 'TEXT'],
                        'RiskEvent': ['RiskEvent', 'TEXT'],
                        'RiskEffect': ['RiskEffect', 'TEXT'],
                        'Author': ['Author', 'TEXT'],
                        'RaisedDate': ['RaisedDate', 'TEXT'],
                        'Category': ['Category', 'TEXT'],
                        'Description': ['Description', 'TEXT'],
                        'Probability': ['Probability', 'TEXT'],
                        'Impact': ['Impact', 'TEXT'],
                        'ExpectedValue': ['ExpectedValue', 'TEXT'],
                        'Proximity': ['Proximity', 'TEXT'],
                        'ResponseCategory': ['ResponseCategory', 'TEXT'],
                        'Response': ['Response', 'TEXT'],
                        'Status': ['Status', 'TEXT'],
                        'Owner': ['Owner', 'TEXT'],
                        'Actionee': ['Actionee', 'TEXT']}, 
        
        'Stakeholder':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                       'RelatedProject': ['RelatedProject', 'INTEGER'],
                       'CurrentRel': ['CurrentRel', 'TEXT'],
                       'Interfaces': ['Interfaces', 'TEXT'],
                       'KeyMessages': ['KeyMessages', 'TEXT'],
                       'InfoToProject': ['InfoToProject', 'TEXT'],
                       'InfoFromProject': ['InfoFromProject', 'TEXT'],
                       'Name': ['Name', 'TEXT'],
                       'EMail': ['EMail', 'TEXT'],
                       'Phone': ['Phone', 'TEXT'],
                       'Birthday': ['Birthday', 'TEXT'],
                       'SupportLevel': ['SupportLevel', 'TEXT'],
                       'InfluenceLevel': ['InfluenceLevel', 'TEXT'],
                       'Interests': ['Interests', 'TEXT']}, 
        
        'WorkPackage':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],  # PRODUCT ID?
                       'BusinessID': ['BusinessID', 'TEXT'],
                       'RelatedProject': ['RelatedProject', 'INTEGER'],
                       'DateAgreement': ['DateAgreement', 'TEXT'],
                       'TeamManager': ['TeamManager', 'TEXT'],
                       'WP': ['WP', 'TEXT'],
                       'DevInterfaces': ['DevInterfaces', 'TEXT'],
                       'OpsInterfaces': ['OpsInterfaces', 'TEXT'],
                       'ChangeControl': ['ChangeControl', 'TEXT'],
                       'JointAgreements': ['JointAgreements', 'TEXT'],
                       'Tolerances': ['Tolerances', 'TEXT'],
                       'Constrains': ['Constrains', 'TEXT'],
                       'ReportingRequirements': ['ReportingRequirements', 'TEXT'],
                       'ProblemHandlingEscalation': ['ProblemHandlingEscalation', 'TEXT'],
                       'ApprovalMethod': ['ApprovalMethod', 'TEXT']}, 
        
        'Stage':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                 'RelatedProject': ['RelatedProject', 'INTEGER'],
                 'StartDate': ['StartDate', 'TEXT'],
                 'EndDate': ['EndDate', 'TEXT'],
                 'Status': ['Status', 'TEXT'],
                 'Title': ['Title', 'TEXT'],
                 'Category': ['Category', 'TEXT']}, 
        
        'CommunicationApproach':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'], 
                                 'RelatedProject': ['RelatedProject', 'INTEGER'],
                                 'Introduction': ['Introduction', 'TEXT'],
                                 'Procedure': ['Procedure', 'TEXT'],
                                 'Techniques': ['Techniques', 'TEXT'],
                                 'Records': ['Records', 'TEXT'],
                                 'Reporting': ['Reporting', 'TEXT'],
                                 'Timing': ['Timing', 'TEXT'],
                                 'RolesResponsibilities': ['RolesResponsibilities', 'TEXT']}, 
        
        'Team':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                'RelatedProject': ['RelatedProject', 'INTEGER'],
                'Person': ['Person', 'TEXT'],
                'Role': ['Role', 'TEXT'],
                'Responsibilities': ['Responsibilities', 'TEXT']}, 
        
        'ChangeApproach':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                          'Introduction': ['Introduction', 'TEXT'],
                          'RelatedProject': ['RelatedProject', 'INTEGER'],
                          'Procedure': ['Procedure', 'TEXT'],
                          'Techniques': ['Techniques', 'TEXT'],
                          'Records': ['Records', 'TEXT'],
                          'Reporting': ['Reporting', 'TEXT']},
        
        'BenefitApproach':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],  
                           'RelatedProject': ['RelatedProject', 'INTEGER'],
                           'Introduction': ['Introduction', 'TEXT'],
                           'ManagementActions': ['ManagementActions', 'TEXT'],
                           'Review': ['Review', 'TEXT']},
        
        'QualityCriteria':{'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                           'BusinessID': ['BusinessID', 'TEXT'],
                           'RelatedProject': ['RelatedProject', 'INTEGER'],
                           'RelatedProduct': ['RelatedProduct', 'INTEGER'],
                           'Title': ['Title', 'TEXT'],
                           'Expectation': ['Expectation', 'TEXT'],
                           'Description': ['Description', 'TEXT'],
                           'AcceptCriteria': ['AcceptCriteria', 'TEXT'],
                           'Tolerance': ['Tolerance', 'TEXT'],
                           'Method': ['Method', 'TEXT'],
                           'Responsibility': ['Responsibility', 'TEXT'],
                           'Inspector': ['Inspector', 'TEXT'],
                           'InspectionDate': ['InspectionDate', 'TEXT'],
                           'InspectionStatus': ['InspectionStatus', 'TEXT'],
                           'InspectorCommentary': ['InspectorCommentary', 'TEXT']},
        
        'Project': {'ID': ['ID', 'INTEGER PRIMARY KEY AUTOINCREMENT'],
                    'Project': ['Project', 'TEXT'],
                    'BusinessID': ['BusinessID', 'TEXT'],
                    'TechStatus': ['TechStatus', 'TEXT'],
                    'SnapshotAsOfDate': ['SnapshotAsOfDate', 'TEXT'],
                    'SnapshotBoardConfirmed': ['SnapshotBoardConfirmed', 'TEXT'],
                    'SnapshotCommentary': ['SnapshotCommentary', 'TEXT']}
        
        }
"""Converts (mapping) Class attribute name into database field name  
Instruction: DB_FIELDS_MAPPING[class_name: Str ][attribute_name: str] -> field_name: str"""


DB_TABLE_MAPPING={'Product': 'reg_Product',         #Class            -> Db Table
                  'Benefit': 'reg_Benefits', 
                  'BusinessCase': 'prj_BusinessCase', 
                  'DailyLog': 'reg_daily', 
                  'ErrorRegister': 'reg_Errors', 
                  'Issue': 'reg_issue', 
                  'Lesson': 'reg_lessons', 
                  'Mandate': 'prj_Mandate',
                  'Project': 'reg_Projects',
                  'ProjectApproach': 'ProjectApproach',
                  'ProjectBrief': 'proj_ProjectBrief', 
                  'QualityApproach': 'appr_Quality', 
                  'QualityRegister': 'reg_Quality', 
                  'RiskApproach': 'appr_Risk', 
                  'RiskRegister': 'reg_Risk', 
                  'Stakeholder': 'reg_Stakeholders', 
                  'WorkPackage': 'reg_WP', 
                  'Stage': 'reg_Stages', 
                  'CommunicationApproach': 'appr_Communication', 
                  'Team': 'reg_Team', 
                  'ChangeApproach': 'appr_Change',
                  'BenefitApproach': "appr_Benefits",
                  'QualityCriteria': "reg_QualityCriteria"}

DB_FIELDS_PK={'Product': 'ID',                      #Class            -> Primary Key Db Field
              'Benefit': 'ID', 
              'BusinessCase': 'ID', 
              'DailyLog': 'ID', 
              'ErrorRegister': 'ID', 
              'Issue': 'ID', 
              'Lesson': 'ID', 
              'Mandate': 'ID',
              'Project': 'ID',
              'ProjectBrief': 'ID', 
              'ProjectApproach': 'ID',
              'QualityApproach': 'ID', 
              'QualityRegister': 'ID', 
              'RiskApproach': 'ID', 
              'RiskRegister': 'ID', 
              'Stakeholder': 'ID', 
              'WorkPackage': 'ID', 
              'Stage': 'ID', 
              'CommunicationApproach': 'ID', 
              'Team': 'ID', 
              'ChangeApproach': 'ID',
              'BenefitApproach': "ID",
              'QualityCriteria': "ID"}

def main():
        print(DB_FIELDS_MAPPING['Product']['ID'])
        print(DB_TABLE_MAPPING['Product'])
        print(DB_FIELDS_PK['Product'])

if __name__ == '__main__':
        main()