from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField
from wtforms.validators import DataRequired
import numpy as np
import pickle as pk

class PatientStayForm(FlaskForm):
    Haematocrit = FloatField('Value of Haematocrit :', validators=[DataRequired()])
    Haemoglobins = FloatField('Value of Haemoglobins :', validators=[DataRequired()])
    Erythrocyte = FloatField('Value of Erythrocyte :', validators=[DataRequired()])
    Leucocyte = FloatField('Value of Leucocyte :', validators=[DataRequired()])
    Thrombocyte = FloatField('Value of Thrombocyte :', validators=[DataRequired()])
    Age = FloatField('The Age :', validators=[DataRequired()])
    Gender = StringField('The Gender :', validators=[DataRequired()])
    submit = SubmitField('Confirm')
    #---------------------------------------------------------------------
    loaded_scaler = pk.load(open('../Patient-Treatment-Classification-Task/scaler.pkl', 'rb'))
    loaded_model = pk.load(open('../Patient-Treatment-Classification-Task/model.pkl', 'rb'))
    

    positive_result = 'The patient may not return to the hospital!'
    negative_result = 'The patient may return to the hospital!'
    result = ''
    #---------------------------------------------------------------------
    GenderValue = ''
    
    #---------------------------------------------------------------------
    def checkPrediction(self, Haematocrit, Haemoglobins, Erythrocyte, Leucocyte, Thrombocyte, Age, Gender):
        if Gender == 'Male' or 'male' or 'm' or 'M' :
            self.GenderValue = 1
        elif Gender == 'Female' or 'female' or 'f' or 'F' :
            self.GenderValue = 0
        
        instance = (Haematocrit.data, Haemoglobins.data, Erythrocyte.data, Leucocyte.data, Thrombocyte.data, Age.data)

        arr = np.asarray(instance)
        reshape = arr.reshape(1, -1)

        std = self.loaded_scaler.transform(reshape)
        prediction = self.loaded_model.predict(std + self.GenderValue)

        if (prediction[0] == 0):
            result = self.negative_result
        else :
            result = self.positive_result

        return result




