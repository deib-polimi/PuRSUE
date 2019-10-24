#!/usr/bin/env python
#runtime_controller
import sys
import random
from pursue_library import *
import exeggutor
import rospy
from std_msgs.msg import String
from time import sleep
from threading import Event
class Runtime_controller:



	def if_start(self, event_string):
		if (event_string.data == "_start_"):
			self.startFlag = True
		return

	def update_state(self, state_string):
		if hasattr(state_string, 'data'):
			all_updates=state_string.data.split("\n\n")
		else:
			all_updates=state_string.split("\n\n")
		state_updates =all_updates[0].split("\n")
		for st in state_updates:
			state_and_value = st.split("=")
			if (state_and_value[0]=="PthrowingPlastic"):
				self.PthrowingPlastic=state_and_value[1]
			if (state_and_value[0]=="plasticBin"):
				self.plasticBin=state_and_value[1]
			if (state_and_value[0]=="makingTrash"):
				self.makingTrash=state_and_value[1]
			if (state_and_value[0]=="SpaperOrPlastic"):
				self.SpaperOrPlastic=state_and_value[1]
			if (state_and_value[0]=="PplasticBin"):
				self.PplasticBin=state_and_value[1]
			if (state_and_value[0]=="Phuman"):
				self.Phuman=state_and_value[1]
			if (state_and_value[0]=="PmakingTrash"):
				self.PmakingTrash=state_and_value[1]
			if (state_and_value[0]=="PpaperBin"):
				self.PpaperBin=state_and_value[1]
			if (state_and_value[0]=="states"):
				self.states=state_and_value[1]
			if (state_and_value[0]=="PecoBot"):
				self.PecoBot=state_and_value[1]
			if (state_and_value[0]=="PpickingUp"):
				self.PpickingUp=state_and_value[1]
			if (state_and_value[0]=="ecoBot"):
				self.ecoBot=state_and_value[1]
			if (state_and_value[0]=="obj"):
				self.obj=state_and_value[1]
			if (state_and_value[0]=="PthrowingPaper"):
				self.PthrowingPaper=state_and_value[1]
			if (state_and_value[0]=="paperBin"):
				self.paperBin=state_and_value[1]
			if (state_and_value[0]=="pickingUp"):
				self.pickingUp=state_and_value[1]
			if (state_and_value[0]=="throwingPaper"):
				self.throwingPaper=state_and_value[1]
			if (state_and_value[0]=="throwingPlastic"):
				self.throwingPlastic=state_and_value[1]
			if (state_and_value[0]=="human"):
				self.human=state_and_value[1]
		clock_updates =all_updates[1].split("\n")
		for cl in clock_updates:
			clock_and_value = cl.split("=")
			if (clock_and_value[0]=="Cobj"):
				self.Cobj=float(clock_and_value[1])
			if (clock_and_value[0]=="CecoBot"):
				self.CecoBot=float(clock_and_value[1])
			if (clock_and_value[0]=="Chuman"):
				self.Chuman=float(clock_and_value[1])
		self.event_flag.set()
		self.print_state()

	def __init__(self):
		rospy.init_node('pursue_controller_node')

		self.TIMEUNIT = 0.1
		self.startFlag= False
		self.event_flag = Event()
		self.event_flag.clear()
		self.exegg = exeggutor.Exeggutor(self.TIMEUNIT)
		self.Cobj= 0
		self.CecoBot= 0
		self.Chuman= 0
		self.PthrowingPlastic= ""
		self.plasticBin= ""
		self.makingTrash= ""
		self.SpaperOrPlastic= ""
		self.PplasticBin= ""
		self.Phuman= ""
		self.PmakingTrash= ""
		self.PpaperBin= ""
		self.states= ""
		self.PecoBot= ""
		self.PpickingUp= ""
		self.ecoBot= ""
		self.obj= ""
		self.PthrowingPaper= ""
		self.paperBin= ""
		self.pickingUp= ""
		self.throwingPaper= ""
		self.throwingPlastic= ""
		self.human= ""
		rospy.Subscriber("pursue/system_state", String, self.update_state)
		rospy.Subscriber("pursue/events", String, self.if_start)
		sleep(1)
		print("waiting for start signal")
		while (not self.startFlag):
			sleep(0.2)

	def print_state(self):
		print("the system state is:")
		print("PthrowingPlastic is ",self.PthrowingPlastic)
		print("plasticBin is ",self.plasticBin)
		print("makingTrash is ",self.makingTrash)
		print("SpaperOrPlastic is ",self.SpaperOrPlastic)
		print("PplasticBin is ",self.PplasticBin)
		print("Phuman is ",self.Phuman)
		print("PmakingTrash is ",self.PmakingTrash)
		print("PpaperBin is ",self.PpaperBin)
		print("states is ",self.states)
		print("PecoBot is ",self.PecoBot)
		print("PpickingUp is ",self.PpickingUp)
		print("ecoBot is ",self.ecoBot)
		print("obj is ",self.obj)
		print("PthrowingPaper is ",self.PthrowingPaper)
		print("paperBin is ",self.paperBin)
		print("pickingUp is ",self.pickingUp)
		print("throwingPaper is ",self.throwingPaper)
		print("throwingPlastic is ",self.throwingPlastic)
		print("human is ",self.human)
		print("Cobj is ",self.Cobj)
		print("CecoBot is ",self.CecoBot)
		print("Chuman is ",self.Chuman)

	def run(self):

		while(not rospy.is_shutdown()):

			sleep(self.TIMEUNIT)
			#state header
			if ( self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PthrowingPlastic== "3" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.states== "base" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PecoBot== "-44" and self.paperBin== "base" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PthrowingPlastic== "3" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.states== "base" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PecoBot== "-44" and self.paperBin== "base" and self.PpaperBin== "2"  ):
						if ( (1<self.Chuman and 3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "trashRoom" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp1f" and self.states== "base" and self.PecoBot== "4" and self.PplasticBin== "4" and self.paperBin== "base" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.Cobj-11 - self.TIMEUNIT ] , [-3- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-11 - self.TIMEUNIT ] , [self.Chuman-self.Cobj, 3-(self.Chuman-self.CecoBot) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "trashRoom" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp1f" and self.states== "base" and self.PecoBot== "4" and self.PplasticBin== "4" and self.paperBin== "base" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0" and self.PpaperBin== "2"  ):
						if ( (1<self.CecoBot and 1<self.Chuman and self.Cobj<11 and self.CecoBot- self.Cobj<-3 )  or  (1<self.CecoBot and self.Chuman<11 and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=3 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "0" and self.PecoBot== "4" and self.human== "doing_wait_in_office" and self.states== "base" and self.ecoBot== "trashRoom" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "1" and self.Phuman== "-11" and self.paperBin== "base" and self.plasticBin== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-37 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "0" and self.PecoBot== "4" and self.human== "doing_wait_in_office" and self.states== "base" and self.ecoBot== "trashRoom" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "1" and self.Phuman== "-11" and self.paperBin== "base" and self.plasticBin== "trashRoom"  ):
						if ( (1<self.CecoBot and self.Chuman<37 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "going_hallway_to_trashRoom" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.states== "base" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s" and self.PecoBot== "-34" and self.SpaperOrPlastic== "0" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "idle" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.Phuman== "1" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "going_hallway_to_trashRoom" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.states== "base" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s" and self.PecoBot== "-34" and self.SpaperOrPlastic== "0" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "idle" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.Phuman== "1" and self.PthrowingPaper== "0"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "going_hallway_to_trashRoom" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PmakingTrash== "3" and self.pickingUp== "pickingUp_initial_location" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.states== "base" and self.PpickingUp== "0" and self.PecoBot== "-34" and self.obj== "idle" and self.Phuman== "-11" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "going_hallway_to_trashRoom" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PmakingTrash== "3" and self.pickingUp== "pickingUp_initial_location" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.states== "base" and self.PpickingUp== "0" and self.PecoBot== "-34" and self.obj== "idle" and self.Phuman== "-11" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.PpaperBin== "2"  ):
						if ( (12<self.CecoBot and self.Chuman<=55 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.states== "base" and self.PmakingTrash== "3" and self.Phuman== "-11" and self.SpaperOrPlastic== "1" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-31" and self.ecoBot== "going_hallway_to_office" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Chuman-39 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.states== "base" and self.PmakingTrash== "3" and self.Phuman== "-11" and self.SpaperOrPlastic== "1" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-31" and self.ecoBot== "going_hallway_to_office" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman<39 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.human== "office" and self.PplasticBin== "4" and self.obj== "atRisk" and self.PmakingTrash== "2" and self.ecoBot== "going_hallway_to_trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.paperBin== "base" and self.PpaperBin== "2" and self.PecoBot== "-34" and self.Phuman== "1" and self.pickingUp== "pickingUp1f" and self.SpaperOrPlastic== "1" and self.states== "base" and self.PpickingUp== "1"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-6 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.human== "office" and self.PplasticBin== "4" and self.obj== "atRisk" and self.PmakingTrash== "2" and self.ecoBot== "going_hallway_to_trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.paperBin== "base" and self.PpaperBin== "2" and self.PecoBot== "-34" and self.Phuman== "1" and self.pickingUp== "pickingUp1f" and self.SpaperOrPlastic== "1" and self.states== "base" and self.PpickingUp== "1"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<6 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.PecoBot== "1" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "office" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.states== "base" and self.PpaperBin== "2" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-40 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.PecoBot== "1" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "office" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.states== "base" and self.PpaperBin== "2" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (1<self.CecoBot and self.Chuman<40 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "1" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.paperBin== "base" and self.PpaperBin== "2" and self.PthrowingPlastic== "3" and self.pickingUp== "pickingUp1f" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-44" and self.PthrowingPaper== "0" and self.states== "base" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.obj== "atRisk" and self.PmakingTrash== "2" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-10 - self.TIMEUNIT, self.CecoBot-4 ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "1" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.paperBin== "base" and self.PpaperBin== "2" and self.PthrowingPlastic== "3" and self.pickingUp== "pickingUp1f" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-44" and self.PthrowingPaper== "0" and self.states== "base" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.obj== "atRisk" and self.PmakingTrash== "2" and self.human== "office"  ):
						if ( (3<self.CecoBot and self.Chuman<10 and self.CecoBot<=4 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PecoBot== "1" and self.obj== "atRisk" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.pickingUp== "pickingUp0" and self.PplasticBin== "4" and self.states== "base" and self.PpaperBin== "2" and self.PpickingUp== "4" and self.PthrowingPaper== "0" and self.ecoBot== "office" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-40 ] , [-5- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PecoBot== "1" and self.obj== "atRisk" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.pickingUp== "pickingUp0" and self.PplasticBin== "4" and self.states== "base" and self.PpaperBin== "2" and self.PpickingUp== "4" and self.PthrowingPaper== "0" and self.ecoBot== "office" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait"  ):
						if ( (1<self.CecoBot and self.Cobj<=40 and self.CecoBot- self.Cobj<-5 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "officeClean!", "office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "3" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper0f_doing_paperTrash" and self.plasticBin== "trashRoom" and self.human== "office" and self.ecoBot== "doing_paperTrash_in_office" and self.paperBin== "base" and self.PplasticBin== "4" and self.pickingUp== "pickingUp2fs_sec_doing_paperTrash" and self.SpaperOrPlastic== "1" and self.PthrowingPaper== "1" and self.Phuman== "1" and self.PecoBot== "-11" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.obj== "atRisk"   ):
				temps=set()
				temp0= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-39 - self.TIMEUNIT, self.CecoBot-6 ] , [-10- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-6 ] , [10-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj, self.Chuman-self.CecoBot ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "3" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper0f_doing_paperTrash" and self.plasticBin== "trashRoom" and self.human== "office" and self.ecoBot== "doing_paperTrash_in_office" and self.paperBin== "base" and self.PplasticBin== "4" and self.pickingUp== "pickingUp2fs_sec_doing_paperTrash" and self.SpaperOrPlastic== "1" and self.PthrowingPaper== "1" and self.Phuman== "1" and self.PecoBot== "-11" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.obj== "atRisk"  ):
						if ( (5<self.CecoBot and self.Cobj<39 and self.CecoBot<=6 and self.CecoBot- self.Cobj<-10 and self.CecoBot- self.Chuman<-1 )  or  (5<self.CecoBot and self.CecoBot<=6 and self.Chuman- self.CecoBot<=10 and self.Chuman==self.Cobj and self.CecoBot<=self.Chuman )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "paperTrashDONE!", "doing_paperTrash_in_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "1" and self.states== "base" and self.PecoBot== "-43" and self.PthrowingPaper== "0" and self.ecoBot== "going_trashRoom_to_hallway" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "atRisk" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.pickingUp== "pickingUp1f" and self.paperBin== "base" and self.Phuman== "1" and self.PthrowingPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [4-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Cobj-23 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman), -4- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "1" and self.states== "base" and self.PecoBot== "-43" and self.PthrowingPaper== "0" and self.ecoBot== "going_trashRoom_to_hallway" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "atRisk" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.pickingUp== "pickingUp1f" and self.paperBin== "base" and self.Phuman== "1" and self.PthrowingPlastic== "0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman- self.CecoBot<=4 and self.Chuman==self.Cobj )  or  (12<self.CecoBot and self.CecoBot<=13 and self.Cobj<23 and self.CecoBot- self.Chuman<-1 and self.CecoBot- self.Cobj<-4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "-13" and self.PmakingTrash== "3" and self.PpickingUp== "4" and self.pickingUp== "pickingUp0" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.obj== "atRisk" and self.ecoBot== "going_office_to_hallway" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.human== "doing_wait_in_office" and self.states== "base" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Cobj-29 - self.TIMEUNIT ] , [-6- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "-13" and self.PmakingTrash== "3" and self.PpickingUp== "4" and self.pickingUp== "pickingUp0" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.obj== "atRisk" and self.ecoBot== "going_office_to_hallway" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.human== "doing_wait_in_office" and self.states== "base" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Cobj<29 and self.CecoBot- self.Cobj<-6 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.PmakingTrash== "3" and self.obj== "atRisk" and self.PplasticBin== "4" and self.Phuman== "-11" and self.PpickingUp== "1" and self.PecoBot== "-34" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.ecoBot== "going_hallway_to_trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp1f" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Cobj-6 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.PmakingTrash== "3" and self.obj== "atRisk" and self.PplasticBin== "4" and self.Phuman== "-11" and self.PpickingUp== "1" and self.PecoBot== "-34" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.ecoBot== "going_hallway_to_trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp1f" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Cobj<6 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "3" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.human== "office" and self.PecoBot== "-22" and self.obj== "idle" and self.ecoBot== "doing_throwPaper_in_base" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.PpickingUp== "0" and self.states== "base" and self.PplasticBin== "4" and self.makingTrash== "makingTrash_initial_location" and self.paperBin== "base" and self.PmakingTrash== "0" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "3" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.human== "office" and self.PecoBot== "-22" and self.obj== "idle" and self.ecoBot== "doing_throwPaper_in_base" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.PpickingUp== "0" and self.states== "base" and self.PplasticBin== "4" and self.makingTrash== "makingTrash_initial_location" and self.paperBin== "base" and self.PmakingTrash== "0" and self.PpaperBin== "2"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "base" and self.human== "doing_wait_in_office" and self.PthrowingPaper== "2" and self.PecoBot== "2" and self.states== "base" and self.Phuman== "-11" and self.PplasticBin== "4" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.obj== "atRisk" and self.pickingUp== "pickingUp1f" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.PpickingUp== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-7 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "base" and self.human== "doing_wait_in_office" and self.PthrowingPaper== "2" and self.PecoBot== "2" and self.states== "base" and self.Phuman== "-11" and self.PplasticBin== "4" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.obj== "atRisk" and self.pickingUp== "pickingUp1f" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.PpickingUp== "1"  ):
						if ( (1<self.CecoBot and self.Cobj<7 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.PpaperBin== "2" and self.ecoBot== "going_base_to_hallway" and self.Phuman== "1" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash_initial_location" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "0" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-23" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.PpaperBin== "2" and self.ecoBot== "going_base_to_hallway" and self.Phuman== "1" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash_initial_location" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "0" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-23" and self.PpickingUp== "0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "atRisk" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "4" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.ecoBot== "going_hallway_to_office" and self.PecoBot== "-31" and self.paperBin== "base" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-39 - self.TIMEUNIT, self.CecoBot-10 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj), -16- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "atRisk" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "4" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.ecoBot== "going_hallway_to_office" and self.PecoBot== "-31" and self.paperBin== "base" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp0"  ):
						if ( (9<self.CecoBot and self.Cobj<39 and self.CecoBot<=10 and self.Chuman- self.Cobj<-1 and self.CecoBot- self.Cobj<-16 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "2" and self.states== "base" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.obj== "idle" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.PpickingUp== "0" and self.PecoBot== "-23" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_base_to_hallway" and self.human== "office" and self.PplasticBin== "4" and self.PmakingTrash== "2"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "2" and self.states== "base" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.obj== "idle" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.PpickingUp== "0" and self.PecoBot== "-23" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_base_to_hallway" and self.human== "office" and self.PplasticBin== "4" and self.PmakingTrash== "2"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp1f" and self.states== "base" and self.paperBin== "base" and self.obj== "atRisk" and self.PplasticBin== "4" and self.PecoBot== "1" and self.ecoBot== "office" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.PmakingTrash== "3" and self.Phuman== "-11" and self.PpickingUp== "1" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-34 - self.TIMEUNIT, self.Chuman-3 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp1f" and self.states== "base" and self.paperBin== "base" and self.obj== "atRisk" and self.PplasticBin== "4" and self.PecoBot== "1" and self.ecoBot== "office" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.PmakingTrash== "3" and self.Phuman== "-11" and self.PpickingUp== "1" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (1<self.CecoBot and self.Cobj<34 and self.Chuman<3 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "paperTrash!", "office", "doing_paperTrash_in_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.plasticBin== "trashRoom" and self.human== "office" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_base" and self.PthrowingPlastic== "2" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PecoBot== "-32" and self.states== "base" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.plasticBin== "trashRoom" and self.human== "office" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_base" and self.PthrowingPlastic== "2" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PecoBot== "-32" and self.states== "base" and self.PplasticBin== "4"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "0" and self.ecoBot== "going_hallway_to_base" and self.obj== "idle" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.states== "base" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PecoBot== "-32" and self.PpaperBin== "2" and self.Phuman== "-11"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-32 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "0" and self.ecoBot== "going_hallway_to_base" and self.obj== "idle" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.states== "base" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PecoBot== "-32" and self.PpaperBin== "2" and self.Phuman== "-11"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<32 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "-11" and self.SpaperOrPlastic== "1" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "3" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "going_trashRoom_to_hallway" and self.paperBin== "base" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.human== "doing_wait_in_office" and self.PecoBot== "-43" and self.plasticBin== "trashRoom" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "-11" and self.SpaperOrPlastic== "1" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "3" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "going_trashRoom_to_hallway" and self.paperBin== "base" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.human== "doing_wait_in_office" and self.PecoBot== "-43" and self.plasticBin== "trashRoom" and self.obj== "idle"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "4" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "2" and self.obj== "idle" and self.PpickingUp== "0" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.ecoBot== "trashRoom" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.states== "base" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "4" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "2" and self.obj== "idle" and self.PpickingUp== "0" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.ecoBot== "trashRoom" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.states== "base" and self.PpaperBin== "2"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "0" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "base" and self.PpaperBin== "2" and self.Phuman== "1" and self.PecoBot== "2" and self.PpickingUp== "0" and self.human== "office" and self.makingTrash== "makingTrash_initial_location" and self.PthrowingPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "0" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "base" and self.PpaperBin== "2" and self.Phuman== "1" and self.PecoBot== "2" and self.PpickingUp== "0" and self.human== "office" and self.makingTrash== "makingTrash_initial_location" and self.PthrowingPlastic== "0"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "1" and self.PpickingUp== "0" and self.makingTrash== "makingTrash0" and self.PecoBot== "-34" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.human== "office" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_trashRoom" and self.PthrowingPlastic== "2" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "1" and self.PpickingUp== "0" and self.makingTrash== "makingTrash0" and self.PecoBot== "-34" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.human== "office" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_trashRoom" and self.PthrowingPlastic== "2" and self.obj== "idle"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "1" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_base_to_hallway" and self.pickingUp== "pickingUp1f" and self.obj== "atRisk" and self.PecoBot== "-23" and self.PpaperBin== "2" and self.Phuman== "1" and self.PmakingTrash== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.paperBin== "base" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-23 - self.TIMEUNIT, self.CecoBot-13 ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman), -4- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [4-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "1" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_base_to_hallway" and self.pickingUp== "pickingUp1f" and self.obj== "atRisk" and self.PecoBot== "-23" and self.PpaperBin== "2" and self.Phuman== "1" and self.PmakingTrash== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.paperBin== "base" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0"  ):
						if ( (12<self.CecoBot and self.Cobj<23 and self.CecoBot<=13 and self.CecoBot- self.Chuman<-1 and self.CecoBot- self.Cobj<-4 )  or  (12<self.CecoBot and self.CecoBot<=13 and self.Chuman- self.CecoBot<=4 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PecoBot== "-44" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "3" and self.PthrowingPaper== "2" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PecoBot== "-44" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "3" and self.PthrowingPaper== "2" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.human== "office"  ):
						if ( (3<self.CecoBot and 1<self.Chuman and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.ecoBot== "going_hallway_to_trashRoom" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.states== "base" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-34" and self.PmakingTrash== "2" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp1f" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "1" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.obj== "atRisk"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-10 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.ecoBot== "going_hallway_to_trashRoom" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.states== "base" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-34" and self.PmakingTrash== "2" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp1f" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "1" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.obj== "atRisk"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<10 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "1" and self.ecoBot== "base" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.obj== "idle" and self.PplasticBin== "4" and self.paperBin== "base" and self.PecoBot== "2" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "1" and self.ecoBot== "base" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.obj== "idle" and self.PplasticBin== "4" and self.paperBin== "base" and self.PecoBot== "2" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "2"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.obj== "idle" and self.Phuman== "-11" and self.ecoBot== "hallway" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.PecoBot== "3" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 30 + self.TIMEUNIT-self.Chuman, 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-50 ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 24 + self.TIMEUNIT-self.Chuman ] , [ self.Chuman-50 ] , [9-(self.Chuman-self.CecoBot) ])
				if (temp1 >= 0):
					temps.add(temp1)
				temp2= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-30 - self.TIMEUNIT ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp2 >= 0):
					temps.add(temp2)
				temp3= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-24 - self.TIMEUNIT ] , [9-(self.Chuman-self.CecoBot) ])
				if (temp3 >= 0):
					temps.add(temp3)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.obj== "idle" and self.Phuman== "-11" and self.ecoBot== "hallway" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.PecoBot== "3" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "0"  ):
						if ( (30<=self.Chuman and 1<self.CecoBot and self.Chuman<=50 and self.CecoBot- self.Chuman<-9 )  or  (24<=self.Chuman and self.Chuman<=50 and self.Chuman- self.CecoBot<=9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2base!", "hallway", "going_hallway_to_base")
						if ( (1<self.CecoBot and self.Chuman<30 and self.CecoBot- self.Chuman<-9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
						if ( (1<self.CecoBot and self.Chuman<24 and self.Chuman- self.CecoBot<=9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic0" and self.human== "office" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "0" and self.PpickingUp== "4" and self.Phuman== "1" and self.pickingUp== "pickingUp0" and self.obj== "atRisk" and self.PecoBot== "1" and self.PpaperBin== "2" and self.states== "base" and self.ecoBot== "office" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.paperBin== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.Cobj-40 ] , [-5- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic0" and self.human== "office" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "0" and self.PpickingUp== "4" and self.Phuman== "1" and self.pickingUp== "pickingUp0" and self.obj== "atRisk" and self.PecoBot== "1" and self.PpaperBin== "2" and self.states== "base" and self.ecoBot== "office" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.paperBin== "base"  ):
						if ( (1<self.CecoBot and 1<self.Chuman and self.Cobj<=40 and self.CecoBot- self.Cobj<-5 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "officeClean!", "office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PecoBot== "-43" and self.PmakingTrash== "2" and self.Phuman== "1" and self.states== "base" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.ecoBot== "going_trashRoom_to_hallway" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PecoBot== "-43" and self.PmakingTrash== "2" and self.Phuman== "1" and self.states== "base" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.ecoBot== "going_trashRoom_to_hallway" and self.human== "office"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.states== "base" and self.human== "doing_wait_in_office" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "atRisk" and self.Phuman== "-11" and self.pickingUp== "pickingUp1f" and self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-31" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Cobj-33 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.states== "base" and self.human== "doing_wait_in_office" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "atRisk" and self.Phuman== "-11" and self.pickingUp== "pickingUp1f" and self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-31" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Cobj<33 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PpickingUp== "4" and self.plasticBin== "trashRoom" and self.PecoBot== "1" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.ecoBot== "office" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp0" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "1" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-40 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj), -5- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PpickingUp== "4" and self.plasticBin== "trashRoom" and self.PecoBot== "1" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.ecoBot== "office" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp0" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "1" and self.states== "base"  ):
						if ( (1<self.CecoBot and self.Cobj<=40 and self.Chuman- self.Cobj<-1 and self.CecoBot- self.Cobj<-5 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "officeClean!", "office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.paperBin== "base" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-32" and self.SpaperOrPlastic== "0" and self.ecoBot== "going_hallway_to_base" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.paperBin== "base" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-32" and self.SpaperOrPlastic== "0" and self.ecoBot== "going_hallway_to_base" and self.PthrowingPaper== "0"  ):
						if ( (12<self.CecoBot and self.Chuman<=55 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.states== "base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.ecoBot== "trashRoom" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "4" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.PplasticBin== "4" and self.human== "office" and self.PmakingTrash== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.states== "base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.ecoBot== "trashRoom" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "4" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.PplasticBin== "4" and self.human== "office" and self.PmakingTrash== "2"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.PecoBot== "-23" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.obj== "atRisk" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.ecoBot== "going_base_to_hallway" and self.PpickingUp== "1" and self.pickingUp== "pickingUp1f" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.human== "doing_wait_in_office"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-23 - self.TIMEUNIT, self.CecoBot-13 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.PecoBot== "-23" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.obj== "atRisk" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.ecoBot== "going_base_to_hallway" and self.PpickingUp== "1" and self.pickingUp== "pickingUp1f" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.human== "doing_wait_in_office"  ):
						if ( (12<self.CecoBot and self.Cobj<23 and self.CecoBot<=13 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "0" and self.states== "base" and self.SpaperOrPlastic== "0" and self.human== "office" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.PecoBot== "1" and self.Phuman== "1" and self.paperBin== "base" and self.ecoBot== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.obj== "atRisk" and self.PpickingUp== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.Cobj-34 - self.TIMEUNIT ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-34 - self.TIMEUNIT ] , [self.Chuman-self.Cobj, 9-(self.Chuman-self.CecoBot) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "0" and self.states== "base" and self.SpaperOrPlastic== "0" and self.human== "office" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.PecoBot== "1" and self.Phuman== "1" and self.paperBin== "base" and self.ecoBot== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.obj== "atRisk" and self.PpickingUp== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "2"  ):
						if ( (1<self.CecoBot and 1<self.Chuman and self.Cobj<34 and self.CecoBot- self.Cobj<-9 )  or  (1<self.CecoBot and self.Chuman<34 and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "plasticTrash!", "office", "doing_plasticTrash_in_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.states== "base" and self.SpaperOrPlastic== "1" and self.obj== "atRisk" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.pickingUp== "pickingUp0" and self.PplasticBin== "4" and self.ecoBot== "office" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "4" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.PecoBot== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-9 - self.TIMEUNIT, self.Cobj-40 ] , [-5- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.states== "base" and self.SpaperOrPlastic== "1" and self.obj== "atRisk" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.pickingUp== "pickingUp0" and self.PplasticBin== "4" and self.ecoBot== "office" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "4" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.PecoBot== "1"  ):
						if ( (1<self.CecoBot and self.Chuman<9 and self.Cobj<=40 and self.CecoBot- self.Cobj<-5 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "officeClean!", "office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_trashRoom" and self.human== "office" and self.SpaperOrPlastic== "1" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.PecoBot== "-34" and self.states== "base" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_trashRoom" and self.human== "office" and self.SpaperOrPlastic== "1" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.PecoBot== "-34" and self.states== "base" and self.Phuman== "1"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.ecoBot== "going_hallway_to_trashRoom" and self.PthrowingPlastic== "0" and self.human== "office" and self.PplasticBin== "4" and self.PecoBot== "-34" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.ecoBot== "going_hallway_to_trashRoom" and self.PthrowingPlastic== "0" and self.human== "office" and self.PplasticBin== "4" and self.PecoBot== "-34" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp0" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.PmakingTrash== "2" and self.PecoBot== "-13" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "4" and self.states== "base" and self.ecoBot== "going_office_to_hallway" and self.obj== "atRisk"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-29 - self.TIMEUNIT, self.CecoBot-10 ] , [-6- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp0" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.PmakingTrash== "2" and self.PecoBot== "-13" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "4" and self.states== "base" and self.ecoBot== "going_office_to_hallway" and self.obj== "atRisk"  ):
						if ( (9<self.CecoBot and self.Cobj<29 and self.CecoBot<=10 and self.CecoBot- self.Cobj<-6 and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11" and self.PecoBot== "-23" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.ecoBot== "going_base_to_hallway" and self.obj== "idle" and self.PmakingTrash== "3" and self.PthrowingPlastic== "0" and self.human== "doing_wait_in_office" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.paperBin== "base"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-49 - self.TIMEUNIT, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11" and self.PecoBot== "-23" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.ecoBot== "going_base_to_hallway" and self.obj== "idle" and self.PmakingTrash== "3" and self.PthrowingPlastic== "0" and self.human== "doing_wait_in_office" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.paperBin== "base"  ):
						if ( (12<self.CecoBot and self.Chuman<49 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.states== "base" and self.SpaperOrPlastic== "1" and self.obj== "idle" and self.makingTrash== "makingTrash_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "0" and self.plasticBin== "trashRoom" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.ecoBot== "hallway" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.paperBin== "base" and self.PecoBot== "3"   ):
				temps=set()
				temp0= optimal_wait([ 0 + self.TIMEUNIT-self.Chuman, 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.states== "base" and self.SpaperOrPlastic== "1" and self.obj== "idle" and self.makingTrash== "makingTrash_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "0" and self.plasticBin== "trashRoom" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.ecoBot== "hallway" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.paperBin== "base" and self.PecoBot== "3"  ):
						if ( (0<self.Chuman and 1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.human== "office" and self.states== "base" and self.Phuman== "1" and self.pickingUp== "pickingUp1f" and self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_office" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.PthrowingPlastic== "0" and self.PecoBot== "-31" and self.paperBin== "base"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [self.Chuman-self.Cobj, 10-(self.Chuman-self.CecoBot) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Cobj-33 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman), -10- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.human== "office" and self.states== "base" and self.Phuman== "1" and self.pickingUp== "pickingUp1f" and self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_office" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.PthrowingPlastic== "0" and self.PecoBot== "-31" and self.paperBin== "base"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=10 )  or  (9<self.CecoBot and self.CecoBot<=10 and self.Cobj<33 and self.CecoBot- self.Chuman<-1 and self.CecoBot- self.Cobj<-10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "2" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.PecoBot== "2" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.states== "base" and self.ecoBot== "base" and self.PmakingTrash== "2" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.human== "office" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "2" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.PecoBot== "2" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.states== "base" and self.ecoBot== "base" and self.PmakingTrash== "2" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.human== "office" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.ecoBot== "doing_throwPaper_in_base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp_initial_location" and self.obj== "idle" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "3" and self.states== "base" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PecoBot== "-22" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.ecoBot== "doing_throwPaper_in_base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp_initial_location" and self.obj== "idle" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "3" and self.states== "base" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PecoBot== "-22" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.human== "office" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.obj== "idle" and self.Phuman== "1" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.states== "base" and self.PmakingTrash== "1" and self.PecoBot== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.human== "office" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.obj== "idle" and self.Phuman== "1" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.states== "base" and self.PmakingTrash== "1" and self.PecoBot== "4"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "idle" and self.SpaperOrPlastic== "1" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.PecoBot== "-32" and self.PpickingUp== "0" and self.makingTrash== "makingTrash_initial_location" and self.ecoBot== "going_hallway_to_base" and self.paperBin== "base" and self.states== "base" and self.plasticBin== "trashRoom" and self.PmakingTrash== "0" and self.Phuman== "1" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "idle" and self.SpaperOrPlastic== "1" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.PecoBot== "-32" and self.PpickingUp== "0" and self.makingTrash== "makingTrash_initial_location" and self.ecoBot== "going_hallway_to_base" and self.paperBin== "base" and self.states== "base" and self.plasticBin== "trashRoom" and self.PmakingTrash== "0" and self.Phuman== "1" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "office" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.paperBin== "base" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.human== "office" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "1" and self.obj== "idle" and self.PmakingTrash== "2" and self.states== "base" and self.throwingPaper== "throwingPaper0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "office" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.paperBin== "base" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.human== "office" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "1" and self.obj== "idle" and self.PmakingTrash== "2" and self.states== "base" and self.throwingPaper== "throwingPaper0"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "atRisk" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.PecoBot== "-43" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "going_trashRoom_to_hallway" and self.pickingUp== "pickingUp1f" and self.human== "office" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.states== "base" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [self.Chuman-self.Cobj, 4-(self.Chuman-self.CecoBot) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-23 - self.TIMEUNIT, self.CecoBot-13 ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman), -4- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "atRisk" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.PecoBot== "-43" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "going_trashRoom_to_hallway" and self.pickingUp== "pickingUp1f" and self.human== "office" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.states== "base" and self.SpaperOrPlastic== "1"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=4 )  or  (12<self.CecoBot and self.Cobj<23 and self.CecoBot<=13 and self.CecoBot- self.Chuman<-1 and self.CecoBot- self.Cobj<-4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.SpaperOrPlastic== "0" and self.ecoBot== "going_hallway_to_office" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "1" and self.Phuman== "-11" and self.pickingUp== "pickingUp1f" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PecoBot== "-31" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.states== "base" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-33 - self.TIMEUNIT, self.Chuman-2 - self.TIMEUNIT, self.CecoBot-10 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.SpaperOrPlastic== "0" and self.ecoBot== "going_hallway_to_office" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "1" and self.Phuman== "-11" and self.pickingUp== "pickingUp1f" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PecoBot== "-31" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.states== "base" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0"  ):
						if ( (9<self.CecoBot and self.Cobj<33 and self.Chuman<2 and self.CecoBot<=10 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "-34" and self.Phuman== "-11" and self.PpaperBin== "2" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PmakingTrash== "3" and self.obj== "idle" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "going_hallway_to_trashRoom" and self.PthrowingPaper== "0" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "-34" and self.Phuman== "-11" and self.PpaperBin== "2" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PmakingTrash== "3" and self.obj== "idle" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "going_hallway_to_trashRoom" and self.PthrowingPaper== "0" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash_initial_location" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.human== "office" and self.obj== "idle" and self.ecoBot== "trashRoom" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.states== "base" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "0" and self.PecoBot== "4" and self.paperBin== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash_initial_location" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.human== "office" and self.obj== "idle" and self.ecoBot== "trashRoom" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.states== "base" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "0" and self.PecoBot== "4" and self.paperBin== "base"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-32" and self.human== "doing_wait_in_office" and self.PpickingUp== "1" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.obj== "atRisk" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "going_hallway_to_base" and self.PplasticBin== "4" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.states== "base" and self.PmakingTrash== "3"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Cobj-10 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-32" and self.human== "doing_wait_in_office" and self.PpickingUp== "1" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.obj== "atRisk" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "going_hallway_to_base" and self.PplasticBin== "4" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.states== "base" and self.PmakingTrash== "3"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Cobj<10 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.PecoBot== "4" and self.obj== "atRisk" and self.SpaperOrPlastic== "0" and self.ecoBot== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.PplasticBin== "4" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.pickingUp== "pickingUp1f" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.states== "base" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-7 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.PecoBot== "4" and self.obj== "atRisk" and self.SpaperOrPlastic== "0" and self.ecoBot== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.PplasticBin== "4" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.pickingUp== "pickingUp1f" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.states== "base" and self.PpaperBin== "2"  ):
						if ( (1<self.CecoBot and self.Cobj<7 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.states== "base" and self.PecoBot== "4" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.PthrowingPaper== "0" and self.Phuman== "-11" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.human== "doing_wait_in_office" and self.PthrowingPlastic== "2" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.states== "base" and self.PecoBot== "4" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.PthrowingPaper== "0" and self.Phuman== "-11" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.human== "doing_wait_in_office" and self.PthrowingPlastic== "2" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "trashRoom"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PecoBot== "4" and self.Phuman== "-11" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-37 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PecoBot== "4" and self.Phuman== "-11" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0"  ):
						if ( (1<self.CecoBot and self.Chuman<37 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.ecoBot== "going_hallway_to_base" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "2" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.PecoBot== "-32" and self.human== "office" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.PpaperBin== "2" and self.obj== "idle" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.ecoBot== "going_hallway_to_base" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "2" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.PecoBot== "-32" and self.human== "office" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.PpaperBin== "2" and self.obj== "idle" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "2" and self.plasticBin== "trashRoom" and self.states== "base" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper0" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.ecoBot== "office" and self.Phuman== "1" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp0" and self.SpaperOrPlastic== "1" and self.human== "office" and self.PecoBot== "1" and self.PpickingUp== "4" and self.makingTrash== "makingTrash1s"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-40 ] , [-5- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "2" and self.plasticBin== "trashRoom" and self.states== "base" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper0" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.ecoBot== "office" and self.Phuman== "1" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp0" and self.SpaperOrPlastic== "1" and self.human== "office" and self.PecoBot== "1" and self.PpickingUp== "4" and self.makingTrash== "makingTrash1s"  ):
						if ( (1<self.Chuman and 1<self.CecoBot and self.Cobj<=40 and self.CecoBot- self.Cobj<-5 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "officeClean!", "office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.ecoBot== "doing_throwPaper_in_base" and self.Phuman== "-11" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.obj== "atRisk" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.PpickingUp== "1" and self.PthrowingPaper== "3" and self.PecoBot== "-22" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "3" and self.pickingUp== "pickingUp1f"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4, self.Cobj-10 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.ecoBot== "doing_throwPaper_in_base" and self.Phuman== "-11" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.obj== "atRisk" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.PpickingUp== "1" and self.PthrowingPaper== "3" and self.PecoBot== "-22" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "3" and self.pickingUp== "pickingUp1f"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 and self.Cobj<10 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.ecoBot== "going_base_to_hallway" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.PecoBot== "-23" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.human== "office" and self.PpickingUp== "0" and self.obj== "idle" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.ecoBot== "going_base_to_hallway" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.PecoBot== "-23" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.human== "office" and self.PpickingUp== "0" and self.obj== "idle" and self.PpaperBin== "2"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "2" and self.PecoBot== "1" and self.Phuman== "-11" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.ecoBot== "office" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-10 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "2" and self.PecoBot== "1" and self.Phuman== "-11" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.ecoBot== "office" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (1<self.CecoBot and self.Chuman<10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.ecoBot== "going_hallway_to_base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "-11" and self.PecoBot== "-32" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.ecoBot== "going_hallway_to_base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "-11" and self.PecoBot== "-32" and self.PpaperBin== "2"  ):
						if ( (12<self.CecoBot and self.Chuman<=55 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-31" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "-11" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.ecoBot== "going_hallway_to_office" and self.PthrowingPlastic== "0" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-31" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "-11" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.ecoBot== "going_hallway_to_office" and self.PthrowingPlastic== "0" and self.obj== "idle"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.human== "doing_wait_in_office" and self.ecoBot== "trashRoom" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "3" and self.paperBin== "base" and self.PpickingUp== "1" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp1f" and self.PecoBot== "4" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "atRisk" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.plasticBin== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-7 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.human== "doing_wait_in_office" and self.ecoBot== "trashRoom" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "3" and self.paperBin== "base" and self.PpickingUp== "1" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp1f" and self.PecoBot== "4" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "atRisk" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.plasticBin== "trashRoom"  ):
						if ( (1<self.CecoBot and self.Cobj<7 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.human== "office" and self.PplasticBin== "4" and self.obj== "idle" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.PpickingUp== "0" and self.ecoBot== "office" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "1" and self.PmakingTrash== "2" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.PthrowingPlastic== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.human== "office" and self.PplasticBin== "4" and self.obj== "idle" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.PpickingUp== "0" and self.ecoBot== "office" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "1" and self.PmakingTrash== "2" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.PthrowingPlastic== "2"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "0" and self.states== "base" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.makingTrash== "makingTrash_initial_location" and self.PplasticBin== "4" and self.PecoBot== "-31" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_office" and self.human== "office" and self.obj== "idle" and self.PmakingTrash== "0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "0" and self.states== "base" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.makingTrash== "makingTrash_initial_location" and self.PplasticBin== "4" and self.PecoBot== "-31" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_office" and self.human== "office" and self.obj== "idle" and self.PmakingTrash== "0"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.SpaperOrPlastic== "1" and self.obj== "atRisk" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp1f" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.states== "base" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "3" and self.PplasticBin== "4" and self.PecoBot== "-44" and self.PthrowingPaper== "0" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4, self.Chuman-10 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.SpaperOrPlastic== "1" and self.obj== "atRisk" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp1f" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.states== "base" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "3" and self.PplasticBin== "4" and self.PecoBot== "-44" and self.PthrowingPaper== "0" and self.Phuman== "1"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 and self.Chuman<10 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.obj== "idle" and self.paperBin== "base" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.PecoBot== "-23" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.Phuman== "-11" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic0" and self.ecoBot== "going_base_to_hallway" and self.pickingUp== "pickingUp_initial_location" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-49 - self.TIMEUNIT, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.obj== "idle" and self.paperBin== "base" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.PecoBot== "-23" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.Phuman== "-11" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic0" and self.ecoBot== "going_base_to_hallway" and self.pickingUp== "pickingUp_initial_location" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.states== "base"  ):
						if ( (12<self.CecoBot and self.Chuman<49 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.paperBin== "base" and self.obj== "idle" and self.PthrowingPlastic== "3" and self.PthrowingPaper== "0" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-44"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55, self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.paperBin== "base" and self.obj== "idle" and self.PthrowingPlastic== "3" and self.PthrowingPaper== "0" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-44"  ):
						if ( (3<self.CecoBot and self.Chuman<=55 and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.paperBin== "base" and self.PecoBot== "-23" and self.human== "office" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_base_to_hallway" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash_initial_location" and self.PpickingUp== "0" and self.Phuman== "1" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.paperBin== "base" and self.PecoBot== "-23" and self.human== "office" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_base_to_hallway" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash_initial_location" and self.PpickingUp== "0" and self.Phuman== "1" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.SpaperOrPlastic== "1" and self.PpickingUp== "1" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp1f" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom" and self.obj== "atRisk" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PecoBot== "3" and self.paperBin== "base" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-24 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.SpaperOrPlastic== "1" and self.PpickingUp== "1" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp1f" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom" and self.obj== "atRisk" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PecoBot== "3" and self.paperBin== "base" and self.PthrowingPaper== "0"  ):
						if ( (1<self.CecoBot and self.Cobj<24 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "3" and self.PthrowingPaper== "3" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.PpaperBin== "2" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "-22" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.ecoBot== "doing_throwPaper_in_base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.states== "base" and self.human== "doing_wait_in_office"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4, self.Chuman-36 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "3" and self.PthrowingPaper== "3" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.PpaperBin== "2" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "-22" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.ecoBot== "doing_throwPaper_in_base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.states== "base" and self.human== "doing_wait_in_office"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 and self.Chuman<36 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "2" and self.human== "office" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.PpaperBin== "2" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.ecoBot== "hallway" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.PecoBot== "3" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "2" and self.human== "office" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.PpaperBin== "2" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.ecoBot== "hallway" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.PecoBot== "3" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "atRisk" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.human== "office" and self.pickingUp== "pickingUp1f" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "trashRoom" and self.states== "base" and self.PpickingUp== "1" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.PecoBot== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-7 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "atRisk" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.human== "office" and self.pickingUp== "pickingUp1f" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "trashRoom" and self.states== "base" and self.PpickingUp== "1" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.PecoBot== "4"  ):
						if ( (1<self.CecoBot and self.Chuman<7 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "2" and self.states== "base" and self.ecoBot== "hallway" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.paperBin== "base" and self.PecoBot== "3" and self.PmakingTrash== "3" and self.PplasticBin== "4" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-24 - self.TIMEUNIT ] , [-13- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-24 - self.TIMEUNIT ] , [self.CecoBot+ self.TIMEUNIT-self.Chuman ])
				if (temp1 >= 0):
					temps.add(temp1)
				temp2= optimal_wait([ 24 + self.TIMEUNIT-self.Chuman ] , [ self.Chuman-50 ] , [self.CecoBot+ self.TIMEUNIT-self.Chuman ])
				if (temp2 >= 0):
					temps.add(temp2)
				temp3= optimal_wait([ 30 + self.TIMEUNIT-self.Chuman ] , [ self.Chuman-50 ] , [13-(self.Chuman-self.CecoBot), self.Chuman-self.CecoBot ])
				if (temp3 >= 0):
					temps.add(temp3)
				temp4= optimal_wait([ 24 + self.TIMEUNIT-self.Chuman, 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-50 ] , [-13- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp4 >= 0):
					temps.add(temp4)
				temp5= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-30 - self.TIMEUNIT ] , [13-(self.Chuman-self.CecoBot), self.Chuman-self.CecoBot ])
				if (temp5 >= 0):
					temps.add(temp5)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "2" and self.states== "base" and self.ecoBot== "hallway" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.paperBin== "base" and self.PecoBot== "3" and self.PmakingTrash== "3" and self.PplasticBin== "4" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait"  ):
						if ( (1<self.CecoBot and self.Chuman<24 and self.CecoBot- self.Chuman<-13 )  or  (1<self.CecoBot and self.Chuman<24 and self.Chuman<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
						if ( (24<=self.Chuman and self.Chuman<=50 and self.Chuman<self.CecoBot )  or  (30<=self.Chuman and self.Chuman<=50 and self.Chuman- self.CecoBot<=13 and self.CecoBot<=self.Chuman )  or  (24<=self.Chuman and 1<self.CecoBot and self.Chuman<=50 and self.CecoBot- self.Chuman<-13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2base!", "hallway", "going_hallway_to_base")
						if ( (1<self.CecoBot and self.Chuman<30 and self.Chuman- self.CecoBot<=13 and self.CecoBot<=self.Chuman )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.PplasticBin== "4" and self.PecoBot== "-32" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash0" and self.ecoBot== "going_hallway_to_base" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.paperBin== "base" and self.PmakingTrash== "1" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.PplasticBin== "4" and self.PecoBot== "-32" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash0" and self.ecoBot== "going_hallway_to_base" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.paperBin== "base" and self.PmakingTrash== "1" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash_initial_location" and self.PecoBot== "2" and self.PpaperBin== "2" and self.obj== "idle" and self.states== "base" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.PthrowingPlastic== "0" and self.human== "office" and self.ecoBot== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.pickingUp== "pickingUp_initial_location" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash_initial_location" and self.PecoBot== "2" and self.PpaperBin== "2" and self.obj== "idle" and self.states== "base" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.PthrowingPlastic== "0" and self.human== "office" and self.ecoBot== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.pickingUp== "pickingUp_initial_location" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.PthrowingPaper== "0"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "1" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "0" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.human== "office" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "office" and self.throwingPaper== "throwingPaper_initial_location" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.makingTrash== "makingTrash_initial_location" and self.PplasticBin== "4" and self.paperBin== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "1" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "0" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.human== "office" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "office" and self.throwingPaper== "throwingPaper_initial_location" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.makingTrash== "makingTrash_initial_location" and self.PplasticBin== "4" and self.paperBin== "base"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.human== "office" and self.paperBin== "base" and self.makingTrash== "makingTrash0" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.ecoBot== "going_hallway_to_office" and self.states== "base" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.PecoBot== "-31"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.human== "office" and self.paperBin== "base" and self.makingTrash== "makingTrash0" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.ecoBot== "going_hallway_to_office" and self.states== "base" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.PecoBot== "-31"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.Phuman== "1" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "0" and self.human== "office" and self.PmakingTrash== "0" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.obj== "idle" and self.ecoBot== "base" and self.PecoBot== "2" and self.makingTrash== "makingTrash_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.Phuman== "1" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "0" and self.human== "office" and self.PmakingTrash== "0" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.obj== "idle" and self.ecoBot== "base" and self.PecoBot== "2" and self.makingTrash== "makingTrash_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PpickingUp== "0"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "0" and self.Phuman== "-11" and self.SpaperOrPlastic== "0" and self.obj== "atRisk" and self.paperBin== "base" and self.PpickingUp== "1" and self.pickingUp== "pickingUp1f" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-34" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.states== "base" and self.human== "doing_wait_in_office" and self.ecoBot== "going_hallway_to_trashRoom" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Cobj-10 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "0" and self.Phuman== "-11" and self.SpaperOrPlastic== "0" and self.obj== "atRisk" and self.paperBin== "base" and self.PpickingUp== "1" and self.pickingUp== "pickingUp1f" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-34" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.states== "base" and self.human== "doing_wait_in_office" and self.ecoBot== "going_hallway_to_trashRoom" and self.PplasticBin== "4"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Cobj<10 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "2" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "base" and self.PpaperBin== "2" and self.Phuman== "-11"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "2" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "base" and self.PpaperBin== "2" and self.Phuman== "-11"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.obj== "idle" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "2" and self.ecoBot== "going_hallway_to_base" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.PecoBot== "-32" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.obj== "idle" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "2" and self.ecoBot== "going_hallway_to_base" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.PecoBot== "-32" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.human== "office"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.PecoBot== "-44" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.PthrowingPlastic== "3" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.states== "base" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4, self.Chuman-36 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.PecoBot== "-44" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.PthrowingPlastic== "3" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.states== "base" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.obj== "idle"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 and self.Chuman<36 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic0" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.Phuman== "-11" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.obj== "idle" and self.PthrowingPaper== "2" and self.states== "base" and self.PplasticBin== "4" and self.paperBin== "base" and self.PecoBot== "-34" and self.ecoBot== "going_hallway_to_trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-32 - self.TIMEUNIT, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic0" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.Phuman== "-11" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.obj== "idle" and self.PthrowingPaper== "2" and self.states== "base" and self.PplasticBin== "4" and self.paperBin== "base" and self.PecoBot== "-34" and self.ecoBot== "going_hallway_to_trashRoom"  ):
						if ( (12<self.CecoBot and self.Chuman<32 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.ecoBot== "trashRoom" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.human== "doing_wait_in_office" and self.paperBin== "base" and self.PmakingTrash== "3" and self.obj== "idle" and self.PecoBot== "4" and self.Phuman== "-11" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.ecoBot== "trashRoom" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.human== "doing_wait_in_office" and self.paperBin== "base" and self.PmakingTrash== "3" and self.obj== "idle" and self.PecoBot== "4" and self.Phuman== "-11" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.ecoBot== "trashRoom" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.human== "office" and self.PmakingTrash== "0" and self.obj== "idle" and self.paperBin== "base" and self.makingTrash== "makingTrash_initial_location" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.PecoBot== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.ecoBot== "trashRoom" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.human== "office" and self.PmakingTrash== "0" and self.obj== "idle" and self.paperBin== "base" and self.makingTrash== "makingTrash_initial_location" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.PecoBot== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.states== "base"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "3" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.PthrowingPaper== "2" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.Phuman== "-11" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.states== "base" and self.ecoBot== "going_trashRoom_to_hallway" and self.PecoBot== "-43" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-19 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "3" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.PthrowingPaper== "2" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.Phuman== "-11" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.states== "base" and self.ecoBot== "going_trashRoom_to_hallway" and self.PecoBot== "-43" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<19 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.PplasticBin== "4" and self.PmakingTrash== "1" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.makingTrash== "makingTrash0" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.PecoBot== "2" and self.PthrowingPlastic== "0" and self.ecoBot== "base" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.PplasticBin== "4" and self.PmakingTrash== "1" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.makingTrash== "makingTrash0" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.PecoBot== "2" and self.PthrowingPlastic== "0" and self.ecoBot== "base" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.human== "office"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "2" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "base" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-37 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "2" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "base" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "0"  ):
						if ( (1<self.CecoBot and self.Chuman<37 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.makingTrash== "makingTrash_initial_location" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.PthrowingPlastic== "2" and self.PthrowingPaper== "0" and self.PecoBot== "4" and self.PmakingTrash== "0" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.ecoBot== "trashRoom" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.makingTrash== "makingTrash_initial_location" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.PthrowingPlastic== "2" and self.PthrowingPaper== "0" and self.PecoBot== "4" and self.PmakingTrash== "0" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.ecoBot== "trashRoom" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic0"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.PmakingTrash== "2" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp1f" and self.human== "office" and self.SpaperOrPlastic== "1" and self.PpickingUp== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.obj== "atRisk" and self.PthrowingPlastic== "0" and self.PecoBot== "-13" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.ecoBot== "going_office_to_hallway" and self.paperBin== "base" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [10-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Cobj-23 - self.TIMEUNIT ] , [-10- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.PmakingTrash== "2" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp1f" and self.human== "office" and self.SpaperOrPlastic== "1" and self.PpickingUp== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.obj== "atRisk" and self.PthrowingPlastic== "0" and self.PecoBot== "-13" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.ecoBot== "going_office_to_hallway" and self.paperBin== "base" and self.states== "base"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman- self.CecoBot<=10 and self.Chuman==self.Cobj )  or  (9<self.CecoBot and self.CecoBot<=10 and self.Cobj<23 and self.CecoBot- self.Cobj<-10 and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.PmakingTrash== "3" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "-32" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_base" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-32 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.PmakingTrash== "3" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "-32" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_base" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.obj== "idle"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<32 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "0" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0" and self.human== "office" and self.PplasticBin== "4" and self.states== "base" and self.PecoBot== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.obj== "idle" and self.ecoBot== "trashRoom" and self.paperBin== "base" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "0" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0" and self.human== "office" and self.PplasticBin== "4" and self.states== "base" and self.PecoBot== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.obj== "idle" and self.ecoBot== "trashRoom" and self.paperBin== "base" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.ecoBot== "office" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "0" and self.PecoBot== "1" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.states== "base" and self.obj== "idle" and self.PmakingTrash== "3" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.ecoBot== "office" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "0" and self.PecoBot== "1" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.states== "base" and self.obj== "idle" and self.PmakingTrash== "3" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.PecoBot== "-13" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.obj== "atRisk" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.Phuman== "-11" and self.ecoBot== "going_office_to_hallway" and self.pickingUp== "pickingUp0" and self.PpickingUp== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "2"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-29 - self.TIMEUNIT, self.CecoBot-10 ] , [-6- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.PecoBot== "-13" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.obj== "atRisk" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.Phuman== "-11" and self.ecoBot== "going_office_to_hallway" and self.pickingUp== "pickingUp0" and self.PpickingUp== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "2"  ):
						if ( (9<self.CecoBot and self.Cobj<29 and self.CecoBot<=10 and self.CecoBot- self.Cobj<-6 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "1" and self.PpaperBin== "2" and self.human== "office" and self.PecoBot== "-31" and self.PmakingTrash== "1" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.states== "base" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_office" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "1" and self.PpaperBin== "2" and self.human== "office" and self.PecoBot== "-31" and self.PmakingTrash== "1" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.states== "base" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_office" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.states== "base" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.paperBin== "base" and self.ecoBot== "office" and self.PecoBot== "1" and self.SpaperOrPlastic== "0" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.states== "base" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.paperBin== "base" and self.ecoBot== "office" and self.PecoBot== "1" and self.SpaperOrPlastic== "0" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "1" and self.ecoBot== "base" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.PecoBot== "2" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.PmakingTrash== "3"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-37 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "1" and self.ecoBot== "base" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.PecoBot== "2" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.PmakingTrash== "3"  ):
						if ( (1<self.CecoBot and self.Chuman<37 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "office" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.PecoBot== "1" and self.Phuman== "-11" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-40 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "office" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.PecoBot== "1" and self.Phuman== "-11" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "2"  ):
						if ( (1<self.CecoBot and self.Chuman<40 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.human== "office" and self.ecoBot== "going_office_to_hallway" and self.SpaperOrPlastic== "0" and self.Phuman== "1" and self.paperBin== "base" and self.PmakingTrash== "2" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.states== "base" and self.PpickingUp== "0" and self.PecoBot== "-13" and self.obj== "idle" and self.throwingPaper== "throwingPaper0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.human== "office" and self.ecoBot== "going_office_to_hallway" and self.SpaperOrPlastic== "0" and self.Phuman== "1" and self.paperBin== "base" and self.PmakingTrash== "2" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.states== "base" and self.PpickingUp== "0" and self.PecoBot== "-13" and self.obj== "idle" and self.throwingPaper== "throwingPaper0"  ):
						if ( (1<self.Chuman and 9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.obj== "atRisk" and self.PpickingUp== "1" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PecoBot== "2" and self.pickingUp== "pickingUp1f" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.states== "base" and self.Phuman== "1" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-11 - self.TIMEUNIT ] , [self.Chuman-self.Cobj, 3-(self.Chuman-self.CecoBot) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.Cobj-11 - self.TIMEUNIT ] , [-3- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.obj== "atRisk" and self.PpickingUp== "1" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PecoBot== "2" and self.pickingUp== "pickingUp1f" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.states== "base" and self.Phuman== "1" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "base"  ):
						if ( (1<self.CecoBot and self.Chuman<11 and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=3 )  or  (1<self.CecoBot and 1<self.Chuman and self.Cobj<11 and self.CecoBot- self.Cobj<-3 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PecoBot== "-32" and self.ecoBot== "going_hallway_to_base" and self.states== "base" and self.paperBin== "base" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-36 - self.TIMEUNIT, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PecoBot== "-32" and self.ecoBot== "going_hallway_to_base" and self.states== "base" and self.paperBin== "base" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait"  ):
						if ( (12<self.CecoBot and self.Chuman<36 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.PecoBot== "3" and self.PplasticBin== "4" and self.states== "base" and self.Phuman== "1" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.PpaperBin== "2" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.PecoBot== "3" and self.PplasticBin== "4" and self.states== "base" and self.Phuman== "1" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.PpaperBin== "2" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.human== "office" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.makingTrash== "makingTrash1s" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.ecoBot== "going_trashRoom_to_hallway" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.PecoBot== "-43" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.obj== "idle" and self.states== "base" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.human== "office" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.makingTrash== "makingTrash1s" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.ecoBot== "going_trashRoom_to_hallway" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.PecoBot== "-43" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.obj== "idle" and self.states== "base" and self.PplasticBin== "4"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.PecoBot== "2" and self.states== "base" and self.paperBin== "base" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.makingTrash== "makingTrash0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.pickingUp== "pickingUp_initial_location" and self.plasticBin== "trashRoom" and self.ecoBot== "base" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "1" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.PecoBot== "2" and self.states== "base" and self.paperBin== "base" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.makingTrash== "makingTrash0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.pickingUp== "pickingUp_initial_location" and self.plasticBin== "trashRoom" and self.ecoBot== "base" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "1" and self.obj== "idle"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PplasticBin== "4" and self.PecoBot== "4" and self.paperBin== "base" and self.PpickingUp== "0" and self.states== "base" and self.ecoBot== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "idle" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "-11" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "0" and self.human== "doing_wait_in_office" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PplasticBin== "4" and self.PecoBot== "4" and self.paperBin== "base" and self.PpickingUp== "0" and self.states== "base" and self.ecoBot== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "idle" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "-11" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "0" and self.human== "doing_wait_in_office" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PthrowingPaper== "0" and self.human== "office" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.PthrowingPlastic== "3" and self.PecoBot== "-44" and self.makingTrash== "makingTrash0" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "1" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.PplasticBin== "4" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PthrowingPaper== "0" and self.human== "office" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.PthrowingPlastic== "3" and self.PecoBot== "-44" and self.makingTrash== "makingTrash0" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "1" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.PplasticBin== "4" and self.Phuman== "1"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_trashRoom" and self.PecoBot== "-34" and self.makingTrash== "makingTrash_initial_location" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_trashRoom" and self.PecoBot== "-34" and self.makingTrash== "makingTrash_initial_location" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp1f" and self.PmakingTrash== "2" and self.human== "office" and self.PplasticBin== "4" and self.Phuman== "1" and self.PecoBot== "-31" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.obj== "atRisk" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "1" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0" and self.ecoBot== "going_hallway_to_office"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-33 - self.TIMEUNIT, self.CecoBot-10 ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman), -10- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [10-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp1f" and self.PmakingTrash== "2" and self.human== "office" and self.PplasticBin== "4" and self.Phuman== "1" and self.PecoBot== "-31" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.obj== "atRisk" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "1" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0" and self.ecoBot== "going_hallway_to_office"  ):
						if ( (9<self.CecoBot and self.Cobj<33 and self.CecoBot<=10 and self.CecoBot- self.Chuman<-1 and self.CecoBot- self.Cobj<-10 )  or  (9<self.CecoBot and self.CecoBot<=10 and self.Chuman- self.CecoBot<=10 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.SpaperOrPlastic== "1" and self.ecoBot== "base" and self.states== "base" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.pickingUp== "pickingUp1f" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PecoBot== "2" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.human== "office" and self.PthrowingPaper== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-7 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.SpaperOrPlastic== "1" and self.ecoBot== "base" and self.states== "base" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.pickingUp== "pickingUp1f" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PecoBot== "2" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.human== "office" and self.PthrowingPaper== "2"  ):
						if ( (1<self.CecoBot and self.Chuman<7 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "3" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.states== "base" and self.paperBin== "base" and self.obj== "idle" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic0" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.PecoBot== "-22" and self.ecoBot== "doing_throwPaper_in_base" and self.human== "office" and self.Phuman== "1" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "3" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.states== "base" and self.paperBin== "base" and self.obj== "idle" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic0" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.PecoBot== "-22" and self.ecoBot== "doing_throwPaper_in_base" and self.human== "office" and self.Phuman== "1" and self.SpaperOrPlastic== "0"  ):
						if ( (1<self.Chuman and 3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "atRisk" and self.PpickingUp== "4" and self.PthrowingPaper== "0" and self.PmakingTrash== "3" and self.ecoBot== "hallway" and self.PthrowingPlastic== "2" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.Phuman== "-11" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "3" and self.PpaperBin== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-30 - self.TIMEUNIT ] , [-15- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "atRisk" and self.PpickingUp== "4" and self.PthrowingPaper== "0" and self.PmakingTrash== "3" and self.ecoBot== "hallway" and self.PthrowingPlastic== "2" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.Phuman== "-11" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "3" and self.PpaperBin== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp0"  ):
						if ( (1<self.CecoBot and self.Cobj<30 and self.CecoBot- self.Cobj<-15 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "doing_wait_in_office" and self.ecoBot== "office" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.PecoBot== "1" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-40 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "doing_wait_in_office" and self.ecoBot== "office" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.PecoBot== "1" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.PplasticBin== "4"  ):
						if ( (1<self.CecoBot and self.Chuman<40 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "going_hallway_to_office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "idle" and self.PthrowingPlastic== "0" and self.human== "office" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.PecoBot== "-31" and self.states== "base" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "going_hallway_to_office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "idle" and self.PthrowingPlastic== "0" and self.human== "office" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.PecoBot== "-31" and self.states== "base" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1"  ):
						if ( (9<self.CecoBot and 1<self.Chuman and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp1f" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.obj== "atRisk" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper0" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.PecoBot== "2" and self.states== "base" and self.PmakingTrash== "3" and self.PpickingUp== "1" and self.ecoBot== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-7 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp1f" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.obj== "atRisk" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper0" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.PecoBot== "2" and self.states== "base" and self.PmakingTrash== "3" and self.PpickingUp== "1" and self.ecoBot== "base"  ):
						if ( (1<self.CecoBot and self.Cobj<7 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.ecoBot== "going_office_to_hallway" and self.states== "base" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "-13" and self.paperBin== "base" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "3" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-49 - self.TIMEUNIT, self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.ecoBot== "going_office_to_hallway" and self.states== "base" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "-13" and self.paperBin== "base" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "3" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (9<self.CecoBot and self.Chuman<49 and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.obj== "atRisk" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.ecoBot== "going_hallway_to_office" and self.PecoBot== "-31" and self.PplasticBin== "4" and self.human== "doing_wait_in_office" and self.PthrowingPlastic== "0" and self.states== "base" and self.PpickingUp== "1" and self.pickingUp== "pickingUp1f" and self.Phuman== "-11" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-33 - self.TIMEUNIT, self.CecoBot-10 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.obj== "atRisk" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.ecoBot== "going_hallway_to_office" and self.PecoBot== "-31" and self.PplasticBin== "4" and self.human== "doing_wait_in_office" and self.PthrowingPlastic== "0" and self.states== "base" and self.PpickingUp== "1" and self.pickingUp== "pickingUp1f" and self.Phuman== "-11" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (9<self.CecoBot and self.Cobj<33 and self.CecoBot<=10 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "3" and self.ecoBot== "hallway" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.states== "base" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PmakingTrash== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "3" and self.ecoBot== "hallway" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.states== "base" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PmakingTrash== "2"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.ecoBot== "office" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.PplasticBin== "4" and self.obj== "idle" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.makingTrash== "makingTrash0" and self.PpaperBin== "2" and self.states== "base" and self.human== "office" and self.PecoBot== "1" and self.PmakingTrash== "1" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.PmakingTrash== "3" and self.ecoBot== "base" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper0" and self.human== "doing_wait_in_office" and self.PecoBot== "2" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.PthrowingPaper== "2" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-33 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.PmakingTrash== "3" and self.ecoBot== "base" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper0" and self.human== "doing_wait_in_office" and self.PecoBot== "2" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.PthrowingPaper== "2" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base"  ):
						if ( (1<self.CecoBot and self.Chuman<33 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.ecoBot== "trashRoom" and self.PpickingUp== "1" and self.pickingUp== "pickingUp1f" and self.PecoBot== "4" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "2" and self.obj== "atRisk" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-7 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.ecoBot== "trashRoom" and self.PpickingUp== "1" and self.pickingUp== "pickingUp1f" and self.PecoBot== "4" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "2" and self.obj== "atRisk" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2"  ):
						if ( (1<self.CecoBot and self.Chuman<7 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.obj== "atRisk" and self.states== "base" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "4" and self.PplasticBin== "4" and self.Phuman== "1" and self.pickingUp== "pickingUp0" and self.ecoBot== "office" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.PecoBot== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.Cobj-40 ] , [-5- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.obj== "atRisk" and self.states== "base" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "4" and self.PplasticBin== "4" and self.Phuman== "1" and self.pickingUp== "pickingUp0" and self.ecoBot== "office" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.PecoBot== "1"  ):
						if ( (1<self.CecoBot and 1<self.Chuman and self.Cobj<=40 and self.CecoBot- self.Cobj<-5 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "officeClean!", "office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "going_hallway_to_base" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.makingTrash== "makingTrash_initial_location" and self.obj== "idle" and self.PpickingUp== "0" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "0" and self.states== "base" and self.Phuman== "1" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-32"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "going_hallway_to_base" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.makingTrash== "makingTrash_initial_location" and self.obj== "idle" and self.PpickingUp== "0" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "0" and self.states== "base" and self.Phuman== "1" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-32"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "0" and self.Phuman== "1" and self.ecoBot== "going_trashRoom_to_hallway" and self.paperBin== "base" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.human== "office" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.PecoBot== "-43" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "0" and self.Phuman== "1" and self.ecoBot== "going_trashRoom_to_hallway" and self.paperBin== "base" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.human== "office" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.PecoBot== "-43" and self.PpaperBin== "2"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "0" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PpaperBin== "2" and self.obj== "atRisk" and self.Phuman== "1" and self.PplasticBin== "4" and self.PpickingUp== "1" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.PecoBot== "-32" and self.PthrowingPaper== "0" and self.ecoBot== "going_hallway_to_base" and self.pickingUp== "pickingUp1f" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-10 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "0" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PpaperBin== "2" and self.obj== "atRisk" and self.Phuman== "1" and self.PplasticBin== "4" and self.PpickingUp== "1" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.PecoBot== "-32" and self.PthrowingPaper== "0" and self.ecoBot== "going_hallway_to_base" and self.pickingUp== "pickingUp1f" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<10 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.PecoBot== "4" and self.Phuman== "1" and self.PmakingTrash== "2" and self.ecoBot== "trashRoom" and self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.states== "base" and self.makingTrash== "makingTrash1s"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.PecoBot== "4" and self.Phuman== "1" and self.PmakingTrash== "2" and self.ecoBot== "trashRoom" and self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.states== "base" and self.makingTrash== "makingTrash1s"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.PpaperBin== "2" and self.human== "office" and self.states== "base" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.PecoBot== "-23" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.ecoBot== "going_base_to_hallway" and self.plasticBin== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.PpaperBin== "2" and self.human== "office" and self.states== "base" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.PecoBot== "-23" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.ecoBot== "going_base_to_hallway" and self.plasticBin== "trashRoom"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.plasticBin== "trashRoom" and self.human== "office" and self.PecoBot== "4" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.PmakingTrash== "2" and self.obj== "idle" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.ecoBot== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.plasticBin== "trashRoom" and self.human== "office" and self.PecoBot== "4" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.PmakingTrash== "2" and self.obj== "idle" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.ecoBot== "trashRoom"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.PmakingTrash== "2" and self.human== "office" and self.obj== "idle" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.plasticBin== "trashRoom" and self.ecoBot== "base" and self.PpickingUp== "0" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.states== "base" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.PmakingTrash== "2" and self.human== "office" and self.obj== "idle" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.plasticBin== "trashRoom" and self.ecoBot== "base" and self.PpickingUp== "0" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.states== "base" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "2"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.obj== "idle" and self.PpickingUp== "0" and self.PecoBot== "1" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.ecoBot== "office" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.obj== "idle" and self.PpickingUp== "0" and self.PecoBot== "1" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.ecoBot== "office" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "1"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "going_office_to_hallway" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.Phuman== "1" and self.human== "office" and self.PplasticBin== "4" and self.states== "base" and self.PecoBot== "-13" and self.PpaperBin== "2" and self.PthrowingPaper== "2" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.obj== "idle" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper0" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "going_office_to_hallway" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.Phuman== "1" and self.human== "office" and self.PplasticBin== "4" and self.states== "base" and self.PecoBot== "-13" and self.PpaperBin== "2" and self.PthrowingPaper== "2" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.obj== "idle" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper0" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (9<self.CecoBot and 1<self.Chuman and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "4" and self.PthrowingPaper== "2" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom" and self.obj== "atRisk" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp0" and self.PecoBot== "3"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-30 - self.TIMEUNIT ] , [-15- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "4" and self.PthrowingPaper== "2" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom" and self.obj== "atRisk" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp0" and self.PecoBot== "3"  ):
						if ( (1<self.CecoBot and self.Cobj<30 and self.CecoBot- self.Cobj<-15 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "office" and self.paperBin== "base" and self.pickingUp== "pickingUp1f" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "1" and self.PthrowingPlastic== "0" and self.human== "doing_wait_in_office" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.obj== "atRisk" and self.PmakingTrash== "3" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "1" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-3 - self.TIMEUNIT, self.Cobj-34 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "office" and self.paperBin== "base" and self.pickingUp== "pickingUp1f" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "1" and self.PthrowingPlastic== "0" and self.human== "doing_wait_in_office" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.obj== "atRisk" and self.PmakingTrash== "3" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "1" and self.SpaperOrPlastic== "0"  ):
						if ( (1<self.CecoBot and self.Chuman<3 and self.Cobj<34 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "plasticTrash!", "office", "doing_plasticTrash_in_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "3" and self.human== "doing_wait_in_office" and self.ecoBot== "going_hallway_to_office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "0" and self.PecoBot== "-31" and self.PpaperBin== "2" and self.states== "base" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.obj== "idle" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55, self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "3" and self.human== "doing_wait_in_office" and self.ecoBot== "going_hallway_to_office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "0" and self.PecoBot== "-31" and self.PpaperBin== "2" and self.states== "base" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.obj== "idle" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (9<self.CecoBot and self.Chuman<=55 and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.PecoBot== "-31" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.ecoBot== "going_hallway_to_office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.states== "base" and self.throwingPaper== "throwingPaper0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-39 - self.TIMEUNIT, self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.PecoBot== "-31" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.ecoBot== "going_hallway_to_office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.states== "base" and self.throwingPaper== "throwingPaper0"  ):
						if ( (9<self.CecoBot and self.Chuman<39 and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "-11" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.states== "base" and self.obj== "idle" and self.PplasticBin== "4" and self.PecoBot== "-32" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "going_hallway_to_base" and self.PmakingTrash== "3"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-36 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "-11" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.states== "base" and self.obj== "idle" and self.PplasticBin== "4" and self.PecoBot== "-32" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "going_hallway_to_base" and self.PmakingTrash== "3"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<36 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "1" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.ecoBot== "office" and self.PmakingTrash== "1" and self.PecoBot== "1" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.obj== "idle" and self.makingTrash== "makingTrash0" and self.states== "base" and self.SpaperOrPlastic== "0" and self.human== "office" and self.throwingPaper== "throwingPaper0"   ):
				temps=set()
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "going_trashRoom_to_hallway" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.PecoBot== "-43" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.paperBin== "base" and self.makingTrash== "makingTrash0" and self.PthrowingPaper== "0" and self.PmakingTrash== "1"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "going_trashRoom_to_hallway" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.PecoBot== "-43" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.paperBin== "base" and self.makingTrash== "makingTrash0" and self.PthrowingPaper== "0" and self.PmakingTrash== "1"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.obj== "idle" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "hallway" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.PecoBot== "3" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.Phuman== "-11"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-20 - self.TIMEUNIT ] , [self.Chuman-self.CecoBot, 13-(self.Chuman-self.CecoBot) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-20 - self.TIMEUNIT ] , [-13- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp1 >= 0):
					temps.add(temp1)
				temp2= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-20 - self.TIMEUNIT ] , [self.CecoBot+ self.TIMEUNIT-self.Chuman ])
				if (temp2 >= 0):
					temps.add(temp2)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.obj== "idle" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "hallway" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.PecoBot== "3" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.Phuman== "-11"  ):
						if ( (1<self.CecoBot and self.Chuman<20 and self.CecoBot<=self.Chuman and self.Chuman- self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2base!", "hallway", "going_hallway_to_base")
						if ( (1<self.CecoBot and self.Chuman<20 and self.CecoBot- self.Chuman<-13 )  or  (1<self.CecoBot and self.Chuman<20 and self.Chuman<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.PmakingTrash== "1" and self.ecoBot== "going_hallway_to_office" and self.paperBin== "base" and self.states== "base" and self.PthrowingPlastic== "2" and self.PecoBot== "-31" and self.makingTrash== "makingTrash0" and self.obj== "idle" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic0" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.PmakingTrash== "1" and self.ecoBot== "going_hallway_to_office" and self.paperBin== "base" and self.states== "base" and self.PthrowingPlastic== "2" and self.PecoBot== "-31" and self.makingTrash== "makingTrash0" and self.obj== "idle" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic0" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "hallway" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.states== "base" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.PecoBot== "3" and self.obj== "idle" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "hallway" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.states== "base" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.PecoBot== "3" and self.obj== "idle" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.PecoBot== "-13" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "1" and self.human== "office" and self.PplasticBin== "4" and self.states== "base" and self.paperBin== "base" and self.ecoBot== "going_office_to_hallway" and self.Phuman== "1" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash0" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.PecoBot== "-13" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "1" and self.human== "office" and self.PplasticBin== "4" and self.states== "base" and self.paperBin== "base" and self.ecoBot== "going_office_to_hallway" and self.Phuman== "1" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash0" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11" and self.obj== "idle" and self.PecoBot== "2" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0" and self.human== "doing_wait_in_office" and self.PmakingTrash== "3" and self.ecoBot== "base" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.PthrowingPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11" and self.obj== "idle" and self.PecoBot== "2" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0" and self.human== "doing_wait_in_office" and self.PmakingTrash== "3" and self.ecoBot== "base" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.PthrowingPlastic== "0"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper0" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.SpaperOrPlastic== "0" and self.PecoBot== "-34" and self.PplasticBin== "4" and self.Phuman== "-11" and self.paperBin== "base" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_hallway_to_trashRoom" and self.states== "base" and self.PpaperBin== "2" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-36 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper0" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.SpaperOrPlastic== "0" and self.PecoBot== "-34" and self.PplasticBin== "4" and self.Phuman== "-11" and self.paperBin== "base" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_hallway_to_trashRoom" and self.states== "base" and self.PpaperBin== "2" and self.obj== "idle"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<36 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.PecoBot== "-31" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "atRisk" and self.SpaperOrPlastic== "0" and self.PpickingUp== "4" and self.Phuman== "-11" and self.states== "base" and self.pickingUp== "pickingUp0" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.paperBin== "base" and self.ecoBot== "going_hallway_to_office"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-8 - self.TIMEUNIT, self.Cobj-39 - self.TIMEUNIT, self.CecoBot-10 ] , [-16- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.PecoBot== "-31" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "atRisk" and self.SpaperOrPlastic== "0" and self.PpickingUp== "4" and self.Phuman== "-11" and self.states== "base" and self.pickingUp== "pickingUp0" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.paperBin== "base" and self.ecoBot== "going_hallway_to_office"  ):
						if ( (9<self.CecoBot and self.Chuman<8 and self.Cobj<39 and self.CecoBot<=10 and self.CecoBot- self.Cobj<-16 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.paperBin== "base" and self.PecoBot== "-23" and self.PpickingUp== "0" and self.states== "base" and self.obj== "idle" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.PmakingTrash== "3" and self.ecoBot== "going_base_to_hallway" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.Phuman== "-11" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-49 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.paperBin== "base" and self.PecoBot== "-23" and self.PpickingUp== "0" and self.states== "base" and self.obj== "idle" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.PmakingTrash== "3" and self.ecoBot== "going_base_to_hallway" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.Phuman== "-11" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<49 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.obj== "idle" and self.ecoBot== "going_office_to_hallway" and self.PmakingTrash== "3" and self.PecoBot== "-13" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.obj== "idle" and self.ecoBot== "going_office_to_hallway" and self.PmakingTrash== "3" and self.PecoBot== "-13" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.PplasticBin== "4"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.states== "base" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.obj== "atRisk" and self.human== "office" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp1f" and self.plasticBin== "trashRoom" and self.PecoBot== "-32"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-10 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.states== "base" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.obj== "atRisk" and self.human== "office" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp1f" and self.plasticBin== "trashRoom" and self.PecoBot== "-32"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<10 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.Phuman== "1" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.ecoBot== "base" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PecoBot== "2" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.Phuman== "1" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.ecoBot== "base" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PecoBot== "2" and self.human== "office"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.obj== "idle" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "hallway" and self.PthrowingPlastic== "0" and self.Phuman== "-11" and self.PecoBot== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "doing_wait_in_office" and self.states== "base" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [9-(self.Chuman-self.CecoBot) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.obj== "idle" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "hallway" and self.PthrowingPlastic== "0" and self.Phuman== "-11" and self.PecoBot== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "doing_wait_in_office" and self.states== "base" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 and self.CecoBot- self.Chuman<-9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
						if ( (1<self.CecoBot and self.Chuman<=55 and self.Chuman- self.CecoBot<=9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "doing_wait_in_office" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.SpaperOrPlastic== "0" and self.PpickingUp== "1" and self.Phuman== "-11" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.PecoBot== "1" and self.paperBin== "base" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.ecoBot== "office" and self.states== "base" and self.PmakingTrash== "3"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-34 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "doing_wait_in_office" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.SpaperOrPlastic== "0" and self.PpickingUp== "1" and self.Phuman== "-11" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.PecoBot== "1" and self.paperBin== "base" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.ecoBot== "office" and self.states== "base" and self.PmakingTrash== "3"  ):
						if ( (1<self.CecoBot and self.Cobj<34 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "plasticTrash!", "office", "doing_plasticTrash_in_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper0" and self.PmakingTrash== "2" and self.Phuman== "1" and self.ecoBot== "hallway" and self.PthrowingPlastic== "2" and self.obj== "idle" and self.PthrowingPaper== "2" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.states== "base" and self.PecoBot== "3" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper0" and self.PmakingTrash== "2" and self.Phuman== "1" and self.ecoBot== "hallway" and self.PthrowingPlastic== "2" and self.obj== "idle" and self.PthrowingPaper== "2" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.states== "base" and self.PecoBot== "3" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.human== "office"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "3" and self.PecoBot== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.states== "base" and self.PpickingUp== "0" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.ecoBot== "base" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11" and self.PpaperBin== "2" and self.obj== "idle" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "3" and self.PecoBot== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.states== "base" and self.PpickingUp== "0" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.ecoBot== "base" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11" and self.PpaperBin== "2" and self.obj== "idle" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.PplasticBin== "4"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.states== "base" and self.PthrowingPaper== "2" and self.ecoBot== "going_hallway_to_base" and self.Phuman== "-11" and self.PpaperBin== "2" and self.obj== "atRisk" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp1f" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "-32"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-6 - self.TIMEUNIT, self.CecoBot-13 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.states== "base" and self.PthrowingPaper== "2" and self.ecoBot== "going_hallway_to_base" and self.Phuman== "-11" and self.PpaperBin== "2" and self.obj== "atRisk" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp1f" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "-32"  ):
						if ( (12<self.CecoBot and self.Cobj<6 and self.CecoBot<=13 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "doing_wait_in_office" and self.PthrowingPaper== "0" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp1f" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.Phuman== "-11" and self.PthrowingPlastic== "3" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PecoBot== "-44" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PpickingUp== "1" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-10 - self.TIMEUNIT, self.CecoBot-4 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "doing_wait_in_office" and self.PthrowingPaper== "0" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp1f" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.Phuman== "-11" and self.PthrowingPlastic== "3" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PecoBot== "-44" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PpickingUp== "1" and self.states== "base"  ):
						if ( (3<self.CecoBot and self.Cobj<10 and self.CecoBot<=4 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.obj== "idle" and self.throwingPaper== "throwingPaper0" and self.throwingPlastic== "throwingPlastic0" and self.PpickingUp== "0" and self.states== "base" and self.PthrowingPlastic== "2" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.human== "office" and self.ecoBot== "going_hallway_to_trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-34" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "2" and self.PmakingTrash== "2" and self.paperBin== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.obj== "idle" and self.throwingPaper== "throwingPaper0" and self.throwingPlastic== "throwingPlastic0" and self.PpickingUp== "0" and self.states== "base" and self.PthrowingPlastic== "2" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.human== "office" and self.ecoBot== "going_hallway_to_trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-34" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "2" and self.PmakingTrash== "2" and self.paperBin== "base"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "-31" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_office" and self.Phuman== "1" and self.states== "base" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.PthrowingPaper== "2" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.obj== "atRisk" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp1f"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [self.Chuman-self.Cobj, 10-(self.Chuman-self.CecoBot) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Cobj-33 - self.TIMEUNIT ] , [-10- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "-31" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_office" and self.Phuman== "1" and self.states== "base" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.PthrowingPaper== "2" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.obj== "atRisk" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp1f"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=10 )  or  (9<self.CecoBot and self.CecoBot<=10 and self.Cobj<33 and self.CecoBot- self.Cobj<-10 and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.PthrowingPlastic== "2" and self.PmakingTrash== "1" and self.makingTrash== "makingTrash0" and self.PplasticBin== "4" and self.human== "office" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.obj== "idle" and self.SpaperOrPlastic== "1" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.PecoBot== "-34" and self.Phuman== "1" and self.ecoBot== "going_hallway_to_trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.PthrowingPlastic== "2" and self.PmakingTrash== "1" and self.makingTrash== "makingTrash0" and self.PplasticBin== "4" and self.human== "office" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.obj== "idle" and self.SpaperOrPlastic== "1" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.PecoBot== "-34" and self.Phuman== "1" and self.ecoBot== "going_hallway_to_trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "2" and self.PecoBot== "-31" and self.PplasticBin== "4" and self.paperBin== "base" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.ecoBot== "going_hallway_to_office" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "2" and self.PecoBot== "-31" and self.PplasticBin== "4" and self.paperBin== "base" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.ecoBot== "going_hallway_to_office" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom"  ):
						if ( (1<self.Chuman and 9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.pickingUp== "pickingUp1f" and self.obj== "atRisk" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.PecoBot== "-43" and self.states== "base" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.ecoBot== "going_trashRoom_to_hallway" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Cobj-23 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.pickingUp== "pickingUp1f" and self.obj== "atRisk" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.PecoBot== "-43" and self.states== "base" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.ecoBot== "going_trashRoom_to_hallway" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Cobj<23 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "going_trashRoom_to_hallway" and self.PpickingUp== "0" and self.states== "base" and self.Phuman== "1" and self.PpaperBin== "2" and self.PecoBot== "-43" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.human== "office" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic0" and self.makingTrash== "makingTrash1s" and self.paperBin== "base" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "going_trashRoom_to_hallway" and self.PpickingUp== "0" and self.states== "base" and self.Phuman== "1" and self.PpaperBin== "2" and self.PecoBot== "-43" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.human== "office" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic0" and self.makingTrash== "makingTrash1s" and self.paperBin== "base" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.obj== "idle"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "3" and self.Phuman== "-11" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.obj== "idle" and self.PecoBot== "-22" and self.states== "base" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.plasticBin== "trashRoom" and self.ecoBot== "doing_throwPaper_in_base" and self.human== "doing_wait_in_office" and self.paperBin== "base" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "3" and self.Phuman== "-11" and self.PplasticBin== "4" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.obj== "idle" and self.PecoBot== "-22" and self.states== "base" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.plasticBin== "trashRoom" and self.ecoBot== "doing_throwPaper_in_base" and self.human== "doing_wait_in_office" and self.paperBin== "base" and self.SpaperOrPlastic== "0"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.PpickingUp== "0" and self.ecoBot== "going_hallway_to_trashRoom" and self.PpaperBin== "2" and self.PecoBot== "-34" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.PpickingUp== "0" and self.ecoBot== "going_hallway_to_trashRoom" and self.PpaperBin== "2" and self.PecoBot== "-34" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.human== "office"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.PpickingUp== "0" and self.PecoBot== "-22" and self.SpaperOrPlastic== "0" and self.ecoBot== "doing_throwPaper_in_base" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.human== "office" and self.PpaperBin== "2" and self.states== "base" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "3" and self.PthrowingPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.PpickingUp== "0" and self.PecoBot== "-22" and self.SpaperOrPlastic== "0" and self.ecoBot== "doing_throwPaper_in_base" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.human== "office" and self.PpaperBin== "2" and self.states== "base" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "3" and self.PthrowingPlastic== "0"  ):
						if ( (1<self.Chuman and 3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "-31" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.states== "base" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.ecoBot== "going_hallway_to_office" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "-31" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.states== "base" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.ecoBot== "going_hallway_to_office" and self.PpickingUp== "0"  ):
						if ( (1<self.Chuman and 9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.ecoBot== "going_trashRoom_to_hallway" and self.obj== "idle" and self.Phuman== "-11" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.PpickingUp== "0" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-43" and self.PplasticBin== "4" and self.PthrowingPaper== "2"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-49 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.ecoBot== "going_trashRoom_to_hallway" and self.obj== "idle" and self.Phuman== "-11" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.PpickingUp== "0" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-43" and self.PplasticBin== "4" and self.PthrowingPaper== "2"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<49 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic0" and self.PpickingUp== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.states== "base" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.paperBin== "base" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "1" and self.PecoBot== "-43" and self.human== "office" and self.ecoBot== "going_trashRoom_to_hallway"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic0" and self.PpickingUp== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.states== "base" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.paperBin== "base" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "1" and self.PecoBot== "-43" and self.human== "office" and self.ecoBot== "going_trashRoom_to_hallway"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "1" and self.paperBin== "base" and self.ecoBot== "office" and self.obj== "idle" and self.PpickingUp== "0" and self.Phuman== "1" and self.makingTrash== "makingTrash_initial_location" and self.PthrowingPaper== "0" and self.PmakingTrash== "0" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.human== "office" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "1" and self.paperBin== "base" and self.ecoBot== "office" and self.obj== "idle" and self.PpickingUp== "0" and self.Phuman== "1" and self.makingTrash== "makingTrash_initial_location" and self.PthrowingPaper== "0" and self.PmakingTrash== "0" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.human== "office" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PplasticBin== "4" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.PecoBot== "-23" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.PpaperBin== "2" and self.states== "base" and self.obj== "idle" and self.Phuman== "1" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.ecoBot== "going_base_to_hallway" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PplasticBin== "4" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.PecoBot== "-23" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.PpaperBin== "2" and self.states== "base" and self.obj== "idle" and self.Phuman== "1" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.ecoBot== "going_base_to_hallway" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "base" and self.human== "office" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.PplasticBin== "4" and self.PecoBot== "2" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.states== "base" and self.obj== "atRisk" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "2" and self.pickingUp== "pickingUp1f" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-7 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "base" and self.human== "office" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.PplasticBin== "4" and self.PecoBot== "2" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.states== "base" and self.obj== "atRisk" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "2" and self.pickingUp== "pickingUp1f" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "1"  ):
						if ( (1<self.CecoBot and self.Chuman<7 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.SpaperOrPlastic== "1" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "0" and self.PecoBot== "-13" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.PmakingTrash== "2" and self.obj== "idle" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.human== "office" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.ecoBot== "going_office_to_hallway" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.SpaperOrPlastic== "1" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "0" and self.PecoBot== "-13" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.PmakingTrash== "2" and self.obj== "idle" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.human== "office" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.ecoBot== "going_office_to_hallway" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base"  ):
						if ( (1<self.Chuman and 9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.PmakingTrash== "1" and self.makingTrash== "makingTrash0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PecoBot== "1" and self.states== "base" and self.PpaperBin== "2" and self.ecoBot== "office" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.paperBin== "base" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.PmakingTrash== "1" and self.makingTrash== "makingTrash0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PecoBot== "1" and self.states== "base" and self.PpaperBin== "2" and self.ecoBot== "office" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.paperBin== "base" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "1"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.PthrowingPlastic== "0" and self.ecoBot== "office" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "1" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.states== "base" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.PthrowingPlastic== "0" and self.ecoBot== "office" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "1" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.states== "base" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.SpaperOrPlastic== "1"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.obj== "idle" and self.PthrowingPlastic== "3" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.PecoBot== "-44" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.human== "office" and self.paperBin== "base" and self.PpaperBin== "2" and self.states== "base" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.obj== "idle" and self.PthrowingPlastic== "3" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.PecoBot== "-44" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.human== "office" and self.paperBin== "base" and self.PpaperBin== "2" and self.states== "base" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.SpaperOrPlastic== "1"  ):
						if ( (3<self.CecoBot and 1<self.Chuman and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.obj== "idle" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "going_office_to_hallway" and self.PmakingTrash== "3" and self.PthrowingPaper== "0" and self.states== "base" and self.SpaperOrPlastic== "1" and self.PecoBot== "-13" and self.PplasticBin== "4" and self.paperBin== "base"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Chuman-49 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.obj== "idle" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "going_office_to_hallway" and self.PmakingTrash== "3" and self.PthrowingPaper== "0" and self.states== "base" and self.SpaperOrPlastic== "1" and self.PecoBot== "-13" and self.PplasticBin== "4" and self.paperBin== "base"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman<49 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "-13" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "atRisk" and self.PpaperBin== "2" and self.PpickingUp== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.Phuman== "-11" and self.pickingUp== "pickingUp1f" and self.PmakingTrash== "3" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.states== "base" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.ecoBot== "going_office_to_hallway"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Cobj-23 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "-13" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "atRisk" and self.PpaperBin== "2" and self.PpickingUp== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.Phuman== "-11" and self.pickingUp== "pickingUp1f" and self.PmakingTrash== "3" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.states== "base" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.ecoBot== "going_office_to_hallway"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Cobj<23 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "3" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.states== "base" and self.Phuman== "-11" and self.paperBin== "base" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [9-(self.Chuman-self.CecoBot) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "3" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.states== "base" and self.Phuman== "-11" and self.paperBin== "base" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 and self.Chuman- self.CecoBot<=9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
						if ( (1<self.CecoBot and self.Chuman<=55 and self.CecoBot- self.Chuman<-9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "-34" and self.ecoBot== "going_hallway_to_trashRoom" and self.states== "base" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.Phuman== "1" and self.PmakingTrash== "1" and self.human== "office" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "-34" and self.ecoBot== "going_hallway_to_trashRoom" and self.states== "base" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.Phuman== "1" and self.PmakingTrash== "1" and self.human== "office" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.obj== "idle"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.obj== "idle" and self.PthrowingPlastic== "2" and self.Phuman== "1" and self.human== "office" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "4" and self.paperBin== "base" and self.ecoBot== "trashRoom" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.obj== "idle" and self.PthrowingPlastic== "2" and self.Phuman== "1" and self.human== "office" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "4" and self.paperBin== "base" and self.ecoBot== "trashRoom" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.SpaperOrPlastic== "1"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "-31" and self.ecoBot== "going_hallway_to_office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper0" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.obj== "idle" and self.PpickingUp== "0" and self.Phuman== "-11" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.states== "base" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-39 - self.TIMEUNIT, self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "-31" and self.ecoBot== "going_hallway_to_office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper0" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.obj== "idle" and self.PpickingUp== "0" and self.Phuman== "-11" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.states== "base" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (9<self.CecoBot and self.Chuman<39 and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "1" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "trashRoom" and self.PpaperBin== "2" and self.obj== "idle" and self.PecoBot== "4" and self.makingTrash== "makingTrash0" and self.throwingPlastic== "throwingPlastic0" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.human== "office" and self.Phuman== "1" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.states== "base" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "1" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "trashRoom" and self.PpaperBin== "2" and self.obj== "idle" and self.PecoBot== "4" and self.makingTrash== "makingTrash0" and self.throwingPlastic== "throwingPlastic0" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.human== "office" and self.Phuman== "1" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.states== "base" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.ecoBot== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PecoBot== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.PthrowingPlastic== "0" and self.human== "office" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "atRisk" and self.pickingUp== "pickingUp1f"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-11 - self.TIMEUNIT ] , [self.Chuman-self.Cobj, 3-(self.Chuman-self.CecoBot) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.Cobj-11 - self.TIMEUNIT ] , [-3- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.ecoBot== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PecoBot== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PpickingUp== "1" and self.PthrowingPlastic== "0" and self.human== "office" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "atRisk" and self.pickingUp== "pickingUp1f"  ):
						if ( (1<self.CecoBot and self.Chuman<11 and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=3 )  or  (1<self.CecoBot and 1<self.Chuman and self.Cobj<11 and self.CecoBot- self.Cobj<-3 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.ecoBot== "going_hallway_to_base" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "0" and self.PecoBot== "-32" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.ecoBot== "going_hallway_to_base" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "0" and self.PecoBot== "-32" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.human== "office"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "-32" and self.obj== "idle" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.human== "office" and self.states== "base" and self.PpaperBin== "2" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_hallway_to_base" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "-32" and self.obj== "idle" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.human== "office" and self.states== "base" and self.PpaperBin== "2" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_hallway_to_base" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic0"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "0" and self.ecoBot== "going_hallway_to_trashRoom" and self.PthrowingPaper== "2" and self.SpaperOrPlastic== "1" and self.states== "base" and self.PecoBot== "-34" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.PplasticBin== "4" and self.Phuman== "-11" and self.paperBin== "base" and self.PthrowingPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-36 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "0" and self.ecoBot== "going_hallway_to_trashRoom" and self.PthrowingPaper== "2" and self.SpaperOrPlastic== "1" and self.states== "base" and self.PecoBot== "-34" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.PplasticBin== "4" and self.Phuman== "-11" and self.paperBin== "base" and self.PthrowingPlastic== "0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<36 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "0" and self.paperBin== "base" and self.ecoBot== "base" and self.PpickingUp== "0" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.PplasticBin== "4" and self.PecoBot== "2" and self.PthrowingPaper== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash_initial_location" and self.throwingPaper== "throwingPaper0" and self.Phuman== "1" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "0" and self.paperBin== "base" and self.ecoBot== "base" and self.PpickingUp== "0" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.PplasticBin== "4" and self.PecoBot== "2" and self.PthrowingPaper== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash_initial_location" and self.throwingPaper== "throwingPaper0" and self.Phuman== "1" and self.states== "base"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.PpickingUp== "0" and self.PecoBot== "-13" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.ecoBot== "going_office_to_hallway" and self.obj== "idle" and self.PmakingTrash== "0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash_initial_location" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.PpickingUp== "0" and self.PecoBot== "-13" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.ecoBot== "going_office_to_hallway" and self.obj== "idle" and self.PmakingTrash== "0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash_initial_location" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "1" and self.throwingPlastic== "throwingPlastic0f_doing_plasticTrash" and self.PpickingUp== "2" and self.human== "doing_wait_in_office" and self.obj== "atRisk" and self.paperBin== "base" and self.PecoBot== "-11" and self.PmakingTrash== "3" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp2fs_fir_doing_plasticTrash" and self.throwingPaper== "throwingPaper0" and self.Phuman== "-11" and self.states== "base" and self.ecoBot== "doing_plasticTrash_in_office" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-8 - self.TIMEUNIT, self.Cobj-39 - self.TIMEUNIT, self.CecoBot-6 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj), self.Cobj-self.CecoBot ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "1" and self.throwingPlastic== "throwingPlastic0f_doing_plasticTrash" and self.PpickingUp== "2" and self.human== "doing_wait_in_office" and self.obj== "atRisk" and self.paperBin== "base" and self.PecoBot== "-11" and self.PmakingTrash== "3" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp2fs_fir_doing_plasticTrash" and self.throwingPaper== "throwingPaper0" and self.Phuman== "-11" and self.states== "base" and self.ecoBot== "doing_plasticTrash_in_office" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom"  ):
						if ( (5<self.CecoBot and self.Chuman<8 and self.Cobj<39 and self.CecoBot<=6 and self.Chuman- self.Cobj<-1 and self.CecoBot<=self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "plasticTrashDONE!", "doing_plasticTrash_in_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "-34" and self.Phuman== "1" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.obj== "idle" and self.makingTrash== "makingTrash_initial_location" and self.states== "base" and self.PmakingTrash== "0" and self.ecoBot== "going_hallway_to_trashRoom" and self.PthrowingPlastic== "0" and self.human== "office" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "-34" and self.Phuman== "1" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.obj== "idle" and self.makingTrash== "makingTrash_initial_location" and self.states== "base" and self.PmakingTrash== "0" and self.ecoBot== "going_hallway_to_trashRoom" and self.PthrowingPlastic== "0" and self.human== "office" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.ecoBot== "going_office_to_hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-13" and self.paperBin== "base" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Chuman-49 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.ecoBot== "going_office_to_hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-13" and self.paperBin== "base" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman<49 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "atRisk" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.PmakingTrash== "2" and self.human== "office" and self.pickingUp== "pickingUp0" and self.PpaperBin== "2" and self.paperBin== "base" and self.PecoBot== "-31" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.PthrowingPlastic== "2" and self.PpickingUp== "4" and self.ecoBot== "going_hallway_to_office" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-39 - self.TIMEUNIT, self.CecoBot-10 ] , [-16- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "atRisk" and self.makingTrash== "makingTrash1s" and self.Phuman== "1" and self.PmakingTrash== "2" and self.human== "office" and self.pickingUp== "pickingUp0" and self.PpaperBin== "2" and self.paperBin== "base" and self.PecoBot== "-31" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.PthrowingPlastic== "2" and self.PpickingUp== "4" and self.ecoBot== "going_hallway_to_office" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (9<self.CecoBot and self.Cobj<39 and self.CecoBot<=10 and self.CecoBot- self.Cobj<-16 and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "2" and self.PecoBot== "4" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.Phuman== "1" and self.ecoBot== "trashRoom" and self.obj== "idle" and self.PthrowingPaper== "2" and self.states== "base" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "2" and self.PecoBot== "4" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.Phuman== "1" and self.ecoBot== "trashRoom" and self.obj== "idle" and self.PthrowingPaper== "2" and self.states== "base" and self.PpickingUp== "0"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.PecoBot== "1" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.PpickingUp== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "atRisk" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.plasticBin== "trashRoom" and self.states== "base" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.ecoBot== "office" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.pickingUp== "pickingUp1f" and self.PthrowingPlastic== "2" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-34 - self.TIMEUNIT ] , [9-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-34 - self.TIMEUNIT ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.PecoBot== "1" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.PpickingUp== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "atRisk" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.plasticBin== "trashRoom" and self.states== "base" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.ecoBot== "office" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.pickingUp== "pickingUp1f" and self.PthrowingPlastic== "2" and self.Phuman== "1"  ):
						if ( (1<self.CecoBot and self.Chuman<34 and self.Chuman- self.CecoBot<=9 and self.Chuman==self.Cobj )  or  (1<self.Chuman and 1<self.CecoBot and self.Cobj<34 and self.CecoBot- self.Cobj<-9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "paperTrash!", "office", "doing_paperTrash_in_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash0" and self.obj== "idle" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.PmakingTrash== "1" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.paperBin== "base" and self.Phuman== "1" and self.states== "base" and self.human== "office" and self.PecoBot== "3" and self.ecoBot== "hallway"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash0" and self.obj== "idle" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.PmakingTrash== "1" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.paperBin== "base" and self.Phuman== "1" and self.states== "base" and self.human== "office" and self.PecoBot== "3" and self.ecoBot== "hallway"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "-11" and self.SpaperOrPlastic== "0" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-32" and self.states== "base" and self.paperBin== "base" and self.PpickingUp== "0" and self.ecoBot== "going_hallway_to_base" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0" and self.obj== "idle" and self.plasticBin== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "-11" and self.SpaperOrPlastic== "0" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-32" and self.states== "base" and self.paperBin== "base" and self.PpickingUp== "0" and self.ecoBot== "going_hallway_to_base" and self.PthrowingPaper== "2" and self.throwingPaper== "throwingPaper0" and self.obj== "idle" and self.plasticBin== "trashRoom"  ):
						if ( (12<self.CecoBot and self.Chuman<=55 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.ecoBot== "going_trashRoom_to_hallway" and self.PecoBot== "-43" and self.makingTrash== "makingTrash_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.obj== "idle" and self.PthrowingPlastic== "0" and self.PmakingTrash== "0" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.ecoBot== "going_trashRoom_to_hallway" and self.PecoBot== "-43" and self.makingTrash== "makingTrash_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.obj== "idle" and self.PthrowingPlastic== "0" and self.PmakingTrash== "0" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "3" and self.PpaperBin== "2" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.obj== "atRisk" and self.PecoBot== "2" and self.SpaperOrPlastic== "1" and self.ecoBot== "base" and self.pickingUp== "pickingUp1f" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-11 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "3" and self.PpaperBin== "2" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.obj== "atRisk" and self.PecoBot== "2" and self.SpaperOrPlastic== "1" and self.ecoBot== "base" and self.pickingUp== "pickingUp1f" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11"  ):
						if ( (1<self.CecoBot and self.Cobj<11 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "1" and self.obj== "idle" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.Phuman== "1" and self.ecoBot== "office" and self.makingTrash== "makingTrash1s" and self.PpickingUp== "0" and self.human== "office" and self.states== "base" and self.PthrowingPlastic== "0" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "1" and self.obj== "idle" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.Phuman== "1" and self.ecoBot== "office" and self.makingTrash== "makingTrash1s" and self.PpickingUp== "0" and self.human== "office" and self.states== "base" and self.PthrowingPlastic== "0" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "1" and self.paperBin== "base" and self.Phuman== "-11" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PpickingUp== "3" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp2fs_sec_doing_paperTrash" and self.PmakingTrash== "3" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0f_doing_paperTrash" and self.PecoBot== "-11" and self.obj== "atRisk" and self.ecoBot== "doing_paperTrash_in_office"   ):
				temps=set()
				temp0= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-39 - self.TIMEUNIT, self.CecoBot-6 ] , [self.Cobj-self.CecoBot, -1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "1" and self.paperBin== "base" and self.Phuman== "-11" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PpickingUp== "3" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp2fs_sec_doing_paperTrash" and self.PmakingTrash== "3" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0f_doing_paperTrash" and self.PecoBot== "-11" and self.obj== "atRisk" and self.ecoBot== "doing_paperTrash_in_office"  ):
						if ( (5<self.CecoBot and self.Cobj<39 and self.CecoBot<=6 and self.CecoBot<=self.Cobj and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "paperTrashDONE!", "doing_paperTrash_in_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.Phuman== "1" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_office_to_hallway" and self.throwingPlastic== "throwingPlastic0" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.states== "base" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-13"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.Phuman== "1" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_office_to_hallway" and self.throwingPlastic== "throwingPlastic0" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.states== "base" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-13"  ):
						if ( (1<self.Chuman and 9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.PecoBot== "-23" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.throwingPlastic== "throwingPlastic0" and self.ecoBot== "going_base_to_hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.paperBin== "base" and self.obj== "idle" and self.states== "base" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-19 - self.TIMEUNIT, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.PecoBot== "-23" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.throwingPlastic== "throwingPlastic0" and self.ecoBot== "going_base_to_hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.paperBin== "base" and self.obj== "idle" and self.states== "base" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.PplasticBin== "4"  ):
						if ( (12<self.CecoBot and self.Chuman<19 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.human== "doing_wait_in_office" and self.PplasticBin== "4" and self.Phuman== "-11" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.ecoBot== "going_hallway_to_trashRoom" and self.obj== "idle" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-34" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-32 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.human== "doing_wait_in_office" and self.PplasticBin== "4" and self.Phuman== "-11" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.ecoBot== "going_hallway_to_trashRoom" and self.obj== "idle" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-34" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<32 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "0" and self.Phuman== "-11" and self.ecoBot== "doing_throwPaper_in_base" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "3" and self.pickingUp== "pickingUp1f" and self.states== "base" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.PecoBot== "-22" and self.PpickingUp== "1" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-10 - self.TIMEUNIT, self.CecoBot-4 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "0" and self.Phuman== "-11" and self.ecoBot== "doing_throwPaper_in_base" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "3" and self.pickingUp== "pickingUp1f" and self.states== "base" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.PecoBot== "-22" and self.PpickingUp== "1" and self.PpaperBin== "2"  ):
						if ( (3<self.CecoBot and self.Cobj<10 and self.CecoBot<=4 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "1" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.human== "office" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PecoBot== "3" and self.obj== "atRisk" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp0" and self.PpickingUp== "4" and self.states== "base" and self.PmakingTrash== "2" and self.ecoBot== "hallway" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-30 - self.TIMEUNIT ] , [-15- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "1" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.human== "office" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PecoBot== "3" and self.obj== "atRisk" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp0" and self.PpickingUp== "4" and self.states== "base" and self.PmakingTrash== "2" and self.ecoBot== "hallway" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.PpaperBin== "2"  ):
						if ( (1<self.Chuman and 1<self.CecoBot and self.Cobj<30 and self.CecoBot- self.Cobj<-15 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "0" and self.PthrowingPaper== "0" and self.PmakingTrash== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.makingTrash== "makingTrash0" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.human== "office" and self.obj== "idle" and self.ecoBot== "going_office_to_hallway" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.PecoBot== "-13" and self.Phuman== "1" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "0" and self.PthrowingPaper== "0" and self.PmakingTrash== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.makingTrash== "makingTrash0" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.human== "office" and self.obj== "idle" and self.ecoBot== "going_office_to_hallway" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.PecoBot== "-13" and self.Phuman== "1" and self.states== "base"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "atRisk" and self.Phuman== "1" and self.ecoBot== "doing_throwPaper_in_base" and self.plasticBin== "trashRoom" and self.states== "base" and self.pickingUp== "pickingUp1f" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.human== "office" and self.PpickingUp== "1" and self.PmakingTrash== "2" and self.PthrowingPaper== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-22" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0s_doing_throwPaper"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4, self.Chuman-10 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "atRisk" and self.Phuman== "1" and self.ecoBot== "doing_throwPaper_in_base" and self.plasticBin== "trashRoom" and self.states== "base" and self.pickingUp== "pickingUp1f" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.human== "office" and self.PpickingUp== "1" and self.PmakingTrash== "2" and self.PthrowingPaper== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-22" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0s_doing_throwPaper"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 and self.Chuman<10 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PplasticBin== "4" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "0" and self.obj== "atRisk" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp1f" and self.PpickingUp== "1" and self.PthrowingPlastic== "0" and self.ecoBot== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "4" and self.states== "base" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "3" and self.human== "doing_wait_in_office"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-11 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PplasticBin== "4" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "0" and self.obj== "atRisk" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp1f" and self.PpickingUp== "1" and self.PthrowingPlastic== "0" and self.ecoBot== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "4" and self.states== "base" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "3" and self.human== "doing_wait_in_office"  ):
						if ( (1<self.CecoBot and self.Cobj<11 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.ecoBot== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PecoBot== "4" and self.states== "base" and self.human== "office" and self.PmakingTrash== "2" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.ecoBot== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PecoBot== "4" and self.states== "base" and self.human== "office" and self.PmakingTrash== "2" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "1"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "2" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.human== "office" and self.SpaperOrPlastic== "0" and self.states== "base" and self.PpickingUp== "1" and self.ecoBot== "going_hallway_to_trashRoom" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.PecoBot== "-34" and self.pickingUp== "pickingUp1f" and self.obj== "atRisk"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-10 - self.TIMEUNIT, self.CecoBot-13 ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "2" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.human== "office" and self.SpaperOrPlastic== "0" and self.states== "base" and self.PpickingUp== "1" and self.ecoBot== "going_hallway_to_trashRoom" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.PecoBot== "-34" and self.pickingUp== "pickingUp1f" and self.obj== "atRisk"  ):
						if ( (12<self.CecoBot and self.Chuman<10 and self.CecoBot<=13 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp2fs_fir_doing_plasticTrash" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic0f_doing_plasticTrash" and self.states== "base" and self.Phuman== "-11" and self.PecoBot== "-11" and self.ecoBot== "doing_plasticTrash_in_office" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "3" and self.PthrowingPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "2" and self.obj== "atRisk" and self.human== "doing_wait_in_office"   ):
				temps=set()
				temp0= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-6, self.Cobj-39 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj), self.Cobj-self.CecoBot ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp2fs_fir_doing_plasticTrash" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic0f_doing_plasticTrash" and self.states== "base" and self.Phuman== "-11" and self.PecoBot== "-11" and self.ecoBot== "doing_plasticTrash_in_office" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "3" and self.PthrowingPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "2" and self.obj== "atRisk" and self.human== "doing_wait_in_office"  ):
						if ( (5<self.CecoBot and self.CecoBot<=6 and self.Cobj<39 and self.Chuman- self.Cobj<-1 and self.CecoBot<=self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "plasticTrashDONE!", "doing_plasticTrash_in_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.SpaperOrPlastic== "1" and self.PpickingUp== "0" and self.human== "office" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "2" and self.ecoBot== "office" and self.obj== "idle" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "1" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.SpaperOrPlastic== "1" and self.PpickingUp== "0" and self.human== "office" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "2" and self.ecoBot== "office" and self.obj== "idle" and self.Phuman== "1" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "1" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.PpaperBin== "2"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp0" and self.PmakingTrash== "2" and self.PpickingUp== "4" and self.PthrowingPlastic== "0" and self.obj== "atRisk" and self.PthrowingPaper== "2" and self.PecoBot== "-13" and self.PpaperBin== "2" and self.human== "office" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.states== "base" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.ecoBot== "going_office_to_hallway" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-29 - self.TIMEUNIT, self.CecoBot-10 ] , [-6- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp0" and self.PmakingTrash== "2" and self.PpickingUp== "4" and self.PthrowingPlastic== "0" and self.obj== "atRisk" and self.PthrowingPaper== "2" and self.PecoBot== "-13" and self.PpaperBin== "2" and self.human== "office" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.states== "base" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.ecoBot== "going_office_to_hallway" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (9<self.CecoBot and self.Cobj<29 and self.CecoBot<=10 and self.CecoBot- self.Cobj<-6 and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "2" and self.PpickingUp== "1" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "0" and self.ecoBot== "going_office_to_hallway" and self.PpaperBin== "2" and self.Phuman== "1" and self.pickingUp== "pickingUp1f" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.obj== "atRisk" and self.PecoBot== "-13" and self.PplasticBin== "4" and self.states== "base" and self.human== "office" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-23 - self.TIMEUNIT, self.CecoBot-10 ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman), -10- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [10-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "2" and self.PpickingUp== "1" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "0" and self.ecoBot== "going_office_to_hallway" and self.PpaperBin== "2" and self.Phuman== "1" and self.pickingUp== "pickingUp1f" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.obj== "atRisk" and self.PecoBot== "-13" and self.PplasticBin== "4" and self.states== "base" and self.human== "office" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0"  ):
						if ( (9<self.CecoBot and self.Cobj<23 and self.CecoBot<=10 and self.CecoBot- self.Chuman<-1 and self.CecoBot- self.Cobj<-10 )  or  (9<self.CecoBot and self.CecoBot<=10 and self.Chuman- self.CecoBot<=10 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "3" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "1" and self.PpaperBin== "2" and self.paperBin== "base" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "office" and self.states== "base" and self.PpickingUp== "0" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-40 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "3" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "1" and self.PpaperBin== "2" and self.paperBin== "base" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "office" and self.states== "base" and self.PpickingUp== "0" and self.PplasticBin== "4"  ):
						if ( (1<self.CecoBot and self.Chuman<40 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.PecoBot== "-32" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper0" and self.PmakingTrash== "3" and self.human== "doing_wait_in_office" and self.Phuman== "-11" and self.ecoBot== "going_hallway_to_base" and self.states== "base" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.PecoBot== "-32" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper0" and self.PmakingTrash== "3" and self.human== "doing_wait_in_office" and self.Phuman== "-11" and self.ecoBot== "going_hallway_to_base" and self.states== "base" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.Phuman== "1" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.ecoBot== "office" and self.PpickingUp== "0" and self.PecoBot== "1" and self.throwingPaper== "throwingPaper0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.Phuman== "1" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.ecoBot== "office" and self.PpickingUp== "0" and self.PecoBot== "1" and self.throwingPaper== "throwingPaper0"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "going_trashRoom_to_hallway" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.Phuman== "1" and self.obj== "idle" and self.PpickingUp== "0" and self.PecoBot== "-43" and self.paperBin== "base" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "going_trashRoom_to_hallway" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.Phuman== "1" and self.obj== "idle" and self.PpickingUp== "0" and self.PecoBot== "-43" and self.paperBin== "base" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0" and self.states== "base"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.obj== "idle" and self.PpaperBin== "2" and self.paperBin== "base" and self.PplasticBin== "4" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "1" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_base_to_hallway" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash0" and self.human== "office" and self.PthrowingPaper== "0" and self.PecoBot== "-23" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.obj== "idle" and self.PpaperBin== "2" and self.paperBin== "base" and self.PplasticBin== "4" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "1" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_base_to_hallway" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash0" and self.human== "office" and self.PthrowingPaper== "0" and self.PecoBot== "-23" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.ecoBot== "going_trashRoom_to_hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.PecoBot== "-43" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.obj== "atRisk" and self.PplasticBin== "4" and self.states== "base" and self.PthrowingPlastic== "0" and self.PmakingTrash== "3" and self.PpickingUp== "1" and self.pickingUp== "pickingUp1f" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-23 - self.TIMEUNIT, self.CecoBot-13 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.ecoBot== "going_trashRoom_to_hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.PecoBot== "-43" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.obj== "atRisk" and self.PplasticBin== "4" and self.states== "base" and self.PthrowingPlastic== "0" and self.PmakingTrash== "3" and self.PpickingUp== "1" and self.pickingUp== "pickingUp1f" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (12<self.CecoBot and self.Cobj<23 and self.CecoBot<=13 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.obj== "idle" and self.makingTrash== "makingTrash_initial_location" and self.PplasticBin== "4" and self.states== "base" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.PthrowingPaper== "0" and self.PecoBot== "-44" and self.PmakingTrash== "0" and self.human== "office" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "3" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.obj== "idle" and self.makingTrash== "makingTrash_initial_location" and self.PplasticBin== "4" and self.states== "base" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.PthrowingPaper== "0" and self.PecoBot== "-44" and self.PmakingTrash== "0" and self.human== "office" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "3" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.PpaperBin== "2"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "2" and self.PpaperBin== "2" and self.Phuman== "-11" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.ecoBot== "base" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.obj== "idle" and self.paperBin== "base" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.states== "base" and self.human== "doing_wait_in_office"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-33 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "2" and self.PpaperBin== "2" and self.Phuman== "-11" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.ecoBot== "base" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.obj== "idle" and self.paperBin== "base" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.states== "base" and self.human== "doing_wait_in_office"  ):
						if ( (1<self.CecoBot and self.Chuman<33 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.human== "doing_wait_in_office" and self.ecoBot== "going_hallway_to_trashRoom" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "1" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.states== "base" and self.PthrowingPlastic== "0" and self.PecoBot== "-34" and self.PplasticBin== "4" and self.paperBin== "base" and self.Phuman== "-11"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-10 - self.TIMEUNIT, self.CecoBot-13 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.human== "doing_wait_in_office" and self.ecoBot== "going_hallway_to_trashRoom" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "1" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.states== "base" and self.PthrowingPlastic== "0" and self.PecoBot== "-34" and self.PplasticBin== "4" and self.paperBin== "base" and self.Phuman== "-11"  ):
						if ( (12<self.CecoBot and self.Cobj<10 and self.CecoBot<=13 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.states== "base" and self.human== "doing_wait_in_office" and self.PecoBot== "1" and self.ecoBot== "office" and self.pickingUp== "pickingUp1f" and self.obj== "atRisk" and self.SpaperOrPlastic== "1" and self.Phuman== "-11" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.PpickingUp== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-34 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.states== "base" and self.human== "doing_wait_in_office" and self.PecoBot== "1" and self.ecoBot== "office" and self.pickingUp== "pickingUp1f" and self.obj== "atRisk" and self.SpaperOrPlastic== "1" and self.Phuman== "-11" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.PpickingUp== "1"  ):
						if ( (1<self.CecoBot and self.Cobj<34 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "paperTrash!", "office", "doing_paperTrash_in_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.ecoBot== "base" and self.states== "base" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.human== "office" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.PpickingUp== "0" and self.PmakingTrash== "2" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.PthrowingPaper== "2" and self.PecoBot== "2" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.ecoBot== "base" and self.states== "base" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.human== "office" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.PpickingUp== "0" and self.PmakingTrash== "2" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPlastic== "2" and self.PthrowingPaper== "2" and self.PecoBot== "2" and self.PplasticBin== "4"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.makingTrash== "makingTrash_initial_location" and self.human== "office" and self.paperBin== "base" and self.states== "base" and self.PplasticBin== "4" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PecoBot== "-44" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.PthrowingPlastic== "3" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.PmakingTrash== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.makingTrash== "makingTrash_initial_location" and self.human== "office" and self.paperBin== "base" and self.states== "base" and self.PplasticBin== "4" and self.obj== "idle" and self.PthrowingPaper== "0" and self.PecoBot== "-44" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.PthrowingPlastic== "3" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.PmakingTrash== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.makingTrash== "makingTrash_initial_location" and self.PecoBot== "-31" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.PmakingTrash== "0" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.states== "base" and self.ecoBot== "going_hallway_to_office" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.obj== "idle" and self.human== "office" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.makingTrash== "makingTrash_initial_location" and self.PecoBot== "-31" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.PmakingTrash== "0" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.states== "base" and self.ecoBot== "going_hallway_to_office" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.obj== "idle" and self.human== "office" and self.PpickingUp== "0"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.PplasticBin== "4" and self.pickingUp== "pickingUp1f" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PpickingUp== "1" and self.Phuman== "1" and self.obj== "atRisk" and self.PthrowingPlastic== "0" and self.PecoBot== "3" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash1s" and self.states== "base" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-24 - self.TIMEUNIT ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-24 - self.TIMEUNIT ] , [9-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.PplasticBin== "4" and self.pickingUp== "pickingUp1f" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PpickingUp== "1" and self.Phuman== "1" and self.obj== "atRisk" and self.PthrowingPlastic== "0" and self.PecoBot== "3" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash1s" and self.states== "base" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom" and self.PpaperBin== "2"  ):
						if ( (1<self.Chuman and 1<self.CecoBot and self.Cobj<24 and self.CecoBot- self.Cobj<-9 )  or  (1<self.CecoBot and self.Chuman<24 and self.Chuman- self.CecoBot<=9 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.SpaperOrPlastic== "0" and self.states== "base" and self.ecoBot== "going_hallway_to_trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "2" and self.PpickingUp== "0" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.PecoBot== "-34" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.human== "office" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.Phuman== "1" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.SpaperOrPlastic== "0" and self.states== "base" and self.ecoBot== "going_hallway_to_trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "2" and self.PpickingUp== "0" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.PecoBot== "-34" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.human== "office" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.Phuman== "1" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "0" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.obj== "idle" and self.human== "office" and self.paperBin== "base" and self.Phuman== "1" and self.PecoBot== "-43" and self.makingTrash== "makingTrash_initial_location" and self.ecoBot== "going_trashRoom_to_hallway" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "0" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.obj== "idle" and self.human== "office" and self.paperBin== "base" and self.Phuman== "1" and self.PecoBot== "-43" and self.makingTrash== "makingTrash_initial_location" and self.ecoBot== "going_trashRoom_to_hallway" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "1" and self.PthrowingPlastic== "0" and self.PpickingUp== "0" and self.human== "office" and self.obj== "idle" and self.Phuman== "1" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash0" and self.PthrowingPaper== "0" and self.ecoBot== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.states== "base" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "1" and self.PthrowingPlastic== "0" and self.PpickingUp== "0" and self.human== "office" and self.obj== "idle" and self.Phuman== "1" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash0" and self.PthrowingPaper== "0" and self.ecoBot== "base"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "0" and self.PecoBot== "1" and self.human== "office" and self.PthrowingPlastic== "2" and self.ecoBot== "office" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "2" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.pickingUp== "pickingUp0" and self.paperBin== "base" and self.obj== "atRisk" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PpickingUp== "4" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-40 ] , [-5- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "0" and self.PecoBot== "1" and self.human== "office" and self.PthrowingPlastic== "2" and self.ecoBot== "office" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "2" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.pickingUp== "pickingUp0" and self.paperBin== "base" and self.obj== "atRisk" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PpickingUp== "4" and self.PplasticBin== "4"  ):
						if ( (1<self.Chuman and 1<self.CecoBot and self.Cobj<=40 and self.CecoBot- self.Cobj<-5 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "officeClean!", "office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "going_hallway_to_office" and self.PthrowingPaper== "2" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.states== "base" and self.throwingPlastic== "throwingPlastic0" and self.human== "office" and self.PpaperBin== "2" and self.obj== "idle" and self.Phuman== "1" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "-31" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "going_hallway_to_office" and self.PthrowingPaper== "2" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.states== "base" and self.throwingPlastic== "throwingPlastic0" and self.human== "office" and self.PpaperBin== "2" and self.obj== "idle" and self.Phuman== "1" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "-31" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1"  ):
						if ( (9<self.CecoBot and 1<self.Chuman and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "4" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.throwingPlastic== "throwingPlastic0" and self.ecoBot== "going_hallway_to_office" and self.plasticBin== "trashRoom" and self.PecoBot== "-31" and self.paperBin== "base" and self.PplasticBin== "4" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "0" and self.PthrowingPaper== "2" and self.PmakingTrash== "2" and self.Phuman== "1" and self.obj== "atRisk" and self.PpaperBin== "2" and self.states== "base" and self.pickingUp== "pickingUp0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-39 - self.TIMEUNIT, self.CecoBot-10 ] , [-16- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "4" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.throwingPlastic== "throwingPlastic0" and self.ecoBot== "going_hallway_to_office" and self.plasticBin== "trashRoom" and self.PecoBot== "-31" and self.paperBin== "base" and self.PplasticBin== "4" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "0" and self.PthrowingPaper== "2" and self.PmakingTrash== "2" and self.Phuman== "1" and self.obj== "atRisk" and self.PpaperBin== "2" and self.states== "base" and self.pickingUp== "pickingUp0"  ):
						if ( (9<self.CecoBot and self.Cobj<39 and self.CecoBot<=10 and self.CecoBot- self.Cobj<-16 and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "office" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.PecoBot== "1" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.Phuman== "-11" and self.PplasticBin== "4" and self.states== "base" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-10 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "office" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.PecoBot== "1" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.Phuman== "-11" and self.PplasticBin== "4" and self.states== "base" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "2"  ):
						if ( (1<self.CecoBot and self.Chuman<10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "2" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "-13" and self.ecoBot== "going_office_to_hallway"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-19 - self.TIMEUNIT, self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "2" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "-13" and self.ecoBot== "going_office_to_hallway"  ):
						if ( (9<self.CecoBot and self.Chuman<19 and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PplasticBin== "4" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.states== "base" and self.PthrowingPaper== "0" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PecoBot== "-13" and self.ecoBot== "going_office_to_hallway" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.makingTrash== "makingTrash1s"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PplasticBin== "4" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.states== "base" and self.PthrowingPaper== "0" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PecoBot== "-13" and self.ecoBot== "going_office_to_hallway" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.makingTrash== "makingTrash1s"  ):
						if ( (9<self.CecoBot and 1<self.Chuman and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_base" and self.throwingPaper== "throwingPaper0" and self.Phuman== "-11" and self.states== "base" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp1f" and self.PecoBot== "-32" and self.SpaperOrPlastic== "1" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.obj== "atRisk" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PmakingTrash== "3"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-6 - self.TIMEUNIT, self.CecoBot-13 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_base" and self.throwingPaper== "throwingPaper0" and self.Phuman== "-11" and self.states== "base" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp1f" and self.PecoBot== "-32" and self.SpaperOrPlastic== "1" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.obj== "atRisk" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PmakingTrash== "3"  ):
						if ( (12<self.CecoBot and self.Cobj<6 and self.CecoBot<=13 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.PmakingTrash== "2" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-23" and self.ecoBot== "going_base_to_hallway" and self.Phuman== "1" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.states== "base" and self.PmakingTrash== "2" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-23" and self.ecoBot== "going_base_to_hallway" and self.Phuman== "1" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.obj== "idle"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.PecoBot== "-23" and self.states== "base" and self.ecoBot== "going_base_to_hallway" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "0" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-19 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.PecoBot== "-23" and self.states== "base" and self.ecoBot== "going_base_to_hallway" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "0" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<19 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp2fs_fir_doing_plasticTrash" and self.PecoBot== "-11" and self.PpickingUp== "2" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "1" and self.Phuman== "1" and self.states== "base" and self.throwingPlastic== "throwingPlastic0f_doing_plasticTrash" and self.ecoBot== "doing_plasticTrash_in_office" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.obj== "atRisk"   ):
				temps=set()
				temp0= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-39 - self.TIMEUNIT, self.CecoBot-6 ] , [-10- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-6 ] , [self.Chuman-self.CecoBot, 10-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp2fs_fir_doing_plasticTrash" and self.PecoBot== "-11" and self.PpickingUp== "2" and self.human== "office" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "1" and self.Phuman== "1" and self.states== "base" and self.throwingPlastic== "throwingPlastic0f_doing_plasticTrash" and self.ecoBot== "doing_plasticTrash_in_office" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.PplasticBin== "4" and self.obj== "atRisk"  ):
						if ( (5<self.CecoBot and self.Cobj<39 and self.CecoBot<=6 and self.CecoBot- self.Cobj<-10 and self.CecoBot- self.Chuman<-1 )  or  (5<self.CecoBot and self.CecoBot<=6 and self.CecoBot<=self.Chuman and self.Chuman- self.CecoBot<=10 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "plasticTrashDONE!", "doing_plasticTrash_in_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "1" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.PpaperBin== "2" and self.obj== "atRisk" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PthrowingPaper== "3" and self.states== "base" and self.pickingUp== "pickingUp1f" and self.ecoBot== "doing_throwPaper_in_base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.human== "office" and self.PecoBot== "-22" and self.throwingPaper== "throwingPaper0s_doing_throwPaper"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4, self.Chuman-10 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "1" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.paperBin== "base" and self.PpaperBin== "2" and self.obj== "atRisk" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PthrowingPaper== "3" and self.states== "base" and self.pickingUp== "pickingUp1f" and self.ecoBot== "doing_throwPaper_in_base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.human== "office" and self.PecoBot== "-22" and self.throwingPaper== "throwingPaper0s_doing_throwPaper"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 and self.Chuman<10 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.PecoBot== "-43" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.states== "base" and self.obj== "idle" and self.human== "doing_wait_in_office" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.ecoBot== "going_trashRoom_to_hallway"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-19 - self.TIMEUNIT, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.PecoBot== "-43" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.states== "base" and self.obj== "idle" and self.human== "doing_wait_in_office" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.ecoBot== "going_trashRoom_to_hallway"  ):
						if ( (12<self.CecoBot and self.Chuman<19 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.ecoBot== "hallway" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.states== "base" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.human== "office" and self.PecoBot== "3" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "1" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.ecoBot== "hallway" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.states== "base" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0" and self.human== "office" and self.PecoBot== "3" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "1" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.human== "office" and self.SpaperOrPlastic== "0" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.ecoBot== "going_office_to_hallway" and self.plasticBin== "trashRoom" and self.PecoBot== "-13" and self.states== "base" and self.makingTrash== "makingTrash_initial_location" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PmakingTrash== "0" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.human== "office" and self.SpaperOrPlastic== "0" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.ecoBot== "going_office_to_hallway" and self.plasticBin== "trashRoom" and self.PecoBot== "-13" and self.states== "base" and self.makingTrash== "makingTrash_initial_location" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PmakingTrash== "0" and self.PpickingUp== "0"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "4" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "trashRoom" and self.PthrowingPlastic== "2" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-33 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "4" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "trashRoom" and self.PthrowingPlastic== "2" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3"  ):
						if ( (1<self.CecoBot and self.Chuman<33 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.ecoBot== "doing_throwPaper_in_base" and self.human== "office" and self.SpaperOrPlastic== "0" and self.states== "base" and self.PpickingUp== "0" and self.paperBin== "base" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-22" and self.makingTrash== "makingTrash0" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.PmakingTrash== "1" and self.PthrowingPaper== "3" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.ecoBot== "doing_throwPaper_in_base" and self.human== "office" and self.SpaperOrPlastic== "0" and self.states== "base" and self.PpickingUp== "0" and self.paperBin== "base" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-22" and self.makingTrash== "makingTrash0" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.PmakingTrash== "1" and self.PthrowingPaper== "3" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.obj== "idle"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.states== "base" and self.PmakingTrash== "3" and self.PecoBot== "-34" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_hallway_to_trashRoom" and self.PplasticBin== "4" and self.Phuman== "-11" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.states== "base" and self.PmakingTrash== "3" and self.PecoBot== "-34" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_hallway_to_trashRoom" and self.PplasticBin== "4" and self.Phuman== "-11" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.human== "office" and self.states== "base" and self.ecoBot== "going_hallway_to_base" and self.obj== "idle" and self.Phuman== "1" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.makingTrash== "makingTrash_initial_location" and self.PthrowingPaper== "2" and self.PpickingUp== "0" and self.PmakingTrash== "0" and self.PthrowingPlastic== "0" and self.PecoBot== "-32" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.human== "office" and self.states== "base" and self.ecoBot== "going_hallway_to_base" and self.obj== "idle" and self.Phuman== "1" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.makingTrash== "makingTrash_initial_location" and self.PthrowingPaper== "2" and self.PpickingUp== "0" and self.PmakingTrash== "0" and self.PthrowingPlastic== "0" and self.PecoBot== "-32" and self.SpaperOrPlastic== "0" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.states== "base" and self.ecoBot== "hallway" and self.obj== "idle" and self.human== "office" and self.PecoBot== "3" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.states== "base" and self.ecoBot== "hallway" and self.obj== "idle" and self.human== "office" and self.PecoBot== "3" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.SpaperOrPlastic== "1"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.states== "base" and self.PthrowingPaper== "0" and self.ecoBot== "office" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "1" and self.paperBin== "base" and self.human== "office" and self.Phuman== "1" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.states== "base" and self.PthrowingPaper== "0" and self.ecoBot== "office" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "1" and self.paperBin== "base" and self.human== "office" and self.Phuman== "1" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.SpaperOrPlastic== "0" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.PecoBot== "-13" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "going_office_to_hallway" and self.plasticBin== "trashRoom" and self.human== "office" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0" and self.PpickingUp== "0" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.SpaperOrPlastic== "0" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.PecoBot== "-13" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "going_office_to_hallway" and self.plasticBin== "trashRoom" and self.human== "office" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.PthrowingPlastic== "0" and self.PpickingUp== "0" and self.PpaperBin== "2"  ):
						if ( (1<self.Chuman and 9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PplasticBin== "4" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.PpaperBin== "2" and self.ecoBot== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "atRisk" and self.PpickingUp== "1" and self.PecoBot== "4" and self.human== "doing_wait_in_office" and self.PthrowingPlastic== "0" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-11 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PplasticBin== "4" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.PpaperBin== "2" and self.ecoBot== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "atRisk" and self.PpickingUp== "1" and self.PecoBot== "4" and self.human== "doing_wait_in_office" and self.PthrowingPlastic== "0" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1"  ):
						if ( (1<self.CecoBot and self.Cobj<11 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.throwingPaper== "throwingPaper0" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.PthrowingPaper== "2" and self.PecoBot== "4" and self.paperBin== "base" and self.PplasticBin== "4" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.states== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-33 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.throwingPaper== "throwingPaper0" and self.human== "doing_wait_in_office" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.PthrowingPaper== "2" and self.PecoBot== "4" and self.paperBin== "base" and self.PplasticBin== "4" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.SpaperOrPlastic== "1" and self.states== "base"  ):
						if ( (1<self.CecoBot and self.Chuman<33 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.Phuman== "1" and self.PecoBot== "-22" and self.ecoBot== "doing_throwPaper_in_base" and self.states== "base" and self.SpaperOrPlastic== "1" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.human== "office" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "3" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "1" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.Phuman== "1" and self.PecoBot== "-22" and self.ecoBot== "doing_throwPaper_in_base" and self.states== "base" and self.SpaperOrPlastic== "1" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.human== "office" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "3" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "1" and self.PplasticBin== "4"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "1" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.human== "office" and self.states== "base" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.ecoBot== "office" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "1" and self.plasticBin== "trashRoom" and self.PpickingUp== "0" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.human== "office" and self.states== "base" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.ecoBot== "office" and self.PthrowingPaper== "0"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_office2hallway!", "office", "going_office_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.PecoBot== "3" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "hallway" and self.Phuman== "1" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.states== "base" and self.obj== "idle" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.PmakingTrash== "1" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.PecoBot== "3" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "hallway" and self.Phuman== "1" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.states== "base" and self.obj== "idle" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.PmakingTrash== "1" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "0" and self.makingTrash== "makingTrash0"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp1f" and self.human== "doing_wait_in_office" and self.PmakingTrash== "3" and self.obj== "atRisk" and self.PthrowingPlastic== "0" and self.PpickingUp== "1" and self.PecoBot== "-32" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.Phuman== "-11" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_hallway_to_base" and self.makingTrash== "makingTrash1s_sec_doing_wait"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-10 - self.TIMEUNIT, self.CecoBot-13 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp1f" and self.human== "doing_wait_in_office" and self.PmakingTrash== "3" and self.obj== "atRisk" and self.PthrowingPlastic== "0" and self.PpickingUp== "1" and self.PecoBot== "-32" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PplasticBin== "4" and self.Phuman== "-11" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_hallway_to_base" and self.makingTrash== "makingTrash1s_sec_doing_wait"  ):
						if ( (12<self.CecoBot and self.Cobj<10 and self.CecoBot<=13 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "1" and self.PpaperBin== "2" and self.obj== "idle" and self.human== "office" and self.PthrowingPlastic== "3" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash0" and self.states== "base" and self.paperBin== "base" and self.PecoBot== "-44" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "1" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "1" and self.PpaperBin== "2" and self.obj== "idle" and self.human== "office" and self.PthrowingPlastic== "3" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash0" and self.states== "base" and self.paperBin== "base" and self.PecoBot== "-44" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "1" and self.PthrowingPaper== "0"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "0" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.Phuman== "-11" and self.states== "base" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PmakingTrash== "3" and self.ecoBot== "going_office_to_hallway" and self.PecoBot== "-13"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-49 - self.TIMEUNIT, self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "0" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.Phuman== "-11" and self.states== "base" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PmakingTrash== "3" and self.ecoBot== "going_office_to_hallway" and self.PecoBot== "-13"  ):
						if ( (9<self.CecoBot and self.Chuman<49 and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp0" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.states== "base" and self.PecoBot== "1" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.ecoBot== "office" and self.PmakingTrash== "3" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-40, self.Chuman-9 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj), -5- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp0" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.states== "base" and self.PecoBot== "1" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.ecoBot== "office" and self.PmakingTrash== "3" and self.obj== "atRisk" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpickingUp== "4"  ):
						if ( (1<self.CecoBot and self.Cobj<=40 and self.Chuman<9 and self.Chuman- self.Cobj<-1 and self.CecoBot- self.Cobj<-5 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "officeClean!", "office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_hallway_to_office" and self.PpickingUp== "0" and self.Phuman== "-11" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-31" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "doing_wait_in_office" and self.PthrowingPlastic== "2" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Chuman-39 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_hallway_to_office" and self.PpickingUp== "0" and self.Phuman== "-11" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-31" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "doing_wait_in_office" and self.PthrowingPlastic== "2" and self.obj== "idle"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman<39 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.PecoBot== "4" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.human== "office" and self.PmakingTrash== "1" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash0" and self.obj== "idle" and self.ecoBot== "trashRoom" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.PecoBot== "4" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.human== "office" and self.PmakingTrash== "1" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash0" and self.obj== "idle" and self.ecoBot== "trashRoom" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.SpaperOrPlastic== "1"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "-11" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.PecoBot== "-13" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "3" and self.states== "base" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.PpickingUp== "0" and self.ecoBot== "going_office_to_hallway" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "-11" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.PecoBot== "-13" and self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "doing_wait_in_office" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "3" and self.states== "base" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.PpickingUp== "0" and self.ecoBot== "going_office_to_hallway" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "atRisk" and self.states== "base" and self.ecoBot== "base" and self.pickingUp== "pickingUp1f" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.Phuman== "1" and self.PplasticBin== "4" and self.PpickingUp== "1" and self.PecoBot== "2" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-11 - self.TIMEUNIT ] , [-3- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-11 - self.TIMEUNIT ] , [self.Chuman-self.Cobj, 3-(self.Chuman-self.CecoBot) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "atRisk" and self.states== "base" and self.ecoBot== "base" and self.pickingUp== "pickingUp1f" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.Phuman== "1" and self.PplasticBin== "4" and self.PpickingUp== "1" and self.PecoBot== "2" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (1<self.Chuman and 1<self.CecoBot and self.Cobj<11 and self.CecoBot- self.Cobj<-3 )  or  (1<self.CecoBot and self.Chuman<11 and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=3 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "1" and self.PmakingTrash== "2" and self.human== "office" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.obj== "atRisk" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_office" and self.PthrowingPlastic== "2" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.PecoBot== "-31"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [10-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-33 - self.TIMEUNIT, self.CecoBot-10 ] , [-10- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "1" and self.PmakingTrash== "2" and self.human== "office" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.obj== "atRisk" and self.PplasticBin== "4" and self.ecoBot== "going_hallway_to_office" and self.PthrowingPlastic== "2" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.PecoBot== "-31"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman- self.CecoBot<=10 and self.Chuman==self.Cobj )  or  (9<self.CecoBot and self.Cobj<33 and self.CecoBot<=10 and self.CecoBot- self.Cobj<-10 and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "0" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.Phuman== "1" and self.states== "base" and self.PplasticBin== "4" and self.pickingUp== "pickingUp1f" and self.PecoBot== "-32" and self.ecoBot== "going_hallway_to_base" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-6 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "0" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.human== "office" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.Phuman== "1" and self.states== "base" and self.PplasticBin== "4" and self.pickingUp== "pickingUp1f" and self.PecoBot== "-32" and self.ecoBot== "going_hallway_to_base" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.SpaperOrPlastic== "1"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<6 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.ecoBot== "going_trashRoom_to_hallway" and self.PecoBot== "-43" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.obj== "idle" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.states== "base" and self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-49 - self.TIMEUNIT, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PthrowingPaper== "0" and self.ecoBot== "going_trashRoom_to_hallway" and self.PecoBot== "-43" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.obj== "idle" and self.PthrowingPlastic== "2" and self.Phuman== "-11" and self.states== "base" and self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic0"  ):
						if ( (12<self.CecoBot and self.Chuman<49 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.paperBin== "base" and self.PecoBot== "3" and self.Phuman== "-11" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.obj== "idle" and self.ecoBot== "hallway"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-20 - self.TIMEUNIT ] , [self.Chuman-self.CecoBot, 13-(self.Chuman-self.CecoBot) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-20 - self.TIMEUNIT ] , [-13- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp1 >= 0):
					temps.add(temp1)
				temp2= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-20 - self.TIMEUNIT ] , [self.CecoBot+ self.TIMEUNIT-self.Chuman ])
				if (temp2 >= 0):
					temps.add(temp2)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "2" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.paperBin== "base" and self.PecoBot== "3" and self.Phuman== "-11" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.obj== "idle" and self.ecoBot== "hallway"  ):
						if ( (1<self.CecoBot and self.Chuman<20 and self.CecoBot<=self.Chuman and self.Chuman- self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2base!", "hallway", "going_hallway_to_base")
						if ( (1<self.CecoBot and self.Chuman<20 and self.CecoBot- self.Chuman<-13 )  or  (1<self.CecoBot and self.Chuman<20 and self.Chuman<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_hallway_to_office" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "0" and self.states== "base" and self.paperBin== "base" and self.obj== "idle" and self.PmakingTrash== "2" and self.Phuman== "1" and self.human== "office" and self.PecoBot== "-31" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.PthrowingPlastic== "2" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_hallway_to_office" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.SpaperOrPlastic== "0" and self.states== "base" and self.paperBin== "base" and self.obj== "idle" and self.PmakingTrash== "2" and self.Phuman== "1" and self.human== "office" and self.PecoBot== "-31" and self.PpickingUp== "0"  ):
						if ( (9<self.CecoBot and 1<self.Chuman and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "1" and self.throwingPlastic== "throwingPlastic0" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "2" and self.ecoBot== "going_hallway_to_office" and self.obj== "idle" and self.PecoBot== "-31" and self.PpaperBin== "2" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper0" and self.PmakingTrash== "2" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "1" and self.throwingPlastic== "throwingPlastic0" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "2" and self.ecoBot== "going_hallway_to_office" and self.obj== "idle" and self.PecoBot== "-31" and self.PpaperBin== "2" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper0" and self.PmakingTrash== "2" and self.human== "office"  ):
						if ( (1<self.Chuman and 9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.human== "office" and self.obj== "idle" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "3" and self.Phuman== "1" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-44" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.PplasticBin== "4" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.human== "office" and self.obj== "idle" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "3" and self.Phuman== "1" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-44" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.PplasticBin== "4" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1"  ):
						if ( (1<self.Chuman and 3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "going_hallway_to_trashRoom" and self.human== "office" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PecoBot== "-34" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "going_hallway_to_trashRoom" and self.human== "office" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PecoBot== "-34" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.PthrowingPaper== "2" and self.Phuman== "1"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "1" and self.states== "base" and self.PecoBot== "-32" and self.human== "office" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PpickingUp== "0" and self.obj== "idle" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "going_hallway_to_base" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "1" and self.states== "base" and self.PecoBot== "-32" and self.human== "office" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PpickingUp== "0" and self.obj== "idle" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.ecoBot== "going_hallway_to_base" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic0" and self.ecoBot== "going_office_to_hallway" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.Phuman== "1" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.PecoBot== "-13" and self.human== "office" and self.paperBin== "base" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic0" and self.ecoBot== "going_office_to_hallway" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "0" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.PthrowingPlastic== "2" and self.Phuman== "1" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.PecoBot== "-13" and self.human== "office" and self.paperBin== "base" and self.SpaperOrPlastic== "0"  ):
						if ( (9<self.CecoBot and 1<self.Chuman and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-13" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.human== "office" and self.paperBin== "base" and self.PplasticBin== "4" and self.ecoBot== "going_office_to_hallway" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-13" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.human== "office" and self.paperBin== "base" and self.PplasticBin== "4" and self.ecoBot== "going_office_to_hallway" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.Phuman== "1"  ):
						if ( (1<self.Chuman and 9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.obj== "idle" and self.PpickingUp== "0" and self.paperBin== "base" and self.ecoBot== "going_base_to_hallway" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-23" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-49 - self.TIMEUNIT, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.obj== "idle" and self.PpickingUp== "0" and self.paperBin== "base" and self.ecoBot== "going_base_to_hallway" and self.Phuman== "-11" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "0" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-23" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait"  ):
						if ( (12<self.CecoBot and self.Chuman<49 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "1" and self.PplasticBin== "4" and self.obj== "atRisk" and self.ecoBot== "going_hallway_to_office" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.states== "base" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "2" and self.PmakingTrash== "2" and self.PecoBot== "-31" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp0" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.human== "office" and self.PpickingUp== "4"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-39 - self.TIMEUNIT, self.CecoBot-10 ] , [-16- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "1" and self.PplasticBin== "4" and self.obj== "atRisk" and self.ecoBot== "going_hallway_to_office" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.states== "base" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "2" and self.PmakingTrash== "2" and self.PecoBot== "-31" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp0" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.human== "office" and self.PpickingUp== "4"  ):
						if ( (9<self.CecoBot and self.Cobj<39 and self.CecoBot<=10 and self.CecoBot- self.Cobj<-16 and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.human== "doing_wait_in_office" and self.PthrowingPaper== "2" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-44" and self.PthrowingPlastic== "3" and self.obj== "idle" and self.paperBin== "base" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.Phuman== "-11" and self.ecoBot== "doing_throwPlastic_in_trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-36 - self.TIMEUNIT, self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.human== "doing_wait_in_office" and self.PthrowingPaper== "2" and self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PecoBot== "-44" and self.PthrowingPlastic== "3" and self.obj== "idle" and self.paperBin== "base" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.Phuman== "-11" and self.ecoBot== "doing_throwPlastic_in_trashRoom"  ):
						if ( (3<self.CecoBot and self.Chuman<36 and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "1" and self.Phuman== "1" and self.pickingUp== "pickingUp1f" and self.PecoBot== "-23" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.ecoBot== "going_base_to_hallway" and self.throwingPaper== "throwingPaper_initial_location" and self.plasticBin== "trashRoom" and self.obj== "atRisk" and self.human== "office" and self.PpaperBin== "2" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Cobj-23 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman), -4- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [self.Chuman-self.Cobj, 4-(self.Chuman-self.CecoBot) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.PthrowingPlastic== "0" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "1" and self.Phuman== "1" and self.pickingUp== "pickingUp1f" and self.PecoBot== "-23" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.ecoBot== "going_base_to_hallway" and self.throwingPaper== "throwingPaper_initial_location" and self.plasticBin== "trashRoom" and self.obj== "atRisk" and self.human== "office" and self.PpaperBin== "2" and self.PplasticBin== "4"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Cobj<23 and self.CecoBot- self.Chuman<-1 and self.CecoBot- self.Cobj<-4 )  or  (12<self.CecoBot and self.CecoBot<=13 and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "-11" and self.obj== "atRisk" and self.paperBin== "base" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.pickingUp== "pickingUp1f" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "3" and self.ecoBot== "hallway" and self.SpaperOrPlastic== "0" and self.PecoBot== "3" and self.PthrowingPlastic== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-24 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "-11" and self.obj== "atRisk" and self.paperBin== "base" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.pickingUp== "pickingUp1f" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "3" and self.ecoBot== "hallway" and self.SpaperOrPlastic== "0" and self.PecoBot== "3" and self.PthrowingPlastic== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait"  ):
						if ( (1<self.CecoBot and self.Cobj<24 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.Phuman== "-11" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "-31" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.obj== "idle" and self.PthrowingPlastic== "2" and self.states== "base" and self.ecoBot== "going_hallway_to_office" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-9 - self.TIMEUNIT, self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.Phuman== "-11" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "-31" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.obj== "idle" and self.PthrowingPlastic== "2" and self.states== "base" and self.ecoBot== "going_hallway_to_office" and self.PpickingUp== "0"  ):
						if ( (9<self.CecoBot and self.Chuman<9 and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.PecoBot== "-32" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PpickingUp== "0" and self.Phuman== "1" and self.ecoBot== "going_hallway_to_base" and self.human== "office" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "2" and self.obj== "idle" and self.PmakingTrash== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.PecoBot== "-32" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PpickingUp== "0" and self.Phuman== "1" and self.ecoBot== "going_hallway_to_base" and self.human== "office" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "2" and self.obj== "idle" and self.PmakingTrash== "2" and self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "0" and self.ecoBot== "going_hallway_to_trashRoom" and self.paperBin== "base" and self.PmakingTrash== "2" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.human== "office" and self.PplasticBin== "4" and self.obj== "atRisk" and self.PecoBot== "-34" and self.SpaperOrPlastic== "0" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.pickingUp== "pickingUp1f" and self.PpickingUp== "1"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-6 - self.TIMEUNIT, self.CecoBot-13 ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "0" and self.ecoBot== "going_hallway_to_trashRoom" and self.paperBin== "base" and self.PmakingTrash== "2" and self.states== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "2" and self.human== "office" and self.PplasticBin== "4" and self.obj== "atRisk" and self.PecoBot== "-34" and self.SpaperOrPlastic== "0" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.pickingUp== "pickingUp1f" and self.PpickingUp== "1"  ):
						if ( (12<self.CecoBot and self.Chuman<6 and self.CecoBot<=13 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.PthrowingPlastic== "0" and self.PecoBot== "2" and self.PpaperBin== "2" and self.ecoBot== "base" and self.PpickingUp== "0" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.throwingPaper== "throwingPaper0" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.PthrowingPlastic== "0" and self.PecoBot== "2" and self.PpaperBin== "2" and self.ecoBot== "base" and self.PpickingUp== "0" and self.PplasticBin== "4"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.PecoBot== "-34" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash_initial_location" and self.PpickingUp== "0" and self.Phuman== "1" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.states== "base" and self.human== "office" and self.throwingPlastic== "throwingPlastic0" and self.obj== "idle" and self.PmakingTrash== "0" and self.ecoBot== "going_hallway_to_trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.PecoBot== "-34" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash_initial_location" and self.PpickingUp== "0" and self.Phuman== "1" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location" and self.paperBin== "base" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.states== "base" and self.human== "office" and self.throwingPlastic== "throwingPlastic0" and self.obj== "idle" and self.PmakingTrash== "0" and self.ecoBot== "going_hallway_to_trashRoom"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "atRisk" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "base" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PecoBot== "2" and self.pickingUp== "pickingUp1f" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.states== "base" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.Phuman== "-11" and self.SpaperOrPlastic== "0" and self.PpickingUp== "1" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-11 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "atRisk" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "base" and self.paperBin== "base" and self.PmakingTrash== "3" and self.PecoBot== "2" and self.pickingUp== "pickingUp1f" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.states== "base" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office" and self.PpaperBin== "2" and self.Phuman== "-11" and self.SpaperOrPlastic== "0" and self.PpickingUp== "1" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (1<self.CecoBot and self.Cobj<11 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.PpickingUp== "0" and self.PecoBot== "2" and self.paperBin== "base" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.Phuman== "1" and self.PthrowingPaper== "0" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.plasticBin== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "2" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.PpickingUp== "0" and self.PecoBot== "2" and self.paperBin== "base" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.Phuman== "1" and self.PthrowingPaper== "0" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.plasticBin== "trashRoom"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "1" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s" and self.ecoBot== "office" and self.pickingUp== "pickingUp1f" and self.Phuman== "1" and self.obj== "atRisk" and self.human== "office" and self.paperBin== "base" and self.PplasticBin== "4" and self.PpickingUp== "1" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.PthrowingPaper== "2" and self.states== "base" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.Cobj-34 - self.TIMEUNIT ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-34 - self.TIMEUNIT ] , [9-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "1" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash1s" and self.ecoBot== "office" and self.pickingUp== "pickingUp1f" and self.Phuman== "1" and self.obj== "atRisk" and self.human== "office" and self.paperBin== "base" and self.PplasticBin== "4" and self.PpickingUp== "1" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.PthrowingPaper== "2" and self.states== "base" and self.PpaperBin== "2"  ):
						if ( (1<self.CecoBot and 1<self.Chuman and self.Cobj<34 and self.CecoBot- self.Cobj<-9 )  or  (1<self.CecoBot and self.Chuman<34 and self.Chuman- self.CecoBot<=9 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "plasticTrash!", "office", "doing_plasticTrash_in_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.Phuman== "-11" and self.PecoBot== "-31" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.states== "base" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.PpickingUp== "4" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.ecoBot== "going_hallway_to_office" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp0" and self.PthrowingPaper== "2" and self.obj== "atRisk"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-39 - self.TIMEUNIT, self.CecoBot-10 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj), -16- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.Phuman== "-11" and self.PecoBot== "-31" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.states== "base" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.PpickingUp== "4" and self.paperBin== "base" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PmakingTrash== "3" and self.ecoBot== "going_hallway_to_office" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp0" and self.PthrowingPaper== "2" and self.obj== "atRisk"  ):
						if ( (9<self.CecoBot and self.Cobj<39 and self.CecoBot<=10 and self.Chuman- self.Cobj<-1 and self.CecoBot- self.Cobj<-16 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.Phuman== "-11" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.states== "base" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.obj== "idle" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "going_trashRoom_to_hallway" and self.PecoBot== "-43" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-49 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpaperBin== "2" and self.throwingPlastic== "throwingPlastic0" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.Phuman== "-11" and self.PthrowingPlastic== "2" and self.human== "doing_wait_in_office" and self.states== "base" and self.PplasticBin== "4" and self.plasticBin== "trashRoom" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.paperBin== "base" and self.obj== "idle" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "going_trashRoom_to_hallway" and self.PecoBot== "-43" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<49 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-31" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PthrowingPaper== "2" and self.human== "office" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.PthrowingPlastic== "0" and self.states== "base" and self.ecoBot== "going_hallway_to_office" and self.plasticBin== "trashRoom" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-31" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.PmakingTrash== "2" and self.PthrowingPaper== "2" and self.human== "office" and self.obj== "idle" and self.makingTrash== "makingTrash1s" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.PthrowingPlastic== "0" and self.states== "base" and self.ecoBot== "going_hallway_to_office" and self.plasticBin== "trashRoom" and self.PplasticBin== "4"  ):
						if ( (9<self.CecoBot and 1<self.Chuman and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "2" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "2" and self.ecoBot== "going_hallway_to_office" and self.paperBin== "base" and self.PecoBot== "-31"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-9 - self.TIMEUNIT, self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "2" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.Phuman== "-11" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "1" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "2" and self.ecoBot== "going_hallway_to_office" and self.paperBin== "base" and self.PecoBot== "-31"  ):
						if ( (9<self.CecoBot and self.Chuman<9 and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "2" and self.human== "office" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "3" and self.states== "base" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.PpickingUp== "4" and self.ecoBot== "hallway" and self.paperBin== "base" and self.obj== "atRisk" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-30 - self.TIMEUNIT ] , [-15- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "2" and self.human== "office" and self.SpaperOrPlastic== "1" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "3" and self.states== "base" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.PpickingUp== "4" and self.ecoBot== "hallway" and self.paperBin== "base" and self.obj== "atRisk" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp0"  ):
						if ( (1<self.Chuman and 1<self.CecoBot and self.Cobj<30 and self.CecoBot- self.Cobj<-15 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "doing_throwPaper_in_base" and self.PthrowingPaper== "3" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.PecoBot== "-22" and self.states== "base" and self.human== "office" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.PmakingTrash== "2" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "doing_throwPaper_in_base" and self.PthrowingPaper== "3" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.PecoBot== "-22" and self.states== "base" and self.human== "office" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.SpaperOrPlastic== "1" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.PmakingTrash== "2" and self.Phuman== "1"  ):
						if ( (1<self.Chuman and 3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "3" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "doing_throwPaper_in_base" and self.PmakingTrash== "3" and self.obj== "idle" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "-11" and self.PplasticBin== "4" and self.states== "base" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.PecoBot== "-22" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-36 - self.TIMEUNIT, self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "3" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.ecoBot== "doing_throwPaper_in_base" and self.PmakingTrash== "3" and self.obj== "idle" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "-11" and self.PplasticBin== "4" and self.states== "base" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.PecoBot== "-22" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.SpaperOrPlastic== "0"  ):
						if ( (3<self.CecoBot and self.Chuman<36 and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.PmakingTrash== "1" and self.ecoBot== "trashRoom" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "4" and self.paperBin== "base" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.states== "base" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash0" and self.PthrowingPaper== "0" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.PmakingTrash== "1" and self.ecoBot== "trashRoom" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "4" and self.paperBin== "base" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.states== "base" and self.obj== "idle" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office" and self.PthrowingPlastic== "0" and self.makingTrash== "makingTrash0" and self.PthrowingPaper== "0" and self.PplasticBin== "4"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.Phuman== "1" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.PecoBot== "2" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.obj== "idle" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.ecoBot== "base" and self.human== "office" and self.PmakingTrash== "2"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.Phuman== "1" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.PecoBot== "2" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.obj== "idle" and self.paperBin== "base" and self.PthrowingPaper== "0" and self.ecoBot== "base" and self.human== "office" and self.PmakingTrash== "2"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_base2hallway!", "base", "going_base_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.PecoBot== "-11" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.obj== "atRisk" and self.Phuman== "-11" and self.ecoBot== "doing_paperTrash_in_office" and self.throwingPlastic== "throwingPlastic0" and self.pickingUp== "pickingUp2fs_sec_doing_paperTrash" and self.PmakingTrash== "3" and self.states== "base" and self.PthrowingPaper== "1" and self.SpaperOrPlastic== "1" and self.PpickingUp== "3" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0f_doing_paperTrash"   ):
				temps=set()
				temp0= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-6, self.Chuman-8 - self.TIMEUNIT, self.Cobj-39 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj), self.Cobj-self.CecoBot ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.paperBin== "base" and self.PecoBot== "-11" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.human== "doing_wait_in_office" and self.obj== "atRisk" and self.Phuman== "-11" and self.ecoBot== "doing_paperTrash_in_office" and self.throwingPlastic== "throwingPlastic0" and self.pickingUp== "pickingUp2fs_sec_doing_paperTrash" and self.PmakingTrash== "3" and self.states== "base" and self.PthrowingPaper== "1" and self.SpaperOrPlastic== "1" and self.PpickingUp== "3" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0f_doing_paperTrash"  ):
						if ( (5<self.CecoBot and self.CecoBot<=6 and self.Chuman<8 and self.Cobj<39 and self.Chuman- self.Cobj<-1 and self.CecoBot<=self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "paperTrashDONE!", "doing_paperTrash_in_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_hallway_to_base" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.PecoBot== "-32" and self.paperBin== "base" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "2" and self.states== "base" and self.PpaperBin== "2" and self.human== "office" and self.Phuman== "1" and self.PplasticBin== "4"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_hallway_to_base" and self.throwingPaper== "throwingPaper0" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "2" and self.PecoBot== "-32" and self.paperBin== "base" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "2" and self.states== "base" and self.PpaperBin== "2" and self.human== "office" and self.Phuman== "1" and self.PplasticBin== "4"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "office" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "2" and self.Phuman== "1" and self.ecoBot== "office" and self.PpickingUp== "1" and self.PecoBot== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "atRisk" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.pickingUp== "pickingUp1f"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-34 - self.TIMEUNIT ] , [self.Chuman-self.Cobj, 9-(self.Chuman-self.CecoBot) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-34 - self.TIMEUNIT ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "office" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.PthrowingPaper== "0" and self.plasticBin== "trashRoom" and self.states== "base" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PmakingTrash== "2" and self.Phuman== "1" and self.ecoBot== "office" and self.PpickingUp== "1" and self.PecoBot== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "atRisk" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.pickingUp== "pickingUp1f"  ):
						if ( (1<self.CecoBot and self.Chuman<34 and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=9 )  or  (1<self.Chuman and 1<self.CecoBot and self.Cobj<34 and self.CecoBot- self.Cobj<-9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "paperTrash!", "office", "doing_paperTrash_in_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_hallway_to_trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PmakingTrash== "2" and self.human== "office" and self.states== "base" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash1s" and self.obj== "idle" and self.PpickingUp== "0" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-34" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_hallway_to_trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PmakingTrash== "2" and self.human== "office" and self.states== "base" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.makingTrash== "makingTrash1s" and self.obj== "idle" and self.PpickingUp== "0" and self.Phuman== "1" and self.throwingPaper== "throwingPaper_initial_location" and self.PecoBot== "-34" and self.PpaperBin== "2"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.PecoBot== "-43" and self.makingTrash== "makingTrash0" and self.ecoBot== "going_trashRoom_to_hallway" and self.PmakingTrash== "1" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.human== "office" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.PecoBot== "-43" and self.makingTrash== "makingTrash0" and self.ecoBot== "going_trashRoom_to_hallway" and self.PmakingTrash== "1" and self.PplasticBin== "4" and self.PpaperBin== "2" and self.PthrowingPlastic== "0" and self.human== "office" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.SpaperOrPlastic== "1"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PecoBot== "-23" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_base_to_hallway" and self.Phuman== "1" and self.PplasticBin== "4" and self.states== "base" and self.PmakingTrash== "1" and self.PthrowingPaper== "0" and self.human== "office" and self.PthrowingPlastic== "0" and self.PpickingUp== "0" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "idle" and self.makingTrash== "makingTrash0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PecoBot== "-23" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_base_to_hallway" and self.Phuman== "1" and self.PplasticBin== "4" and self.states== "base" and self.PmakingTrash== "1" and self.PthrowingPaper== "0" and self.human== "office" and self.PthrowingPlastic== "0" and self.PpickingUp== "0" and self.paperBin== "base" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.obj== "idle" and self.makingTrash== "makingTrash0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.SpaperOrPlastic== "0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.ecoBot== "going_hallway_to_office" and self.makingTrash== "makingTrash0" and self.PplasticBin== "4" and self.PecoBot== "-31" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.PthrowingPaper== "2" and self.PpickingUp== "0" and self.human== "office" and self.paperBin== "base" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.PmakingTrash== "1" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.ecoBot== "going_hallway_to_office" and self.makingTrash== "makingTrash0" and self.PplasticBin== "4" and self.PecoBot== "-31" and self.plasticBin== "trashRoom" and self.obj== "idle" and self.PthrowingPaper== "2" and self.PpickingUp== "0" and self.human== "office" and self.paperBin== "base" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.PmakingTrash== "1" and self.SpaperOrPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "atRisk" and self.pickingUp== "pickingUp1f" and self.ecoBot== "going_office_to_hallway" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.paperBin== "base" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.PecoBot== "-13" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.PmakingTrash== "3"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-23 - self.TIMEUNIT, self.CecoBot-10 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "atRisk" and self.pickingUp== "pickingUp1f" and self.ecoBot== "going_office_to_hallway" and self.PpickingUp== "1" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.paperBin== "base" and self.Phuman== "-11" and self.human== "doing_wait_in_office" and self.SpaperOrPlastic== "0" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPlastic== "0" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.PecoBot== "-13" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.PmakingTrash== "3"  ):
						if ( (9<self.CecoBot and self.Cobj<23 and self.CecoBot<=10 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.pickingUp== "pickingUp1f" and self.PecoBot== "-31" and self.Phuman== "-11" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.states== "base" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_office" and self.PpickingUp== "1" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "doing_wait_in_office" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.obj== "atRisk"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-33 - self.TIMEUNIT, self.CecoBot-10, self.Chuman-2 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.pickingUp== "pickingUp1f" and self.PecoBot== "-31" and self.Phuman== "-11" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPlastic== "2" and self.states== "base" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_office" and self.PpickingUp== "1" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "3" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "doing_wait_in_office" and self.PplasticBin== "4" and self.SpaperOrPlastic== "1" and self.obj== "atRisk"  ):
						if ( (9<self.CecoBot and self.Cobj<33 and self.CecoBot<=10 and self.Chuman<2 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "-31" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.ecoBot== "going_hallway_to_office" and self.PpickingUp== "4" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "atRisk" and self.states== "base" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp0" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.PthrowingPlastic== "2" and self.Phuman== "-11"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-8 - self.TIMEUNIT, self.Cobj-39 - self.TIMEUNIT, self.CecoBot-10 ] , [-16- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic0" and self.PecoBot== "-31" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.ecoBot== "going_hallway_to_office" and self.PpickingUp== "4" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "atRisk" and self.states== "base" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp0" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper0" and self.PplasticBin== "4" and self.PthrowingPlastic== "2" and self.Phuman== "-11"  ):
						if ( (9<self.CecoBot and self.Chuman<8 and self.Cobj<39 and self.CecoBot<=10 and self.CecoBot- self.Cobj<-16 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.obj== "idle" and self.human== "office" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "3" and self.PecoBot== "-22" and self.ecoBot== "doing_throwPaper_in_base" and self.SpaperOrPlastic== "1" and self.Phuman== "1" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PpaperBin== "2" and self.PmakingTrash== "2" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.obj== "idle" and self.human== "office" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "3" and self.PecoBot== "-22" and self.ecoBot== "doing_throwPaper_in_base" and self.SpaperOrPlastic== "1" and self.Phuman== "1" and self.PpickingUp== "0"  ):
						if ( (1<self.Chuman and 3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.states== "base" and self.Phuman== "1" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_base_to_hallway" and self.obj== "idle" and self.PecoBot== "-23" and self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.human== "office" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.paperBin== "base" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.states== "base" and self.Phuman== "1" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_base_to_hallway" and self.obj== "idle" and self.PecoBot== "-23" and self.makingTrash== "makingTrash1s" and self.PpaperBin== "2" and self.PthrowingPlastic== "2" and self.PmakingTrash== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic0" and self.human== "office" and self.PplasticBin== "4" and self.PpickingUp== "0" and self.paperBin== "base" and self.SpaperOrPlastic== "0"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "3" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.PecoBot== "-22" and self.makingTrash== "makingTrash_initial_location" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "0" and self.ecoBot== "doing_throwPaper_in_base" and self.paperBin== "base" and self.PpaperBin== "2" and self.states== "base" and self.human== "office" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "3" and self.plasticBin== "trashRoom" and self.Phuman== "1" and self.PecoBot== "-22" and self.makingTrash== "makingTrash_initial_location" and self.throwingPaper== "throwingPaper0s_doing_throwPaper" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.obj== "idle" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "0" and self.ecoBot== "doing_throwPaper_in_base" and self.paperBin== "base" and self.PpaperBin== "2" and self.states== "base" and self.human== "office" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaperDONE!", "doing_throwPaper_in_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.Phuman== "1" and self.pickingUp== "pickingUp2fs_sec_doing_paperTrash" and self.paperBin== "base" and self.obj== "atRisk" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.PthrowingPaper== "1" and self.PpickingUp== "3" and self.PthrowingPlastic== "0" and self.human== "office" and self.PecoBot== "-11" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.states== "base" and self.ecoBot== "doing_paperTrash_in_office" and self.throwingPaper== "throwingPaper0f_doing_paperTrash" and self.PmakingTrash== "2" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-6 ] , [self.Chuman-self.CecoBot, self.Chuman-self.Cobj, 10-(self.Chuman-self.CecoBot) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-39 - self.TIMEUNIT, self.CecoBot-6 ] , [-10- self.TIMEUNIT-(self.CecoBot-self.Cobj), -1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.Phuman== "1" and self.pickingUp== "pickingUp2fs_sec_doing_paperTrash" and self.paperBin== "base" and self.obj== "atRisk" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.PthrowingPaper== "1" and self.PpickingUp== "3" and self.PthrowingPlastic== "0" and self.human== "office" and self.PecoBot== "-11" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.states== "base" and self.ecoBot== "doing_paperTrash_in_office" and self.throwingPaper== "throwingPaper0f_doing_paperTrash" and self.PmakingTrash== "2" and self.PpaperBin== "2"  ):
						if ( (5<self.CecoBot and self.CecoBot<=6 and self.CecoBot<=self.Chuman and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=10 )  or  (5<self.CecoBot and self.Cobj<39 and self.CecoBot<=6 and self.CecoBot- self.Cobj<-10 and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "paperTrashDONE!", "doing_paperTrash_in_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.ecoBot== "going_base_to_hallway" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.obj== "idle" and self.PecoBot== "-23"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PplasticBin== "4" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.ecoBot== "going_base_to_hallway" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "2" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.obj== "idle" and self.PecoBot== "-23"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.Phuman== "1" and self.PecoBot== "-43" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.PthrowingPaper== "2" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper0" and self.obj== "idle" and self.states== "base" and self.human== "office" and self.paperBin== "base" and self.ecoBot== "going_trashRoom_to_hallway"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.Phuman== "1" and self.PecoBot== "-43" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.PthrowingPaper== "2" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.throwingPaper== "throwingPaper0" and self.obj== "idle" and self.states== "base" and self.human== "office" and self.paperBin== "base" and self.ecoBot== "going_trashRoom_to_hallway"  ):
						if ( (12<self.CecoBot and 1<self.Chuman and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "0" and self.PmakingTrash== "3" and self.PecoBot== "-23" and self.PplasticBin== "4" and self.paperBin== "base" and self.Phuman== "-11" and self.PpickingUp== "0" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "going_base_to_hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.states== "base" and self.obj== "idle" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "0" and self.PmakingTrash== "3" and self.PecoBot== "-23" and self.PplasticBin== "4" and self.paperBin== "base" and self.Phuman== "-11" and self.PpickingUp== "0" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.ecoBot== "going_base_to_hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic_initial_location" and self.SpaperOrPlastic== "1" and self.states== "base" and self.obj== "idle" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PmakingTrash== "3" and self.pickingUp== "pickingUp1f" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.paperBin== "base" and self.Phuman== "-11" and self.PplasticBin== "4" and self.obj== "atRisk" and self.states== "base" and self.SpaperOrPlastic== "0" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.PecoBot== "-44" and self.PthrowingPlastic== "3"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-4, self.Cobj-10 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PmakingTrash== "3" and self.pickingUp== "pickingUp1f" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.paperBin== "base" and self.Phuman== "-11" and self.PplasticBin== "4" and self.obj== "atRisk" and self.states== "base" and self.SpaperOrPlastic== "0" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.plasticBin== "trashRoom" and self.PpickingUp== "1" and self.PecoBot== "-44" and self.PthrowingPlastic== "3"  ):
						if ( (3<self.CecoBot and self.CecoBot<=4 and self.Cobj<10 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.PmakingTrash== "2" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PecoBot== "3" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.ecoBot== "hallway" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "1" and self.states== "base" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.PmakingTrash== "2" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.PecoBot== "3" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0" and self.PpaperBin== "2" and self.ecoBot== "hallway" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "1" and self.states== "base" and self.paperBin== "base" and self.PthrowingPlastic== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.human== "office"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.SpaperOrPlastic== "1" and self.obj== "idle" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-43" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.ecoBot== "going_trashRoom_to_hallway" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-49 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.SpaperOrPlastic== "1" and self.obj== "idle" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-43" and self.PplasticBin== "4" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.ecoBot== "going_trashRoom_to_hallway" and self.PpaperBin== "2" and self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.human== "doing_wait_in_office"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<49 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.obj== "idle" and self.PplasticBin== "4" and self.PecoBot== "-32" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_hallway_to_base" and self.human== "office" and self.PthrowingPaper== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.makingTrash== "makingTrash_initial_location" and self.PmakingTrash== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.paperBin== "base" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.obj== "idle" and self.PplasticBin== "4" and self.PecoBot== "-32" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_hallway_to_base" and self.human== "office" and self.PthrowingPaper== "0" and self.states== "base" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.makingTrash== "makingTrash_initial_location" and self.PmakingTrash== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.Phuman== "1" and self.paperBin== "base" and self.PpickingUp== "0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash_initial_location" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.ecoBot== "going_hallway_to_trashRoom" and self.obj== "idle" and self.PecoBot== "-34" and self.human== "office"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.throwingPlastic== "throwingPlastic0" and self.PmakingTrash== "0" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash_initial_location" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "1" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.Phuman== "1" and self.ecoBot== "going_hallway_to_trashRoom" and self.obj== "idle" and self.PecoBot== "-34" and self.human== "office"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.ecoBot== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp_initial_location" and self.human== "doing_wait_in_office" and self.obj== "idle" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PecoBot== "4" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.PthrowingPlastic== "2" and self.throwingPlastic== "throwingPlastic0" and self.PplasticBin== "4" and self.ecoBot== "trashRoom" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp_initial_location" and self.human== "doing_wait_in_office" and self.obj== "idle" and self.PpaperBin== "2" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.SpaperOrPlastic== "0" and self.PpickingUp== "0" and self.PecoBot== "4" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.PthrowingPaper== "0"  ):
						if ( (1<self.CecoBot and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlastic!", "trashRoom", "doing_throwPlastic_in_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.plasticBin== "trashRoom" and self.ecoBot== "going_hallway_to_office" and self.PplasticBin== "4" and self.PecoBot== "-31" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "2" and self.states== "base" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "atRisk" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.PpickingUp== "4" and self.pickingUp== "pickingUp0" and self.PthrowingPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Cobj-39 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman), -16- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.plasticBin== "trashRoom" and self.ecoBot== "going_hallway_to_office" and self.PplasticBin== "4" and self.PecoBot== "-31" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "2" and self.states== "base" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.obj== "atRisk" and self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper0" and self.human== "office" and self.paperBin== "base" and self.makingTrash== "makingTrash1s" and self.PpickingUp== "4" and self.pickingUp== "pickingUp0" and self.PthrowingPlastic== "0"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Cobj<39 and self.CecoBot- self.Chuman<-1 and self.CecoBot- self.Cobj<-16 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.human== "doing_wait_in_office" and self.ecoBot== "going_office_to_hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.Phuman== "-11" and self.PplasticBin== "4" and self.states== "base" and self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-13" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic0"   ):
				temps=set()
				temp0= optimal_wait([ 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10, self.Chuman-19 - self.TIMEUNIT ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "2" and self.PpaperBin== "2" and self.PmakingTrash== "3" and self.PpickingUp== "0" and self.human== "doing_wait_in_office" and self.ecoBot== "going_office_to_hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.obj== "idle" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.Phuman== "-11" and self.PplasticBin== "4" and self.states== "base" and self.throwingPaper== "throwingPaper0" and self.pickingUp== "pickingUp_initial_location" and self.PecoBot== "-13" and self.PthrowingPlastic== "2" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic0"  ):
						if ( (9<self.CecoBot and self.CecoBot<=10 and self.Chuman<19 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_office_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PplasticBin== "4" and self.obj== "idle" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "1" and self.PthrowingPaper== "2" and self.ecoBot== "base" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.human== "office" and self.PecoBot== "2" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.paperBin== "base"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PplasticBin== "4" and self.obj== "idle" and self.PpickingUp== "0" and self.plasticBin== "trashRoom" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.pickingUp== "pickingUp_initial_location" and self.PmakingTrash== "1" and self.PthrowingPaper== "2" and self.ecoBot== "base" and self.makingTrash== "makingTrash0" and self.PthrowingPlastic== "0" and self.Phuman== "1" and self.human== "office" and self.PecoBot== "2" and self.SpaperOrPlastic== "1" and self.throwingPaper== "throwingPaper0" and self.states== "base" and self.paperBin== "base"  ):
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.human== "office" and self.ecoBot== "going_hallway_to_base" and self.obj== "atRisk" and self.pickingUp== "pickingUp1f" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "-32" and self.PpickingUp== "1" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-6 - self.TIMEUNIT ] , [self.Chuman-self.Cobj ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.human== "office" and self.ecoBot== "going_hallway_to_base" and self.obj== "atRisk" and self.pickingUp== "pickingUp1f" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.throwingPaper== "throwingPaper0" and self.PecoBot== "-32" and self.PpickingUp== "1" and self.PplasticBin== "4" and self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.makingTrash== "makingTrash1s" and self.PmakingTrash== "2" and self.PthrowingPaper== "2" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<6 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.Phuman== "1" and self.PthrowingPaper== "2" and self.ecoBot== "going_hallway_to_office" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.PthrowingPlastic== "0" and self.states== "base" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-31" and self.human== "office" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 9 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-10 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.throwingPaper== "throwingPaper0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.Phuman== "1" and self.PthrowingPaper== "2" and self.ecoBot== "going_hallway_to_office" and self.PplasticBin== "4" and self.PmakingTrash== "2" and self.PthrowingPlastic== "0" and self.states== "base" and self.PpaperBin== "2" and self.makingTrash== "makingTrash1s" and self.obj== "idle" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-31" and self.human== "office" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (1<self.Chuman and 9<self.CecoBot and self.CecoBot<=10 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "1" and self.PecoBot== "-34" and self.PplasticBin== "4" and self.states== "base" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_hallway_to_trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.obj== "idle" and self.paperBin== "base" and self.human== "office" and self.makingTrash== "makingTrash0" and self.PthrowingPaper== "0" and self.Phuman== "1"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPlastic== "0" and self.SpaperOrPlastic== "0" and self.PmakingTrash== "1" and self.PecoBot== "-34" and self.PplasticBin== "4" and self.states== "base" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "going_hallway_to_trashRoom" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpaperBin== "2" and self.obj== "idle" and self.paperBin== "base" and self.human== "office" and self.makingTrash== "makingTrash0" and self.PthrowingPaper== "0" and self.Phuman== "1"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PecoBot== "3" and self.PplasticBin== "4" and self.paperBin== "base" and self.states== "base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash_initial_location" and self.PmakingTrash== "0" and self.ecoBot== "hallway" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.human== "office" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot, 0 + self.TIMEUNIT-self.Chuman ] , [ ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PecoBot== "3" and self.PplasticBin== "4" and self.paperBin== "base" and self.states== "base" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash_initial_location" and self.PmakingTrash== "0" and self.ecoBot== "hallway" and self.Phuman== "1" and self.SpaperOrPlastic== "0" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.human== "office" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location"  ):
						if ( (1<self.CecoBot and 0<self.Chuman )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
						if ( (1<self.CecoBot )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.ecoBot== "hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.Phuman== "-11" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "2" and self.obj== "idle" and self.states== "base" and self.PmakingTrash== "3" and self.PecoBot== "3" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-30 - self.TIMEUNIT ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot, 30 + self.TIMEUNIT-self.Chuman ] , [ self.Chuman-50 ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp1 >= 0):
					temps.add(temp1)
				temp2= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-50 ] , [9-(self.Chuman-self.CecoBot) ])
				if (temp2 >= 0):
					temps.add(temp2)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "doing_wait_in_office" and self.plasticBin== "trashRoom" and self.ecoBot== "hallway" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PplasticBin== "4" and self.Phuman== "-11" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "2" and self.obj== "idle" and self.states== "base" and self.PmakingTrash== "3" and self.PecoBot== "3" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic0" and self.PthrowingPaper== "0"  ):
						if ( (1<self.CecoBot and self.Chuman<30 and self.CecoBot- self.Chuman<-9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
						if ( (1<self.CecoBot and 30<=self.Chuman and self.Chuman<=50 and self.CecoBot- self.Chuman<-9 )  or  (1<self.CecoBot and self.Chuman<=50 and self.Chuman- self.CecoBot<=9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_trashRoom_to_hallway" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.states== "base" and self.Phuman== "1" and self.PpaperBin== "2" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PpickingUp== "0" and self.PecoBot== "-43" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PplasticBin== "4" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "2" and self.plasticBin== "trashRoom" and self.makingTrash== "makingTrash1s" and self.ecoBot== "going_trashRoom_to_hallway" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.states== "base" and self.Phuman== "1" and self.PpaperBin== "2" and self.human== "office" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PpickingUp== "0" and self.PecoBot== "-43" and self.obj== "idle"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.human== "office" and self.states== "base" and self.ecoBot== "going_hallway_to_base" and self.PmakingTrash== "1" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.makingTrash== "makingTrash0" and self.PecoBot== "-32" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PplasticBin== "4" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.pickingUp== "pickingUp_initial_location" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.throwingPaper== "throwingPaper0" and self.PpaperBin== "2" and self.human== "office" and self.states== "base" and self.ecoBot== "going_hallway_to_base" and self.PmakingTrash== "1" and self.Phuman== "1" and self.SpaperOrPlastic== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PpickingUp== "0" and self.makingTrash== "makingTrash0" and self.PecoBot== "-32" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.PplasticBin== "4" and self.obj== "idle"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.paperBin== "base" and self.PecoBot== "-44" and self.obj== "idle" and self.PthrowingPlastic== "3" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.plasticBin== "trashRoom" and self.states== "base" and self.PplasticBin== "4" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "3" and self.PthrowingPaper== "0" and self.PpaperBin== "2"   ):
				temps=set()
				temp0= optimal_wait([ 3 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55, self.CecoBot-4 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PpickingUp== "0" and self.pickingUp== "pickingUp_initial_location" and self.ecoBot== "doing_throwPlastic_in_trashRoom" and self.paperBin== "base" and self.PecoBot== "-44" and self.obj== "idle" and self.PthrowingPlastic== "3" and self.throwingPlastic== "throwingPlastic0s_doing_throwPlastic" and self.SpaperOrPlastic== "0" and self.Phuman== "-11" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.plasticBin== "trashRoom" and self.states== "base" and self.PplasticBin== "4" and self.human== "doing_wait_in_office" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "3" and self.PthrowingPaper== "0" and self.PpaperBin== "2"  ):
						if ( (3<self.CecoBot and self.Chuman<=55 and self.CecoBot<=4 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPlasticDONE!", "doing_throwPlastic_in_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.PthrowingPlastic== "0" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "1" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.paperBin== "base" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp1f" and self.PecoBot== "3" and self.PpickingUp== "1"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-24 - self.TIMEUNIT ] , [self.Chuman-self.Cobj, 9-(self.Chuman-self.CecoBot) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot, 1 + self.TIMEUNIT-self.Chuman ] , [ self.Cobj-24 - self.TIMEUNIT ] , [-9- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.SpaperOrPlastic== "1" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic_initial_location" and self.human== "office" and self.PthrowingPlastic== "0" and self.obj== "atRisk" and self.throwingPaper== "throwingPaper_initial_location" and self.Phuman== "1" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.paperBin== "base" and self.ecoBot== "hallway" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp1f" and self.PecoBot== "3" and self.PpickingUp== "1"  ):
						if ( (1<self.CecoBot and self.Chuman<24 and self.Chuman==self.Cobj and self.Chuman- self.CecoBot<=9 )  or  (1<self.CecoBot and 1<self.Chuman and self.Cobj<24 and self.CecoBot- self.Cobj<-9 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.paperBin== "base" and self.ecoBot== "going_hallway_to_trashRoom" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PmakingTrash== "3" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic0" and self.obj== "idle" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.states== "base" and self.plasticBin== "trashRoom" and self.PecoBot== "-34" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp_initial_location" and self.human== "doing_wait_in_office" and self.Phuman== "-11" and self.SpaperOrPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.paperBin== "base" and self.ecoBot== "going_hallway_to_trashRoom" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "0" and self.PmakingTrash== "3" and self.PthrowingPaper== "0" and self.throwingPlastic== "throwingPlastic0" and self.obj== "idle" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PplasticBin== "4" and self.states== "base" and self.plasticBin== "trashRoom" and self.PecoBot== "-34" and self.PthrowingPlastic== "2" and self.pickingUp== "pickingUp_initial_location" and self.human== "doing_wait_in_office" and self.Phuman== "-11" and self.SpaperOrPlastic== "1"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.states== "base" and self.Phuman== "-11" and self.PpaperBin== "2" and self.PecoBot== "3" and self.PthrowingPlastic== "2" and self.ecoBot== "hallway" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.PmakingTrash== "3" and self.obj== "idle"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-30 - self.TIMEUNIT ] , [13-(self.Chuman-self.CecoBot), self.Chuman-self.CecoBot ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-50 ] , [self.CecoBot+ self.TIMEUNIT-self.Chuman ])
				if (temp1 >= 0):
					temps.add(temp1)
				temp2= optimal_wait([ 30 + self.TIMEUNIT-self.Chuman ] , [ self.Chuman-50 ] , [13-(self.Chuman-self.CecoBot), self.Chuman-self.CecoBot ])
				if (temp2 >= 0):
					temps.add(temp2)
				temp3= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-50 ] , [-13- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp3 >= 0):
					temps.add(temp3)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash1s_sec_doing_wait" and self.PthrowingPaper== "0" and self.PplasticBin== "4" and self.SpaperOrPlastic== "0" and self.states== "base" and self.Phuman== "-11" and self.PpaperBin== "2" and self.PecoBot== "3" and self.PthrowingPlastic== "2" and self.ecoBot== "hallway" and self.human== "doing_wait_in_office" and self.throwingPlastic== "throwingPlastic0" and self.plasticBin== "trashRoom" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.paperBin== "base" and self.PmakingTrash== "3" and self.obj== "idle"  ):
						if ( (1<self.CecoBot and self.Chuman<30 and self.Chuman- self.CecoBot<=13 and self.CecoBot<=self.Chuman )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2office!", "hallway", "going_hallway_to_office")
						if ( (1<self.CecoBot and self.Chuman<=50 and self.Chuman<self.CecoBot )  or  (30<=self.Chuman and self.Chuman<=50 and self.Chuman- self.CecoBot<=13 and self.CecoBot<=self.Chuman )  or  (1<self.CecoBot and self.Chuman<=50 and self.CecoBot- self.Chuman<-13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_hallway2trashRoom!", "hallway", "going_hallway_to_trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PthrowingPaper== "2" and self.Phuman== "1" and self.obj== "atRisk" and self.ecoBot== "doing_plasticTrash_in_office" and self.PpickingUp== "2" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp2fs_fir_doing_plasticTrash" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic0f_doing_plasticTrash" and self.paperBin== "base" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.PecoBot== "-11" and self.states== "base" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.human== "office" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "1"   ):
				temps=set()
				temp0= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-39 - self.TIMEUNIT, self.CecoBot-6 ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman), -10- self.TIMEUNIT-(self.CecoBot-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				temp1= optimal_wait([ 5 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-6 ] , [self.Chuman-self.CecoBot, 10-(self.Chuman-self.CecoBot), self.Chuman-self.Cobj ])
				if (temp1 >= 0):
					temps.add(temp1)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PthrowingPaper== "2" and self.Phuman== "1" and self.obj== "atRisk" and self.ecoBot== "doing_plasticTrash_in_office" and self.PpickingUp== "2" and self.SpaperOrPlastic== "0" and self.pickingUp== "pickingUp2fs_fir_doing_plasticTrash" and self.makingTrash== "makingTrash1s" and self.throwingPlastic== "throwingPlastic0f_doing_plasticTrash" and self.paperBin== "base" and self.PpaperBin== "2" and self.PplasticBin== "4" and self.PecoBot== "-11" and self.states== "base" and self.plasticBin== "trashRoom" and self.PmakingTrash== "2" and self.human== "office" and self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "1"  ):
						if ( (5<self.CecoBot and self.Cobj<39 and self.CecoBot<=6 and self.CecoBot- self.Chuman<-1 and self.CecoBot- self.Cobj<-10 )  or  (5<self.CecoBot and self.CecoBot<=6 and self.CecoBot<=self.Chuman and self.Chuman- self.CecoBot<=10 and self.Chuman==self.Cobj )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "plasticTrashDONE!", "doing_plasticTrash_in_office", "office")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.human== "office" and self.PpickingUp== "0" and self.obj== "idle" and self.PecoBot== "2" and self.PthrowingPaper== "2" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "1" and self.states== "base" and self.ecoBot== "base" and self.paperBin== "base" and self.PmakingTrash== "2" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPaper== "throwingPaper0" and self.PthrowingPlastic== "2" and self.PplasticBin== "4" and self.makingTrash== "makingTrash1s" and self.pickingUp== "pickingUp_initial_location" and self.PpaperBin== "2" and self.human== "office" and self.PpickingUp== "0" and self.obj== "idle" and self.PecoBot== "2" and self.PthrowingPaper== "2" and self.throwingPlastic== "throwingPlastic0" and self.Phuman== "1" and self.states== "base" and self.ecoBot== "base" and self.paperBin== "base" and self.PmakingTrash== "2" and self.plasticBin== "trashRoom" and self.SpaperOrPlastic== "0"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "throwPaper!", "base", "doing_throwPaper_in_base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.PecoBot== "-23" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_base_to_hallway" and self.obj== "idle" and self.PthrowingPaper== "2" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.human== "office" and self.PpickingUp== "0"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.Chuman, 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.plasticBin== "trashRoom" and self.PthrowingPlastic== "0" and self.PecoBot== "-23" and self.SpaperOrPlastic== "1" and self.ecoBot== "going_base_to_hallway" and self.obj== "idle" and self.PthrowingPaper== "2" and self.pickingUp== "pickingUp_initial_location" and self.throwingPaper== "throwingPaper0" and self.makingTrash== "makingTrash1s" and self.PplasticBin== "4" and self.Phuman== "1" and self.throwingPlastic== "throwingPlastic_initial_location" and self.paperBin== "base" and self.PmakingTrash== "2" and self.PpaperBin== "2" and self.human== "office" and self.PpickingUp== "0"  ):
						if ( (1<self.Chuman and 12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.SpaperOrPlastic== "0" and self.obj== "idle" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.human== "doing_wait_in_office" and self.paperBin== "base" and self.states== "base" and self.ecoBot== "going_trashRoom_to_hallway" and self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.PecoBot== "-43" and self.PthrowingPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Chuman-55 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.SpaperOrPlastic== "0" and self.obj== "idle" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.human== "doing_wait_in_office" and self.paperBin== "base" and self.states== "base" and self.ecoBot== "going_trashRoom_to_hallway" and self.PthrowingPaper== "0" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.throwingPaper== "throwingPaper_initial_location" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.pickingUp== "pickingUp_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.plasticBin== "trashRoom" and self.Phuman== "-11" and self.PecoBot== "-43" and self.PthrowingPlastic== "0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Chuman<=55 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_trashRoom_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.states== "base" and self.ecoBot== "trashRoom" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.human== "office" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PecoBot== "4" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.Phuman== "1" and self.PplasticBin== "4" and self.obj== "idle" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location"   ):
				temps=set()
				temp0= optimal_wait([ 1 + self.TIMEUNIT-self.CecoBot ] , [ ] , [-1- self.TIMEUNIT-(self.CecoBot-self.Chuman) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.states== "base" and self.ecoBot== "trashRoom" and self.plasticBin== "trashRoom" and self.PpaperBin== "2" and self.human== "office" and self.PmakingTrash== "2" and self.makingTrash== "makingTrash1s" and self.PthrowingPaper== "2" and self.paperBin== "base" and self.PecoBot== "4" and self.SpaperOrPlastic== "0" and self.throwingPaper== "throwingPaper0" and self.PpickingUp== "0" and self.Phuman== "1" and self.PplasticBin== "4" and self.obj== "idle" and self.PthrowingPlastic== "0" and self.throwingPlastic== "throwingPlastic_initial_location" and self.pickingUp== "pickingUp_initial_location"  ):
						if ( (1<self.CecoBot and self.CecoBot- self.Chuman<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "ecoBot_trashRoom2hallway!", "trashRoom", "going_trashRoom_to_hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.PplasticBin== "4" and self.PecoBot== "-34" and self.human== "doing_wait_in_office" and self.obj== "atRisk" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.PpickingUp== "1" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.states== "base" and self.ecoBot== "going_hallway_to_trashRoom" and self.plasticBin== "trashRoom"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13, self.Cobj-6 - self.TIMEUNIT ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.PplasticBin== "4" and self.PecoBot== "-34" and self.human== "doing_wait_in_office" and self.obj== "atRisk" and self.throwingPlastic== "throwingPlastic0" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.pickingUp== "pickingUp1f" and self.PthrowingPaper== "0" and self.SpaperOrPlastic== "1" and self.Phuman== "-11" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.PpickingUp== "1" and self.PthrowingPlastic== "2" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.states== "base" and self.ecoBot== "going_hallway_to_trashRoom" and self.plasticBin== "trashRoom"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 and self.Cobj<6 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_trashRoom", "trashRoom")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.makingTrash== "makingTrash0" and self.states== "base" and self.PecoBot== "-32" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.human== "office" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PmakingTrash== "1" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "going_hallway_to_base"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.makingTrash== "makingTrash0" and self.states== "base" and self.PecoBot== "-32" and self.PplasticBin== "4" and self.PthrowingPaper== "0" and self.Phuman== "1" and self.plasticBin== "trashRoom" and self.human== "office" and self.obj== "idle" and self.pickingUp== "pickingUp_initial_location" and self.PthrowingPlastic== "0" and self.PmakingTrash== "1" and self.PpickingUp== "0" and self.SpaperOrPlastic== "1" and self.PpaperBin== "2" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.throwingPlastic== "throwingPlastic_initial_location" and self.ecoBot== "going_hallway_to_base"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.human== "doing_wait_in_office" and self.ecoBot== "going_base_to_hallway" and self.pickingUp== "pickingUp1f" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "1" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-23" and self.Phuman== "-11" and self.obj== "atRisk"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Cobj-23 - self.TIMEUNIT, self.CecoBot-13 ] , [-1- self.TIMEUNIT-(self.Chuman-self.Cobj) ])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.human== "doing_wait_in_office" and self.ecoBot== "going_base_to_hallway" and self.pickingUp== "pickingUp1f" and self.PplasticBin== "4" and self.PmakingTrash== "3" and self.PpaperBin== "2" and self.PthrowingPaper== "0" and self.throwingPaper== "throwingPaper_initial_location" and self.PpickingUp== "1" and self.PthrowingPlastic== "0" and self.plasticBin== "trashRoom" and self.paperBin== "base" and self.SpaperOrPlastic== "1" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.states== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.PecoBot== "-23" and self.Phuman== "-11" and self.obj== "atRisk"  ):
						if ( (12<self.CecoBot and self.Cobj<23 and self.CecoBot<=13 and self.Chuman- self.Cobj<-1 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.obj== "idle" and self.PplasticBin== "4" and self.makingTrash== "makingTrash0" and self.PecoBot== "-32" and self.PmakingTrash== "1" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0" and self.Phuman== "1" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_base" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.human== "office" and self.SpaperOrPlastic== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.obj== "idle" and self.PplasticBin== "4" and self.makingTrash== "makingTrash0" and self.PecoBot== "-32" and self.PmakingTrash== "1" and self.plasticBin== "trashRoom" and self.throwingPaper== "throwingPaper0" and self.Phuman== "1" and self.paperBin== "base" and self.throwingPlastic== "throwingPlastic_initial_location" and self.states== "base" and self.pickingUp== "pickingUp_initial_location" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.ecoBot== "going_hallway_to_base" and self.PthrowingPaper== "2" and self.PthrowingPlastic== "0" and self.human== "office" and self.SpaperOrPlastic== "0"  ):
						if ( (12<self.CecoBot and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_hallway_to_base", "base")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

			#state header
			if ( self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PecoBot== "-23" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.obj== "idle" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.states== "base" and self.Phuman== "-11" and self.ecoBot== "going_base_to_hallway" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0"   ):
				temps=set()
				temp0= optimal_wait([ 12 + self.TIMEUNIT-self.CecoBot ] , [ self.Chuman-55, self.CecoBot-13 ] , [])
				if (temp0 >= 0):
					temps.add(temp0)
				if(temps):
					wait = min(temps)
					self.event_flag.clear()
					self.event_flag.wait(wait)
					self.exegg.ping_observer()
					if (self.throwingPlastic== "throwingPlastic_initial_location" and self.PthrowingPlastic== "0" and self.PecoBot== "-23" and self.PpickingUp== "0" and self.PpaperBin== "2" and self.obj== "idle" and self.human== "doing_wait_in_office" and self.makingTrash== "makingTrash1s_sec_doing_wait" and self.pickingUp== "pickingUp_initial_location" and self.PplasticBin== "4" and self.states== "base" and self.Phuman== "-11" and self.ecoBot== "going_base_to_hallway" and self.paperBin== "base" and self.throwingPaper== "throwingPaper_initial_location" and self.PmakingTrash== "3" and self.SpaperOrPlastic== "0" and self.plasticBin== "trashRoom" and self.PthrowingPaper== "0"  ):
						if ( (12<self.CecoBot and self.Chuman<=55 and self.CecoBot<=13 )  ):
							#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition
							self.exegg.exeggute("ecoBot", "tau", "going_base_to_hallway", "hallway")
				else:
					self.event_flag.clear()
					self.event_flag.wait()

def main():
	controllore = Runtime_controller()
	controllore.run()
if  __name__ == "__main__":
	controllore = Runtime_controller()
	controllore.run()
