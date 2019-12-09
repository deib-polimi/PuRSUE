package se.cth.pursue;


public class State{
	private String name;
	private int value;

	
	public State(String name, String value){

	this.name =name ;

	this.value=Integer.parseInt(value);

	}

	public void setName(String str){
		this.name = str;
	}

	public void setValue(int val){
		this.value = val;
	}

	public String getName(){
		return this.name;
	}

	public int getValue(){	
		return this.value;

	}





}


