from datetime import datetime
from email.policy import default
from Webapp import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(20), nullable=False, default = 'none')
    last_name = db.Column(db.String(20), nullable=False, default = 'none')
    image_user = db.Column(db.String(20), nullable=False, default = 'default.jpg')
    results = db.relationship('Res', backref='author', lazy=True)
    userType = db.Column(db.String(100), nullable=False, default = 'none')
    department = db.Column(db.String(100), nullable=False, default = 'none')
    
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Res(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(100), nullable=False, default = 'none')
    content = db.Column(db.Text, nullable=False, default = 'none')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #-------------------------------------------------------------------------------

    

    def __repr__(self):
        return f"{self.content}"

class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, default = 'Un assigned')
    age = db.Column(db.Integer, nullable=False, default = 'none')
    nationalID = db.Column(db.String(100), nullable=False, default = 'none')
    date_entered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    diabetes = db.Column(db.String(100), nullable=False, default='Unknowen')
    blood_presure = db.Column(db.String(100), nullable=False, default='Unknowen')
    covid_19 = db.Column(db.String(100), nullable=False, default='Unknowen')
    profileImage = db.Column(db.String(100), nullable=False, default = 'default.jpg')
    blood_tests_image = db.Column(db.String(100), nullable=False, default = 'default.jpg')

    def __repr__(self):
        return f"{self.name}, {self.age}"
