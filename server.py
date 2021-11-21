"""Server for pet website."""
import random
from flask import Flask, render_template, request, session, redirect, flash
from model import *
from crud import *
import os
import crud
from utils.sms import send_sample_sms
import jinja2
from g_maps_code import convert_lat_long, get_places_from_coordinates
import json
from flask_sqlalchemy import SQLAlchemy



from jinja2 import StrictUndefined
app = Flask(__name__)


app.secret_key = os.environ.get('FLASK_SECRET_KEY')
app.jinja_env.undefined = jinja2.StrictUndefined



@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template("login.html")

@app.route('/verifyuser', methods=['GET', 'POST'])
def verify_user():

    email_user= request.form.get('email')
    password_user=request.form.get('password')

    user=User.query.filter((User.email== email_user) & (User.password == password_user)).first()
    print(email_user)
    print(password_user)

    if user:
        flash("Logged In!")
        session['user']= user.user_id
        print(session['user'])
        return redirect('/')
    else:
        flash("Wrong email or password entered. Try again!")
        return redirect('/login')

def is_logged_in():
    if 'user' in session:
        return True
    else:
        return False


@app.route('/register', methods=['GET', 'POST'])
def register():

    return render_template("register.html")



@app.route('/newuser', methods=['GET', 'POST'])
def make_new_user(): 
    
    getemail = request.form.get('email')
    getflname = request.form.get('flname')
    getzpcode = request.form.get('zpcode')
    getphone = request.form.get('phone')
    getpassword = request.form.get('password')
    getcpassword = request.form.get('cpassword')

    user = User.query.filter_by(email=getemail).first() 
   
    if user:
        flash("Email already exists. Try logging in ")
        return redirect('/login')

    else:
        if getpassword==getcpassword:
            new_user = crud.create_user(getflname, getemail, getpassword, getzpcode, getphone) 
            flash ("New account created ")
            return redirect('/login')
        else:
            flash("passwords, do not match. Try again")
            return redirect('/register')
    # # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    # new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))  



@app.route('/')
def Index():
    if is_logged_in():

        user=session['user']
        getuser= User.query.filter_by(user_id=user).first()
        getpet= Pet.query.filter_by(user_id=user).first()

        return render_template('index.html',
                            user=getuser,
                            pet=getpet)
    else:
        return redirect('/login')


@app.route('/profile')
def show_profile(): 
    if is_logged_in():
        # send_sample_sms()
        user=session['user']
        print(user)
        getuser= User.query.filter_by(user_id=user).first()
        getpet= Pet.query.filter_by(user_id=user).first()

    
    return render_template("profile.html",
                            user=getuser,
                            pet=getpet)


@app.route('/findvet', methods=['POST', 'GET'])
def get_vet_map():
   
    if is_logged_in():
        user=session['user']
        getuser= User.query.filter_by(user_id=user).first()
        lat_long_user=convert_lat_long(getuser.zipcode)
        places= get_places_from_coordinates(lat_long_user) 
        print()
        print()
         
    return render_template('vetclinic.html')

@app.route('/jsonifycoordinates', methods=['POST', 'GET'])
def jsonify_coordinates():
    searched_zipcode= request.args.get('zpsrch')
    print(searched_zipcode)
    if searched_zipcode == None or searched_zipcode == "":

        user=session['user']
        getuser= User.query.filter_by(user_id=user).first()
        print(getuser)
        lat_long_user=convert_lat_long(getuser.zipcode)
        print (lat_long_user)
        places= get_places_from_coordinates(lat_long_user)
        json_places=json.dumps(places)
        print (json_places)
        return json_places

    else:
        print("Searching for "+searched_zipcode)
        lat_long_searched=convert_lat_long(searched_zipcode)
        places= get_places_from_coordinates(lat_long_searched)
        json_places=json.dumps(places)
        return json_places
   

@app.route('/findsalon', methods=['POST', 'GET'])
def get_grooming_salon():

    return render_template('groomsalon.html')


@app.route('/logout', methods=['POST', 'GET'])
def log_out():

    if is_logged_in():
        session.pop("user", None)
        return redirect('/login')

if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    app.run(debug=True,  host="0.0.0.0", port="5500")