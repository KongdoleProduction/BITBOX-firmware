# cryptocurrency status alarm
import time
import RPi.GPIO as GPIO

pin_green = 23
pin_red = 24

def init_led():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_green, GPIO.OUT)
    GPIO.setup(pin_red, GPIO.OUT)
    GPIO.output(pin_green, False)
    GPIO.output(pin_red, False)

def blink():
    GPIO.output(pin_red, True)
    GPIO.output(pin_green, True)
    time.sleep(2)

def deinit_led():
    GPIO.output(pin_green, False)
    GPIO.output(pin_red, False)

if __name__ == '__main__':
    init_led()
    blink()
    deinit_led
