#!/usr/bin/python
######################################################################
# This component receives missions from Rest and converts them into
# ros messages
######################################################################

import rospy
import sys
import unicodedata
import roslib
import rosparam
import random
import sys
import time
import threading

from sys import getsizeof
from std_msgs.msg import String
from cgi import parse_header, parse_multipart
from urlparse import parse_qs
from std_msgs.msg import String

from ms2_kth.msg import * 

import yaml



class Reader:

  def __init__(self):
    #si potrebbe mettere anonymous true se volessimo avere più nodi alla volta cheascoltano senza rischiare si picchino a vicenda    
		rospy.init_node('reader',anonymous=False,disable_signals=True) 
		self.counter = 0


  def callback(self, data):
		print("I received data")
		input= data.data
		#very unrobust check if itś controller or observer
		if (input[31]== 'c'):
			f=open("/home/co4robots/Desktop/received_components/controller.py", "w+")
			f.write(input)		
			print("file created in"+f.name)
			f.close()
		if (input[31]== 'o'):
			f=open("/home/co4robots/Desktop/received_components/observer.py", "w+")
			f.write(input)		
			print("file created in"+f.name)
			f.close()


  def run(self):
		print("listening")
		rospy.Subscriber("local_mission", String, self.callback) 
		rospy.spin()


def main():
	print "Running the PURSUE reader"
	reader=Reader()
	reader.run()
	if  __name__ == "__main__":
	  reader=Reader()
	  reader.run()
