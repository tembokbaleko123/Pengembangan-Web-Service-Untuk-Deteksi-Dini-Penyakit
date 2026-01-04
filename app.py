from flask import Flask
from config import Config
from extensions import db
from routes.diagnosis_routes import diagnosis_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# ⬇️ INI PENTING
app.register_blueprint(diagnosis_bp, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)
