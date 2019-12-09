package se.cth.pursue;


//integer values are considered strings at this stage as w ell

public class Status{
	private String var_name;
	private String var_state;

	public Status(String name, String state){
		this.var_name = name;
		this.var_state = state;

	}


	public String getName(){
		return var_name;
	}
	public String getState(){
		return var_state;
	}




}


