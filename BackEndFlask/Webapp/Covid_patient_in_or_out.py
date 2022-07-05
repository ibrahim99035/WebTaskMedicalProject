from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length

class Corona_in_or_out_form(FlaskForm):
    White_Blood_Cell = FloatField('White Blood Cell Value', validators=[DataRequired()])
    Erythrocyte_Sedimentation_Rate = FloatField('Value of Erythrocyte Sedimentation Rate', validators=[DataRequired()])
    C_Reactive_Protein = StringField('Value of C_Reactive_Protein (-ve or +ve)', validators=[DataRequired()])
    Procalcitonin  = StringField('Procalcitonin value (-ve or +ve)', validators=[DataRequired()])
    #---------------------------------------------------------------------------------------------------------
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    age = StringField('Age', validators=[DataRequired(), Length(min=1, max=2)])
    nationalID = StringField('National ID', validators=[DataRequired(), Length(min=14, max=14)])
    Diabetes = StringField('Diabetes', validators=[Length(min=3, max=10)])
    blood_pressure = StringField('Blood Pressure', validators=[Length(min=3, max=10)])
    covid_19 = StringField('Covid-19', validators=[Length(min=3, max=10)])
    
    patient_pic = FileField('Patient Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    blood_tests_pic = FileField('Blood Tests Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    #---------------------------------------------------------------------------------------------------------
    submit = SubmitField('Confirm')

    
    success = 'The Patient is Healthy And can coming out of the hospital'
    failuer = 'The patient has not recovered yet'

    failuerReason1 = ', White Blood Cells are high in order to treat corona'
    failuerReason2 = ', Sedimentation rate in the Blood is high due to the Presence of infections'
    failuerReason3 = ', C_Reactive Protein is active as a result of the presence of an enemy'
    failuerReason4 = ', There are Blood contamination'
    
    Corona_in_or_out_result = ''

    def checkTheCase(self, White_Blood_Cell, Erythrocyte_Sedimentation_Rate, C_Reactive_Protein, Procalcitonin):
        #tests
        test1 = White_Blood_Cell.data <= 11.0 and Erythrocyte_Sedimentation_Rate.data <= 10.0 and C_Reactive_Protein.data == '-ve' and  Procalcitonin.data == '-ve'
        test2 = White_Blood_Cell.data > 11.0
        test3 = Erythrocyte_Sedimentation_Rate.data > 10.0
        test4 = C_Reactive_Protein.data == '+ve'
        test5 = Procalcitonin.data =='+ve'
        #successs or failed
        if test1:
            Corona_in_or_out_result = self.success
        else:
            Corona_in_or_out_result = self.failuer
        
        if test2:
            Corona_in_or_out_result += self.failuerReason1

        if test3:
            Corona_in_or_out_result += self.failuerReason2

        if test4:
            Corona_in_or_out_result += self.failuerReason3
                    
        if test5:
            Corona_in_or_out_result += self.failuerReason4

        return Corona_in_or_out_result