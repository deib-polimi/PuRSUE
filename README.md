
# PuRSUE
<b>PuRSUE</b> (From Specification of Robotic Environments to Synthesis of Controllers) is an approach that supports developers in the rigorous and systematic design of high-level run-time control strategies for robotic applications. The approach includes PuRSUE-ML a high-level  language that allows modelling the environment, the agents deployed therein, and their missions. PuRSUE is able to automatically check whether a controller that allows robots to achieve their missions might exist and, then, it synthesises a controller.


### Organisation of the Repository
The repository is organised in different folders as follows:
- <i>Scenarios</i>: contains the scenarios considered in the evaluation
- <i>PuRSUE</i>: contains the PuRSUE components, installation instruction


## Installation
- The instructions to install PuRSUEML can be found in <a href="https://github.com/deib-polimi/PuRSUE/tree/master/Code/PURSUEML">https://github.com/deib-polimi/PuRSUE/tree/master/Code/PURSUEML</a>


## Deployment and Runtime environment
Branch deploy-alpha contains
- <i>Uppaal2Controller</i>, that translates the Uppaal-TIGA output into a Python executable controller;
- <i>Uppaal2Observer</i>, that translates the TGA model into an observer component, and
- <i>Uppaal2Deployment</i>, that realizes the deployment of the controller and the observer in the environment, and makes use of the output of the previous two components.
- <i>TurteBot-environment</i> includes all the executables used to test the EcoBot scenario in a real environment.
