#!/usr/bin/python3
"""script that starts a Flask web application: listening on 0.0.0.0, port 5000
fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
"""
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    states = sorted(list(storage.all("State").values()), key=lambda s: s.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()

if __name__ == "__main__":
    Flask.run(app)
