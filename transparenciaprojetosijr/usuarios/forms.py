from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SubmitField, PasswordField, BooleanField, SelectField, DateField)
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from transparenciaprojetosijr.usuarios.models import Usuario

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message="Campo Obrigatório"), Email(message="Este não é um email válido"), Length(min=3, max=120, message="Minimo de 3 caracteres e máximo de 120.")])
    senha = PasswordField("Senha", validators=[DataRequired(message="Campo Obrigatório"), Length(min=0, max=50, message="Minimo de 3 caracteres e máximo de 50.")])
    lembrar = BooleanField("Lembrar-me", false_values=(False, 'false', 0, '0'))
    submit = SubmitField("Entrar")

class LogoutForm(FlaskForm):
    submit = SubmitField("Sair")


class AdicionarUserForm(FlaskForm):
    nome = StringField("Nome Completo", validators=[DataRequired(message="Campo Obrigatório")])
    email = StringField("Email", validators=[DataRequired(message="Campo Obrigatório"), Email(message="Campo Obrigatório"), Length(min=3, max=120, message="Minimo de 3 caracteres e máximo de 120.")])
    senha = PasswordField("Senha", validators=[DataRequired(message="Campo Obrigatório"), Length(min=0, max=50, message="Minimo de 3 caracteres e máximo de 50.")])
    conf_senha = PasswordField("Senha", validators=[DataRequired(message="Campo Obrigatório"), EqualTo('senha', message="As senhas devem ser iguais."), Length(min=0, max=50, message="Minimo de 3 caracteres e máximo de 50")]) 
    submit = SubmitField("Cadastrar")

    def check_email(self, field):
        user= Usuario.query.filter_by(email=field.data).first()
        if user is None:
            return True
        else:
            return False

    def check_username(self, field):
        user = Usuario.query.filter_by(username=field.data).first()
        if user is None:
            return True
        else:
            return False

class EditarUserForm(FlaskForm):
    nome = StringField("Nome")
    email = StringField("Email", validators=[Email(message="Este não é um email válido."), Length(min=3, max=120, message="Minimo de 3 caracteres e máximo de 120.")])
    username = StringField("Username")
    data_nascimento = DateField("Data de nascimento", format='%Y-%m-%d')
    avatar = FileField('Foto', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    senha = PasswordField("Senha", validators=[EqualTo('conf_senha', message="As senhas devem ser iguais."), Length(min=0, max=50, message="Minimo de 3 caracteres e máximo de 50.")])
    conf_senha = PasswordField("Senha", validators=[Length(min=0, max=50, message="Minimo de 3 caracteres e máximo de 50.")])
    submit = SubmitField("Atualizar perfil")
