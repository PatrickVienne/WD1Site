import flask
import random
import model

app = flask.Flask(__name__)


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

    receipe_1 = model.Receipe("Apfelstrudel", "Cut Apple Bake Sweet")
    receipe_2 = model.Receipe("Hamburger", "Fry Meat And Eat")
    receipe_3 = model.Receipe("Suppe", "Cut carrots Add Water")

    return flask.render_template("blog.html", receipes=[receipe_1, receipe_2, receipe_3])


if __name__ == '__main__':
    app.run()
