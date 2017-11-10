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

def observe_toilets_status(toilets):
    """sample the toilets gate distance forever"""
    print ">>> observing all toilets status..."
    try:
        while True:
            for toilet in toilets:
                toilet_name=toilet.get(KEY_TOILET_NAME)
                print 'Toilet %s distance: %0.2f cm' % (toilet_name, sample_toilet_distance(toilet))
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

def sample_toilet_distance(toilet):
    """sample the toilet gate distance"""
    trigger_pin=toilet.get(KEY_TOILET_TRIGGER_PIN)
    echo_pin=toilet.get(KEY_TOILET_ECHO_PIN)
    return check_distance(trigger_pin, echo_pin)

initialize_board(TOILETS)     
observe_toilets_status(TOILETS)


time.sleep(2)
