#!/usr/bin/env python
######################################################################
# This component receives missions from Rest and converts them into
# ros messages
######################################################################

import rospy
import actionlib
from std_msgs.msg import String
from time import sleep

class Action_sender:

  def __init__(self):
    self.pub = rospy.Publisher('pursue/actions', String, queue_size = 10)
    sleep(1)


  def send_message(self, action):
    self.pub.publish(action)




