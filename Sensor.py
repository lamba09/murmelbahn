import RPi.GPIO as GPIO


class Lichtschranke(object):

    def __init__(self, pin = 13):
        self._pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._pin, GPIO.IN)

    def blockert(self):
        return bool(GPIO.input(self._pin))
