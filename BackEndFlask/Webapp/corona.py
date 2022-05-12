import os
from flask import flash
from werkzeug.utils import secure_filename
import tensorflow as tf 
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm


from Webapp import UPLOAD_FOLDER, app 

class CoronaForm(FlaskForm):
    file = FileField('Choose the image file', validators=[DataRequired()])
    submit = SubmitField('Confirm')
    #-------------------------------------------------
    def allowed_file(filename):
        ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 
    #-------------------------------------------------

    # if file.filename == '':
    #     flash('No selected file')

    # if file and allowed_file(file.filename):
    #     filename = secure_filename(file.filename)
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # model = tf.keras.models.load_model(r'../covidPredict/model.wdah')
    # img = image.load_img(r'upload/'+ file.filename , target_size=(224, 224)) 
    # x = image.img_to_array(img)
    # x = np.expand_dims(x, axis=0)
    # img_data = preprocess_input(x)
    # classes = model.predict(img_data)
    # New_pred = np.argmax(classes, axis=1)
    # if New_pred==[1]:
    #     result ='Prediction: Normal'
    # else:
    #     result = 'Prediction: Corona' 
    # if os.path.exists('upload/'+ file.filename):
    #     os.remove('upload/'+ file.filename)
    
    if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #-----------------------------------------------------------------
    def check(self, file):
        # if file.filename == '':
        #     flash('No selected file')

        
        model = tf.keras.models.load_model(r'../covidPredict/model.wdah')
        img = image.load_img(r'upload/'+ file.filename , target_size=(224, 224)) 
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)
        classes = model.predict(img_data)
        New_pred = np.argmax(classes, axis=1)
        if New_pred==[1]:
            result ='Prediction: Normal'
        else:
            result = 'Prediction: Corona' 
        if os.path.exists('upload/'+ file.filename):
            os.remove('upload/'+ file.filename)
        
        return result

