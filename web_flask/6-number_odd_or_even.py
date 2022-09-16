#!/usr/bin/python3
"""
    starts a web application using Flask
"""

from flask import Flask, render_template

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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ptext(text="is cool"):
    """returns Python followed by some text with spaces not _
       default text is cool
    """
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def isnumber(n):
    """returns n is a number if n is int """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """returns a HTML page only if n is an int”"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_template(n):
    """returns a HTML page only if n is an int and odd or even”"""
    ooe = "odd"
    if n % 2 == 0:
        ooe = "even"
    return render_template("6-number_odd_or_even.html", n=n, ooe=ooe)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
