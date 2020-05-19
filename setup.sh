#!/bin/bash

# create and activate a new python environment
python3 -m venv venv
. venv/bin/activate

# install libs
pip install Flask
pip install RPi.GPIO

# deactivate python environment
deactivate
