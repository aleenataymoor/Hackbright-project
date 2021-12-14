
"""Models for Pet Website."""
#projectdb
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import arrow

db = SQLAlchemy()

class User( db.Model):
    """A user."""

    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(35), unique=True)
    password= db.Column(db.String(20), nullable=False) # should be hashed (use library)
    zipcode=   db.Column(db.String(10))
    phone_no= db.Column(db.String(12))

    pets= db.relationship('Pet', back_populates="users")
    reminders= db.relationship('Reminder', back_populates="users")

    def __repr__(self):
        return f"<User user_id={self.user_id} name={self.name}>"


class Pet(db.Model):
    """A Pet."""

    __tablename__ = "pets"
    pet_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_name = db.Column(db.String(30), nullable=False)
    species= db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    # look into Cloudinary for image upload 
    # either use the API directly or the Python library (https://docs.google.com/document/d/1bbT4hqq--ORiD0EZ4T470P7OYEqPn0PCH1RbxtFAmpU/edit)
    pic_url= db.Column(db.String(255)) 

    users= db.relationship('User', back_populates="pets")
    
    
    def __repr__(self):
        return f"<Pet pet_id={self.pet_id} pet_name={self.pet_name} species={self.species}>"





class Reminder(db.Model):
    __tablename__ = 'reminders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    delta = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    timezone = db.Column(db.String(50), nullable=False)

    users= db.relationship('User', back_populates="reminders")

    def __repr__(self):
        return f"<Reminder name={self.name}>" 

    def get_notification_time(self):
        appointment_time = arrow.get(self.time)
        reminder_time = appointment_time.shift(minutes=-self.delta)
        return reminder_time




def connect_to_db(app):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///projectdb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

# app = Flask(__name__)

# connect_to_db(app)


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)