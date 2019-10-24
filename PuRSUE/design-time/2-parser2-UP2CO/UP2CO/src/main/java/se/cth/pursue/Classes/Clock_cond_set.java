package se.cth.pursue;

import java.util.Set;
import java.util.HashSet;
//integer values are considered strings at this stage as w ell

public class Clock_cond_set{

	private Set<Clock_cond> clock_higher;
	private Set<Clock_cond> clock_lower;
	private Set<Clock_cond> constant;

	public Clock_cond_set() {
		this.clock_higher = new HashSet<Clock_cond>();
		this.clock_lower = new HashSet<Clock_cond>();
		this.constant = new HashSet<Clock_cond>();

	}

	//first I divide conditions like so, then I add a function (3 in fact) that further discriminates do generate the actual input for "optimal timing"
	public void addCond(Clock_cond condizione){
		String type = condizione.getType();
		switch (type){
			case "higher_strong": case "higher_weak": 
				this.clock_higher.add(condizione);
				break;
			case "lower_strong": case "lower_weak":
				this.clock_lower.add(condizione);
				break;
			case "constant_equality": case "constant_1_equality":
			case "constant_1_strong": case "constant_1_weak":
			case "constant_2_strong": case "constant_2_weak":

				this.constant.add(condizione);
			default:
				break;
			}
	}
	public Set <Clock_cond>  getAllConditions(){
		Set <Clock_cond> all_conditions = new HashSet<Clock_cond>();
		all_conditions.addAll(this.clock_higher);
		all_conditions.addAll(this.clock_lower);
		all_conditions.addAll(this.constant);
		return all_conditions;

	}
	
	//this functions print the conditions as required by the function "optimal_wait"
	public String higherCleaned(){
		StringBuilder builder = new StringBuilder();
		for (Clock_cond condi : clock_higher){
			String type = condi.getType();
			if (type.equals("higher_strong"))
				builder.append(condi.getValue()+" + self.TIMEUNIT" + "-" + "self."+condi.getName());
			if (type.equals("higher_weak"))
				builder.append(condi.getValue() + "-" + "self."+condi.getName());

			builder.append(", ");


		}
		if (builder.length()>=2)
			builder.delete(builder.length()-2, builder.length()-1);
		return builder.toString();
	}


	public String lowerCleaned(){
		StringBuilder builder = new StringBuilder();
		for (Clock_cond condi : clock_lower){
			String type = condi.getType();
			if (type.equals("lower_strong"))
				builder.append("self."+condi.getName()+ "-" + condi.getValue() + " - self.TIMEUNIT");
			if (type.equals("lower_weak"))
				builder.append("self."+condi.getName() + "-" + condi.getValue());
			builder.append(", ");
		}
		if (builder.length()>=2)
			builder.delete(builder.length()-2, builder.length()-1);
		return builder.toString();
	}

	public String constantCleaned(){
		StringBuilder builder = new StringBuilder();
		for (Clock_cond condi : constant){
			String type = condi.getType();
			if (type.equals("constant_equality"))
				builder.append("self."+condi.getName()+ "-" + "self."+condi.getName2());
			if (type.equals("constant_1_equality")) //I pass -(n -(A-B)*2 ), always negative if different from zero
				builder.append("-("+condi.getValue()+ "-(" +"self."+condi.getName() + "-" + "self."+condi.getName2()+ "))*("+condi.getValue()+ "-(" +"self."+condi.getName() + "-" + "self."+condi.getName2()+"))");
			if (type.equals("constant_1_strong"))
				builder.append(condi.getValue()+"- self.TIMEUNIT"+ "-(" +"self."+condi.getName() + "-" + "self."+condi.getName2()+ ")");
			if (type.equals("constant_1_weak"))
				builder.append(condi.getValue()+ "-(" +"self."+condi.getName() + "-" + "self."+condi.getName2()+ ")");
			if (type.equals("constant_2_strong"))
				builder.append( "self."+condi.getName2()+"+ self.TIMEUNIT" + "-" + "self."+condi.getName());
			if (type.equals("constant_2_weak"))
				builder.append( "self."+condi.getName2() + "-" + "self."+condi.getName());
			builder.append(", ");
		}
		if (builder.length()>=2)
			builder.delete(builder.length()-2, builder.length()-1);
		return builder.toString();
	}

	public String cleanedConditions(){
		StringBuilder builder = new StringBuilder();
		builder.append("[ " + this.higherCleaned() + "] , " + "[ " + this.lowerCleaned() + "] , [" + this.constantCleaned() + "]" ); 
		return builder.toString();

	}	

	@Override
	public String toString(){
		StringBuilder builder = new StringBuilder();
		builder.append( " (");
		this.clock_higher.forEach(s -> builder.append(s+ " and "));
		this.clock_lower.forEach(s -> builder.append(s+ " and "));
		this.constant.forEach(s -> builder.append(s+ " and "));
		builder.delete(builder.length()-5, builder.length()-1);
		builder.append(") ");
		return builder.toString();

	}


}


