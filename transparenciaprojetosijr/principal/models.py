from transparenciaprojetosijr import db

class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, email):
        self.email = email