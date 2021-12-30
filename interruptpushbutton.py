#!/usr/bin/python
# This program detects a pushed button via an interrupt and toggles play/pause, moves to next track, or last track depending on what button was pressed


import RPi.GPIO as GPIO
import signal
import sys
import time
import subprocess

#Setup GPIO numbers for button connections
TOGGLE_GPIO = 38
NEXTTRACK_GPIO = 36
PREVTRACK_GPIO = 40

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
def button_pressed_callback(channel):    
    if channel == TOGGLE_GPIO: # Toggle GPIO pressed
    	subprocess.call(["mpc", "toggle"]) # Toggle play/pause
    	print channel
    elif channel == NEXTTRACK_GPIO:
	subprocess.call(["mpc", "next"]) # Next track
	print channel
    elif channel == PREVTRACK_GPIO:
	subprocess.call(["mpc", "prev"]) # Previous track
    else:
	print("Button not known")

	
if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD) # Set to board GPIO number
    #Setup GPIOs - internal pull-up
    GPIO.setup(TOGGLE_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(NEXTTRACK_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PREVTRACK_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #Setup event detects. Bouncetime set to 700msec - seems to work ok
    GPIO.add_event_detect(TOGGLE_GPIO, GPIO.RISING, callback=button_pressed_callback, bouncetime=700)
    GPIO.add_event_detect(NEXTTRACK_GPIO, GPIO.RISING, callback=button_pressed_callback, bouncetime=700)
    GPIO.add_event_detect(PREVTRACK_GPIO, GPIO.RISING, callback=button_pressed_callback, bouncetime=700)
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()







