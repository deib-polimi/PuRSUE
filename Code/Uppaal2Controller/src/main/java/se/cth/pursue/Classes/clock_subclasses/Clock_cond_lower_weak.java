package se.cth.pursue;


//integer values are considered strings at this stage as w ell

public class Clock_cond_lower_weak extends Clock_cond{
	private String name;
	private String value;

	public Clock_cond_lower_weak(String name, String value){
		this.name = name;
		this.value = value;

	}

	@Override
	public String getType(){
		return "lower_weak";
	}
	public String getName(){
		return this.name;
	}

	public String getValue(){
		return this.value;
	}

	@Override
	public String toString(){
		return ("self."+this.name + "<="+this.value);
	}




}


