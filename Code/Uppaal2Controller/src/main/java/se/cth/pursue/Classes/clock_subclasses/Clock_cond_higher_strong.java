package se.cth.pursue;


//integer values are considered strings at this stage as w ell

public class Clock_cond_higher_strong extends Clock_cond{
	private String name;
	private String value;

	public Clock_cond_higher_strong(String name, String value){
		this.name = name;
		this.value = value;

	}

	@Override
	public String getType(){
		return "higher_strong";
	}
	public String getName(){
		return this.name;
	}

	public String getValue(){
		return this.value;
	}

	@Override
	public String toString(){
		return (this.value + "<"+"self."+this.name);
	}




}


