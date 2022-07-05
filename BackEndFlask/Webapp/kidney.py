from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed

class KidneyForm(FlaskForm):
    Creatinin = FloatField('Enter value of Creatinin :', validators=[DataRequired()])

    Creatinin_Clearance = FloatField('Enter value of Creatinin_Clearance :', validators=[DataRequired()])

    Na = FloatField('Enter value of Na :', validators=[DataRequired()])

    K = FloatField('Enter value of K :', validators=[DataRequired()])

    Cl = FloatField('Enter value of Cl :', validators=[DataRequired()])

    Blood_Urine_Nitrogen = FloatField('Enter value of Blood_Urine_Nitrogen :', validators=[DataRequired()])

    Urea = FloatField('Enter value of Urea :', validators=[DataRequired()])

    #----------------------------------------------------------------------------------------------------
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    age = StringField('Age', validators=[DataRequired(), Length(min=1, max=2)])
    nationalID = StringField('National ID', validators=[DataRequired(), Length(min=14, max=14)])
    Diabetes = StringField('Diabetes', validators=[Length(min=3, max=10)])
    blood_pressure = StringField('Blood Pressure', validators=[Length(min=3, max=10)])
    covid_19 = StringField('Covid-19', validators=[Length(min=3, max=10)])
    
    patient_pic = FileField('Patient Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    blood_tests_pic = FileField('Blood Tests Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    #----------------------------------------------------------------------------------------------------

    submit = SubmitField('Confirm')

    case1 = 'The Kidney is Healthy'
    case2 = 'The Kidney is Tired'
    case3 = 'The Kidney need Dialysis'

    KidneyResult = ''

    def checkKidney(self, Creatinin, Creatinin_Clearance, Na, K, Cl, Blood_Urine_Nitrogen, Urea):
        test1 = 0.7 <= Creatinin.data <= 1.4 and 97 <= Creatinin_Clearance.data <= 137 and 135 <= Na.data <= 148 and 3.5 <= K.data <=5 and 95<=Cl.data <=105 and 7<= Blood_Urine_Nitrogen.data <=20 and 20<= Urea.data <=40
        test2 = Creatinin.data >= 1.5 and Creatinin_Clearance.data <95 and 135 <= Na.data <= 148 and  K.data > 3.5 and 95<=Cl.data <=105 and 7<= Blood_Urine_Nitrogen.data <=20 and 40 < Urea.data < 200
        test3 = Creatinin.data > 7.0 and Creatinin_Clearance.data < 15.0 and 135 <= Na.data <= 148 and  K.data > 5.5 and 95<=Cl.data <=105 and 7.0<= Blood_Urine_Nitrogen.data <=20 and  Urea.data >200.0

        if test1 :
            self.KidneyResult = self.case1
        elif test2 :
            self.KidneyResult = self.case1
        elif test3 :
            self.KidneyResult = self.case1
        else :
            self.KidneyResult = 'Unvalid inputs'

        return self.KidneyResult

        