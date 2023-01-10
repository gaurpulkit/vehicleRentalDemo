import os

# Database configuration
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/postgres'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key for signing cookies
SECRET_KEY = 'secret-key'

# Other configuration values
DEBUG = True