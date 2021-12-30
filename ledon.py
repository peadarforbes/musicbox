#!/usr/bin/python
# This program turns on the LEDs at bootup

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)


GPIO.output(33, GPIO.HIGH)
GPIO.output(31, GPIO.HIGH)
GPIO.output(29, GPIO.HIGH)
#GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
#GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)


