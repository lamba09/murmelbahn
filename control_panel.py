from RPi import GPIO
import time

GPIO.setmode(GPIO.BOARD)

START = 37
STOP = 35
LEFT = 33
RIGHT = 31
SWITCH = 29
RED = 40
GREEN = 38
WHITE = 36

inputs = [START, STOP, LEFT, RIGHT, SWITCH]

outputs = [RED, GREEN, WHITE]

for input in inputs:
    GPIO.setup(input, GPIO.IN)

for output in outputs:
    GPIO.setup(output, GPIO.OUT)


def test_inputs(first, second=None, out_first=RED, out_second=GREEN):
    second = second or first
    while True:
        if GPIO.input(first) == 0:
            GPIO.output(out_first, GPIO.HIGH)
        else:
            GPIO.output(out_first, GPIO.LOW)
        if GPIO.input(second) == 0:
            GPIO.output(out_second, GPIO.HIGH)
        else:
            GPIO.output(out_second, GPIO.LOW)
        time.sleep(0.01)

def test_ouputs(sleep=0.3):
    while True:
        for output in outputs:
            GPIO.output(output, GPIO.HIGH)
            time.sleep(sleep)
            GPIO.output(output, GPIO.LOW)
            time.sleep(sleep)
