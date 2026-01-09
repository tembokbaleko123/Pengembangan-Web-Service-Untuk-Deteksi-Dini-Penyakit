# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/sistem_pakar_cp"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # WAJIB untuk JWT
    SECRET_KEY = "secret-flask-sistem-pakar"
    JWT_SECRET_KEY = "secret-jwt-sistem-pakar"
