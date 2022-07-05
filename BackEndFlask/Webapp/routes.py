from unicodedata import name
from flask import Flask, render_template, url_for, request, redirect, flash
from matplotlib.pyplot import title
from Webapp import app, db, bcrypt
from Webapp.auth import RegistrationForm, LoginForm
from Webapp.models import User, Res
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
# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

#     output_size = (125, 125)
#     i = Image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)

#     return picture_fn

# def save_blood_test(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path, 'static/blood_test', picture_fn)

#     output_size = (125, 125)
#     i = Image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)

#     return picture_fn

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
            title="Surgical Operation", user_id=current_user.id, author=current_user, 
            name=SurgicaForm.name.data, age = SurgicaForm.age.data, nationalID = SurgicaForm.nationalID.data, 
            diabetes = SurgicaForm.Diabetes.data, blood_presure = SurgicaForm.blood_pressure.data, covid_19 = SurgicaForm.covid_19.data,)
        
        # if SurgicaForm.patient_pic:
        #     picture_file = save_picture(SurgicaForm.patient_pic.data)
        #     patientResult.profileImage = picture_file
        # if SurgicaForm.blood_tests_pic:
        #     picture_file = save_blood_test(SurgicaForm.blood_tests_pic.data)
        #     patientResult.blood_tests_image = picture_file
        db.session.add(patientResult)
        db.session.commit()
        return redirect(url_for('account')) 
    #--------------------------------------------------------
    diabetesForm = DiabetesForm()
    if diabetesForm.validate_on_submit():
        diabetesResult = Res(content=diabetesForm.checkTheCase(diabetesForm.Fasting, diabetesForm.After_Eating, diabetesForm.Hours_After_Eating)
            , title="Diapetes Check", user_id=current_user.id, author=current_user
            , name=diabetesForm.name.data, age = diabetesForm.age.data, nationalID = diabetesForm.nationalID.data, 
            diabetes = diabetesForm.Diabetes.data, blood_presure = diabetesForm.blood_pressure.data, covid_19 = diabetesForm.covid_19.data,)
        
        # if diabetesForm.patient_pic:
        #     picture_file = save_picture(diabetesForm.patient_pic.data)
        #     diabetesResult.profileImage = picture_file
        # if diabetesForm.blood_tests_pic:
        #     picture_file = save_blood_test(diabetesForm.blood_tests_pic.data)
        #     diabetesResult.blood_tests_image = picture_file
        db.session.add(diabetesResult)
        db.session.commit()
        return redirect(url_for('account'))
    #--------------------------------------------------------
    heartPredictionForm = HeartPredictionForm()
    if heartPredictionForm.validate_on_submit():
        heartPredictionResult = Res(content=heartPredictionForm.checkHeartPrediction(heartPredictionForm.Age, heartPredictionForm.Sex, heartPredictionForm.cp, heartPredictionForm.trestbps, heartPredictionForm.chol, heartPredictionForm.fbs, heartPredictionForm.restecg, heartPredictionForm.thalach, heartPredictionForm.exang, heartPredictionForm.oldpeak, heartPredictionForm.slope, heartPredictionForm.ca, heartPredictionForm.thal)
            , title="Heart disease prediction", user_id=current_user.id, author=current_user
            , name=heartPredictionForm.name.data, age = heartPredictionForm.age.data, nationalID = heartPredictionForm.nationalID.data, 
            diabetes = heartPredictionForm.Diabetes.data, blood_presure = heartPredictionForm.blood_pressure.data, covid_19 = heartPredictionForm.covid_19.data,)
       
        # if heartPredictionForm.patient_pic:
        #     picture_file = save_picture(heartPredictionForm.patient_pic.data)
        #     heartPredictionResult.profileImage = picture_file
        # if heartPredictionForm.blood_tests_pic:
        #     picture_file = save_blood_test(heartPredictionForm.blood_tests_pic.data)
        #     heartPredictionResult.blood_tests_image = picture_file
        db.session.add(heartPredictionResult)
        db.session.commit()
        return redirect(url_for('account'))
    #--------------------------------------------------------
    kideneyForm = KidneyForm()
    if  kideneyForm.validate_on_submit():
        kideneyResult = Res(content = kideneyForm.checkKidney(kideneyForm.Creatinin, kideneyForm.Creatinin_Clearance, kideneyForm.Na, kideneyForm.Cl, kideneyForm.K, kideneyForm.Blood_Urine_Nitrogen, kideneyForm.Urea)
            , title="Kidney Check", user_id=current_user.id, author=current_user
            , name=kideneyForm.name.data, age = kideneyForm.age.data, nationalID = kideneyForm.nationalID.data, 
            diabetes = kideneyForm.Diabetes.data, blood_presure = kideneyForm.blood_pressure.data, covid_19 = kideneyForm.covid_19.data,)
        
        # if kideneyForm.patient_pic:
        #     picture_file = save_picture(kideneyForm.patient_pic.data)
        #     kideneyResult.profileImage = picture_file
        # if kideneyForm.blood_tests_pic:
        #     picture_file = save_blood_test(kideneyForm.blood_tests_pic.data)
        #     kideneyResult.blood_tests_image = picture_file
        db.session.add(kideneyResult)
        db.session.commit()
        return redirect(url_for('account'))
    #---------------------------------------------------------
    corona_in_out = Corona_in_or_out_form()
    if corona_in_out.validate_on_submit():
        CoronaInOutResult = Res(content = corona_in_out.checkTheCase(corona_in_out.White_Blood_Cell, corona_in_out.Erythrocyte_Sedimentation_Rate, corona_in_out.C_Reactive_Protein, corona_in_out.Procalcitonin)
            , title = 'Covid-19 patient can get out the hospital or not?', user_id=current_user.id, author=current_user
            , name=corona_in_out.name.data, age = corona_in_out.age.data, nationalID = corona_in_out.nationalID.data, 
            diabetes = corona_in_out.Diabetes.data, blood_presure = corona_in_out.blood_pressure.data, covid_19 = corona_in_out.covid_19.data,)
        
        # if corona_in_out.patient_pic:
        #     picture_file = save_picture(corona_in_out.patient_pic.data)
        #     CoronaInOutResult.profileImage = picture_file
        # if corona_in_out.blood_tests_pic:
        #     picture_file = save_blood_test(corona_in_out.blood_tests_pic.data)
        #     CoronaInOutResult.blood_tests_image = picture_file
        db.session.add(CoronaInOutResult)
        db.session.commit()
        return redirect(url_for('account'))

    #---------------------------------------------------------
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
@app.route('/cam')
def cam():
    return render_template('camRecognation.html', title='Camera')

@app.route('/signincam')
def signincam():
    return render_template('camSignIn.html', title='Sign In Camera')