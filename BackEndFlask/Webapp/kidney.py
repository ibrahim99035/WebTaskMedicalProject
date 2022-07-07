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

    submit = SubmitField('Confirm')

    case1 = 'The Kidney is Healthy'
    case2 = 'The Kidney is Tired'
    case3 = 'The Kidney need Dialysis'

    KidneyResult = ''

    def checkKidney(self, Creatinin, Creatinin_Clearance, Na, K, Cl, Blood_Urine_Nitrogen, Urea):
        test1 = 0.7 <= Creatinin.data <= 1.4 and 97.0 <= Creatinin_Clearance.data <= 137.0 and 135.0 <= Na.data <= 148.0 and 3.5 <= K.data <=5.0 and 95.0<=Cl.data <=105.0 and 7.0<= Blood_Urine_Nitrogen.data <=20.0 and 20.0<= Urea.data <=40
        test2 = Creatinin.data >= 1.5 and Creatinin_Clearance.data <95.0 and 135.0 <= Na.data <= 148.0 and  K.data > 3.5 and 95.0<=Cl.data <=105.0 and 7.0<= Blood_Urine_Nitrogen.data <=20.0 and 40.0 < Urea.data < 200.0
        test3 = Creatinin.data > 7.0 and Creatinin_Clearance.data < 15.0 and 135.0 <= Na.data <= 148.0 and  K.data > 5.5 and 95.0<=Cl.data <=105.0 and 7.0<= Blood_Urine_Nitrogen.data <=20.0 and  Urea.data >200.0

        if test1 :
            self.KidneyResult = self.case1
        elif test2 :
            self.KidneyResult = self.case1
        elif test3 :
            self.KidneyResult = self.case1
        else :
            self.KidneyResult = 'Unvalid inputs'

        return self.KidneyResult

        