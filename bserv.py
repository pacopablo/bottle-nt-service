__author__ = 'pacopablo'

from bottle import Bottle

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"