package se.cth.pursue;

import java.util.Set;
import java.util.HashSet;


public class InitialConditions{
	public Set <State> stati_iniziali;
	public Set <State> posizioni_iniziali;


	
	public InitialConditions(){

	this.stati_iniziali= new HashSet <State>() ;
	this.posizioni_iniziali=new HashSet <State>();

	}

		public void addInitialState(State stat){
		this.stati_iniziali.add(stat);
	}

	public void addInitialState(String name, String value){
		State stat = new State(name, value);
		this.stati_iniziali.add(stat);
	}

		public void addInitialPosition(State pos){
		this.posizioni_iniziali.add(pos);
	}

		public void addInitialPosition(String name, String value){
		State pos = new State(name, value);
		this.posizioni_iniziali.add(pos);
	}





}


