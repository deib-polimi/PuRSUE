#!/usr/bin/env python
import sys
import random
import Queue
import threading
import time





#Nota: ho testato, l'interrupt funziona
def listen(TIMEUNIT, heard, queue):
    while (True) :
      time.sleep(TIMEUNIT) #It seems necessary to put this in order to make the thing work
      #print("mi chiedo se il Main mi ha scritto <3")
      if not queue.empty():
        item = queue.get(True, 1)#at every cycle, it controls wether the main thread asked to quit
        if item == "quit":
          break
      with heard: #only enters this part if the method is unlocked
        if (False):#read something from topic, da implementare
          heard.notify()
    return 0




def optimal_wait(clock_higher, clock_lower, clock_const):
    wiggle = 0.5
    print("I enter optimal wait, wiggle is "+str(wiggle))

    for number in clock_const:
      if number < (0-wiggle):
	print("constant costraints dicono no causa di " + str(number))
        return -1.0


    highest_ch = 0.0 #smallest wait before a rising condition becoems true (if all true, thus all negative, you wait zero)
    for number in clock_higher:
      if (number > highest_ch):
        highest_ch = number

    if clock_lower:
      lowest_cf = clock_lower[0] #smallest wait before a falling condition becomes false
      for number in clock_lower:
        if number > (0+wiggle):
          print("clock lower costraints dicono no, a causa di " + str(number))
          return -1.0 #if a clock_lower condition is positive, the overall condition shall never be true until some clock are reset
        else:
          if number > lowest_cf: #if it's closer to zero
            lowest_cf = number

      if (highest_ch-wiggle) > (- lowest_cf):#remembering lowest_cf is negative
        print("final check  costraints dicono no, a causa di " + str(highest_ch- lowest_cf))
        return -1.0 #a "C <= int " condition will become false before all "int < C" condition can become true
    print("tutto ok, ritorno"+ str(highest_ch))
    return highest_ch #return the time needed before all conditions become true



def listen_and_wait(TIMEUNIT, wait):
    q = Queue.Queue() # declare a queue, to communicate between threads
    change = threading.Condition() #define a condition
    listener = threading.Thread(target = listen, args = (TIMEUNIT, change, q,) ) #define a thread, with target function listen

    change.acquire() #acquire the lock for the condition

    startTime = time.time()
    listener.start() #start thread
    print("I+ll wait", wait)
    change.wait(wait) #the method autohmatically releasos the lock
    q.put("quit") #wether I quit because of timeout or condition, I ask the thead to quit
    listener.join() #wait for thethread to quit
    endTime = time.time()
    #status.update (con molti threadbisognera stare attenti che non succeda nulla in contemporanea e abbia priorita, se dev dialgoare con altri thread problemi)

    elapsedTime = endTime - startTime 
    return elapsedTime      



