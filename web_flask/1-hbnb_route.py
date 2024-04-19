#!/usr/bin/python3
"""script that starts a Flask web application: listening on 0.0.0.0, port 5000
Routes:"/" and display “Hello HBNB!” strict_slashes=False
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_HBNB():
    return "Hello HBNB!"


@app.route("/hbnb")
def display_HBNB():
    return "HBNB"


if __name__ == "__main__":
    Flask.run(app)
