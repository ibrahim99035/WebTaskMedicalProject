from flask import Flask, render_template, url_for, request, redirect, flash
from matplotlib.pyplot import title
from Webapp import app, db, bcrypt
from Webapp.auth import RegistrationForm, LoginForm, AddPatient
from Webapp.models import User, Res, Patinet
from flask_login import login_user, current_user, logout_user, login_required
import os
import secrets
from PIL import Image
#nassar tasks
from Webapp.surgicalOperation import SurgicalOperationForm
from Webapp.diabetes import DiabetesForm
from Webapp.heartPrediction import HeartPredictionForm
from Webapp.kidney import KidneyForm
from Webapp.Covid_patient_in_or_out import Corona_in_or_out_form

#from Webapp.corona import CoronaForm



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
    kideneyForm = KidneyForm()
    if  kideneyForm.validate_on_submit():
        kideneyResult = Res(content = kideneyForm.checkKidney(kideneyForm.Creatinin, kideneyForm.Creatinin_Clearance, kideneyForm.Na, kideneyForm.Cl, kideneyForm.K, kideneyForm.Blood_Urine_Nitrogen, kideneyForm.Urea), title="Kidney Check", user_id=current_user.id, author=current_user)
        db.session.add(kideneyResult)
        db.session.commit()
        return redirect(url_for('account'))
    #---------------------------------------------------------
    corona_in_out = Corona_in_or_out_form()
    if corona_in_out.validate_on_submit():
        CoronaInOutResult = Res(content = corona_in_out.checkTheCase(corona_in_out.White_Blood_Cell, corona_in_out.Erythrocyte_Sedimentation_Rate, corona_in_out.C_Reactive_Protein, corona_in_out.Procalcitonin), title = 'Covid-19 patient can get out the hospital or not?', user_id=current_user.id, author=current_user)
        db.session.add(CoronaInOutResult)
        db.session.commit()
        return redirect(url_for('account'))
    return render_template('Servises.html', title = 'Servises', form1 = SurgicaForm, form2 = diabetesForm, form4 = heartPredictionForm, form5 = kideneyForm, form6 = corona_in_out)

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
    #check if the Res table have no results depending on user_id
    no_results = False
    if Res.query.filter_by(user_id=current_user.id).first() is None:
        no_results = True
    #pagination
    page = request.args.get('page', 1, type=int)
    results = Res.query.order_by(Res.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('account.html', title='Account', results=results, no_results=no_results)

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


#-------------------------------------------------------------------------------------------
#in this section we are going to build a deletion system for the results
@app.route('/result/<int:result_id>')
@login_required
def result(result_id):
    result = Res.query.get_or_404(result_id)
    return render_template('result.html', title='Result', result=result)

@app.route('/result/<int:result_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_result(result_id):
    result = Res.query.get_or_404(result_id)
    db.session.delete(result)
    db.session.commit()
    return redirect(url_for('account'))

#-------------------------------------------------------------------------------------------

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def save_blood_test(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/blood_test', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/patientslist')
@login_required
def patientslist():
    #check if the Patient taple has no records
    no_results = False
    if Patinet.query.first() is None:
        no_results = True
    #pagination
    page = request.args.get('page', 1, type=int)
    results = Patinet.query.order_by(Patinet.date_entered.desc()).paginate(page=page, per_page=6)
    return render_template('patientslist.html', title='Patients List', results=results, no_results=no_results)

@app.route('/patinet/<int:patinet_id>')
@login_required
def patient(patinet_id):
    no_result = False
    if Patinet.query.filter_by(id=patinet_id).first() is None:
        no_result = True
    patient = Patinet.query.get_or_404(patinet_id)
    profile_image = url_for('static', filename='profile_pics/' + patient.profileImage)
    bloodTests = url_for('static', filename='blood_test/' + patient.blood_tests_image)
    
    return render_template('patientInfo.html', title='Patient', patient = patient, profile_image = profile_image, bloodTests = bloodTests, no_result = no_result)

@app.route('/addpatinet', methods=['GET', 'POST'])
@login_required
def addpatient():
    addingForm = AddPatient()
    if addingForm.validate_on_submit():
        patient = Patinet(name=addingForm.name.data, age=addingForm.age.data,nationalID=addingForm.nationalID.data,
        diabetes=addingForm.Diabetes.data,blood_presure=addingForm.blood_pressure.data,covid_19=addingForm.covid_19.data)
        if addingForm.patient_pic.data:
            picture_file = save_picture(addingForm.patient_pic.data)
            patient.profileImage = picture_file
        if addingForm.blood_tests_pic.data:
            picture_file = save_blood_test(addingForm.blood_tests_pic.data)
            patient.blood_test = picture_file
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('patientslist'))
    return render_template('addPateient.html', title='Add Patient', form=addingForm)

@app.route('/patinet/<int:result_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_patient(result_id):
    patient = Patinet.query.get_or_404(result_id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('patientslist'))
#-------------------------------------------------------------------------------------------
@app.route('/cam')
def cam():
    return render_template('camRecognation.html', title='Camera')

@app.route('/signincam')
def signincam():
    return render_template('camSignIn.html', title='Sign In Camera')