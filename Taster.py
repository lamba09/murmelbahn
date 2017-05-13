import RPi.GPIO as GPIO


class Knopf(object):

    def __init__(self, pin = 40, invertiert = True):
        self._pin = pin
        self._invertiert = invertiert
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def aktiviert(self):
        if self._invertiert:
            return not bool(GPIO.input(self._pin))
        else :
            return bool(GPIO.input(self._pin))

start = Knopf(37, False)
stop = Knopf(38, True)
