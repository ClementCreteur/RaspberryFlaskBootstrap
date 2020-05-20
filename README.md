# RaspberryFlaskBootstrap

This is a minimal bootstrap Flask application to run on you Raspberry Pi. It allows you to control GPIOs via a simple REST API and can easily be extended.

## Prerequisite

* Python3
* A raspberry PI

## Setup

* Login/ssh on you Raspberry Pi
* Clone repository
* Run `./setup.sh`. This will create a virtual python env and download the required libraries (Flask and Rasp.GPIO)

## Launch
* Run `./run.sh` on your raspberry
* Go to http://<your_raspberry_ip>:5000 from another device

## Usage example
* Plug a led (+) on Pin GPIO17 and connect to ground (use resistor if needed)
* http://<your_raspberry_ip>:5000/api/outHigh/17 will turn on the led
* http://<your_raspberry_ip>:5000/api/outLow/17 will turn off the led

## Note
* You can use the application as a json REST API or you can display actual pages using the Flask templating engine. You can also use more advanced front technologies like Angular. If you want to do so, update the index.html in the templates/ directory and add you js script files in the static/ directory
* The application is not exactly stateless since we use a singleton to keep track of the GPIOs state