package se.cth.pursue;

import java.util.Set;
import java.util.HashSet;


public class State_block{
	private String informazioni;
	private Set<Status> config;
	private Set <When_block> whens;

	
	public State_block(String str, Set<Status> conf){

	this.informazioni = str;
	this.config = new HashSet <Status>();
	conf.forEach(el -> this.config.add(el));
	this.whens = new HashSet <When_block>();
	}


	public void addStatus(Status stat){	// non utilizzato al momento
		config.add(stat);

	}

	public void addWhen(When_block whe){
		whens.add(whe);

	}


	public Set <When_block> getWhens(){
		return this.whens;
	}

	public Set<Status> getConfig(){
		return this.config;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		StringBuilder state = new StringBuilder();

		//header
		builder.append("\t\t\t"+this.informazioni + "\n");
		//if condition
		builder.append("\t\t\tif ( ");
		config.forEach(s -> state.append("self." + s.getName() + "== \""+ s.getState()+ "\" and " ));
		state.delete(state.length()-4, state.length()-1);
		builder.append(state.toString());
		builder.append(" ):\n");
		//sleep and wait
		int i = 0;
		builder.append("\t\t\t\ttemps=set()\n");
		for (When_block whe : this.whens){
			for (Clock_cond_set setto : whe.getAllConditions()){
				builder.append("\t\t\t\ttemp"+i+"= optimal_wait("+ setto.cleanedConditions()+")\n");
				builder.append("\t\t\t\tif (temp"+i+" >= 0):\n");
				builder.append("\t\t\t\t\ttemps.add(temp"+i+")\n")	;
				i++;	
			}
		}	
		builder.append("\t\t\t\tif(temps):\n");		
		builder.append("\t\t\t\t\twait = min(temps)\n");
		builder.append("\t\t\t\t\tself.event_flag.clear()\n");
		builder.append("\t\t\t\t\tself.event_flag.wait(wait)\n");

		
		
		builder.append("\t\t\t\t\tself.exegg.ping_observer()\n");
		if(!whens.isEmpty()){
			builder.append("\t\t\t\t\tif (" + state.toString()+"):\n");

			whens.forEach(w -> builder.append(w));
		}
		builder.append("\t\t\t\telse:\n");

		builder.append("\t\t\t\t\tself.event_flag.clear()\n");	
		builder.append("\t\t\t\t\tself.event_flag.wait()\n");	

		return builder.toString();


	}




}


