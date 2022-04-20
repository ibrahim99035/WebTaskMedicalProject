from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired
class SurgicalOperationForm(FlaskForm):
    #fields
    hemoglopen = FloatField('Hemoglopen', validators=[DataRequired()])
    whiteBlood = FloatField('White Blood', validators=[DataRequired()])
    platelets = FloatField('Platelets', validators=[DataRequired()])
    liver = FloatField('Liver', validators=[DataRequired()])
    kidney = FloatField('Kidney', validators=[DataRequired()])
    fluidity = FloatField('Fluidity', validators=[DataRequired()])
    #basic tests
    test1  = 'Hemoglopen'
    test2  = 'White Blood'
    test3  = 'Platelets'
    test4  = 'Liver'
    test5  = 'Kidney'
    test6  = 'Fluidity'
    #strings
    safe = 'None'
    message = 'The patient has a problem with '
    splited =''
    patientResult = ''
    objectionResult = ''
    qualified = 'The patient is qualified'
    unqualified = 'The patient is not qualified'
    
    #checking patient's results
    def checkpatientResult(self, hemoglopen, whiteBlood, platelets, liver, kidney, fluidity):
        if 9 <= hemoglopen.data <= 11 and 5 <= whiteBlood.data <= 18 and 150000 <= platelets.data <= 350000 and \
        20 <= liver.data <= 40 and 0.5 <= kidney.data <= 1.5 and 0.7 <= fluidity.data <= 1.5:
            patientResult = self.qualified
        else:
            patientResult = self.unqualified
        return patientResult
    
    #checking the patient's objections
    def objections(self, hemoglopen, whiteBlood, platelets, liver, kidney, fluidity):
        #objections 
        objection1 = hemoglopen.data < 9 or hemoglopen.data > 11
        objection2 = whiteBlood.data < 5 or whiteBlood.data > 18
        objection3 = platelets.data < 150000 or platelets.data > 350000
        objection4 = liver.data < 20 or liver.data > 40
        objection5 = kidney.data < 0.5 or kidney.data > 1.5
        objection6 = fluidity.data < 0.7 or fluidity > 1.5
        objectionList = [objection1, objection2, objection3, objection4, objection5, objection6]
        TruesList = []
        problemsList = []
        
        for i in objectionList :
            if i == True :
                TruesList.append(i)
        
        if objection1 in TruesList :
            problemsList.append(self.test1)
        if objection2 in TruesList :
            problemsList.append(self.test2)
        if objection3 in TruesList :
            problemsList.append(self.test3)
        if objection4 in TruesList :
            problemsList.append(self.test4)
        if objection5 in TruesList :
            problemsList.append(self.test5)
        if objection6 in TruesList :
            problemsList.append(self.test6)
        
        if len(problemsList) == 0 :
            objectionResult = self.message + self.safe
        else :
            self.splited = ', '.join(problemsList)
            objectionResult = self.message + self.splited
        return objectionResult
#------------------------------------------------------------------------------
