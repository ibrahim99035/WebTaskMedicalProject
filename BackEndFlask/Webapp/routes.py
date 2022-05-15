from flask import Flask, render_template, url_for, request, redirect, flash
from matplotlib.pyplot import title
from Webapp import app, db, bcrypt
from Webapp.auth import RegistrationForm, LoginForm
from Webapp.models import User, Res
from flask_login import login_user, current_user, logout_user, login_required
#nassar tasks
from Webapp.surgicalOperation import SurgicalOperationForm
from Webapp.diabetes import DiabetesForm
from Webapp.heartPrediction import HeartPredictionForm

#from Webapp.corona import CoronaForm

from Webapp.patientStay import PatientStayForm

#------------------------------------------------------------------------------------
import os
from werkzeug.utils import secure_filename
import tensorflow as tf 
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

UPLOAD_FOLDER = 'upload/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 
#------------------------------------------------------------------------------------
#Routes
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/servises', methods=('GET', 'POST'))
@login_required
def servises():
    SurgicaForm = SurgicalOperationForm()
    if SurgicaForm.validate_on_submit():
        patientResult = Res(content=SurgicaForm.checkpatientResult(SurgicaForm.hemoglopen, SurgicaForm.whiteBlood, SurgicaForm.platelets, SurgicaForm.liver, SurgicaForm.kidney, SurgicaForm.fluidity.data) + SurgicaForm.objections(SurgicaForm.hemoglopen, SurgicaForm.whiteBlood, SurgicaForm.platelets, SurgicaForm.liver, SurgicaForm.kidney, SurgicaForm.fluidity), title="Surgical Operation", user_id=current_user.id, author=current_user)
        db.session.add(patientResult)
        db.session.commit()
        return redirect(url_for('account')) 
    #--------------------------------------------------------
    diabetesForm = DiabetesForm()
    if diabetesForm.validate_on_submit():
        diabetesResult = Res(content=diabetesForm.checkTheCase(diabetesForm.Fasting, diabetesForm.After_Eating, diabetesForm.Hours_After_Eating), title="Diapetes Check", user_id=current_user.id, author=current_user)
        db.session.add(diabetesResult)
        db.session.commit()
        return redirect(url_for('account'))
    #--------------------------------------------------------
    treatmentForm = PatientStayForm()
    if treatmentForm.validate_on_submit():
        treatmentResult = Res(content=treatmentForm.checkPrediction(treatmentForm.Haematocrit, treatmentForm.Haemoglobins, treatmentForm.Erythrocyte, treatmentForm.Leucocyte, treatmentForm.Thrombocyte, treatmentForm.Age, treatmentForm.Gender), title="Patient Stay or not", user_id=current_user.id, author=current_user)
        db.session.add(treatmentResult)
        db.session.commit()
        return redirect(url_for('account'))
    #--------------------------------------------------------
    heartPredictionForm = HeartPredictionForm()
    if heartPredictionForm.validate_on_submit():
        heartPredictionResult = Res(content=heartPredictionForm.checkHeartPrediction(heartPredictionForm.Age, heartPredictionForm.Sex, heartPredictionForm.cp, heartPredictionForm.trestbps, heartPredictionForm.chol, heartPredictionForm.fbs, heartPredictionForm.restecg, heartPredictionForm.thalach, heartPredictionForm.exang, heartPredictionForm.oldpeak, heartPredictionForm.slope, heartPredictionForm.ca, heartPredictionForm.thal), title="Heart disease prediction", user_id=current_user.id, author=current_user)
        db.session.add(heartPredictionResult)
        db.session.commit()
        return redirect(url_for('account'))
    #--------------------------------------------------------
    # coronaForm = CoronaForm()
    # if coronaForm.validate_on_submit():
    #     coronaResult = Res(content=coronaForm.check(coronaForm.file), title="Corona Check", user_id=current_user.id, author=current_user)
    #     db.session.add(coronaResult)
    #     db.session.commit()
    #     return redirect(url_for('account'))
    #--------------------------------------------------------
    return render_template('Servises.html', title = 'Servises', form1 = SurgicaForm, form2 = diabetesForm, form3 = treatmentForm, form4 = heartPredictionForm)

@app.route('/elements')
def elements():
    return render_template('elements.html', title = 'Elements')

@app.route('/doctors')
def doctors():
    return render_template('doctors.html', title = 'Doctors')

@app.route('/departments')
def departments():
    return render_template('departments.html', title = 'departments')

@app.route('/contact')
def contact():
    return render_template('contact.html', title = 'Contact')

@app.route('/blog-details')
def blog_details():
    return render_template('blog-details.html', title = 'Blog Details')

@app.route('/blog-home')
def blog_home():
    return render_template('blog-home.html', title = 'Blog Home')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', title = 'Sign up', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', title = 'Log in', form = form)



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/account")
@login_required
def account():
    results = Res.query.all()
    return render_template('account.html', title='Account', results=results)

#-------------------------------------------------------------------------------------------


@app.route('/coronavirus', methods=('GET', 'POST'))
@login_required
def coronavirus():
    result = ''
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

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

        covidResult = Res(content=result, title="Corona Check", user_id=current_user.id, author=current_user)
        db.session.add(covidResult)
        db.session.commit()
        
        
        
    return render_template('coronavirus.html', title='Covid-19 prediction', res = result)