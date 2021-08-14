from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, URL, Optional


class AddPetForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    age = IntegerField("Age")
    photo_url = StringField("URL of Photo", validators=[Optional(), URL()])
    notes = StringField("Notes")