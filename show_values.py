#!/usr/env python

from pydimitri import *
from time import time
from math import pi

d = Dimitri()

t = time()
while (True):
    d.receiveCurrAngles()
    for joint in d.joints:
	if joint:
        	print str(joint.servo_id) + (':%3.0f' % (joint.currAngle*180/pi)), 
    print time() - t
    t = time()

