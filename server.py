"""Server for pet website."""
import random
from flask import Flask, render_template, request, flash, session, redirect
from model import *
from crud import *
import os
import crud
from utils.sms import send_sample_sms


from jinja2 import StrictUndefined
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():

    return render_template("register.html")



@app.route('/')
def Index():
    getuser= User.query.filter_by(user_id=3).first()
    getpet= Pet.query.filter_by(user_id=3).first()
    
    return render_template("index.html",
                            user=getuser,
                            pet=getpet)


@app.route('/profile')
def show_profile(): 
    send_sample_sms()
    getuser= User.query.filter_by(user_id=3).first()
    getpet= Pet.query.filter_by(user_id=3).first()

    
    return render_template("profile.html",
                            user=getuser,
                            pet=getpet)



if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    app.run(debug=True,  host="0.0.0.0")