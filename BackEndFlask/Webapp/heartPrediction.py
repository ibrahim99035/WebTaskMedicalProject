from flask_wtf import FlaskForm
from pyparsing import cpp_style_comment
from wtforms import FloatField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired, Length, InputRequired, Length
from flask_wtf.file import FileField, FileAllowed
import numpy as np
import pickle as pk

class HeartPredictionForm(FlaskForm):
    Age = IntegerField('Yoal Age :', validators=[InputRequired()])
    Sex = IntegerField('Your Gender :', validators=[InputRequired()])
    cp = IntegerField('Value of cpp :', validators=[InputRequired()])
    trestbps = FloatField('Value of trestbps :', validators=[InputRequired()])
    chol = FloatField('Value of chol :', validators=[InputRequired()])
    fbs = IntegerField('Value of fbs :', validators=[InputRequired()])
    restecg = IntegerField('Value of restecg :', validators=[InputRequired()])
    thalach = FloatField('Value of thalach :', validators=[InputRequired()])
    exang = IntegerField('Value of exang :', validators=[InputRequired()])
    oldpeak = FloatField('Value of oldpeak :', validators=[InputRequired()])
    slope = IntegerField('Value of slope :', validators=[InputRequired()])
    ca = IntegerField('Value of ca :', validators=[InputRequired()])
    thal = IntegerField('Value of thal :', validators=[InputRequired()])
    #---------------------------------------------------------------------
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    age = StringField('Age', validators=[DataRequired(), Length(min=1, max=2)])
    nationalID = StringField('National ID', validators=[DataRequired(), Length(min=14, max=14)])
    Diabetes = StringField('Diabetes', validators=[Length(min=3, max=10)])
    blood_pressure = StringField('Blood Pressure', validators=[Length(min=3, max=10)])
    covid_19 = StringField('Covid-19', validators=[Length(min=3, max=10)])
    
    patient_pic = FileField('Patient Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    blood_tests_pic = FileField('Blood Tests Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    #---------------------------------------------------------------------
    submit = SubmitField('Confirm')

    loaded_scaler = pk.load(open('../HeartPrediction/scalar.pkl', 'rb'))
    loaded_model = pk.load(open('../HeartPrediction/model.pkl', 'rb'))
        

    positive_result = 'The patient has heart problems'
    negative_result = 'The patient has heart problems'
    result = ''
    #---------------------------------------------------------------------
    def checkHeartPrediction(self, Age, Sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
        instance = (Age.data, Sex.data, cp.data, trestbps.data, chol.data, fbs.data, restecg.data, thalach.data, exang.data, oldpeak.data, slope.data, ca.data, thal.data)

        arr = np.asarray(instance)
        reshape = arr.reshape(1, -1)

        std = self.loaded_scaler.transform(reshape)
        prediction = self.loaded_model.predict(std)

        if (prediction[0] == 0):
            result = self.negative_result
        else :
            result = self.positive_result

        return result



