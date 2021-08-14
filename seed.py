from models import db, Pet
from app import app

db.drop_all()
db.create_all()

Pets = [
    Pet(name="Stevie Chicks", species="chicken"),
    Pet(name="Blue", species="cat"),
    Pet(name="Red", species="dog"),
    Pet(name="Bubblina", species="fish"),
    Pet(name="Tammy", species="cat"),
    Pet(name="Sushi", species="pig"),
    Pet(name="Scout", species="dog"),
    Pet(name="Piggie", species="dog"),
    Pet(name="Carrot Face", species="rabbit"),
    Pet(name="Jerry", species="mouse"),
    Pet(name="Rocket", species="racoon"),
    Pet(name="Mango", species="fish"),
    Pet(name="Tom", species="cat")
]

db.session.add_all(Pets)
db.session.commit()
