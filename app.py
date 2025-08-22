from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from database import db
from routes.router_auth import auth_bp
from routes.feedback_routes import feedback_bp

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)
db.init_app(app)

jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(feedback_bp)

with app.app_context():
    db.create_all()

@app.route("/")
def last():
    return "Hello, Flask server is running"

if __name__ == "__main__":
    app.run(debug=True)
