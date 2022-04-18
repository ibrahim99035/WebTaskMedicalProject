from flask import Flask, render_template, url_for, request, redirect, flash
from auth import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    results = db.relationship('Res', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Res(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Result ('{self.title}', '{self.date_posted}')"

#-------------------------------------------------------------------------------------------
#HTML pages :
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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('signup.html', title = 'Sign up', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title = 'Log in', form = form)
#-------------------------------------------------------------------------------------------


if __name__ == '__main__' :
    app.run(debug=True)