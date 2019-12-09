#!/usr/bin/env python
######################################################################
# This component receives missions from Rest and converts them into
# ros messages
######################################################################
from Move_command_sender import Move_command_sender
from Action_sender import Action_sender
from Transition_sender import Transition_sender
from time import sleep


class Exeggutor:

  def __init__(self, timeunit):
    #dictionary here brutally defined for simplicity, in the future it should implemented so it's read form file
    self.location_dictionary = {
    "office" : [3.0,  1.54, 0.0, 0.0, 0.0, 0.67 ,0.73],
    "base" : [-0.57,  0.62, 0.0, 0.0, 0.0, 0.71 , 0.70] ,
    "hallway" : [0.47, 2.89, 0.0, 0.0, 0.0, 0.76, 0.65],
    "trashRoom" : [-3.19, 3.58, 0.0, 0.0, 0.0, -0.04, 1.0]
    }
    self.move = Move_command_sender()
    self.act = Action_sender()
    self.transition = Transition_sender()
    self.TIMEUNIT = timeunit

  #this function sends an "impossible" trigger, this will result in no transition taken but clocks updated and publishing of state 
  def ping_observer(self):
    self.transition.send_message("_ping_")
    print("I pinged the observer")
    sleep(self.TIMEUNIT)

  def start_observer(self):
    self.transition.send_message("_start_")
    print("I started the observer")
    sleep(self.TIMEUNIT)

  def exeggute (self, agent, trigger, origin, target):
    
    #first I check wether I'm triggering a movement
    trg = target.split("_")
    org = origin.split("_")

    if (trg[0] == "going"):
      #I send the coordinates to the bot andthe transition trigger to the enviroment 
      self.move.send_message(self.location_dictionary[trg[-1]])
      if(trigger[-1]=='!' or trigger[-1]=='?'):
        trigger_cleaned = trigger[0:-1]
      else:
        trigger_cleaned = trigger
      self.transition.send_message(trigger_cleaned)

      #print to screen
      print("I send the trigger"+ trigger_cleaned+ "so I'll go to coordinates")
      temp = self.location_dictionary[trg[-1]]
      for p in temp : print p
    
    #then i check for action with duration 
    elif (trg[0] == "doing"):
      if(trigger[-1]=='!' or trigger[-1]=='?'):
        trigger_cleaned = trigger[0:-1]
      else:
        trigger_cleaned = trigger

      self.act.send_message(trigger_cleaned)
      self.transition.send_message(trigger_cleaned)

      print("I do" + trigger_cleaned)

    #then I check if I finished a movement
    elif(org[0] == "going"):
      #I generate the trigger since as of right now the model doesn't have them for finishing movments
      if (trigger == "tau"):
        trigger_cleaned = agent+"_"+origin+"2"+target
      else:
        if(trigger[-1]=='!' or trigger[-1]=='?'):
          trigger_cleaned = trigger[0:-1]
        else:
          trigger_cleaned = trigger
      self.transition.send_message(trigger_cleaned)

    #then I check if I finished an action
    elif(org[0] == "doing"):
      if(trigger[-1]=='!' or trigger[-1]=='?'):
        trigger_cleaned = trigger[0:-1]
      else:
        trigger_cleaned = trigger
      self.transition.send_message(trigger_cleaned)
      print ("agent has finished action, trigger is "+ trigger_cleaned)

    #finally, last remaining option is that the action was istanteneus
    else:
      if(trigger[-1]=='!' or trigger[-1]=='?'):
        trigger_cleaned = trigger[0:-1]
      else:
        trigger_cleaned = trigger

      self.transition.send_message(trigger_cleaned)    
      print("agent has done instantaneuos action" + trigger_cleaned)

    sleep(self.TIMEUNIT)




















































