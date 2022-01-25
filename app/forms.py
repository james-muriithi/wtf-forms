from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired


class ReviewForm(FlaskForm):
    title = StringField("Review Title", validators=[InputRequired()])
    review = TextAreaField("Movie Review", validators=[InputRequired()])
    submit = SubmitField("Submit")

