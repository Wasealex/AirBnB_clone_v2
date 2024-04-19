#!/usr/bin/python3
"""script that starts a Flask web application: listening on 0.0.0.0, port 5000
Routes:"/" and display “Hello HBNB!” strict_slashes=False
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def hello_HBNB():
    return "Hello HBNB!"


@app.route("/hbnb")
def display_HBNB():
    return "HBNB"


@app.route("/c/<text>")
def hello(text):
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == "__main__":
    Flask.run(app)
