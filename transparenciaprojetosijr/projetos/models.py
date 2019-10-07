from transparenciaprojetosijr import db
from datetime import datetime

class Projetos(db.Model):
    """Projetos e sua descrição"""

    __tablename__ = 'projetos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    descricao = db.Column(db.String)
    data_criacao = db.Column(db.Date, default=datetime.today())

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Semana(db.Model):
    """Quantidade de projetos de acordo com cada semana"""

    __tablename__ = 'semanas'

    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer)
    data = db.Column(db.Date)

    def __init__(self, quantidade, data):
        self.quantidade = quantidade
        self.data = data

    
class Atividades(db.Model):
    """Atividades e sua descrição"""

    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    descricao = db.Column(db.String)
    data_criacao = db.Column(db.Date, default=datetime.today())

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao