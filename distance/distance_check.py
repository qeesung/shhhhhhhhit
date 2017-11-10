#! /usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time

# Get the distance
def check_distance(TRIG, ECHO):

        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(TRIG, GPIO.LOW)

        while not GPIO.input(ECHO):
                pass
        t1 = time.time()

        while GPIO.input(ECHO):
                pass
        t2 = time.time()

        return (t2-t1)*340/2*100
