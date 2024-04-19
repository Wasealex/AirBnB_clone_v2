#!/usr/bin/python3
"""script that starts a Flask web application: listening on 0.0.0.0, port 5000
Routes:"/" and display “Hello HBNB!” strict_slashes=False
"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>')
def number_let(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    my_status = ''
    if n % 2 == 0:
        my_status += 'is even'
    else:
        my_status += 'is odd'
    return render_template('6-number_odd_or_even.html', number=n, check=my_status)


if __name__ == "__main__":
    Flask.run(app)
