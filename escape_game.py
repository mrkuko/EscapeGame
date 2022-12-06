import os
import json
import scripts.haiku as haiku

import flask
from flask import Flask, request

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


@app.route("/game_lvl01/haiku", methods=['POST'])
def lvl01_haiku():
    print(request.form["data"])
    is_correct, msg = haiku.is_haiku(request.form["data"])
    print(is_correct, msg)
    return json.dumps({'success': True, "correct": is_correct, "msg": msg}),\
        200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
