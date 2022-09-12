from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from models import user_model
import email_validator


class SignInForm(FlaskForm):
    username = StringField("Username", validators=(DataRequired(),))
    password = PasswordField("Password", validators=(DataRequired(),))
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.user = None



