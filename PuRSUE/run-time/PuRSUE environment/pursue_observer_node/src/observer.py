#!/usr/bin/env python
#runtime_observer

from transitions import Machine
from functools import partial
import random
import time
import rospy
from std_msgs.msg import String


class Classstates():

	def reset_clock(self):
		self.need_reset = True

	def trigger(self, trigger):
		if (trigger in self.machine.get_triggers(self.state)):
			if (trigger=="isPlastic"):
				self.isPlastic()
				self.SpaperOrPlastic="0"
			if (trigger=="isPaper"):
				self.isPaper()
				self.SpaperOrPlastic="1"

	def updateP(self, newP):
		self.P = newP

	def printStates(self):
		stati = ""
		stati  = stati +"\nSpaperOrPlastic="+str(self.SpaperOrPlastic)
		return stati

	def __init__(self):
		self.name="states"
		self.need_reset = False
		self.clock=0.0
		self.P =0
		self.SpaperOrPlastic=1

		states =['base']
		transitions = [
			{'trigger' : 'isPlastic' , 'source' : 'base' , 'dest' : 'base' },
			{'trigger' : 'isPaper' , 'source' : 'base' , 'dest' : 'base' }
		]

		self.machine= Machine(model = self, states=states, transitions=transitions, initial='base',auto_transitions=False)


class ClasspickingUp():

	def reset_clock(self):
		self.need_reset = True

	def trigger(self, trigger):
		if (trigger in self.machine.get_triggers(self.state)):
			if (trigger=="officeClean"):
				self.officeClean()
			if (trigger=="plasticTrash"):
				self.plasticTrash()
			if (trigger=="paperTrashDONE"):
				self.paperTrashDONE()
			if (trigger=="plasticTrashDONE"):
				self.plasticTrashDONE()
			if (trigger=="callBot"):
				self.callBot()
			if (trigger=="paperTrash"):
				self.paperTrash()

	def updateP(self, newP):
		self.P = newP

	def __init__(self):
		self.name="pickingUp"
		self.need_reset = False
		self.clock=0.0
		self.P =0

		states =['pickingUp2fs_fir_doing_plasticTrash','pickingUp1f','pickingUp0','pickingUp_initial_location','pickingUp2fs_sec_doing_paperTrash']
		transitions = [
			{'trigger' : 'officeClean' , 'source' : 'pickingUp0' , 'dest' : 'pickingUp_initial_location', 'before' : partial(self.updateP, '0') },
			{'trigger' : 'plasticTrash' , 'source' : 'pickingUp1f' , 'dest' : 'pickingUp2fs_fir_doing_plasticTrash', 'before' : partial(self.updateP, '2') },
			{'trigger' : 'paperTrashDONE' , 'source' : 'pickingUp2fs_sec_doing_paperTrash' , 'dest' : 'pickingUp0', 'before' : partial(self.updateP, '4') },
			{'trigger' : 'plasticTrashDONE' , 'source' : 'pickingUp2fs_fir_doing_plasticTrash' , 'dest' : 'pickingUp0', 'before' : partial(self.updateP, '4') },
			{'trigger' : 'callBot' , 'source' : 'pickingUp_initial_location' , 'dest' : 'pickingUp1f', 'before' : partial(self.updateP, '1') },
			{'trigger' : 'paperTrash' , 'source' : 'pickingUp1f' , 'dest' : 'pickingUp2fs_sec_doing_paperTrash', 'before' : partial(self.updateP, '3') }
		]

		self.machine= Machine(model = self, states=states, transitions=transitions, initial='pickingUp_initial_location',auto_transitions=False)


class ClassthrowingPaper():

	def reset_clock(self):
		self.need_reset = True

	def trigger(self, trigger):
		if (trigger in self.machine.get_triggers(self.state)):
			if (trigger=="paperTrashDONE"):
				self.paperTrashDONE()
			if (trigger=="paperTrash"):
				self.paperTrash()
			if (trigger=="throwPaperDONE"):
				self.throwPaperDONE()
			if (trigger=="throwPaper"):
				self.throwPaper()

	def updateP(self, newP):
		self.P = newP

	def __init__(self):
		self.name="throwingPaper"
		self.need_reset = False
		self.clock=0.0
		self.P =0

		states =['throwingPaper0','throwingPaper0f_doing_paperTrash','throwingPaper0s_doing_throwPaper','throwingPaper_initial_location']
		transitions = [
			{'trigger' : 'paperTrashDONE' , 'source' : 'throwingPaper0f_doing_paperTrash' , 'dest' : 'throwingPaper0', 'before' : partial(self.updateP, '2') },
			{'trigger' : 'paperTrash' , 'source' : 'throwingPaper_initial_location' , 'dest' : 'throwingPaper0f_doing_paperTrash', 'before' : partial(self.updateP, '1') },
			{'trigger' : 'throwPaperDONE' , 'source' : 'throwingPaper0s_doing_throwPaper' , 'dest' : 'throwingPaper_initial_location', 'before' : partial(self.updateP, '0') },
			{'trigger' : 'throwPaper' , 'source' : 'throwingPaper0' , 'dest' : 'throwingPaper0s_doing_throwPaper', 'before' : partial(self.updateP, '3') }
		]

		self.machine= Machine(model = self, states=states, transitions=transitions, initial='throwingPaper_initial_location',auto_transitions=False)


class ClassthrowingPlastic():

	def reset_clock(self):
		self.need_reset = True

	def trigger(self, trigger):
		if (trigger in self.machine.get_triggers(self.state)):
			if (trigger=="plasticTrash"):
				self.plasticTrash()
			if (trigger=="plasticTrashDONE"):
				self.plasticTrashDONE()
			if (trigger=="throwPlasticDONE"):
				self.throwPlasticDONE()
			if (trigger=="throwPlastic"):
				self.throwPlastic()

	def updateP(self, newP):
		self.P = newP

	def __init__(self):
		self.name="throwingPlastic"
		self.need_reset = False
		self.clock=0.0
		self.P =0

		states =['throwingPlastic0f_doing_plasticTrash','throwingPlastic0s_doing_throwPlastic','throwingPlastic_initial_location','throwingPlastic0']
		transitions = [
			{'trigger' : 'plasticTrash' , 'source' : 'throwingPlastic_initial_location' , 'dest' : 'throwingPlastic0f_doing_plasticTrash', 'before' : partial(self.updateP, '1') },
			{'trigger' : 'plasticTrashDONE' , 'source' : 'throwingPlastic0f_doing_plasticTrash' , 'dest' : 'throwingPlastic0', 'before' : partial(self.updateP, '2') },
			{'trigger' : 'throwPlasticDONE' , 'source' : 'throwingPlastic0s_doing_throwPlastic' , 'dest' : 'throwingPlastic_initial_location', 'before' : partial(self.updateP, '0') },
			{'trigger' : 'throwPlastic' , 'source' : 'throwingPlastic0' , 'dest' : 'throwingPlastic0s_doing_throwPlastic', 'before' : partial(self.updateP, '3') }
		]

		self.machine= Machine(model = self, states=states, transitions=transitions, initial='throwingPlastic_initial_location',auto_transitions=False)


class ClassmakingTrash():

	def reset_clock(self):
		self.need_reset = True

	def trigger(self, trigger):
		if (trigger in self.machine.get_triggers(self.state)):
			if (trigger=="wait"):
				self.wait()
			if (trigger=="isPaper"):
				self.isPaper()
			if (trigger=="isPlastic"):
				self.isPlastic()
			if (trigger=="callBot"):
				self.callBot()
			if (trigger=="waitDONE"):
				self.waitDONE()

	def updateP(self, newP):
		self.P = newP

	def __init__(self):
		self.name="makingTrash"
		self.need_reset = False
		self.clock=0.0
		self.P =0

		states =['makingTrash1s_sec_doing_wait','makingTrash_initial_location','makingTrash0','makingTrash1s']
		transitions = [
			{'trigger' : 'wait' , 'source' : 'makingTrash1s' , 'dest' : 'makingTrash1s_sec_doing_wait', 'before' : partial(self.updateP, '3') },
			{'trigger' : 'isPaper' , 'source' : 'makingTrash_initial_location' , 'dest' : 'makingTrash0', 'before' : partial(self.updateP, '1') },
			{'trigger' : 'isPlastic' , 'source' : 'makingTrash_initial_location' , 'dest' : 'makingTrash0', 'before' : partial(self.updateP, '1') },
			{'trigger' : 'callBot' , 'source' : 'makingTrash0' , 'dest' : 'makingTrash1s', 'before' : partial(self.updateP, '2') },
			{'trigger' : 'waitDONE' , 'source' : 'makingTrash1s_sec_doing_wait' , 'dest' : 'makingTrash_initial_location', 'before' : partial(self.updateP, '0') }
		]

		self.machine= Machine(model = self, states=states, transitions=transitions, initial='makingTrash_initial_location',auto_transitions=False)


class ClassecoBot():

	def reset_clock(self):
		self.need_reset = True

	def trigger(self, trigger):
		if (trigger in self.machine.get_triggers(self.state)):
			if (trigger=="ecoBot_going_base_to_hallway2hallway"):
				self.ecoBot_going_base_to_hallway2hallway()
			if (trigger=="ecoBot_trashRoom2hallway"):
				self.ecoBot_trashRoom2hallway()
			if (trigger=="throwPlasticDONE"):
				self.throwPlasticDONE()
			if (trigger=="ecoBot_going_hallway_to_base2base"):
				self.ecoBot_going_hallway_to_base2base()
			if (trigger=="officeClean"):
				self.officeClean()
			if (trigger=="plasticTrashDONE"):
				self.plasticTrashDONE()
			if (trigger=="throwPlastic"):
				self.throwPlastic()
			if (trigger=="ecoBot_hallway2office"):
				self.ecoBot_hallway2office()
			if (trigger=="ecoBot_going_hallway_to_office2office"):
				self.ecoBot_going_hallway_to_office2office()
			if (trigger=="ecoBot_base2hallway"):
				self.ecoBot_base2hallway()
			if (trigger=="throwPaper"):
				self.throwPaper()
			if (trigger=="paperTrash"):
				self.paperTrash()
			if (trigger=="ecoBot_hallway2base"):
				self.ecoBot_hallway2base()
			if (trigger=="plasticTrash"):
				self.plasticTrash()
			if (trigger=="ecoBot_office2hallway"):
				self.ecoBot_office2hallway()
			if (trigger=="paperTrashDONE"):
				self.paperTrashDONE()
			if (trigger=="ecoBot_going_hallway_to_trashRoom2trashRoom"):
				self.ecoBot_going_hallway_to_trashRoom2trashRoom()
			if (trigger=="ecoBot_going_trashRoom_to_hallway2hallway"):
				self.ecoBot_going_trashRoom_to_hallway2hallway()
			if (trigger=="ecoBot_going_office_to_hallway2hallway"):
				self.ecoBot_going_office_to_hallway2hallway()
			if (trigger=="throwPaperDONE"):
				self.throwPaperDONE()
			if (trigger=="ecoBot_hallway2trashRoom"):
				self.ecoBot_hallway2trashRoom()

	def updateP(self, newP):
		self.P = newP

	def __init__(self):
		self.name="ecoBot"
		self.need_reset = False
		self.clock=0.0
		self.P =2

		states =['hallway','going_hallway_to_trashRoom','doing_throwPaper_in_base','office','going_base_to_hallway','doing_throwPaper_in_office','doing_throwPlastic_in_hallway','doing_throwPaper_in_trashRoom','going_trashRoom_to_hallway','going_hallway_to_base','doing_plasticTrash_in_office','trashRoom','doing_throwPlastic_in_base','going_office_to_hallway','doing_paperTrash_in_office','doing_throwPlastic_in_trashRoom','doing_throwPlastic_in_office','doing_throwPaper_in_hallway','base','going_hallway_to_office']
		transitions = [
			{'trigger' : 'ecoBot_going_base_to_hallway2hallway' , 'source' : 'going_base_to_hallway' , 'dest' : 'hallway', 'before' : partial(self.updateP, '3'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPlasticDONE' , 'source' : 'doing_throwPlastic_in_base' , 'dest' : 'base', 'before' : partial(self.updateP, '2'), 'after' : 'reset_clock' },
			{'trigger' : 'plasticTrashDONE' , 'source' : 'doing_plasticTrash_in_office' , 'dest' : 'office', 'before' : partial(self.updateP, '1'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPlastic' , 'source' : 'trashRoom' , 'dest' : 'doing_throwPlastic_in_trashRoom', 'before' : partial(self.updateP, '-44'), 'after' : 'reset_clock' },
			{'trigger' : 'ecoBot_hallway2office' , 'source' : 'hallway' , 'dest' : 'going_hallway_to_office', 'before' : partial(self.updateP, '-31'), 'after' : 'reset_clock' },
			{'trigger' : 'ecoBot_going_hallway_to_office2office' , 'source' : 'going_hallway_to_office' , 'dest' : 'office', 'before' : partial(self.updateP, '1'), 'after' : 'reset_clock' },
			{'trigger' : 'ecoBot_base2hallway' , 'source' : 'base' , 'dest' : 'going_base_to_hallway', 'before' : partial(self.updateP, '-23'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPlasticDONE' , 'source' : 'doing_throwPlastic_in_office' , 'dest' : 'office', 'before' : partial(self.updateP, '1'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPaper' , 'source' : 'base' , 'dest' : 'doing_throwPaper_in_base', 'before' : partial(self.updateP, '-22'), 'after' : 'reset_clock' },
			{'trigger' : 'paperTrash' , 'source' : 'office' , 'dest' : 'doing_paperTrash_in_office', 'before' : partial(self.updateP, '-11'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPlasticDONE' , 'source' : 'doing_throwPlastic_in_hallway' , 'dest' : 'hallway', 'before' : partial(self.updateP, '3'), 'after' : 'reset_clock' },
			{'trigger' : 'paperTrashDONE' , 'source' : 'doing_paperTrash_in_office' , 'dest' : 'office', 'before' : partial(self.updateP, '1'), 'after' : 'reset_clock' },
			{'trigger' : 'ecoBot_going_hallway_to_trashRoom2trashRoom' , 'source' : 'going_hallway_to_trashRoom' , 'dest' : 'trashRoom', 'before' : partial(self.updateP, '4'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPlasticDONE' , 'source' : 'doing_throwPlastic_in_trashRoom' , 'dest' : 'trashRoom', 'before' : partial(self.updateP, '4'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPaper' , 'source' : 'office' , 'dest' : 'doing_throwPaper_in_office', 'before' : partial(self.updateP, '-11'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPlastic' , 'source' : 'base' , 'dest' : 'doing_throwPlastic_in_base', 'before' : partial(self.updateP, '-22'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPaperDONE' , 'source' : 'doing_throwPaper_in_base' , 'dest' : 'base', 'before' : partial(self.updateP, '2'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPaperDONE' , 'source' : 'doing_throwPaper_in_trashRoom' , 'dest' : 'trashRoom', 'before' : partial(self.updateP, '4'), 'after' : 'reset_clock' },
			{'trigger' : 'ecoBot_trashRoom2hallway' , 'source' : 'trashRoom' , 'dest' : 'going_trashRoom_to_hallway', 'before' : partial(self.updateP, '-43'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPaperDONE' , 'source' : 'doing_throwPaper_in_hallway' , 'dest' : 'hallway', 'before' : partial(self.updateP, '3'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPaper' , 'source' : 'hallway' , 'dest' : 'doing_throwPaper_in_hallway', 'before' : partial(self.updateP, '-33'), 'after' : 'reset_clock' },
			{'trigger' : 'ecoBot_going_hallway_to_base2base' , 'source' : 'going_hallway_to_base' , 'dest' : 'base', 'before' : partial(self.updateP, '2'), 'after' : 'reset_clock' },
			{'trigger' : 'officeClean' , 'source' : 'office' , 'dest' : 'office', 'after' : 'reset_clock' },
			{'trigger' : 'throwPlastic' , 'source' : 'hallway' , 'dest' : 'doing_throwPlastic_in_hallway', 'before' : partial(self.updateP, '-33'), 'after' : 'reset_clock' },
			{'trigger' : 'ecoBot_hallway2base' , 'source' : 'hallway' , 'dest' : 'going_hallway_to_base', 'before' : partial(self.updateP, '-32'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPaperDONE' , 'source' : 'doing_throwPaper_in_office' , 'dest' : 'office', 'before' : partial(self.updateP, '1'), 'after' : 'reset_clock' },
			{'trigger' : 'plasticTrash' , 'source' : 'office' , 'dest' : 'doing_plasticTrash_in_office', 'before' : partial(self.updateP, '-11'), 'after' : 'reset_clock' },
			{'trigger' : 'ecoBot_office2hallway' , 'source' : 'office' , 'dest' : 'going_office_to_hallway', 'before' : partial(self.updateP, '-13'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPaper' , 'source' : 'trashRoom' , 'dest' : 'doing_throwPaper_in_trashRoom', 'before' : partial(self.updateP, '-44'), 'after' : 'reset_clock' },
			{'trigger' : 'ecoBot_going_trashRoom_to_hallway2hallway' , 'source' : 'going_trashRoom_to_hallway' , 'dest' : 'hallway', 'before' : partial(self.updateP, '3'), 'after' : 'reset_clock' },
			{'trigger' : 'ecoBot_going_office_to_hallway2hallway' , 'source' : 'going_office_to_hallway' , 'dest' : 'hallway', 'before' : partial(self.updateP, '3'), 'after' : 'reset_clock' },
			{'trigger' : 'throwPlastic' , 'source' : 'office' , 'dest' : 'doing_throwPlastic_in_office', 'before' : partial(self.updateP, '-11'), 'after' : 'reset_clock' },
			{'trigger' : 'ecoBot_hallway2trashRoom' , 'source' : 'hallway' , 'dest' : 'going_hallway_to_trashRoom', 'before' : partial(self.updateP, '-34'), 'after' : 'reset_clock' }
		]

		self.machine= Machine(model = self, states=states, transitions=transitions, initial='base',auto_transitions=False)


class ClassplasticBin():

	def reset_clock(self):
		self.need_reset = True

	def trigger(self, trigger):
		return

	def updateP(self, newP):
		self.P = newP

	def __init__(self):
		self.name="plasticBin"
		self.need_reset = False
		self.clock=0.0
		self.P =4

		states =['trashRoom']
		transitions = [
		]

		self.machine= Machine(model = self, states=states, transitions=transitions, initial='trashRoom',auto_transitions=False)


class Classhuman():

	def reset_clock(self):
		self.need_reset = True

	def trigger(self, trigger):
		if (trigger in self.machine.get_triggers(self.state)):
			if (trigger=="waitDONE"):
				self.waitDONE()
			if (trigger=="isPaper"):
				self.isPaper()
			if (trigger=="callBot"):
				self.callBot()
			if (trigger=="isPlastic"):
				self.isPlastic()
			if (trigger=="wait"):
				self.wait()

	def updateP(self, newP):
		self.P = newP

	def __init__(self):
		self.name="human"
		self.need_reset = False
		self.clock=0.0
		self.P =1

		states =['doing_wait_in_office','office']
		transitions = [
			{'trigger' : 'waitDONE' , 'source' : 'doing_wait_in_office' , 'dest' : 'office', 'before' : partial(self.updateP, '1'), 'after' : 'reset_clock' },
			{'trigger' : 'isPaper' , 'source' : 'office' , 'dest' : 'office', 'after' : 'reset_clock' },
			{'trigger' : 'callBot' , 'source' : 'office' , 'dest' : 'office', 'after' : 'reset_clock' },
			{'trigger' : 'isPlastic' , 'source' : 'office' , 'dest' : 'office', 'after' : 'reset_clock' },
			{'trigger' : 'wait' , 'source' : 'office' , 'dest' : 'doing_wait_in_office', 'before' : partial(self.updateP, '-11'), 'after' : 'reset_clock' }
		]

		self.machine= Machine(model = self, states=states, transitions=transitions, initial='office',auto_transitions=False)


class ClasspaperBin():

	def reset_clock(self):
		self.need_reset = True

	def trigger(self, trigger):
		return

	def updateP(self, newP):
		self.P = newP

	def __init__(self):
		self.name="paperBin"
		self.need_reset = False
		self.clock=0.0
		self.P =2

		states =['base']
		transitions = [
		]

		self.machine= Machine(model = self, states=states, transitions=transitions, initial='base',auto_transitions=False)


class Classobj():

	def reset_clock(self):
		self.need_reset = True

	def trigger(self, trigger):
		if (trigger in self.machine.get_triggers(self.state)):
			if (trigger=="officeClean"):
				self.officeClean()
			if (trigger=="callBot"):
				self.callBot()
			if (trigger=="obj_atRisk2lose"):
				self.obj_atRisk2lose()

	def updateP(self, newP):
		self.P = newP

	def __init__(self):
		self.name="obj"
		self.need_reset = False
		self.clock=0.0
		self.P =0

		states =['idle','lose','atRisk']
		transitions = [
			{'trigger' : 'officeClean' , 'source' : 'atRisk' , 'dest' : 'idle' },
			{'trigger' : 'callBot' , 'source' : 'idle' , 'dest' : 'atRisk', 'after' : 'reset_clock' },
			{'trigger' : 'obj_atRisk2lose' , 'source' : 'atRisk' , 'dest' : 'lose' }
		]

		self.machine= Machine(model = self, states=states, transitions=transitions, initial='idle',auto_transitions=False)

class Observer():

	def callback(self, data):
		trigger = data.data
		for automaton in self.automa:
			automaton.trigger(trigger)

		if trigger == "_start_":
			self.startTime=time.time()
		self.stopTime = time.time()
		elapsedTime =self.stopTime - self.startTime
		self.startTime = time.time()
		for automaton in self.automa:
			if automaton.need_reset:
				automaton.clock = 0
				automaton.need_reset = False
			else:
				automaton.clock += elapsedTime

		state = ""
		clocks = ""
		for automaton in self.automa:
			state +="\n"+ automaton.name + "=" + automaton.state + "\n"+"P"+automaton.name+"="+str(automaton.P)
			clocks += "\n"+'C'+automaton.name +"=" +str(automaton.clock) 
		state = state + self.automa[0].printStates()

		print ("the following will be sent to state topic:\n"+state+"\n\n"+clocks)
		self.pub.publish(state+"\n\n"+clocks)

	def __init__(self):

		self.automa = []
		self.automa.append(Classstates())
		self.automa.append(ClasspickingUp())
		self.automa.append(ClassthrowingPaper())
		self.automa.append(ClassthrowingPlastic())
		self.automa.append(ClassmakingTrash())
		self.automa.append(ClassecoBot())
		self.automa.append(ClassplasticBin())
		self.automa.append(Classhuman())
		self.automa.append(ClasspaperBin())
		self.automa.append(Classobj())

		self.startTime = time.time()
		self.stopTime = self.startTime

		rospy.init_node('pursue_observer')
		self.pub = rospy.Publisher('pursue/system_state', String, queue_size=1)

	def run(self):

		rospy.Subscriber("pursue/events", String, self.callback)
		rospy.spin()

def main():
	observer = Observer()
	observer.run()
if  __name__ == "__main__":
	observer = Observer()
	observer.run()
