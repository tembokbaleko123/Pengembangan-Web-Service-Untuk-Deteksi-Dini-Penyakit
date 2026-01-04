from extensions import db

class Penyakit(db.Model):
    __tablename__ = "penyakit"

    id = db.Column(db.Integer, primary_key=True)
    kode = db.Column(db.String(10), unique=True)
    nama = db.Column(db.String(100))
