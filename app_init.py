from flask import Flask, render_template, request, session, redirect, flash
import os
import jinja2

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')
app.jinja_env.undefined = jinja2.StrictUndefined

def run_app():
    app.run(debug=False , host="0.0.0.0", port="4444")
    
        