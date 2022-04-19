from flask import Flask, render_template, url_for, request, redirect, flash
from Webapp import app, db, bcrypt
from Webapp.auth import RegistrationForm, LoginForm
from Webapp.models import User, Res


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/servises', methods=('GET', 'POST'))
def servises():
    hemoglopen = 0
    blood = 0
    platelets = 0
    liver = 0
    kidney = 0
    fluidity = 0
    fasting = 0
    eating = 0
    afterEating = 0
    if request.method == 'POST':
        # surgical part
        hemoglopen = request.form.get('hemoglopen')
        blood = request.form.get('blood')
        platelets = request.form.get('platelets')
        liver = request.form.get('liver')
        kidney = request.form.get('kidney')
        fluidity = request.form.get('fluidity')

        #diapets part
        fasting = request.form.get('fasting')
        eating = request.form.get('eating')
        afterEating = request.form.get('afterEating')

    #--------------------------------------------------------
    message = 'not predicted yet'
    reason = ''
    diapetsResult = ''
    #System
    if 9 <= float(hemoglopen) <= 11 and 5 <= float(blood) <= 18 and 150000 <= float(platelets) <= 350000 and \
        20 <= float(liver) <= 40 and 0.5 <= float(kidney) <= 1.5 and 0.7 <= float(fluidity) <= 1.5:
        message = 'The patient is qualified'
        
    else:
        message = 'The patient is not qualified'
        
    if float(hemoglopen)<9 or float(hemoglopen)>11:
        reason += 'the patient have a problem with hemoglopen \n'

    if float(blood)<5 or float(blood)>18:
        reason += 'the patient have a problem with whiteBlood \n'

    if float(platelets)<150000 or float(platelets)>350000:
        reason += 'the patient have a problem with platelets \n'

    if float(liver)<20 or float(liver)>40:
        reason += 'the patient have a problem with liver \n'

    if float(kidney)<0.5 or float(kidney)>1.5:
        reason += 'the patient have a problem with kidney \n'

    if float(fluidity)<0.7 or float(fluidity)>1.5:
        reason += 'the patient have a problem with fluidity \n'

    #--------------------------------------------------------

    if 80 <= fasting <= 100 and 170 <= eating <= 200 and 120 <= afterEating <= 140:
        diapetsResult = 'The patient is normal'
        
    if 101 <= fasting <= 125 and 190 <= eating <= 230 and 140 <= afterEating <= 160:
        diapetsResult = 'The patient is Impaired Glucose'
        
    if fasting >=126 and 220 <= eating <= 300 and  afterEating >= 200:
        diapetsResult = 'The patient is Diabetic'
        
    if fasting <80 :
        diapetsResult = 'The patient is in a diabetic coma'
        


    #--------------------------------------------------------
    return render_template('Servises.html', title = 'Servises', message = message, reason = reason, diapetsResult = diapetsResult)

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
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', title = 'Sign up', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title = 'Log in', form = form)