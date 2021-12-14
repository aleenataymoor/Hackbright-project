"""CRUD operations."""

from model import db, User, Pet, Reminder, connect_to_db


def create_user(name_param,email_param, password_param, zipcode_param, phone_no_param):
    """Create and return a new user."""

    user = User(name=name_param,email=email_param, password=password_param, zipcode=zipcode_param, phone_no=phone_no_param)

    db.session.add(user)
    db.session.commit()

    return user


def create_pet(pet_name_param, species_param,user_id_param, pic_url_param):
    """Create and return a new pet."""

    pet = Pet(pet_name=pet_name_param, species=species_param, user_id=user_id_param, pic_url=pic_url_param)

    db.session.add(pet)
    db.session.commit()

    return pet


def create_reminder( user_parm,name_param, phone_number_param,delta_param, time_param,timezone_param):
    """Create and return a reminder."""

    reminder= Reminder(user_id=user_parm, name=name_param, phone_number=phone_number_param,delta=delta_param, time=time_param,
    timezone=timezone_param)

    db.session.add(reminder)
    db.session.commit()

    return reminder




if __name__ == '__main__':
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)