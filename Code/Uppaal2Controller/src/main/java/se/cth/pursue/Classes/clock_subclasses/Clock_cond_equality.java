package se.cth.pursue;


//integer values are considered strings at this stage as w ell

public class Clock_cond_equality extends Clock_cond{
	private String name;
	private String value;

	public Clock_cond_equality(String name, String value){
		this.name = name;
		this.value = value;

	}

	@Override
	public String getType(){
		return "equality";
	}
	public String getName(){
		return this.name;
	}

	public String getValue(){
		return this.value;
	}

	@Override
	public String toString(){
		return (this.value + "=="+"self."+this.name);
	}




}


