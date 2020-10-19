# from wtforms import SelectField
# from flask_wtf import FlaskForm
#
# class MyForm(FlaskForm):
#     choice = SelectField()

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    Imie = StringField(
        "Twoje imię", validators=[DataRequired("Podaj swoje imię")]
    )
    Email = StringField("Twoje e-mail", validators=[DataRequired()])
    submits = StringField("Tytuł wiadomości", validators=[DataRequired()])
    messege = StringField("Wiadomość", validators=[DataRequired()])
