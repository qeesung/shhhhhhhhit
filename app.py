#! /usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
from distance import *
import time
from toilet_config import *


def initialize_pin(trigger_pin, echo_pin):
    """initialize the io pin"""
    print ">>> initializing the io pin: trigger pin->%s echo pin->%s..." % (trigger_pin, echo_pin)
    GPIO.setup(trigger_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(echo_pin, GPIO.IN)

def initialize_board(toilets):
    """initialize the board"""
    print ">>> initializing the borad..."
    GPIO.setmode(GPIO.BCM)
    for toilet in toilets:
        trigger_pin=toilet.get(KEY_TOILET_TRIGGER_PIN)
        echo_pin=toilet.get(KEY_TOILET_ECHO_PIN)
        toilet_name=toilet.get(KEY_TOILET_NAME)
        if trigger_pin and echo_pin:
            print ">>> initializing the toilet %s" % (toilet_name)
            initialize_pin(trigger_pin, echo_pin)
     
initialize_board(TOILETS)     


time.sleep(2)
try:
        while True:
                print 'Distance: %0.2f cm' %check_distance(2, 3)
                time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()
