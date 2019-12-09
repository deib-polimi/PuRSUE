#!/usr/bin/env python
######################################################################
# This component receives missions from Rest and converts them into
# ros messages
######################################################################

import rospy
import actionlib
from std_msgs.msg import String, Empty
from geometry_msgs.msg import PoseStamped
from time import sleep

class Move_command_sender:

  def __init__(self):
    self.pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size = 10)
    sleep(1)


  def send_message(self, coordinates):
    goal = PoseStamped()
    goal.header.frame_id = "map"
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = coordinates[0]
    goal.pose.position.y = coordinates[1]
    goal.pose.position.z = coordinates[2] #always
    goal.pose.orientation.x = coordinates[3]
    goal.pose.orientation.y = coordinates[4]
    goal.pose.orientation.z = coordinates[5]
    goal.pose.orientation.w = coordinates[6]
    self.pub.publish(goal)



