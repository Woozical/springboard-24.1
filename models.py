from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(flask_app):
    db.app = flask_app
    db.init_app(flask_app)


class Pet(db.Model):
    __tablename__ = "pets"

    # Required fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    available = db.Column(db.Boolean, nullable=False, default=True)
    # Optional fields
    photo_url = db.Column(db.String)
    age = db.Column(db.Integer)
    notes = db.Column(db.String)