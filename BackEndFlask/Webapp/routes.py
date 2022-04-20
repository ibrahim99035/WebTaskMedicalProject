from flask import Flask, render_template, url_for, request, redirect, flash
from Webapp import app, db, bcrypt
from Webapp.auth import RegistrationForm, LoginForm
from Webapp.models import User, Res
from flask_login import login_user, current_user, logout_user, login_required
from Webapp.surgicalOperation import SurgicalOperationForm

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/servises', methods=('GET', 'POST'))
def servises():
    SurgicaForm = SurgicalOperationForm()
    if SurgicaForm.validate_on_submit():
        patientResult = Res(content=SurgicaForm.checkpatientResult(SurgicaForm.hemoglopen.data, SurgicaForm.whiteBlood.data, SurgicaForm.platelets.data, SurgicaForm.liver.data, SurgicaForm.kidney.data, SurgicaForm.fluidity.data) + SurgicaForm.objections(SurgicaForm.hemoglopen.data, SurgicaForm.whiteBlood.data, SurgicaForm.platelets.data, SurgicaForm.liver.data, SurgicaForm.kidney.data, SurgicaForm.fluidity.data))
        db.session.add(patientResult)
        db.session.commit()
        return redirect(url_for('account'))
    #--------------------------------------------------------
    return render_template('Servises.html', title = 'Servises', form1 = SurgicaForm)

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
    return render_template('account.html', title='Account')