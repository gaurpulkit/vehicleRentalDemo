from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create the Flask app
app = Flask(__name__)

# Load the configuration from config.py
app.config.from_object('config')

# Create the database connection
db = SQLAlchemy(app)

# Import the routes module
from app import routes

# Migrate
migrate = Migrate(app, db)

