from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CreatePostForm(FlaskForm):
    post = TextAreaField('say something', validators=[DataRequired(), Length(min=0, max=200)])
    submit = SubmitField('submit')
