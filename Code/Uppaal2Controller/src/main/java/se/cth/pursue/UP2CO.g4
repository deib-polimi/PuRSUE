



grammar UP2CO;

options {
/*language = Python2;*/


}
@header {
   package se.cth.pursue;
   import java.util.Set;
   import java.util.HashSet;
} 




controller returns [Controller contr]

	@init
	{
		System.out.println("I start parsing!");
		String str = "#Controller header";
		$contr = new Controller(str);



	}

	:
	//ANYTHING_BEFORE 
	(stato = state_block 


		{
			//System.out.println("new state!");

			$contr.addState($stato.stato);
		}



		('\n' | <EOF>) )+ 
		
		{

		}
	;




state_block returns [State_block stato]

	:
	'State: ' (config = state_if) 
	{
		
		$stato = new State_block("#state header", $config.sts);


	}

	(


		while_block | whe = when_block

		{
			$stato.addWhen($whe.when);
		}

		)+
	;


state_if returns [Set<Status> sts]
	@init
	{
		//System.out.println("new if_block!");
		 $sts = new HashSet<Status>();
	}
	:
	'(' ' ' (state = automa_state ' '

	{
		$sts.add($state.stat);
	}

	)+ ')' ' ' (variable = state_variable ' '
	{
		$sts.add($variable.stat);
	}

	)+ '\n' 

	;


/*Non elegante, matcha non qualunque carattere ma qualunque token, problema è che se metto uan regola per qualnque carattere tra parentesi todne poi non le posso più usare xD*/
/*nota: lui mangia tutte le transizioni, ma salva solo la prima, le sincronizzazioni sono gestite dall'observer*/
while_block
	:
	{
		//System.out.println("new while_block!");
	}
	'While you are in '( ('true') | ( (clock_conditions_set) (' ' OR ' ' clock_conditions_set)*) )', wait.\n'
	;



when_block returns [When_block when]
	:
	{
		//System.out.println("new when_block!");
		$when = new When_block();

	}
	'When you are in 'set = clock_conditions_set 

	{ 
		$when.addClockSet($set.condizioni);

	}

	(' ' OR ' ' other_set = clock_conditions_set

		 
	{ 
		$when.addClockSet($other_set.condizioni);

	}

	)*?

	', take transition ' transiz = transition'\n' (transition'\n')*?
	{
		$when.setOrigin($transiz.origin);
		$when.setTarget($transiz.target);
		$when.setTrigger($transiz.syncro);
	}
	;


clock_conditions_set returns [Clock_cond_set condizioni]
	:
	{
		//System.out.println("new clock condition set");
		$condizioni = new Clock_cond_set();

	}

	'('(cond = clock_condition)
		{
			//System.out.println("new clock condition");
			$condizioni.addCond($cond.condizione);
		}


	 (' 'AND' 'cond = clock_condition

	 	{
	 		//System.out.println("other clock condition");
	 		$condizioni.addCond($cond.condizione);
	 	}


	 )*? ')'
	;

/* constant conditios are the one betweeen two clocks, that will thus not change withthe passage of time*/
clock_condition returns [Clock_cond condizione]
	:
		(

		cond1 = clock_higher_strong 

			{
			$condizione = $cond1.condo;
			}


		| cond2 = clock_higher_weak 

			{
			$condizione = $cond2.condo;
			}
		



		| cond3 = clock_lower_strong 

			{
			$condizione = $cond3.condo;
			}


		| cond4 = clock_lower_weak 

			{
			$condizione = $cond4.condo;
			}

		| cond10 = clock_equal

			{
			$condizione = $cond10.condo;
			}

		| cond5 =clock_constant_condition_equality

			{
			$condizione = $cond5.condo;
			}

		|cond11 = clock_constant_condition_1_equality

			{
			$condizione = $cond11.condo;
			}

		| cond6 =clock_constant_condition_1_strong 
			{
			$condizione = $cond6.condo;
			}


		| cond7 = clock_constant_condition_1_weak 

			{
			$condizione = $cond7.condo;
			}
		| cond8 = clock_constant_condition_2_strong

			{
			$condizione = $cond8.condo;
			}
		| cond9 =clock_constant_condition_2_weak
			{
			$condizione = $cond9.condo;
			}


		)

	;

clock_higher_strong returns [Clock_cond_higher_strong condo]
	:
	val = INT SMALLER_STRONG id = CLOCK_ID
	{$condo = new Clock_cond_higher_strong($id.text, $val.text);}
	;

clock_higher_weak returns [Clock_cond_higher_weak condo]
	:
	val = INT SMALLER_WEAK  id = CLOCK_ID
	{$condo = new Clock_cond_higher_weak($id.text, $val.text);}
	;

clock_lower_strong returns [Clock_cond_lower_strong condo]
	:
 	id = CLOCK_ID SMALLER_STRONG val = INT
 	{$condo = new Clock_cond_lower_strong($id.text, $val.text);}
	;

clock_lower_weak returns [Clock_cond_lower_weak condo]
	:
 	id = CLOCK_ID SMALLER_WEAK val = INT
 	{$condo = new Clock_cond_lower_weak($id.text, $val.text);}
	;


clock_equal returns [Clock_cond_equality condo]
	:
	id = CLOCK_ID EQUALS val = INT
	{$condo = new Clock_cond_equality($id.text, $val.text);
		//this condition is ognored in all forther generation
	}
	;


clock_constant_condition_equality returns [Clock_cond_constant_equality condo]
	:
	id1 = CLOCK_ID EQUALS id2 = CLOCK_ID
 	{$condo = new Clock_cond_constant_equality($id1.text, $id2.text);}
	;
clock_constant_condition_1_equality returns [Clock_cond_constant_1_equality condo]
	:
	id1=CLOCK_ID '-' id2=CLOCK_ID EQUALS value=INT
	{$condo = new Clock_cond_constant_1_equality($id1.text, $id2.text, $value.text);}
	;

clock_constant_condition_1_strong returns [Clock_cond_constant_1_strong condo]
	:
	id1=CLOCK_ID '-' id2=CLOCK_ID SMALLER_STRONG value=INT

 	{$condo = new Clock_cond_constant_1_strong($id1.text, $id2.text, $value.text);}
	;

clock_constant_condition_1_weak returns [Clock_cond_constant_1_weak condo]
	:
	id1 = CLOCK_ID '-' id2 = CLOCK_ID SMALLER_WEAK value =INT
 	{$condo = new Clock_cond_constant_1_weak($id1.text, $id2.text, $value.text);}
	;

clock_constant_condition_2_strong returns [Clock_cond_constant_2_strong condo]
	:
	id1 = CLOCK_ID SMALLER_STRONG id2 =CLOCK_ID
 	{$condo = new Clock_cond_constant_2_strong($id1.text, $id2.text);}

	;

clock_constant_condition_2_weak returns [Clock_cond_constant_2_weak condo]
	:
	id1 = CLOCK_ID SMALLER_WEAK id2 =CLOCK_ID
 	{$condo = new Clock_cond_constant_2_weak($id1.text, $id2.text);}
	;

transition returns [Status origin, Status target, Set<String> clocks, String syncro]
	@init
	{
		$clocks = new HashSet<String>();
		$syncro = new String();
	}
	:
	origine = automa_state '->' targeto = automa_state' ' '{' ' ' preconditions 
			' ' (sync = SYNC_MASTER 
				{
					$syncro = $sync.text;
				}
				| synch = SYNC_SLAVE 
				{
					$syncro = "undefined"; //decision for now to treat slave syncs as undefined, trated by observer
				}
				| 'tau'
				{
					$syncro = "tau";
				}

				) 

			(','' ' ( (POSITION_ID ASSIGNMENT INT) 
				| (STATE_ID ASSIGNMENT INT)
				| (clock = CLOCK_ID ASSIGNMENT INT) 

				| INT )
			)*?' ' '}'
	{
		$origin = $origine.stat;
		$target = $targeto.stat;
	}
	;

/*questa definizione un pò porcata funziona perchè le sto facendo io con l'altro parser queste*/
preconditions
	:
	(( (CLOCK_ID ' > ' INT) (' ' AND ' '(POSITION_ID| STATE_ID)' ' EQUALS ' ' (INT| POSITION_ID) )*?)| INT ) ','
	;


automa_state returns [ Status stat]
	:
	(id = ID) '.' ('_')? (loc = ID)
	{
		$stat = new Status($id.text,  $loc.text);


	}
	;

state_variable returns [ Status stat]
	:
	((id = POSITION_ID) '=' (val = INT) |(id = STATE_ID) '=' (val = INT) )
	{
		$stat = new Status($id.text,  $val.text);

	}
	;



/*lerser rules */





/*must start with letter to distinguish from INT and NOT A CAPITAL LETTER!!!, ignorant exception madefor OBJ, to be fixed*/
ID
	:
	('O'|LOWER)(ACCEPTED_CHARACTER)*
	;
CLOCK_ID
	:
	('C')(ID)
	;
POSITION_ID
	:
	('P')(ID)
	;
STATE_ID
	:
	('S')(ID)
	;
INT	
	:
	'-'? (DIGIT)+
	;
SYNC_MASTER
	:
	ID('!')
	;

SYNC_SLAVE
	:
	ID('?')
	;


ACCEPTED_CHARACTER
	: 
	(LETTER | DIGIT | ACCEPTED_SYMBOL)
	;

ASSIGNMENT
	:
	' := '
	;

SMALLER_STRONG
	:
	'<'
	;

SMALLER_WEAK
	:
	'<='
	;

EQUALS
	:
	'=='
	;

AND
	:
	'&&'
	;

OR
	:
	'||'
	;




//ANYTHING_BEFORE
//	:
//	 .*? ':\n\n'
//	;




fragment LETTER: (LOWER | UPPER);
fragment LOWER: 'a'..'z';
fragment UPPER: 'A'..'Z';
fragment DIGIT: '0'..'9';
fragment ACCEPTED_SYMBOL: '_'; 
fragment NON_ACCEPTED_SYMBOL: '!' | '#'..'/' | ':'..'@' | '['..'^' | '`' | '{'..'~';

WS : ( '\t' | '\r') -> skip ;








