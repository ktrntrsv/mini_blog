from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length


class EditBioForm(FlaskForm):
    bio = StringField("editBio", validators=(DataRequired(), Length(min=1, max=30),))
    save = SubmitField("submit")

    def __init__(self, *args, **kwargs):
        super(EditBioForm, self).__init__(*args, **kwargs)


