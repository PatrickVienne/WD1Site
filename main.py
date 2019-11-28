import flask
import random
import model
import string

from flask import request
from flask import url_for

N_USERS = 10
N_RECEIPES = 10

app = flask.Flask(__name__)
db = model.db


db.create_all()


def create_dummy_users():
    users = []
    for x in range(N_USERS):
        name = "".join(random.choices(string.ascii_lowercase, k=10))
        user = model.User(username=name, email=f"{name}@home.com")
        users.append(user)

    my_user = model.User(username="admin", email="admin@home.com")
    users.append(my_user)
    test_user = model.User(username="test", email="test@home.com")
    users.append(test_user)

    for user in users:
        if not db.query(model.User).filter_by(username=user.username).first():
            db.add(user)

    db.commit()


def create_dummy_receipes():
    receipes = []
    for x in range(N_RECEIPES):

        name = "".join(random.choices(string.ascii_lowercase, k=10))
        name = name.capitalize()
        description = "".join(random.choices(string.ascii_lowercase + "    ", k=80))
        taste = "".join(random.choices(string.ascii_lowercase, k=5))

        new_receipe = model.Receipe(name=name, description=description, taste=taste)
        receipes.append(new_receipe)

    receipe_1 = model.Receipe(name="Apfelstrudel", description="Cut Apple Bake Sweet", taste="sweet")
    receipes.append(receipe_1)
    receipe_2 = model.Receipe(name="Hamburger", description="Fry Meat And Eat", taste="salty")
    receipes.append(receipe_2)
    receipe_3 = model.Receipe(name="Suppe", description="Cut carrots Add Water", taste="sweet")
    receipes.append(receipe_3)

    for receipe in receipes:
        if not db.query(model.Receipe).filter_by(name=receipe.name).first():
            db.add(receipe)

    db.commit()


def add_dummy_data():
    create_dummy_users()
    create_dummy_receipes()


@app.route("/")
def index():
    return flask.render_template("index.html", myname="Patrick")


@app.route("/fakebook")
def fakebook():
    return flask.render_template("fakebook.html")


@app.route("/secret-number-game")
def secret_number_game():
    secret = random.randint(0, 10)
    return flask.render_template("secret_number_game.html", secret_number=secret)


@app.route("/blog")
def blog():
    db_receipes = db.query(model.Receipe).filter_by(taste="sweet").all()
    return flask.render_template("blog.html", receipes=db_receipes)


@app.route("/register", methods=["GET", "POST"])
def register():

    current_request = flask.request

    if current_request.method=="GET":
        return flask.render_template("register.html")

    elif current_request.method=="POST":
        # TODO: register valid user
        email = current_request.form.get('email')
        username = current_request.form.get('username')
        user_exists = db.query(model.User).filter_by(username=username).first()
        email_exists = db.query(model.User).filter_by(email=email).first()
        if user_exists:
            print("User already exists")
        elif email_exists:
            print("Email already exists")
        else:
            new_user = model.User(username=username, email=email)
            db.add(new_user)
            db.commit()
            return flask.redirect(flask.url_for('register'))


@app.route("/accounts")
def accounts():
    all_users = db.query(model.User).all()
    return flask.render_template('accounts.html', accounts=all_users)


@app.route("/accounts/<account_id>/delete", methods=["GET", "POST"])
def account_delete(account_id):
    user_to_delete = db.query(model.User).get(account_id)
    if user_to_delete is None:
        return flask.redirect(flask.url_for('accounts'))

    current_request = flask.request
    if current_request.method=="GET":
        return flask.render_template("account_delete.html", account=user_to_delete)
    elif current_request.method=="POST":
        db.delete(user_to_delete)
        db.commit()
        return flask.redirect(flask.url_for('accounts'))
    else:
        return flask.redirect(flask.url_for('accounts'))


if __name__ == '__main__':
    add_dummy_data()
    app.run()
