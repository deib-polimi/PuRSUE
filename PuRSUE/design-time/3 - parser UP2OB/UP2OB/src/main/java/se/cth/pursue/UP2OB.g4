 



grammar UP2OB;

options {
/*language = Python2;*/

}
@header {
	package se.cth.pursue;

   import java.util.Set;
   import java.util.HashSet;
} 




model returns [Model mod]

	@init
	{
		String str = "#Model name";
		$mod = new Model(str);
	}

	:

	'<nta>'
	declared = declaration_block
	{
		$mod.setInitialConditions($declared.dichiarazioni);
	}
	'automata_declaration'
	('state_updater'

	mac = machine_block
	{
		$mod.addStateUpdater($mac.machine);
	}
	)?
	'rules'
	(reg = machine_block

		
		{
			$mod.addRule($reg.machine);
		}
		


	)*? 
		
	'agents' /* da aggiungere al primo parser*/
	(agent = machine_block

	
		{
			$mod.addAgent($agent.machine);
		}
	


	)*? 

	'objectives'

	(obj = machine_block

		{
			$mod.addObjective($obj.machine);
		}

	)*? 

	SYSTEM_DECLARATION
	'</nta>'
	EOF
	;

	

declaration_block returns [InitialConditions dichiarazioni]
	@init
	{
		$dichiarazioni = new InitialConditions();

	}
	:
	'<declaration>'
	{

	}
	'broadcast chan ' (COMMA | ID |CHAN_DEC)* SEMICOLON
	'broadcast chan ' (COMMA | ID |CHAN_DEC)*  SEMICOLON

	('int ' (POSITION_ID ASSIGNMENT INT | ',')* SEMICOLON)?
	'clock ' (CLOCK_ID | COMMA)* SEMICOLON

	'int '( name = POSITION_ID ASSIGNMENT value = INT 

	{

		$dichiarazioni.addInitialPosition($name.text, $value.text);

	}
	| COMMA 

		)+ SEMICOLON

	('int ' (name = STATE_ID ASSIGNMENT value = INT
		{
		$dichiarazioni.addInitialState($name.text, $value.text);
		}
		| COMMA 
		)*
		 SEMICOLON )?

	('clock ' CLOCK_ID SEMICOLON)?
	('clock ' CLOCK_ID SEMICOLON)?
	'</declaration>'
	;



machine_block returns [Machine machine]
	@init
	{
		$machine = new Machine();
	}
	:
	'<template>' 
		'<name>' nome = ID '</name>'
		
		{
		$machine.setName($nome.text);
		}

		(loc = location_block
			{
			$machine.addLocation($loc.loc);
			}
		)+

		'<init ref = ' '"'init =ID'"' '/>'	
			{
			$machine.setInitialLocation($init.text);
			}

		(tran = transition_block

			{
			$machine.addTransition($tran.tran);
			}

			)*?
	'</template>'
	;

location_block returns [String loc]
	:
	('<location id='|'<location id = ' ) '"' loc_id = ID '"' '>'
	{
		$loc = $loc_id.text;
		
	}
	('<name>'ID'</name>')?

	('<label kind="invariant">'CLOCK_ID SMALLER_WEAK INT'</label>')?

	'</location>'


	;

transition_block returns [Transition tran]
	:
	('<transition>' | '<transition controllable="false" >')
		'<source ref=' '"'source = ID '"' '/>'
		'<target ref=' '"'target = ID'"' '/>'
	{
		$tran = new Transition($source.text, $target.text);
	}

	(
		('<label kind="synchronisation">'(synch = ID'!'|synch = ID'?')'</label>')
		{
			$tran.setSynch($synch.text);
		}
	|
		( ('<label' 'kind' ASSIGNMENT '"assignment">')

			(CLOCK_ID ASSIGNMENT INT

			{
				$tran.clockReset(); //I assume any clock assignment is a reset
			}
			|


			POSITION_ID ASSIGNMENT value = INT

			{
				$tran.setPositionSet($value.text);
			}

			|

			state_name = STATE_ID ASSIGNMENT value = INT

			{
				$tran.setStateSet($state_name.text, $value.text);
			}

			|COMMA


			)*?'</label>')
	|
		('<label' 'kind' ASSIGNMENT '"guard">'(CLOCK_ID GREATER_STRONG INT | POSITION_ID EQUALS INT | STATE_ID EQUALS INT | AND  | PAR_OPEN | PAR_CLOSE)*'</label>')
	)*?

	'</transition>'

	;


/*must start with letter to distinguish from INT and NOT A CAPITAL LETTER!!!, ignorant exception madefor OBJ, to be fixed*/

	CHAN_DEC
	:
	(ID)(COMMA)
	;

ID
	:
	(LOWER)(ACCEPTED_CHARACTER)*
	;
CLOCK_ID
	:
	('C')(ID)
	;

COMMA
	:
	','
	;

SEMICOLON
	:
	';'
	;

PAR_OPEN
	:
	'('
	;

PAR_CLOSE
	:
	')'
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


ACCEPTED_CHARACTER
	: 
	(LETTER | DIGIT | ACCEPTED_SYMBOL)
	;

ASSIGNMENT
	:
	'='
	;


SMALLER_WEAK
	:
	'&lt;='
	;

GREATER_STRONG
	:
	'&gt;'
	;
EQUALS
	:
	'=='
	;

AND
	:
	'&amp;&amp;'
	;






SYSTEM_DECLARATION
	:
	'<system>'.*'</system>'
	;




fragment LETTER: (LOWER | UPPER);
fragment LOWER: 'a'..'z';
fragment UPPER: 'A'..'Z';
fragment DIGIT: '0'..'9';
fragment ACCEPTED_SYMBOL: '_'; 
fragment NON_ACCEPTED_SYMBOL: '!' | '#'..'/' | ':'..'@' | '['..'^' | '`' | '{'..'~';

WS 
	: 
	( '\t' | '\r' | 'true' | '\n' | ' ') -> skip 
	;

LINE_COMMENT
    : 
    '//' ~[\r\n]* -> skip
	;





