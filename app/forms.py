# pip install flask-wtf 
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    title = StringField("Review Title", validators=[DataRequired()])
    review = TextAreaField("Movie Review", validators=[DataRequired()])
    submit = SubmitField("Submit")

