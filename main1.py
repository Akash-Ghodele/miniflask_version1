""" Hello world application of Flask
"""

from flask import Flask


# `Flask` is a class we use to instantiate an application
app = Flask(__name__)


# First http GET request
@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

