from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField
from wtforms.validators import DataRequired

class DiabetesForm(FlaskForm):
    Fasting = FloatField('Fasting Value', validators=[DataRequired()])
    After_Eating = FloatField('Value After Eating', validators=[DataRequired()])
    Hours_After_Eating = FloatField('2-3 Hours After Eating', validators=[DataRequired()])
    submit = SubmitField('Confirm')
















Fasting = float(input("enter value of Fasting :"))
After_Eating =float(input("enter value of After_Eating :"))
Hours_After_Eating = float(input("enter value of 2-3Hours_After_Eating :"))

#patient cases with diabetes
case1 = 'The patient is normal'
case2 = 'The patient is Impaired Glucose'
case3 = 'The patient is Diabetic'
case4 = 'The patient is in a diabetic coma'

#diabetes tests boolean variables
test1 = 80 <= Fasting <= 100 and 170 <= After_Eating <= 200 and 120 <= Hours_After_Eating <= 140
test2 = 101 <= Fasting <= 125 and 190 <= After_Eating <= 230 and 140 <= Hours_After_Eating <= 160
test3 = Fasting >=126 and 220 <= After_Eating <= 300 and  Hours_After_Eating >= 200
test4 = Fasting <80

#the functionality 
diabetesResult = ''
if test1:
    diabetesResult = case1
elif test2:
    diabetesResult = case2
elif test3:
    diabetesResult = case3
elif test4:
    diabetesResult = case4

