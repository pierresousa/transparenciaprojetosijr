from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SubmitField, PasswordField, BooleanField, SelectField, DateField)
from wtforms.validators import DataRequired, Email, EqualTo, Length

class AdicionarEmailForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message="Campo Obrigatório"), Email(message="Campo Obrigatório"), Length(min=3, max=120, message="Minimo de 3 caracteres e máximo de 120.")])
    submit = SubmitField("Cadastrar")