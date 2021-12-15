Learn more about the developer: https://www.linkedin.com/in/aleena-waseem/

contact: aleenataymoor@gmail.com
# PETOOTIE
Full Stack project; a pet website that enables you to view pet profile, set appointment reminders, shop pet products, filter them and add to the cart.

## Overview
A full-stack web pet portal that allowed pet profile creation, storing the information in an SQL database. Within a user's Flask session, users can 
search for nearby Vet Clinics (achieved through an AJAX request to Google Places API and Google Geocoding API), set reminders for upcoming vet appointments
(achieved through Twilio API, Celery and Redis) and explore pet products in the shopping section. Pet products can be filtered on the basis of type , and
can be added to a shopping cart.

## Technologies Used
Python, Jinja, Flask, Javascript, AJAX, PostgreSQL, HTML, CSS, Bootstrap, Google Maps Api( Google Places, Google Geocoding and Google Maps Javascript), Twilio API, Celery, Redis

## Demo
https://www.youtube.com/watch?v=FnC6oCMLDyI

## How to run "Petootie" locally:

Download the files

Create virtual environment inside of the /api folder

Then create virtual environment by using command: env/bin/activate

Run pip3 install -r requirements.txt

In the main folder, run npm install

source database by 1) run command: dropdb projectdb 2) run command: createdb projectdb 3) run command: psql projectdb < database.sql

Create a secrets.sh folder to host API key for Google Maps

Run source secrets.sh

Open three terminals - in one run command: redis-server , in second terminal run command: celery -A tasks.celery worker -l info   , and in the third terminal run: python3 server.py

On local host, register and login to experience all the services that petootie provides
