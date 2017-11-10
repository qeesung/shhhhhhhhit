#! /usr/bin/python
# -*- coding:utf-8 -*-

KEY_TOILET_ID="id"
KEY_TOILET_NAME="name"
KEY_TOILET_TRIGGER_PIN="trigger_pin"
KEY_TOILET_ECHO_PIN="echo_pin"
KEY_TOILET_TYPE="toilet_type"

TOILET1={
    KEY_TOILET_ID: 1,
    KEY_TOILET_NAME: "slot1",
    KEY_TOILET_TRIGGER_PIN: 2,
    KEY_TOILET_ECHO_PIN: 3,
    KEY_TOILET_TYPE: "坐的"
}

TOILET2={
    KEY_TOILET_ID: 2,
    KEY_TOILET_NAME: "slot1",
    KEY_TOILET_TRIGGER_PIN: 20,
    KEY_TOILET_ECHO_PIN: 21,
    KEY_TOILET_TYPE: "蹲的"
}

TOILETS=(TOILET1,)

if __name__ == "__main__":
    print "========== toilet list =========="
    for toilet in TOILETS:
        print "id: %s" % toilet[KEY_TOILET_ID]
        print "name: %s" % toilet[KEY_TOILET_NAME]
        print "trigger pin: %s" % toilet[KEY_TOILET_TRIGGER_PIN]
        print "echo pin: %s" % toilet[KEY_TOILET_ECHO_PIN]
        print "toilet type: %s" % toilet[KEY_TOILET_TYPE]
        print "----------------------------------------"
