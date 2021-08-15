"""Pet Adoption App"""

from flask import Flask, redirect, render_template, request, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

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

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data, species=form.species.data.lower(), age=form.age.data,
            notes=form.notes.data, photo_url=form.photo_url.data)

        db.session.add(new_pet)
        try:
            db.session.commit()
            return redirect('/')
        except:
            flash("An error occured")
            db.session.rollback()
            return redirect('/add')
    else:   
        return render_template('add-pet.html', form=form)

@app.route('/<int:pet_id>')
def pet_detail_view(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    return render_template('pet-detail.html', pet=pet, form=form)