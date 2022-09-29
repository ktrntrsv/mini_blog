from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CreatePostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField('Submit')
