from extensions import db
from datetime import datetime

class DiagnosisHistory(db.Model):
    __tablename__ = "diagnosis_history"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    hasil = db.Column(db.JSON, nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
