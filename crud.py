"""CRUD operations."""

from model import db, User, Pet, Appointment, Schedule, connect_to_db


def create_user(name_param,email_param, password_param, zipcode_param, phone_no_param):
    """Create and return a new user."""

    user = User(name=name_param,email=email_param, password=password_param, zipcode=zipcode_param, phone_no=phone_no_param)

    db.session.add(user)
    db.session.commit

    return user


def create_pet(pet_name_param, species_param,user_id_param, pic_url_param):
    """Create and return a new pet."""

    pet = Pet(pet_name=pet_name_param, species=species_param, user_id=user_id_param, pic_url=pic_url_param)

    db.session.add(pet)
    db.session.commit

    return pet


def create_appointment(pet_id_param , appointment_time_stamp_param, appointment_type_param,send_reminder_param):
    """Create and return an appointment."""

    appointment= Appointment(pet_id=pet_id_param , appointment_time_stamp=appointment_time_stamp_param, appointment_type=appointment_type_param,send_reminder=send_reminder_param)

    db.session.add(appointment)
    db.session.commit

    return appointment

def create_schedule(pet_id_param , meal_schedule_param, medicine_schedule_param):
    """Create and return an appointment."""

    schedule= Schedule(pet_id=pet_id_param , schedule_type=schedule_type_param, time_schedule=time_schedule_param)

    db.session.add(schedule)
    db.session.commit

    return schedule

# def create_sample_data():
#     users= User.query.filter_by().all()
#     if len(users) == 0:
#         create_user("aleena waseem", "aleena@gmail.com", "1234", "94582", "5103998740");
#         create_user("taymoor", "taymoor@gmail.com", "12345", "94582", "5108945182");

if __name__ == '__main__':
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)