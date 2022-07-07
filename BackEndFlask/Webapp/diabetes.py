from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed

class DiabetesForm(FlaskForm):
    Fasting = FloatField('Fasting Value', validators=[DataRequired()])
    After_Eating = FloatField('Value After Eating', validators=[DataRequired()])
    Hours_After_Eating = FloatField('2-3 Hours After Eating', validators=[DataRequired()])
    #---------------------------------------------------------------------------------------------------------
   
    #---------------------------------------------------------------------------------------------------------
    submit = SubmitField('Confirm')

    #patient cases with diabetes
    case1 = 'The patient is normal'
    case2 = 'The patient is Impaired Glucose'
    case3 = 'The patient is Diabetic'
    case4 = 'The patient is in a diabetic coma'
    
    diabetesResult = ''

    def checkTheCase(self, Fasting, After_Eating, Hours_After_Eating):
        #diabetes tests boolean variables
        test1 = 80.0 <= Fasting.data <= 100.0 and 170.0 <= After_Eating.data <= 200.0 and 120.0 <= Hours_After_Eating.data <= 140.0
        test2 = 101.0 <= Fasting.data <= 125.0 and 190.0 <= After_Eating.data <= 230.0 and 140.0 <= Hours_After_Eating.data <= 160.0
        test3 = Fasting.data >=126.0 and 220.0 <= After_Eating.data <= 300.0 and  Hours_After_Eating.data >= 200.0
        test4 = Fasting.data <80.0

        #the functionality 
        if test1:
            diabetesResult = self.case1
        elif test2:
            diabetesResult = self.case2
        elif test3:
            diabetesResult = self.case3
        elif test4:
            diabetesResult = self.case4
        else:
            diabetesResult = 'invalid inputs'
        
        return diabetesResult