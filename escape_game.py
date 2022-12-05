import os

import flask
from flask import Flask

print(os.getcwd())
app = Flask(__name__, template_folder="root", static_folder=os.getcwd())


@app.route("/")
def index():
    # with open("root/index.html", "r") as f:
    #     return f.read()
    return flask.render_template("index.html")


@app.route("/game_welcome")
def lvl00():
    return flask.render_template("game_welcome.html")


@app.route("/game_lvl01")
def lvl01():
    return flask.render_template("game_lvl01.html")


@app.route("/game_lvl02")
def lvl02():
    return flask.render_template("game_lvl02.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
