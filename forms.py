from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import InputRequired, URL, Optional, NumberRange, AnyOf


def anyof_typesafe(form, field):
    if field.data.lower() not in {"cat", "dog", "porcupine"}:
        return ValidationError("Only accepting dogs, cats and porcupines at this time")


class AddPetForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), anyof_typesafe])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    photo_url = StringField("URL of Photo", validators=[Optional(), URL()])
    notes = StringField("Notes")