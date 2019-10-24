package se.cth.pursue;

import java.util.Set;
import java.util.HashSet;


public class Machine{
	private String name;
	private String initial_location;
	private Set<Transition> transizioni;
	private Set <String> locazioni;
	private Set <State> stati;
	private int initial_position;

	
	public Machine(){

	this.name ="default" ;
	this.initial_location="default";
	this.transizioni = new HashSet <Transition>();
	this.locazioni = new HashSet <String>();
	this.stati = new HashSet<State>();
	this.initial_position = 0;
	}

	public void setName(String str){
		this.name = str;
	}

	public void setInitialLocation(String str){
		this.initial_location = str;
	}

	public String getName(){
		return this.name;
	}

	public Set<State> getStates(){
		return this.stati;
	}

	public void addLocation(String loc){	
		locazioni.add(loc);

	}

	public void addTransition(Transition tran){
		tran.setAgentName(this.name);
		transizioni.add(tran);

	}

	public void setInitialStates(Set<State> stat){
		stat.forEach(st -> this.stati.add(st));

	}

	public void setInitialPosition(int p){
		this.initial_position = p;
	}



	@Override
	public String toString() {



		StringBuilder builder = new StringBuilder();

		builder.append("\n\n\nclass Class"+this.name+"():");

		//reset clock method
		builder.append("\n\n\tdef reset_clock(self):\n\t\tself.need_reset = True");

		//trigger method
		//faccio uan finta lista transizioni per togliere i doppioni...
		Set <Transition> tranzi = new HashSet<Transition>();
		Set <String> tranziaggiunte = new HashSet<String>();
		for (Transition complete : this.transizioni){
			if ( !tranziaggiunte.contains(complete.getSynch()) ){
					tranzi.add(complete);
					tranziaggiunte.add(complete.getSynch());
				}
		}
		//poi stampo iltrigger
		builder.append("\n\n\tdef trigger(self, trigger):");
		if (!this.transizioni.isEmpty()){
			builder.append("\n\t\tif (trigger in self.machine.get_triggers(self.state)):");
			tranzi.forEach(tr -> builder.append(tr.printForTrigger()));
		}
		//update Position method
		else {
			builder.append("\n\t\treturn");
		}
		builder.append("\n\n\tdef updateP(self, newP):\n\t\tself.P = newP");

		//state updater method
		if (!stati.isEmpty()){//funzione print states se ce ne sono
			builder.append("\n\n\tdef printStates(self):");
			builder.append("\n\t\tstati = \"\"");
			this.stati.forEach(st -> builder.append("\n\t\tstati  = stati +\"\\n"+st.getName()+"=\"+str(self."+st.getName()+")"));
			builder.append("\n\t\treturn stati");
		}
		//initialization
		builder.append("\n\n\tdef __init__(self):\n\t\tself.name=\""+this.name+"\"\n\t\tself.need_reset = False\n\t\tself.clock=0.0");
		builder.append("\n\t\tself.P ="+this.initial_position);
		this.stati.forEach(stt -> builder.append("\n\t\tself."+stt.getName()+"="+stt.getValue()));
		builder.append("\n\n\t\tstates =[");
		this.locazioni.forEach(state -> builder.append("'"+state+"',"));
		builder.delete(builder.length()-1, builder.length());
		builder.append("]\n\t\ttransitions = [");
		this.transizioni.forEach(tr -> builder.append("\n\t\t\t"+tr.printForTransitions()+","));
		if (!this.transizioni.isEmpty()){
			builder.delete(builder.length()-1, builder.length());
		}
		builder.append("\n\t\t]");

		builder.append("\n\n\t\tself.machine= Machine(model = self, states=states, transitions=transitions, initial='"+this.initial_location+"',auto_transitions=False)");


		return builder.toString();


	}




}


