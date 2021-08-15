from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, ValidationError, BooleanField
from wtforms.validators import InputRequired, URL, Optional, NumberRange, Length


def anyof_casesafe(form, field):
    if field.data.lower() not in {"cat", "dog", "porcupine"}:
        return ValidationError("Only accepting dogs, cats and porcupines at this time")


class AddPetForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), anyof_casesafe])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    photo_url = StringField("URL of Photo", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[
        Length(max=50, message="50 characters or less"),
        Optional()
    ])

class EditPetForm(FlaskForm):
    photo_url = StringField("URL of Photo", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[
        Length(max=100, message="Character Limit Reached"),
        Optional()
    ])
    available = BooleanField("Available?", default=True)