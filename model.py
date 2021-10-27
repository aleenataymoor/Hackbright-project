
"""Models for Pet Website."""
#projectdb

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(35), unique=True)
    password= db.Column(db.String(20), nullable=False) # should be hashed (use library)
    zipcode=   db.Column(db.String(10))
    phone_no= db.Column(db.String(12))

    pets= db.relationship('Pet', back_populates="users")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


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
    appointments= db.relationship('Appointment', back_populates="pets")
    schedules= db.relationship('Schedule', back_populates="pets")
    
    def __repr__(self):
        return f"<Pet pet_id={self.pet_id} pet_name={self.pet_name} species={self.species}>"

class Appointment(db.Model):
    """An Appointment."""

    __tablename__ = "appointments"
    appointment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.pet_id'), nullable=False)
    appointment_time_stamp = db.Column(db.DateTime, nullable= False)
    appointment_type= db.Column(db.String(15))
    # rename this to send_reminder or something more descriptive
    twilio= db.Column(db.Boolean)

    pets= db.relationship('Pet', back_populates="appointments")

    def __repr__(self):
        return f"<Appointment appointment_id={self.appointment_id} appointment_type={self.appointment_type}>"
        #Can i use foreign key pet_id here with self?


class Schedule(db.Model): 
    """Pet Schedule"""

    __tablename__ = "schedules"
    schedule_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.pet_id'), nullable=False)
    schedule_type= db.Column(db.String(15))
    time_schedule= db.Column(db.DateTime)

    pets= db.relationship('Pet', back_populates="schedules")

    def __repr__(self):
        return f"<Schedule schedule_id={self.schedule_id} meal_schedule={self.meal_schedule} medicine_schedule={self.medicine_schedule}>"




# class Shopping(db.Model):
#     """A Shop."""

#     __tablename__ = "shoppings"
#     product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    
    




def connect_to_db(app):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///projectdb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

app = Flask(__name__)

connect_to_db(app)



if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)