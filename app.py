#! /usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
from toilet_distance import *
from toilet_status import *
import time
from toilet_config import *
from toilet_logger import *
import datetime

STATUS_DOOR_CLOSED="CLOSED"
STATUS_DOOR_OPEN="OPEN"

toilet_status={}

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
                door_distance=round(sample_toilet_distance(toilet), 2)

                print 'Toilet %s distance: %0.2f cm' % (toilet_name, door_distance)
                if is_toilet_status_changed(toilet, door_distance):
                    status=get_door_status(door_distance)
                    update_toilet_status(toilet, status)
                    print 'Toilet %s status is changed: %s' % (toilet_name, status)
                    sync_toilet_status(toilet, is_door_open(status))
#                log_toilet_status_to_file(toilet, door_distance)
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

def sample_toilet_distance(toilet):
    """sample the toilet gate distance"""
    trigger_pin=toilet.get(KEY_TOILET_TRIGGER_PIN)
    echo_pin=toilet.get(KEY_TOILET_ECHO_PIN)
    return check_distance(trigger_pin, echo_pin)

def log_toilet_status_to_file(toilet, door_distance):
    """log the toilet status to the log file"""
    now = datetime.datetime.now()
    log_toilet_status({
        KEY_TOILET_ID: toilet.get(KEY_TOILET_ID),
        KEY_TOILET_NAME: toilet.get(KEY_TOILET_NAME),
        KEY_TOILET_TYPE: toilet.get(KEY_TOILET_TYPE),
        "disntance": door_distance,
        "sample_time": str(now)
    })
    

def is_toilet_status_changed(toilet, door_distance):
    """check if the toilet status changed"""
    current_door_status=get_door_status(door_distance)
    if not toilet_status.has_key(toilet.get(KEY_TOILET_ID)):
        update_toilet_status(toilet, current_door_status)
        return False
    old_status=toilet_status.get(toilet.get(KEY_TOILET_ID))
    if current_door_status == old_status:
        return False
    for i in xrange(1,2): # recheck the status 2 times
        temp_distance=round(sample_toilet_distance(toilet), 2)
        temp_status=get_door_status(temp_distance)
        if current_door_status != temp_status: # not stable change
            return False
    return True

def get_door_status(door_distance):
    DOOR_CLOSED_DISTANCE_LIMIT=8 # 8cm
    if door_distance < DOOR_CLOSED_DISTANCE_LIMIT:
        return STATUS_DOOR_CLOSED
    else:
        return STATUS_DOOR_OPEN

def is_door_closed(status):
    return status == STATUS_DOOR_CLOSEDgg

def is_door_open(status):
    return status == STATUS_DOOR_OPEN

def update_toilet_status(toilet, status):
    """"update the toilet status""" 
    toilet_id=toilet.get(KEY_TOILET_ID)
    toilet_status[toilet_id]=status

def get_toilet_status(toilet):
    """get the toilet status"""
    toilet_id=toilet.get(KEY_TOILET_ID)
    return toilet_status.get(toilet_id)

initialize_board(TOILETS)     
observe_toilets_status(TOILETS)


time.sleep(2)
