from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Webapp.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name',
                            validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    image_user = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    userType = StringField('Doctor or Nurse',
                           validators=[DataRequired(), Length(min=5, max=6)])
    department = StringField('Department',
                             validators=[DataRequired(), Length(min=2, max=20)])
   
    submit = SubmitField('Sign Up')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AddPatient(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    age = StringField('Age', validators=[DataRequired(), Length(min=1, max=2)])
    nationalID = StringField('National ID', validators=[DataRequired(), Length(min=14, max=14)])
    Diabetes = StringField('Diabetes', validators=[Length(min=3, max=10)])
    blood_pressure = StringField('Blood Pressure', validators=[Length(min=3, max=10)])
    covid_19 = StringField('Covid-19', validators=[Length(min=3, max=10)])
    
    patient_pic = FileField('Patient Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    blood_tests_pic = FileField('Blood Tests Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    submit = SubmitField('Add')