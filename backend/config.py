from flask import Flask
from flask_sqlalchemy import flask_sqlalchemy
from flask_cors import flask_cors

app = Flask(__name__)
CORS(app)

#creates a database as a file on one's local machine
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = flask_sqlalchemy

db = SQLAlchemy(app)