from flask import Flask

app = Flask(__name__)

from app import routes

# para trabalhar com banco de dados

# pip install Flask-SQLAlchemy

# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
# db = SQLAlchemy(app)