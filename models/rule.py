from extensions import db

class Rule(db.Model):
    __tablename__ = "rules"

    id = db.Column(db.Integer, primary_key=True)

    gejala_id = db.Column(
        db.Integer,
        db.ForeignKey("gejala.id"),
        nullable=False
    )

    penyakit_id = db.Column(
        db.Integer,
        db.ForeignKey("penyakit.id"),
        nullable=False
    )
