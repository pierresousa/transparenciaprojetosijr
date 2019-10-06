from transparenciaprojetosijr import db, login_manager
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)

class Usuario(db.Model, UserMixin):
	"""Usuarios do sistema"""

	__tablename__ = "usuarios"

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(120), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	senha = db.Column(db.String, nullable=False)

	urole = db.Column(db.String(80), server_default="user", nullable=False)


	def __init__(self, nome, email, senha, cargo):
		self.nome = nome
		self.email = email
		self.senha = senha
		self.urole = cargo

	def get_urole(self):
		return self.urole

	def check_senha(self, pasword):
		bcript = Bcrypt()
		return bcript.check_password_hash(self.senha, pasword)
