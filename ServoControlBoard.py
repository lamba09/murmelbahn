import Adafruit_PCA9685


class ServoControlBoard(object):

    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)
        self.servo_min = 160  # Min pulse length out of 4096
        self.servo_max = 420  # Max pulse length out of 4096

    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000  # 1,000,000 us per second
        pulse_length //= 60  # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096  # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        self.pwm.set_pwm(channel, 0, pulse)

    def move(self, pos):
        assert self.servo_min <= pos <= self.servo_max
        self.pwm.set_pwm(0, 0, pos)


class Servo(object):

    def __init__(self, channel):
        self._channel = channel
        self._reverse = False
        self._min_pw = 160
        self._max_pw = 420
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)

    def auf(self):
        self.pwm.set_pwm(self._channel, 0, self._max_pw)

    def zu(self):
        self.pwm.set_pwm(self._channel, 0, self._min_pw)


class Blocker(Servo):

    def __init__(self, channel):
        super(Blocker, self).__init__(channel)


class Weiche(Servo):

    def __init__(self, channel):
        super(Weiche, self).__init__(channel)
        self._min_pw, self._max_pw = self._max_pw, self._min_pw
