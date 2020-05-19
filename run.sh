#!/bin/bash

# activate python environment 
. venv/bin/activate
cd venv

# run flask in dev mode (debug) and visible by other computers on the network
export FLASK_ENV=development
export FLASK_APP=app.py
flask run --host=0.0.0.0
