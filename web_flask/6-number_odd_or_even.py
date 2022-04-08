#!/usr/bin/python3
""" Flask Hello Route """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False
app.template_folder = './templates'


@app.route('/')
def HBNB():
    """ Hello, HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB_2():
    """ Hello, HBNB! """
    return "HBNB"


@app.route('/c/<text>')
def C_text(text):
    """ C text """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    """ Python text """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ Number route """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Number route """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ Number route """
    status = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html',
                           number=n, status=status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
