from transparenciaprojetosijr import db

class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text(120), nullable=False)

    def __init__(self, email):
        self.email = email