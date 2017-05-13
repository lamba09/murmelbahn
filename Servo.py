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
        self._ist_auf = None

    def auf(self, warten=True):
        self._pwm.set_pwm(self._channel, 0, self._max_pw)
        if warten:
            time.sleep(self._sleep)
        self._ist_auf = True

    def zu(self, warten=True):
        self._pwm.set_pwm(self._channel, 0, self._min_pw)
        if warten:
            time.sleep(self._sleep)
        self._ist_auf = False

    def ist_offen(self):
        return self._ist_auf

    def switch(self):
        if self._ist_auf:
            self.zu()
        else:
            self.auf()

a = Servo(0)
b = Servo(1)
c = Servo(2)
d = Servo(3)
e = Servo(4)
f = Servo(5)
g = Servo(6)
h = Servo(7)
i = Servo(8)
j = Servo(9)
