import logging

from Model import model

def getProjectsList():
        ObjectClass = getattr(model, 'ProjectsList')
        ObjectInstance = ObjectClass() 
        return ObjectInstance

def appendProjectPack(project_name):
        projectPack = model.ProjectPack()
        projectPack.Create(project_name)

def appendProjectObject (_class, _relatedProjectID):
        ObjectClass = getattr(model, _class)
        ObjectInstance = ObjectClass()
        ObjectInstance.RelatedProject = _relatedProjectID
        ObjectInstance.append()
        #print (ObjectInstance)

def deleteProjectObject (_class, _ID):
        ObjectClass = getattr(model, _class)
        ObjectInstance = ObjectClass()
        ObjectInstance.ID = _ID
        ObjectInstance.delete()
        #print (ObjectInstance)        

def GetPredefinedListValues(_class, _attr):
        return model.PREDEFINED_LISTS_OF_VALUES[_class][_attr]

def GetProjectPack(_projectID):
        ProjectPack = model.ProjectPack()
        ProjectPack.Refresh(_projectID)
        return ProjectPack

def GetRegisterItemClass(_class):
        return getattr(model, _class)

def UpdateAttribute(_class, _attr, _id, _attr_value):
        logging.info(f'  CONTROLLER: Starting UpdateAttribute (_class = {_class}, _attr = {_attr}, _id = {_id}, _attr_value = {_attr_value})')
        #print('Controller UpdateAttribute: ', _class, _attr, _id, _attr_value)
        ObjectClass = getattr(model, _class)
        ObjectInstance = ObjectClass()
        ObjectInstance.update_attr(_class, _attr, _id, _attr_value)        
        #model.Project.update_attr(_class, _attr, _id, _attr_value)


def UpdateAttributeList(_class, _attr_list, _id, _attr_value_list):
        logging.info(f'  CONTROLLER: Starting UpdateAttributeList (_class = {_class}, _attr_list = {_attr_list}, _id = {_id}, _attr_value_list = {_attr_value_list})')
        #print('Controller UpdateAttribute: ', _class, _attr_list, _id, _attr_value_list)
        ObjectClass = getattr(model, _class)
        ObjectInstance = ObjectClass()
        ObjectInstance.update_attr_list (_class, _attr_list, _id, _attr_value_list)        
        #model.Project.update_attr(_class, _attr, _id, _attr_value)        
        
        

def RefreshPortfolioList():
        """populates list of portfolio on the MainFrame Portfolio TreeView"""
        logging.info(f'  CONTROLLER: Starting RefreshPortfolioList ()')
        Project = model.Project()
        Keys, Data = Project.viewList()
        #logging.debug('Keys:')
        #logging.debug(Keys)
        #logging.debug('Data:')
        #logging.debug(Data)        
        return Data

#def RefreshMandate(_projectID):
        #Mandate = model.Mandate()
        #Keys, Data = Mandate.viewItem(_projectID)
        #return Data        

def RefreshProjectHead(_projectID):
        logging.info(f'  CONTROLLER: Starting RefreshProjectHead (_projectID = {_projectID}')
        Project = model.Project()
        Keys, Data = Project.viewItem(_projectID)
        #logging.debug('Keys:')
        #logging.debug(Keys)
        #logging.debug('Data:')
        #logging.debug(Data)
        return Keys, Data     

def RefreshBusinessObject(_class, _dbProjectRecordID):
        """retrievs table records related to the specified project ID """
        logging.info(f'  CONTROLLER: Starting RefreshBusinessObject (_class = {_class}, _ID = {_dbProjectRecordID})')
        
        ObjectClass = getattr(model, _class)
        ObjectInstance = ObjectClass()
        Keys, Data = ObjectInstance.viewProjectRelatedItems(_dbProjectRecordID)
        #logging.debug('Keys:')
        #logging.debug(Keys)
        #logging.debug('Data:')
        #logging.debug(Data)
        
        return Keys, Data   

def RefreshBusinessObject_byID(_class, _ID):
        """retrievs table item based on its PK value"""
        logging.info(f'  CONTROLLER: Starting RefreshBusinessObject_byID (_class = {_class}, _ID = {_ID})')
        ObjectClass = getattr(model, _class)
        ObjectInstance = ObjectClass()
        Keys, Data = ObjectInstance.viewItem(_ID)
        #logging.debug('Keys:')
        #logging.debug(Keys)
        #logging.debug('Data:')
        #logging.debug(Data)        
        return Keys, Data   


# --- TESTING PART --- #
def Main ():
        logging.basicConfig(filename='logging.txt',level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M', filemode='w')        
        #appendProjectPack('TestProject2')
        #print (GetPredefinedListValues('RiskRegister', 'Impact'))
        model.Main()
        
if __name__ == '__main__':
        Main ()
        


