from datetime import datetime
from Webapp import db, login_manager
from flask_login import UserMixin


class Patinet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    diabetes = db.Column(db.String(100), nullable=False)
    blood_presure = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.diabetes}, {self.blood_presure}"