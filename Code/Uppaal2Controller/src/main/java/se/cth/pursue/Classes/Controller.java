package se.cth.pursue;

import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;

public class Controller{

	private String informazioni;
	private Set <State_block> stati;
	private Set <String> all_clocks;
	private Set <String> all_states;

	public Controller(String str){
		this.informazioni = str;
		this.stati = new  HashSet<State_block>();
		this.all_clocks = new HashSet<String>();
		this.all_states = new HashSet<String>();

	}

	public void addState(State_block stato){
		this.stati.add(stato);

	}

	public void getAllClocks(){
		for (State_block stato : this.stati)
			for (When_block when : stato.getWhens())
				for (String clock : when.getClocks()){
					if (!this.all_clocks.contains(clock))
						this.all_clocks.add(clock);
					}

	}
	//LOG delle porcate: qui le variabili di stato sono trattate come stringhe, sarebbe bello tornassero ad interi un bel giorno
	public void getAllStates(){
		List <State_block> temp = new ArrayList<State_block>();
		temp.addAll(this.stati);
		Set <Status> temp2 = new HashSet<Status>();
		temp2.addAll(temp.get(0).getConfig()); //add all states from any of the states
		for (Status s : temp2)
			this.all_states.add(s.getName());

	}

	@Override
	public String toString() {
		this.getAllClocks(); //la faccio qui così ho già rimepito la struttura dato
		this.getAllStates();
		StringBuilder builder = new StringBuilder();
		builder.append("#!/usr/bin/env python\n");
		builder.append("#runtime_controller\n");
		//imports


		builder.append("import sys\nimport random\nfrom pursue_library import *\nimport exeggutor\nimport rospy\nfrom std_msgs.msg import String\nfrom time import sleep\nfrom threading import Event\n");
		//class header
		builder.append("class Runtime_controller:\n\n");
		//updateclocks funciton
		//builder.append("\tdef update_clocks(self, elapsedTime):\n");	
		//this.all_clocks.forEach(cl -> builder.append("\t\tself."+cl+"+= elapsedTime\n"));

		builder.append("\n\n\tdef if_start(self, event_string):");
		builder.append("\n\t\tif (event_string.data == \"_start_\"):");
		builder.append("\n\t\t\tself.startFlag = True");
		builder.append("\n\t\treturn");

		builder.append("\n\n\tdef update_state(self, state_string):");
		builder.append("\n\t\tif hasattr(state_string, 'data'):");
		builder.append("\n\t\t\tall_updates=state_string.data.split(\"\\n\\n\")");
		builder.append("\n\t\telse:");
		builder.append("\n\t\t\tall_updates=state_string.split(\"\\n\\n\")");
		builder.append("\n\t\tstate_updates =all_updates[0].split(\"\\n\")");
		builder.append("\n\t\tfor st in state_updates:");
		builder.append("\n\t\t\tstate_and_value = st.split(\"=\")");
		this.all_states.forEach(st -> builder.append("\n\t\t\tif (state_and_value[0]==\""+st+"\"):\n\t\t\t\tself."+st+"=state_and_value[1]"));
		builder.append("\n\t\tclock_updates =all_updates[1].split(\"\\n\")");
		builder.append("\n\t\tfor cl in clock_updates:");
		builder.append("\n\t\t\tclock_and_value = cl.split(\"=\")");
		this.all_clocks.forEach(cl -> builder.append("\n\t\t\tif (clock_and_value[0]==\""+cl+"\"):\n\t\t\t\tself."+cl+"=float(clock_and_value[1])"));

		builder.append("\n\t\tself.event_flag.set()");		
		builder.append("\n\t\tself.print_state()");		


		//initialization NOTA: per ora la timeunit è fissa, sarebbe da dare nella DSL
		builder.append("\n\n\tdef __init__(self):");	
		builder.append("\n\t\trospy.init_node('pursue_controller_node')");	
		builder.append("\n\n\t\tself.TIMEUNIT = 0.1");

		builder.append("\n\t\tself.startFlag= False");
		builder.append("\n\t\tself.event_flag = Event()");	
		builder.append("\n\t\tself.event_flag.clear()");	

		builder.append("\n\t\tself.exegg = exeggutor.Exeggutor(self.TIMEUNIT)");	
		this.all_clocks.forEach(cl -> builder.append("\n\t\tself."+cl+"= 0"));
		this.all_states.forEach(st -> builder.append("\n\t\tself."+st+"= \"\""));
		builder.append("\n\t\trospy.Subscriber(\"pursue/system_state\", String, self.update_state)");	
		builder.append("\n\t\trospy.Subscriber(\"pursue/events\", String, self.if_start)");	
		builder.append("\n\t\tsleep(1)");	
		builder.append("\n\t\tprint(\"waiting for start signal\")");
		builder.append("\n\t\twhile (not self.startFlag):\n\t\t\tsleep(0.2)");	


		builder.append("\n\n\tdef print_state(self):");
		builder.append("\n\t\tprint(\"the system state is:\")");
		this.all_states.forEach(st -> builder.append("\n\t\tprint(\""+st+" is \",self."+st+")"));
		this.all_clocks.forEach(cl -> builder.append("\n\t\tprint(\""+cl+" is \",self."+cl+")"));
		//run loop
		builder.append("\n\n\tdef run(self):\n");		
		builder.append("\n\t\twhile(not rospy.is_shutdown()):\n");	
		builder.append("\n\t\t\tsleep(self.TIMEUNIT)\n");				
		stati.forEach(s -> builder.append(s+ "\n"));



		//main

		builder.append("def main():\n\tcontrollore = Runtime_controller()\n\tcontrollore.run()\nif  __name__ == \"__main__\":\n\tcontrollore = Runtime_controller()\n\tcontrollore.run()\n");	

		return builder.toString();
	}




}


