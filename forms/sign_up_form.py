from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from models.user_model import User


class SignUpForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField("Email",
                        validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField("Password",
                             validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField("Verify password",
                            validators=[DataRequired(), EqualTo("password", message="Passwords must match")], )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, *args, **kwargs):
        initial_validation = super(SignUpForm, self).validate()
        print(f"{initial_validation=}")
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username already registered.")
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered.")
            return False
        if self.password != self.confirm:
            self.password.errors.append("Passwords do not match.")
        return True
