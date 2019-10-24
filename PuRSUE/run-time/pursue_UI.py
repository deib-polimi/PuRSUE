#!/usr/bin/env python
import sys
import random
import rospy
from std_msgs.msg import String
from time import sleep
from time import time
class Stater:
	def callback_ev(self, data):
		if (data.data == "_start_"):
			self.startTime = time()
		if (data.data != "_ping_"):
			print("\n\non topic events:" + data.data + " at time "+str(time()-self.startTime))

	def callback_act(self, data):
		print("\n\non topic actions:" + data.data+ " at time "+str(time()-self.startTime) )

	def callback_state(self, data):
		print("\n\non topic sysyem_state:" + data.data + " at time "+str(time()-self.startTime))	

	def __init__(self):
		rospy.init_node('stater')
		self.pub = rospy.Publisher("pursue/events", String, queue_size = 1)
		self.mod= raw_input("select mode: ('f' = all communication, 'e'= only events ): ")
		self.sim= raw_input("would you like to start the automatic enemy strace?(traceID/n): ")
		self.startTime = time()
		print("initializing done")
	def run(self):
		rospy.Subscriber("pursue/events", String, self.callback_ev)
		if (self.mod == "f"):
			rospy.Subscriber("pursue/actions", String, self.callback_act)
		if (self.mod == "f"):
			rospy.Subscriber("pursue/system_state", String, self.callback_state)
		events = ["_ping_",
			"callBot",
			"wait",
			 "waitDONE",
			 "isPlastic",	
			 "isPaper"
			]
		bin_mov =[ "bin_trashRoom2hallway",
				"bin_going_trashRoom_to_hallway2hallway",
				"bin_hallway2base",
				"bin_going_hallway_to_base2base"
			]
		while(not rospy.is_shutdown()):	
			#traccia EB1 -experimental	
			raw_input("press any key to start")
			self.pub.publish("_start_")
			sleep(0.5)
			while (self.sim == "a" and not rospy.is_shutdown() ):

				sleep(1.1)
				self.pub.publish(events[1])
				sleep(1.1)
				self.pub.publish(events[2])
				sleep(61.1)
				self.pub.publish(events[3])
			#traccia EB2
			while (self.sim == "b" and not rospy.is_shutdown() ):
				#raw_input("press any key to start")
				sleep(1.1)
				self.pub.publish(events[1])
				sleep(1.1)
				self.pub.publish(events[2])
				sleep(111.1)
				self.pub.publish(events[3])
			#traccia EB2 con movimenti cestino
			if (self.sim == "c" ):
				#raw_input("press any key to start")
				sleep(1.1)
				self.pub.publish(events[1])
				sleep(0.5)
				self.pub.publish(bin_mov[0]) #Cbin =0
				sleep(0.6)
				self.pub.publish(events[2]) #Chuman =0
				sleep(15.5)
				self.pub.publish(bin_mov[1]) #Cbin>16
				sleep (1.1)
				self.pub.publish(bin_mov[2]) #Cbin =0
				sleep (16.1)
				self.pub.publish(bin_mov[3]) #Cbin>16
				sleep(78.4)
				self.pub.publish(events[3])	#Chuman>111	
			#traccia EB3 
			if (self.sim == "d" ):	
				sleep(1.1)
				self.pub.publish(events[4])
				sleep(1.1)
				self.pub.publish(events[1])
				sleep(1.1)
				self.pub.publish(events[2])
				sleep(54.1)
				self.pub.publish(events[3])
				sleep(1.1)
				self.pub.publish(events[5])
				sleep(1.1)
				self.pub.publish(events[1])
				sleep(1.1)
				self.pub.publish(events[2])
				sleep(54.1)
				self.pub.publish(events[3])
			act_code = int(raw_input("select action: "))
			if (act_code < 0):
				i = 0
				while (i < len(events)):
					print("action #"+str(i)+" is "+events[i])
					i= i+1
			elif (act_code < len(events)):
				self.pub.publish(events[act_code])
			else:
				print("input incorrect")

		return 

		

def main():
	stater = Stater()
	stater.run()
if  __name__ == "__main__":
	stater = Stater()
	stater.run()
