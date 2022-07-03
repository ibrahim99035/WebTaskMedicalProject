from datetime import datetime
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
    results = db.relationship('Res', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Res(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"{self.content}"

class Patinet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    nationalID = db.Column(db.String(100), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    diabetes = db.Column(db.String(100), nullable=False, default='Unknowen')
    blood_presure = db.Column(db.String(100), nullable=False, default='Unknowen')
    covid_19 = db.Column(db.String(100), nullable=False, default='Unknowen')
    profileImage = db.Column(db.String(100), nullable=False, default = 'default.jpg')
    blood_tests_image = db.Column(db.String(100), nullable=False, default = 'default.jpg')

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Dibates: {self.diabetes}, Blood pressure: {self.blood_presure}, Covid-19: {self.covid_19}"