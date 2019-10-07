from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, SubmitField, PasswordField, BooleanField, SelectField, DateField)
from wtforms.validators import DataRequired, Email, EqualTo, Length

class AdicionarProjetoForm(FlaskForm):
    nome = StringField("Nome do Projeto", validators=[DataRequired(message="Campo Obrigatório")])
    descricao = TextAreaField("Descrição", validators=[DataRequired(message="Campo Obrigatório")])
    submit = SubmitField("Adicionar")


class AdicionarAtividadeForm(FlaskForm):
    nome = StringField("Nome da atividade", validators=[DataRequired(message="Campo Obrigatório")])
    descricao = TextAreaField("Descrição", validators=[DataRequired(message="Campo Obrigatório")])
    submit = SubmitField("Adicionar")