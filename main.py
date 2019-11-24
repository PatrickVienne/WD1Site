import flask
import random
import model

import string

app = flask.Flask(__name__)
db = model.db

db.create_all()


def add_example_users():
    for x in range(4):
        name = "".join([x for x in random.choices(string.ascii_letters, k=8)]).capitalize()
        user = model.User(username=name,
                          email=f"{name}@haus.at")
        # only add if it does not exist already
        if not db.query(model.User).filter_by(email=user.email).first():
           db.add(user)
    db.commit()


def add_example_receipes():
    receipe_1 = model.Receipe("Apfelstrudel", "Cut Apple Bake Sweet")
    receipe_2 = model.Receipe("Hamburger", "Fry Meat And Eat")
    receipe_3 = model.Receipe("Suppe", "Cut carrots Add Water")
    # only add if it does not exist already
    db.add_all([x for x in (receipe_1, receipe_2, receipe_3)
                if not db.query(model.Receipe).filter_by(name=x.name).first()
                ])
    db.commit()


def add_example_data():
    add_example_users()
    add_example_receipes()


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
    return flask.render_template("blog.html", receipes=db.query(model.Receipe).all())


if __name__ == '__main__':
    add_example_data()
    app.run()
