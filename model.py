import sqla_wrapper
import os

# run sqlite only in memory, then all data is destroyed on application restart.
#SQLITE_FILE = ':memory:'

# save all data in a temporary file so it can be inspected
SQLITE_FILE = 'localhost.sqlite'

db = sqla_wrapper.SQLAlchemy(os.getenv("DATABASE_URL", f"sqlite:///{SQLITE_FILE}"))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)


class Receipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String, unique=True)
    taste = db.Column(db.String)

