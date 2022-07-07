from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField, IntegerField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length
class AnemiaForm(FlaskForm):
    Sex = FloatField('The gender (0 or 1) ', validators=[DataRequired()])
    Red_Blood_Cell = FloatField('Red Blood Cell Value', validators=[DataRequired()])
    White_Blood_Cell = FloatField('White Blood Cell Value', validators=[DataRequired()])
    Platelets = FloatField('Platelets Value', validators=[DataRequired()])
    Hemoglobin = FloatField('Hemoglobin Value', validators=[DataRequired()])

    submit = SubmitField('Confirm')
    #-------------------------------------------------------------
    positiveResult = 'The patient is Anemic'
    negativeResult = 'The patient is norAnemic'
    AnemiaResult = ''

    
    #-------------------------------------------------------------
    def checkAnemia(self, Sex, Red_Blood_Cell, White_Blood_Cell, Platelets, Hemoglobin):
        test1 = Sex ==1.0 and 4000000.0 <= Red_Blood_Cell <=5000000.0 and 4000.0 <= White_Blood_Cell <=11000.0 and 150000.0<= Platelets <=400000.0 and 11.0<= Hemoglobin <=16.0
        test2 = Sex ==0.0  and 3650000.0 <= Red_Blood_Cell <=4500000.0 and 4000.0 <= White_Blood_Cell <=11000.0 and 150000.0<= Platelets <=400000.0 and 10.0<= Hemoglobin <=15.0
        test3 = Sex ==1.0 and Red_Blood_Cell <4000000.0 and Hemoglobin<11.0
        test4 = Sex ==0.0 and Red_Blood_Cell <3650000.0 and Hemoglobin<10.0

        if test1 or test2:
            self.AnemiaResult = self.negativeResult
        elif test3 or test4:
            self.AnemiaResult = self.positiveResult
        else:
            self.AnemiaResult = 'invalid input'

        return self.AnemiaResult

