from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField, BooleanField, URLField
from wtforms.validators import InputRequired, Optional, AnyOf, NumberRange


class AddPetForm(FlaskForm):
    """ Form for adding pets """

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(["Dog", "Fish", "Bird"])])
    photo_url = URLField("Image URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(0, 30)])
    notes = TextAreaField("Tell us about them:", validators=[Optional()])
    available = BooleanField("Currently Available", validators=[Optional()], default=True)

class EditPetForm(FlaskForm):
    """ Form for editing pets """

    photo_url = URLField("Image URL", validators=[Optional()])
    notes = TextAreaField("Tell us about them:", validators=[Optional()])
    available = BooleanField("Currently Available", validators=[Optional()], default=True)