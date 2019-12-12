import sqla_wrapper
import os

# run sqlite only in memory, then all data is destroyed on application restart.
#SQLITE_FILE = ':memory:'

# save all data in a temporary file so it can be inspected
SQLITE_FILE = 'localhost.sqlite'

db = sqla_wrapper.SQLAlchemy(os.getenv("DATABASE_URL", f"sqlite:///{SQLITE_FILE}"))

# db = sqla_wrapper.SQLAlchemy("postgres://qrcrrzujqhrmol:669cb880e4f79ced678ac296be83b6080c3240dc9745d949ca7fddcb45cf18ed@ec2-46-137-187-23.eu-west-1.compute.amazonaws.com:5432/derspsvghaisgh")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    session_token = db.Column(db.String, nullable=True)
    session_expiry_datetime = db.Column(db.DateTime, nullable=True)


class Receipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String, unique=True)
    taste = db.Column(db.String)

