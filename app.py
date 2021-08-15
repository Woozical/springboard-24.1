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
        return try_commit('/add')
    else:   
        return render_template('add-pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_detail_view(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        if try_commit(result_only=True):
            flash('Success!', 'success')
            return redirect(f'/{pet_id}')
        else:
            return redirect(f'/{pet_id}')
    else:
        return render_template('pet-detail.html', pet=pet, form=form)



def try_commit(exception_url="/", success_url="/", result_only=False):
    """
    Attempts to commit session to database. To be used on POST requests after form validation.
    By default, will return an HTTP redirect response with the given success/failure url routes.
    Can set result_only to True, in which case will return True for successful commit, and False for failed commit.
    """
    try:
        db.session.commit()
        return redirect(success_url) if not result_only else True
    except:
        flash('An Error Occured', 'danger')
        db.session.rollback()
        return redirect(exception_url) if not result_only else False