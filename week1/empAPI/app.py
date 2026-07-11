from flask import Flask, render_template
from config import Config
from models import db
from models.employee import Employee
from routes.employee_routes import employee_bp
from routes.api_routes import api_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

# Register Blueprints
app.register_blueprint(employee_bp)
app.register_blueprint(api_bp)

# Create Database Tables
with app.app_context():
    db.create_all()


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)