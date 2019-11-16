import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html", myname="Patrick")

@app.route("/fakebook")
def fakebook():
    return flask.render_template("fakebook.html")


if __name__ == '__main__':
    app.run()
