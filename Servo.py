import Adafruit_PCA9685
import time

class Servo(object):

    def __init__(self, channel):
        self._channel = channel
        self._reverse = False
        self._min_pw = 160
        self._max_pw = 420
        self._pwm = Adafruit_PCA9685.PCA9685()
        self._pwm.set_pwm_freq(60)
        self._sleep = 0.3

    def auf(self, warten=True):
        self._pwm.set_pwm(self._channel, 0, self._max_pw)
        if warten:
            time.sleep(self._sleep)

    def zu(self, warten=True):
        self._pwm.set_pwm(self._channel, 0, self._min_pw)
        if warten:
            time.sleep(self._sleep)
