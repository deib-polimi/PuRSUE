package se.cth.pursue;


//integer values are considered strings at this stage as w ell

public class Clock_cond_constant_2_weak extends Clock_cond{
	private String name1;
	private String name2;


	public Clock_cond_constant_2_weak(String name1,  String name2){
		this.name1 = name1;
		this.name2 = name2;

	}

	@Override
	public String getType(){
		return "constant_2_weak";
	}

	public String getName(){
		return this.name1;
	}
	public String getName2(){
		return this.name2;
	}



	@Override
	public String toString(){
		return ("self."+this.name1 + "<="+"self."+this.name2);
	}




}


