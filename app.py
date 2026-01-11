from flask import Flask, render_template
from config import Config
from extensions import db
from routes.diagnosis import diagnosis_bp
from routes.auth import auth_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(diagnosis_bp)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)