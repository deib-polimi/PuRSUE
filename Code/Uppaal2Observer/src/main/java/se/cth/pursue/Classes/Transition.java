package se.cth.pursue;

import java.util.Set;
import java.util.HashSet;


public class Transition{
	private String source;
	private String target;
	private String synchronization;

	private Boolean clock_reset;

	private String agentName;

	private boolean position_set;
	private int position_value;
	

	private boolean state_set;
	private int state_value;
	private String state_name;

	
	public  Transition(String sou, String tar){

	this.source =sou ;
	this.target=tar;
	this.synchronization = "undefined";
	this.clock_reset = false;
	this.position_set = false;
	this.position_value = 0;

	this.state_set = false;
	this.state_value = 0;

	this.agentName = "undefined";
	}

	public void setSynch(String str){
		this.synchronization = str;
	}

	public void clockReset(){
		this.clock_reset = true;
	}

	
	public void setAgentName(String name){
		this.agentName=name;
		if (this.synchronization == "undefined"){
			this.synchronization = this.agentName+"_"+this.source+"2"+this.target;
		}

	}
	
	public String getSynch(){
		return this.synchronization;
	}

	public void setPositionSet(String value){
		this.position_set = true;
		this.position_value = Integer.parseInt(value);
	}


	//aggiunto per stati ora
	public void setStateSet(String name, String value){
		this.state_set = true;
		this.state_value = Integer.parseInt(value);
		this.state_name = name;
	}

	//tutte hanno clock reset tranne quelle transitive, quindi loro avranno una cosa speciale per distinguerle a livello ditrigger, ma non di
	public String printForTrigger(){
		StringBuilder builder = new StringBuilder();
		builder.append("\n\t\t\tif (trigger==\""+this.synchronization+"\"):\n\t\t\t\tself."+this.synchronization+"()");
		//removed cause now taken care of in transition
		//if(position_set){
		//	builder.append("\n\t\t\t\tself.P =\""+this.position_value+"\"");
		//}
		if(state_set){
			builder.append("\n\t\t\t\tself."+this.state_name+"=\""+this.state_value+"\"");
		}		
		return builder.toString();
	}

	public String printForTransitions(){
		StringBuilder builder = new StringBuilder();
		builder.append("{'trigger' : '"+this.synchronization+"' , 'source' : '"+this.source+"' , 'dest' : '"+this.target+"'");
		if (this.position_set)
			builder.append(", 'before' : partial(self.updateP, '"+this.position_value+"')");
		if (clock_reset)
			builder.append(", 'after' : 'reset_clock'");
		builder.append(" }");
		return builder.toString();

	}


	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		
		return builder.toString();


	}




}


