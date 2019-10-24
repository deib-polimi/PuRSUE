package se.cth.pursue;

import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;

public class Model{

	private String name;
	private Machine state_updater;
	private Boolean hasStates;
	private Set <Machine> regole;
	private Set <Machine> agenti;
	private Set <Machine> obbiettivi;
	private InitialConditions condizioni_iniziali;



	public Model(String str){
		this.name = str;
		this.regole = new  HashSet<Machine>();
		this.agenti = new  HashSet<Machine>();
		this.obbiettivi = new  HashSet<Machine>();
		this.condizioni_iniziali = new InitialConditions();
		this.hasStates = false;
;

	}

	public void addStateUpdater(Machine state_up){
		state_up.setInitialStates(this.condizioni_iniziali.stati_iniziali);
		this.state_updater = state_up;
		this.hasStates = true;

	}



	public void addRule(Machine regola){
		this.regole.add(regola);
	}

	//fondamentale che le condizoni inziali siano create prima degl iagenti xD
	public void addAgent(Machine agente){

		for ( State stat : this.condizioni_iniziali.posizioni_iniziali){
			if (stat.getName().equals('P'+agente.getName())){
				agente.setInitialPosition(stat.getValue());
			}
		
		}
		this.agenti.add(agente);
	}

	public void addObjective(Machine obbiettivo){
		this.obbiettivi.add(obbiettivo);
	}

	public void setInitialConditions(InitialConditions condiz){

		this.condizioni_iniziali = condiz;
	}
	

	@Override
	public String toString() {

		StringBuilder builder = new StringBuilder();

		builder.append("#!/usr/bin/env python\n");
		builder.append("#runtime_observer\n");

		builder.append("\nfrom transitions import Machine\nfrom functools import partial\nimport random\nimport time\nimport rospy\nfrom std_msgs.msg import String");
		if (this.hasStates){
			builder.append(this.state_updater);
		}
		this.regole.forEach(rl -> builder.append(rl));
		this.agenti.forEach(ag -> builder.append(ag));
		this.obbiettivi.forEach(ob -> builder.append(ob));
		builder.append("\n\nclass Observer():");
		//callback function
		//automata evolution
		builder.append("\n\n\tdef callback(self, data):\n\t\ttrigger = data.data\n\t\tfor automaton in self.automa:\n\t\t\tautomaton.trigger(trigger)");
  		//clock update
        builder.append("\n\n\t\tif trigger == \"_start_\":\n\t\t\tself.startTime=time.time()");
		builder.append("\n\t\tself.stopTime = time.time()\n\t\telapsedTime =self.stopTime - self.startTime\n\t\tself.startTime = time.time()\n\t\tfor automaton in self.automa:\n\t\t\tif automaton.need_reset:\n\t\t\t\tautomaton.clock = 0\n\t\t\t\tautomaton.need_reset = False\n\t\t\telse:\n\t\t\t\tautomaton.clock += elapsedTime");
		//message creations
		//varaible declaration
  		builder.append("\n\n\t\tstate = \"\"\n\t\tclocks = \"\"");
  		//automaton position and P
		builder.append("\n\t\tfor automaton in self.automa:\n\t\t\tstate +=\"\\n\"+ automaton.name + \"=\" + automaton.state + \"\\n\"+\"P\"+automaton.name+\"=\"+str(automaton.P)");
  		//clocks
  		builder.append("\n\t\t\tclocks += \"\\n\"+'C'+automaton.name +\"=\" +str(automaton.clock) ");
    	
  		//aggiungo a states gli S
    	if (this.hasStates){
    	builder.append("\n\t\tstate = state + self.automa[0].printStates()" );
    	}
    	//outputtting
  		builder.append("\n\n\t\tprint (\"the following will be sent to state topic:\\n\"+state+\"\\n\\n\"+clocks)\n\t\tself.pub.publish(state+\"\\n\\n\"+clocks)");
		

  		//INITIALIZATION
  		builder.append("\n\n\tdef __init__(self):");
  		//automa initialization
  		builder.append("\n\n\t\tself.automa = []");
  		if (this.hasStates){
  			builder.append("\n\t\tself.automa.append(Class"+state_updater.getName()+"())");
  		}
  		regole.forEach(rl -> builder.append("\n\t\tself.automa.append(Class"+rl.getName()+"())"));
		agenti.forEach(ag -> builder.append("\n\t\tself.automa.append(Class"+ag.getName()+"())"));
		obbiettivi.forEach(ob -> builder.append("\n\t\tself.automa.append(Class"+ob.getName()+"())"));

		//time initialization
		builder.append("\n\n\t\tself.startTime = time.time()\n\t\tself.stopTime = self.startTime");
		
		//communication initializaton
		builder.append("\n\n\t\trospy.init_node('pursue_observer')\n\t\tself.pub = rospy.Publisher('pursue/system_state', String, queue_size=1)");

		//run method 

		builder.append("\n\n\tdef run(self):\n\n\t\trospy.Subscriber(\"pursue/events\", String, self.callback)\n\t\trospy.spin()");
		//mains
		builder.append("\n\ndef main():\n\tobserver = Observer()\n\tobserver.run()\nif  __name__ == \"__main__\":\n\tobserver = Observer()\n\tobserver.run()\n");	

		return builder.toString();
	}




}


