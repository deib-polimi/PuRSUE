package se.cth.pursue;

import java.util.Set;
import java.util.HashSet;


//integer values are considered strings at this stage as w ell
//in qeusto momento ci sono salvati i clock da resettare, ma penso dovrà essere gestito altrove
public class When_block{
	private Set<Clock_cond_set> all_conditions;

	//transition
	private Status origin;
	private Status target;
	private Set<String> clocks;
	private String trigger;

	public When_block(){
		this.all_conditions = new HashSet <Clock_cond_set>();

		this.clocks = new HashSet <String>();
		this.trigger = new String("undefined");
	}


	public void addClockSet(Clock_cond_set ccs ){
		this.all_conditions.add(ccs);
		for (Clock_cond cond : ccs.getAllConditions()){
			if (!cond.getName().equals("undefined"))
				if (!clocks.contains(cond.getName()))
					clocks.add(cond.getName());
			if (!cond.getName2().equals("undefined"))
				if (!clocks.contains(cond.getName2()))
					clocks.add(cond.getName2());
		}


	}

	public Set<Clock_cond_set> getAllConditions(){

		return this.all_conditions;
	}
	public Set<String> getClocks(){
		return this.clocks;
	}

	public void addClock(String clock){
		if (!this.clocks.contains(clock))
			this.clocks.add(clock);
	}

	public void setOrigin(Status stat){
		this.origin = new Status(stat.getName(), stat.getState());

	}
	public void setTarget(Status stat){
		this.target = new Status(stat.getName(), stat.getState());

	}
	public void setTrigger(String str){
		this.trigger = str;
	}

	@Override
	public String toString(){
		StringBuilder builder = new StringBuilder();
		builder.append( "\t\t\t\t\t\tif (");
		this.all_conditions.forEach(c -> builder.append(c + " or "));
		builder.delete(builder.length()-4, builder.length()-1);
		builder.append("):\n");
		builder.append("\t\t\t\t\t\t\t#takes in agent ID, synchronizing action (or tau), and the states or ogirin and target of transition\n");
		builder.append("\t\t\t\t\t\t\tself.exegg.exeggute(\"" + this.origin.getName() + "\", \""+ this.trigger +"\", \"" + this.origin.getState() + "\", \"" + this.target.getState()  +"\")\n");

		return builder.toString();
	} 



}


