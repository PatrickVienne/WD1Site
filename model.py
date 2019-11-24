import sqla_wrapper
import os

# run sqlite only in memory, then all data is destroyed on application restart.
#SQLITE_FILE = ':memory:'

# save all data in a temporary file so it can be inspected
SQLITE_FILE = 'localhost.sqlite'
db = sqla_wrapper.SQLAlchemy(os.getenv("DATABASE_URL", f"sqlite:///{SQLITE_FILE}"))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email, **kwargs):
        self.username = username
        self.email = email
        super().__init__(**kwargs)

    def __repr__(self):
        return f'User[username={self.username}, email={self.email}]'


class Receipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    description = db.Column(db.Text(4000), unique=True)

    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        super().__init__(**kwargs)

    def __repr__(self):
        return f'Receipe[name={self.name}, description={self.description}]'
