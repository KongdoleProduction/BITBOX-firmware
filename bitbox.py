# cryptocurrency status alarm
import time
import argparse
import math

import RPi.GPIO as GPIO
import signal
import os

pin_green = 23
pin_red = 24

def init_led():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_green, GPIO.OUT)
    GPIO.setup(pin_red, GPIO.OUT)
    GPIO.output(pin_green, False)
    GPIO.output(pin_red, False)

def deinit_led():
    GPIO.output(pin_green, False)
    GPIO.output(pin_red, False)

sounds_path = './sounds/'
sounds = {
        'bch': 'voice_bch.mp3',
        'btc': 'voice_btc.mp3',
        'etc': 'voice_etc.mp3',
        'eth': 'voice_eth.mp3',
        'iota': 'voice_iota.mp3',
        'ltc': 'voice_ltc.mp3',
        'qtum': 'voice_qtum.mp3',
        'xrp': 'voice_xrp.mp3',
        'neg1': 'voice_negative1.mp3',
        'neg2': 'voice_negative2.mp3',
        'neg3': 'voice_negative3.mp3',
        'pos1': 'voice_positive1.mp3',
        'pos2': 'voice_positive2.mp3',
        'pos3': 'voice_positive3.mp3',
        }

def play_sound(file_name, file_dir='voices'):
    os.system('mpg123 -q ' + os.path.join(file_dir, file_name) + ' &')

def speak_price(price):
    price = int(price)
    price_str = str(price)
    num_digits = len(price_str)

    for i, digit_str in enumerate(price_str):
        digit = int(digit_str)
        place_value = int(math.pow(10, num_digits - i - 1))
        value = digit * place_value

        if place_value >= 100000:
            temp = int(value / 10000)
            if temp != 0:
                play_sound(str(temp) + '.mp3', file_dir="numbers")
                time.sleep(0.6)

        elif place_value == 10000:
            if digit == 0:
		play_sound('10000p.mp3', file_dir="numbers")
                time.sleep(0.5)
            else:
		play_sound(str(value) + '.mp3', file_dir="numbers")
                time.sleep(0.6)
        else:
            if value != 0:
                play_sound(str(value) + '.mp3', file_dir="numbers")
                time.sleep(0.6)

    play_sound('won.mp3', file_dir="numbers")
    time.sleep(0.6)

def main():
    init_led()
    speak_price(23914567)
    speak_price(23000000)

if __name__ == '__main__':
    main()
