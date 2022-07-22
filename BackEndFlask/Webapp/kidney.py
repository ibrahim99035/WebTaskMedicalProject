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
    sample = ''

    def checkKidney(self, Creatinin, Creatinin_Clearance, Na, K, Cl, Blood_Urine_Nitrogen, Urea):
        CreatininHealthy = Creatinin.data >= 0.7 and Creatinin.data <= 1.4
        Creatinin_ClearanceHealthy = Creatinin_Clearance.data >= 97.0 and Creatinin_Clearance.data <= 137.0
        NaHealthy = Na.data >= 135.0 and Na.data <= 148.0
        KHealthy = K.data >= 3.5 and K.data <= 5.0
        ClHealthy = Cl.data >= 95.0 and Cl.data <= 105.0
        Blood_Urine_NitrogenHealthy = Blood_Urine_Nitrogen.data >= 7.0 and Blood_Urine_Nitrogen.data <= 20.0
        UreaHealthy = Urea.data >= 20.0 and Urea.data <= 40.0
        TestHealthy = CreatininHealthy and Creatinin_ClearanceHealthy and NaHealthy and KHealthy and ClHealthy and Blood_Urine_NitrogenHealthy and UreaHealthy
        #----------------------------------------------------------------------------------------------------
        CreatininTired = Creatinin.data >= 1.5  
        Creatinin_ClearanceTired = Creatinin_Clearance.data <=95.0
        NaTired = Na.data >= 135.0 and Na.data <= 148.0
        KTired = K.data >3.5 
        ClTired = Cl.data >= 95.0 and Cl.data <= 105.0
        Blood_Urine_NitrogenTired = Blood_Urine_Nitrogen.data >= 7.0 and Blood_Urine_Nitrogen.data <= 20.0
        UreaTired = Urea.data >= 40.0 and Urea.data <= 200.0
        TestTired = CreatininTired and Creatinin_ClearanceTired and NaTired and KTired and ClTired and Blood_Urine_NitrogenTired and UreaTired
        #----------------------------------------------------------------------------------------------------
        CreatininDialysis = Creatinin.data >7.0
        Creatinin_ClearanceDialysis = Creatinin_Clearance.data <= 15.0 
        NaDialysis = Na.data >= 135.0 and Na.data <= 148.0
        KDialysis = K.data >5.5
        ClDialysis = Cl.data >= 95.0 and Cl.data <= 105.0
        Blood_Urine_NitrogenDialysis = Blood_Urine_Nitrogen.data >= 7.0 and Blood_Urine_Nitrogen.data <= 20.0
        UreaDialysis = Urea.data >200.0
        TestDialysis = CreatininDialysis and Creatinin_ClearanceDialysis and NaDialysis and KDialysis and ClDialysis and Blood_Urine_NitrogenDialysis and UreaDialysis
        #----------------------------------------------------------------------------------------------------
        if TestHealthy:
            KidneyResult = self.case1
        elif TestTired:
            KidneyResult = self.case2
        elif TestDialysis:
            KidneyResult = self.case3
        else:
            KidneyResult = 'No Result'




        self.sample = f'field 1 :{CreatininHealthy} value : {Creatinin.data} \n field 2 :{Creatinin_ClearanceHealthy} value : {Creatinin_Clearance.data} \n field 3 :{NaHealthy} value : {Na.data} \n field 4 :{KHealthy} value : {K.data} \n field 5 :{ClHealthy} value : {Cl.data} \n field 6 :{Blood_Urine_NitrogenHealthy} value : {Blood_Urine_Nitrogen.data} \n field 7 :{UreaHealthy} value : {Urea.data}'
        return KidneyResult

# test1 = 0.7 <= Creatinin.data <= 1.4 and 97.0 <= Creatinin_Clearance.data <= 137.0 and 135.0 <= Na.data <= 148.0 
# and 3.5 <= K.data <=5.0 and 95.0<=Cl.data <=105.0 and 7.0<= Blood_Urine_Nitrogen.data <=20.0 
# and 20.0<= Urea.data <=40
#         
# 
# test2 = Creatinin.data >= 1.5 and Creatinin_Clearance.data <95.0 and 135.0 <= Na.data <= 148.0 and  K.data > 3.5 and 95.0<=Cl.data <=105.0 and 7.0<= Blood_Urine_Nitrogen.data <=20.0 and 40.0 < Urea.data < 200.0
#         
# 
# test3 = Creatinin.data > 7.0 and Creatinin_Clearance.data < 15.0 and 135.0 <= Na.data <= 148.0 and  K.data > 5.5 and 95.0<=Cl.data <=105.0 and 7.0<= Blood_Urine_Nitrogen.data <=20.0 and  Urea.data >200.0        