from unicodedata import name
from flask import Flask, render_template, url_for, request, redirect, flash
from matplotlib.pyplot import title
from sqlalchemy import null
from Webapp import app, db, bcrypt
from Webapp.auth import RegistrationForm, LoginForm, PatientForm
from Webapp.Excel import Excelentry
from Webapp.models import User, Res, Patients
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
from Webapp.animea import AnemiaForm

#from Webapp.corona import CoronaForm

from Webapp.breastCancer import BreastCancerForm


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
        patientResult = Res(content=SurgicaForm.checkpatientResult(SurgicaForm.hemoglopen, SurgicaForm.whiteBlood, SurgicaForm.platelets, SurgicaForm.liver, SurgicaForm.kidney, SurgicaForm.fluidity.data) + SurgicaForm.objections(SurgicaForm.hemoglopen, SurgicaForm.whiteBlood, SurgicaForm.platelets, SurgicaForm.liver, SurgicaForm.kidney, SurgicaForm.fluidity), 
            title="Surgical Operation", user_id=current_user.id, author=current_user)

        db.session.add(patientResult)
        db.session.commit()
        return redirect(url_for('account')) 
    #--------------------------------------------------------
    diabetesForm = DiabetesForm()
    if diabetesForm.validate_on_submit():
        diabetesResult = Res(content=diabetesForm.checkTheCase(diabetesForm.Fasting, diabetesForm.After_Eating, diabetesForm.Hours_After_Eating),title="Diabetes Prediction", user_id=current_user.id, author=current_user)
        db.session.add(diabetesResult)
        db.session.commit()
        return redirect(url_for('account'))
    #--------------------------------------------------------
    heartPredictionForm = HeartPredictionForm()
    if heartPredictionForm.validate_on_submit():
        heartPredictionResult = Res(content=heartPredictionForm.checkHeartPrediction(heartPredictionForm.Age, heartPredictionForm.Sex, heartPredictionForm.cp, heartPredictionForm.trestbps, heartPredictionForm.chol, heartPredictionForm.fbs, heartPredictionForm.restecg, heartPredictionForm.thalach, heartPredictionForm.exang, heartPredictionForm.oldpeak, heartPredictionForm.slope, heartPredictionForm.ca, heartPredictionForm.thal)
            , title="Heart disease prediction", user_id=current_user.id, author=current_user)
        db.session.add(heartPredictionResult)
        db.session.commit()
        return redirect(url_for('account'))
    #--------------------------------------------------------
    kideneyForm = KidneyForm()
    if  kideneyForm.validate_on_submit():
        kideneyResult = Res(content = kideneyForm.checkKidney(kideneyForm.Creatinin, kideneyForm.Creatinin_Clearance, kideneyForm.Na, kideneyForm.Cl, kideneyForm.K, kideneyForm.Blood_Urine_Nitrogen, kideneyForm.Urea)
            , title="Kidney Check", user_id=current_user.id, author=current_user)
        db.session.add(kideneyResult)
        db.session.commit()
        return redirect(url_for('account'))
    #---------------------------------------------------------
    corona_in_out = Corona_in_or_out_form()
    if corona_in_out.validate_on_submit():
        CoronaInOutResult = Res(content = corona_in_out.checkTheCase(corona_in_out.White_Blood_Cell, corona_in_out.Erythrocyte_Sedimentation_Rate, corona_in_out.C_Reactive_Protein, corona_in_out.Procalcitonin)
            , title = 'Covid-19 patient can get out the hospital or not?', user_id=current_user.id, author=current_user)
        db.session.add(CoronaInOutResult)
        db.session.commit()
        return redirect(url_for('account'))

    #---------------------------------------------------------
    anemiaForm = AnemiaForm()
    if anemiaForm.validate_on_submit():
        AnemiaResult = Res(content = anemiaForm.checkAnemia(anemiaForm.Sex, anemiaForm.Red_Blood_Cell, anemiaForm.White_Blood_Cell, anemiaForm.Platelets, anemiaForm.Hemoglobin)
        , title = 'Anemia Prediction', user_id=current_user.id, author=current_user)
        db.session.add(AnemiaResult)
        db.session.commit()
        return redirect(url_for('account'))
    #---------------------------------------------------------
    breast_cancer_Form = BreastCancerForm()
    if breast_cancer_Form.validate_on_submit():
        BreastCancerResult = Res(content = breast_cancer_Form.checkBreastCancer(breast_cancer_Form.radius_mean, 
        breast_cancer_Form.texture_mean, breast_cancer_Form.perimeter_mean, breast_cancer_Form.area_mean, 
        breast_cancer_Form.smoothness_mean, breast_cancer_Form.compactness_mean, 
        breast_cancer_Form.concavity_mean, breast_cancer_Form.concave_points_mean, breast_cancer_Form.symmetry_mean, 
        breast_cancer_Form.fractal_dimension_mean, breast_cancer_Form.radius_se, breast_cancer_Form.texture_se, 
        breast_cancer_Form.perimeter_se, breast_cancer_Form.area_se, breast_cancer_Form.smoothness_se, 
        breast_cancer_Form.compactness_se, breast_cancer_Form.concavity_se, breast_cancer_Form.concave_points_se, 
        breast_cancer_Form.symmetry_se, breast_cancer_Form.fractal_dimension_se, breast_cancer_Form.radius_worst, 
        breast_cancer_Form.texture_worst, breast_cancer_Form.perimeter_worst, breast_cancer_Form.area_worst, 
        breast_cancer_Form.smoothness_worst, breast_cancer_Form.compactness_worst, breast_cancer_Form.concavity_worst, 
        breast_cancer_Form.concave_points_worst, breast_cancer_Form.symmetry_worst, breast_cancer_Form.fractal_dimension_worst)
        , title = 'Breast Cancer Prediction', user_id=current_user.id, author=current_user)
        db.session.add(BreastCancerResult)
        db.session.commit()
        return redirect(url_for('account'))
    #---------------------------------------------------------
    return render_template('Servises.html', title = 'Servises', form1 = SurgicaForm, form2 = diabetesForm, form4 = heartPredictionForm, form5 = kideneyForm, form6 = corona_in_out, form7 = anemiaForm, form8 = breast_cancer_Form)

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


def Save_User_Pic(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/User_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, first_name = form.first_name.data, last_name = form.last_name.data, userType = form.userType.data, department = form.department.data)
        if form.imageUser.data:
            picture_file = Save_User_Pic(form.imageUser.data)
            user.image_user = picture_file
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
    profile_image = url_for('static', filename='profile_pics/' + current_user.image_user)
    return render_template('account.html', title='Account', results=results, no_results=no_results, profile_image=profile_image)

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
@app.route('/braintumour', methods=('GET', 'POST'))
@login_required
def braintumour():
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

        model = tf.keras.models.load_model(r'../BrainTumour/model.wdah_brain')    
        img = image.load_img(r'upload/'+ file.filename , target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)
        classes = model.predict(img_data)
        New_pred = np.argmax(classes, axis=1)
        if New_pred==[1]:
           result ='Prediction: Positive'
        else:
           result = 'Prediction: Negative'
        if os.path.exists('upload/'+ file.filename):
            os.remove('upload/'+ file.filename)

        BrainResult = Res(content=result, title="Brain Tumour Check", user_id=current_user.id, author=current_user)
        db.session.add(BrainResult)
        db.session.commit()

    return render_template('braintumer.html', title='Brain tumour prediction', result=result)

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
@app.route('/addpatient', methods=('GET', 'POST'))
@login_required
def addpatient():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patients(name=form.name.data, age=form.age.data, nationalID=form.nationalID.data, 
            diabetes=form.Diabetes.data, blood_presure=form.blood_pressure.data,covid_19=form.covid_19.data)
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('patientslist'))
    return render_template('addPateient.html', title='Add Patients', form=form)

@app.route('/patientslist')
@login_required
def patientslist():
    #pagination
    page = request.args.get('page', 1, type=int)
    patients = Patients.query.order_by(Patients.date_entered.desc()).paginate(page=page, per_page=6)

    #check if there us no result in the table
    no_results = False
    if Patients.query.first() is None:
        no_results = True
    return render_template('patientsList.html', title='Patients List', patients=patients, no_results=no_results)

@app.route('/patientslist/<int:patient_id>')
@login_required
def patient(patient_id):
    patient = Patients.query.get_or_404(patient_id)
    return render_template('patientInfo.html', title='Patient', patient=patient)

#delete the patient
@app.route('/patientslist/<int:patient_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_patient(patient_id):
    patient = Patients.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for('patientslist'))
#-------------------------------------------------------------------------------------------
def SaveExcelFile(file_exc):
    randomHex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(file_exc.filename)
    if f_ext not in ('./data/[^~]*.xlsx'):
        file_name = randomHex + f_ext
        file_path = os.path.join(app.root_path, 'static/Save_Excel', file_name)
        file_exc.save(file_path)
    return file_path
@app.route('/ExcelFile', methods=('GET', 'POST'))
@login_required
def uploadexcel():
    userResult = ''
    store = True
    Excel_Form = Excelentry()
    if Excel_Form.validate_on_submit():
        saved = SaveExcelFile(Excel_Form.TheFile.data)
        resultList = Excel_Form.addRecord(saved)
        
        if resultList.is_empty():
            userResult = 'Please check the excel file'
            store = False   
        else:
            userResult = 'Sucess'
        if store:
            dbInstance = Patients(name=resultList[0], age=resultList[1], nationalID=resultList[2],diabetes=resultList[3],blood_presure=resultList[4],covid_19=resultList[5])
            db.session.add(dbInstance)
            db.session.commit()

    return render_template('uploadexcel.html', title='Upload Excel Sheet data', form = Excel_Form, userResult = userResult)
#-------------------------------------------------------------------------------------------
@app.route('/cam')
def cam():
    return render_template('camRecognation.html', title='Camera')

@app.route('/signincam')
def signincam():
    return render_template('camSignIn.html', title='Sign In Camera')