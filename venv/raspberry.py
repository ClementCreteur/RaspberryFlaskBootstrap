import RPi.GPIO as GPIO
from singleton import Singleton

class Raspberry(metaclass=Singleton):
    def __init__(self):
        print('Raspberry: GPIO Init')
        GPIO.setmode(GPIO.BCM)

    def setup(self, pin, in_out):
        GPIO.setup(pin, in_out)

    def setupIn(self, pin, pud):
        GPIO.setup(pin, GPIO.IN, pull_up_down=pud)

    def setupOut(self, pin, value):
        self.setup(pin, GPIO.OUT)
        GPIO.output(pin, value)

    def setupOutHigh(self, pin):
        self.setupOut(pin, GPIO.HIGH)

    def setupOutLow(self, pin):
        self.setupOut(pin, GPIO.LOW)

    def read(self, pin):
        return GPIO.input(pin)
        
    def dispose(self):
        print('Raspberry: GPIO cleanup')
        GPIO.cleanup()
