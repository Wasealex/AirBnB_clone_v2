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
def C_is_fun(text):
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python/', defaults={'text': 'is cool'})
@app.route("/python/<text>")
def python_is_cool(text):
    return f"Python {escape(text.replace('_', ' ') or 'is cool')}"


if __name__ == "__main__":
    Flask.run(app)
