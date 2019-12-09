#!/usr/bin/env python


import rospy
import actionlib
from std_msgs.msg import String
from time import sleep

class Transition_sender:

  def __init__(self):
    self.pub = rospy.Publisher('pursue/events', String, queue_size = 10)
    sleep(1)


  def send_message(self, transition):
    self.pub.publish(transition)




