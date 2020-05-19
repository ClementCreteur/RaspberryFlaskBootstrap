import atexit
import RPi.GPIO as GPIO
from flask import Flask, redirect, url_for, render_template, jsonify
from raspberry import Raspberry

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def other(path):
    # with this endpoint, the path can be handled on the client side
    # eg. by an Angular webpage
    return render_template('index.html')

@app.route('/api/outHigh/<int:pin>')
def out_high(pin):
    Raspberry().setupOutHigh(pin)
    return jsonify(status='OK')

@app.route('/api/outLow/<int:pin>')
def out_low(pin):
    Raspberry().setupOutLow(pin)
    return jsonify(status='OK')

@app.route('/api/setupIn/<int:pin>')
def setup_in(pin):
    Raspberry().setupIn(pin, GPIO.PUD_DOWN)
    return jsonify(status='OK')

@app.route('/api/read/<int:pin>')
def read(pin):
    value = Raspberry().read(pin)
    return jsonify(status='OK', value=value)

@app.teardown_appcontext
def teardown_appcontext(p):
    # end of request
    pass

def dispose():
    Raspberry().dispose()

atexit.register(dispose)
