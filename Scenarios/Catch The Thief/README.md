
# CT1
The environment is modeled through four POIs (a, b, c and d). The agents acting in it are modeled though the two agents policeBot and thief. The act of catching is modeled though a collaborative event catch, which has policeBot as acting agent and thief as reacting agent. Finally, the mission of the control system is modeled with the do catch construct. This encoding of the mission event is kept identical for all the following scenarios.
# CT2
The environment is modeled though the same four POIs as CT1, with the addition of the WeaponCloset location, which is connected to a. The agents are the same of CT1. The additional con- straint is implemented in two different ways: through a rule (CT2a), and though states (CT2b). The first implementation is done by enforcing that the event of catching the thief (catch) can only be triggered af- ter the event of picking up the weapon (pickUpBaton) has been triggered. In the second implementation, a state is added (hasBaton), this state, initially false, is set to true if the event pickUpBaton is triggered. Furthermore, a state dependency is defined, ensuring that the event catch can only be triggered when the state hasBaton is set to true.
# CT3
The environmnet is modeled as in CT1. The agents are the same of CT1, with the difference that two (CT3a) or three (CT3b) policeBot agents are declared. Moreover, the policeBot will move at the same speed as the thief.
# CT4
The environment is modeled by defining POIs in every location in which an agent could change direction on the map. The rest of the definition is identical to that of CT1.
# CT5
The environment is modeled as in CT4, with three additional POIs: window1,window2 and stairs. To model the capability of the thief to enter or exit the building, a state away is added; when away is true, thief is outside the building, when it is false, thief is inside. Accordingly, location specific events leave1, leave2 and leave3 have been defined to change the state of away to true, and location specific event enter has been defined to turn away to false.
To model the capability of the thief to steal objects in the three locations, three location specific events have been defined (steal1, steal2 and steal3).
These events are included in state dependecies, indeed it will only be possible for thief to perform them if away is f alse.
To model the objective of the control system, the event stolen is introduced. The event stolen represents the act of the thief of successfully stealing an object and leave the floor. This event is included on the rule stealing, which prescribes that after one of the three stealing events has been performed, either the event stolen or the event catch can be performed. Furthermore, stolen can only be triggered when away is true, while catch can only happen if away is false. Finally, the construct use to define the mission is avoid stolen.
# CT6
This scenario is modeled as CT5, with the difference that thief is the controllable agent and policeBot the uncontrollable one. Furthermore, the speeds of the two agents are set equal so that the thief objective is achievable. Finally, the mission is defined with the construct do stolen.
