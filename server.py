"""Server for pet website."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

from jinja2 import StrictUndefined
app = Flask(__name__)

# os.system('dropdb projectdb')
# os.system('createdb projectdb')


@app.route('/')
def Index():
    dog_name="tommy"
    dog_image="https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg"
    return render_template("index.html",
                            dog_name_html=dog_name,
                            dog_image_html=dog_image)





if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True,  host="0.0.0.0")