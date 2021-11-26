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

@app.route('/shopping', methods=['POST', 'GET'])
def shop_for_pets():
        product_dict=fetch_products()
        
        return render_template('shopping.html',
                            product_dict=product_dict)


def fetch_products():
    product_dict={}
    with open("petproducts.txt", "r") as file:
        for line in file:
            product_id, product_type, name, weight, description,url,price = line.strip().split("|")
            product_dict[product_id]=[product_id, product_type, name, weight, description,url,price]
    return product_dict


@app.route('/productpage/<product_key>', methods=['POST', 'GET'])
def get_product_page(product_key):
    product_dict=fetch_products()
    specs_list=product_dict[product_key]


    return render_template('productpage.html',
                            specs=specs_list)


@app.route("/add_to_cart/<prod_id>")
def add_to_cart(prod_id):
    """Add a product to cart and redirect to shopping cart page.."""

    if 'cart' in session:
        cart = session['cart']
    else:
        cart = session['cart'] = {}

    product_dict=fetch_products()
    product_id=product_dict[prod_id][0]

    cart[product_id] = cart.get(prod_id, 0) + 1

    
    flash("Product successfully added to cart.")

    return redirect("/cart")


@app.route("/cart")
def show_shopping_cart():
    """Display content of shopping cart."""
    product_dict= fetch_products()
    order_total = float(0)
    final_dict={}
    cart = session.get("cart", {})
  
    for prod_id, quantity in cart.items():
        product = product_dict[prod_id]
    
        total_cost = quantity * float(product[6])
        prod_type=product[1]
        name=product[2]
        url=product[5]
        price=product[6]
        order_total += total_cost

  
        final_dict[prod_id]=[prod_type,name,url,price,total_cost,quantity]
   
    return render_template("cart.html",
                            cart=cart,
                            order_total=order_total,
                            final_dict=final_dict
                            )


@app.route('/logout', methods=['POST', 'GET'])
def log_out():

    if is_logged_in():
        session.pop("user", None)
        session.pop("cart",None)
        return redirect('/login')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=False , host="0.0.0.0", port="5500")