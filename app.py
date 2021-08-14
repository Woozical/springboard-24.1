"""Pet Adoption App"""

from flask import Flask, redirect, render_template, request, flash
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_KEY_HERE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def home_view():
    pets = Pet.query.all()
    return render_template('home.html', pets = pets)