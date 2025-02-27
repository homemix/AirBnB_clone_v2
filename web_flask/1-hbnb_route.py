#!/usr/bin/python3
""" Flask Hello Route """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def HBNB():
    """ Hello, HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB_2():
    """ Hello, HBNB! """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
