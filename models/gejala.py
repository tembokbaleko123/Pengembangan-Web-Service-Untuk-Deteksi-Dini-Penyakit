from extensions import db

class Gejala(db.Model):
    __tablename__ = "gejala"

    id = db.Column(db.Integer, primary_key=True)
    kode = db.Column(db.String(10), unique=True)
    nama = db.Column(db.String(255))
    densitas = db.Column(db.Float)
