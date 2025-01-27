#!/usr/bin/python3
"""
    starts a web application using Flask
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """returns C followed by some text with spaces not _ """
    return 'C ' + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
