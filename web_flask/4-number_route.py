#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """
    Return string
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Return string
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """
    Return formatted text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """
    Reformat text
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """
    Display n if n is int
    """
    return str(n) + ' is a number'


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
    