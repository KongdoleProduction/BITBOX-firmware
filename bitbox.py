# cryptocurrency status alarm
import time
import argparse

import RPi.GPIO as GPIO
import signal
import os

pin_green = 23
pin_red = 24

def init_led():
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

        if place_value >= 10000:
            temp = int(value / 10000)
            if temp != 0:
                play_sound(str(temp) + '.wav', file_dir="numbers")
                time.sleep(0.7)

            if price_value == 10000 and value == 0:
                play_sound('10000.wav', file_dir="numbers")
        else:
            if value != 0:
                play_sound(str(value) + '.wav', file_dir="numbers")
                time.sleep(0.7)

    play_sound('won.wav', file_dir="numbers")
    time.sleep(0.7)

def main():
    init_led()
    speak_price(23934567)

if __name__ == '__main__':
    main()
