"""CRUD operations."""

from model import db, User, Pet, Appointment, Schedule, connect_to_db


def create_user(name,email, password, zipcode, phone_no):
    """Create and return a new user."""

    user = User(name='name',email='email', password='password', zipcode='zipcode', phone_no='phone_no')

    db.session.add(user)
    db.session.commit

    return user


def create_pet(pet_name, species,user_id, pic_url):
    """Create and return a new pet."""

    pet = Pet(pet_name='pet_name', species='species', user_id='user_id', pic_url='pic_url')

    db.session.add(pet)
    db.session.commit

    return pet


def create_appointment(pet_id , appointment_time_stamp, appointment_type,twilio):
    """Create and return an appointment."""

    appointment= Appointment(pet_id='pet_id' , appointment_time_stamp='appointment_time_stamp', appointment_type='appointment_type',twilio='twilio')

    db.session.add(appointment)
    db.session.commit

    return appointment

def create_schedule(pet_id , meal_schedule, medicine_schedule):
    """Create and return an appointment."""

    schedule= Schedule(pet_id='pet_id' , schedule_type='schedule_type', time_schedule='time_schedule')

    db.session.add(schedule)
    db.session.commit

    return schedule



if __name__ == '__main__':
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)