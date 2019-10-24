// Generated from UP2CO.g4 by ANTLR 4.7.1

   package se.cth.pursue;
   import java.util.Set;
   import java.util.HashSet;

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class UP2COParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, ID=21, CLOCK_ID=22, POSITION_ID=23, STATE_ID=24, 
		INT=25, SYNC_MASTER=26, SYNC_SLAVE=27, ACCEPTED_CHARACTER=28, ASSIGNMENT=29, 
		SMALLER_STRONG=30, SMALLER_WEAK=31, EQUALS=32, AND=33, OR=34, WS=35;
	public static final int
		RULE_controller = 0, RULE_state_block = 1, RULE_state_if = 2, RULE_while_block = 3, 
		RULE_when_block = 4, RULE_clock_conditions_set = 5, RULE_clock_condition = 6, 
		RULE_clock_higher_strong = 7, RULE_clock_higher_weak = 8, RULE_clock_lower_strong = 9, 
		RULE_clock_lower_weak = 10, RULE_clock_equal = 11, RULE_clock_constant_condition_equality = 12, 
		RULE_clock_constant_condition_1_equality = 13, RULE_clock_constant_condition_1_strong = 14, 
		RULE_clock_constant_condition_1_weak = 15, RULE_clock_constant_condition_2_strong = 16, 
		RULE_clock_constant_condition_2_weak = 17, RULE_transition = 18, RULE_preconditions = 19, 
		RULE_automa_state = 20, RULE_state_variable = 21;
	public static final String[] ruleNames = {
		"controller", "state_block", "state_if", "while_block", "when_block", 
		"clock_conditions_set", "clock_condition", "clock_higher_strong", "clock_higher_weak", 
		"clock_lower_strong", "clock_lower_weak", "clock_equal", "clock_constant_condition_equality", 
		"clock_constant_condition_1_equality", "clock_constant_condition_1_strong", 
		"clock_constant_condition_1_weak", "clock_constant_condition_2_strong", 
		"clock_constant_condition_2_weak", "transition", "preconditions", "automa_state", 
		"state_variable"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'\n'", "'State: '", "'('", "' '", "')'", "'While you are in '", 
		"'true'", "', wait.\n'", "'When you are in '", "', take transition '", 
		"'-'", "'->'", "'{'", "'tau'", "','", "'}'", "' > '", "'.'", "'_'", "'='", 
		null, null, null, null, null, null, null, null, "' := '", "'<'", "'<='", 
		"'=='", "'&&'", "'||'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, "ID", "CLOCK_ID", 
		"POSITION_ID", "STATE_ID", "INT", "SYNC_MASTER", "SYNC_SLAVE", "ACCEPTED_CHARACTER", 
		"ASSIGNMENT", "SMALLER_STRONG", "SMALLER_WEAK", "EQUALS", "AND", "OR", 
		"WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "UP2CO.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public UP2COParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ControllerContext extends ParserRuleContext {
		public Controller contr;
		public State_blockContext stato;
		public List<State_blockContext> state_block() {
			return getRuleContexts(State_blockContext.class);
		}
		public State_blockContext state_block(int i) {
			return getRuleContext(State_blockContext.class,i);
		}
		public ControllerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_controller; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterController(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitController(this);
		}
	}

	public final ControllerContext controller() throws RecognitionException {
		ControllerContext _localctx = new ControllerContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_controller);

				System.out.println("I start parsing!");
				String str = "#Controller header";
				((ControllerContext)_localctx).contr =  new Controller(str);



			
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(44);
				((ControllerContext)_localctx).stato = state_block();

							//System.out.println("new state!");

							_localctx.contr.addState(((ControllerContext)_localctx).stato.stato);
						
				setState(48);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__0:
					{
					setState(46);
					match(T__0);
					}
					break;
				case EOF:
				case T__1:
					{
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(52); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__1 );


					
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class State_blockContext extends ParserRuleContext {
		public State_block stato;
		public State_ifContext config;
		public When_blockContext whe;
		public State_ifContext state_if() {
			return getRuleContext(State_ifContext.class,0);
		}
		public List<While_blockContext> while_block() {
			return getRuleContexts(While_blockContext.class);
		}
		public While_blockContext while_block(int i) {
			return getRuleContext(While_blockContext.class,i);
		}
		public List<When_blockContext> when_block() {
			return getRuleContexts(When_blockContext.class);
		}
		public When_blockContext when_block(int i) {
			return getRuleContext(When_blockContext.class,i);
		}
		public State_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_state_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterState_block(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitState_block(this);
		}
	}

	public final State_blockContext state_block() throws RecognitionException {
		State_blockContext _localctx = new State_blockContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_state_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(T__1);
			{
			setState(57);
			((State_blockContext)_localctx).config = state_if();
			}

					
					((State_blockContext)_localctx).stato =  new State_block("#state header", ((State_blockContext)_localctx).config.sts);


				
			setState(63); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(63);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__5:
					{
					setState(59);
					while_block();
					}
					break;
				case T__8:
					{
					setState(60);
					((State_blockContext)_localctx).whe = when_block();

								_localctx.stato.addWhen(((State_blockContext)_localctx).whe.when);
							
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(65); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__5 || _la==T__8 );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class State_ifContext extends ParserRuleContext {
		public Set<Status> sts;
		public Automa_stateContext state;
		public State_variableContext variable;
		public List<Automa_stateContext> automa_state() {
			return getRuleContexts(Automa_stateContext.class);
		}
		public Automa_stateContext automa_state(int i) {
			return getRuleContext(Automa_stateContext.class,i);
		}
		public List<State_variableContext> state_variable() {
			return getRuleContexts(State_variableContext.class);
		}
		public State_variableContext state_variable(int i) {
			return getRuleContext(State_variableContext.class,i);
		}
		public State_ifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_state_if; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterState_if(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitState_if(this);
		}
	}

	public final State_ifContext state_if() throws RecognitionException {
		State_ifContext _localctx = new State_ifContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_state_if);

				//System.out.println("new if_block!");
				 ((State_ifContext)_localctx).sts =  new HashSet<Status>();
			
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(T__2);
			setState(68);
			match(T__3);
			setState(73); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(69);
				((State_ifContext)_localctx).state = automa_state();
				setState(70);
				match(T__3);

						_localctx.sts.add(((State_ifContext)_localctx).state.stat);
					
				}
				}
				setState(75); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			setState(77);
			match(T__4);
			setState(78);
			match(T__3);
			setState(83); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(79);
				((State_ifContext)_localctx).variable = state_variable();
				setState(80);
				match(T__3);

						_localctx.sts.add(((State_ifContext)_localctx).variable.stat);
					
				}
				}
				setState(85); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==POSITION_ID || _la==STATE_ID );
			setState(87);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_blockContext extends ParserRuleContext {
		public List<Clock_conditions_setContext> clock_conditions_set() {
			return getRuleContexts(Clock_conditions_setContext.class);
		}
		public Clock_conditions_setContext clock_conditions_set(int i) {
			return getRuleContext(Clock_conditions_setContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(UP2COParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(UP2COParser.OR, i);
		}
		public While_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterWhile_block(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitWhile_block(this);
		}
	}

	public final While_blockContext while_block() throws RecognitionException {
		While_blockContext _localctx = new While_blockContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_while_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{

					//System.out.println("new while_block!");
				
			setState(90);
			match(T__5);
			setState(102);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				{
				{
				setState(91);
				match(T__6);
				}
				}
				break;
			case T__2:
				{
				{
				{
				setState(92);
				clock_conditions_set();
				}
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(93);
					match(T__3);
					setState(94);
					match(OR);
					setState(95);
					match(T__3);
					setState(96);
					clock_conditions_set();
					}
					}
					setState(101);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(104);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class When_blockContext extends ParserRuleContext {
		public When_block when;
		public Clock_conditions_setContext set;
		public Clock_conditions_setContext other_set;
		public TransitionContext transiz;
		public List<Clock_conditions_setContext> clock_conditions_set() {
			return getRuleContexts(Clock_conditions_setContext.class);
		}
		public Clock_conditions_setContext clock_conditions_set(int i) {
			return getRuleContext(Clock_conditions_setContext.class,i);
		}
		public List<TransitionContext> transition() {
			return getRuleContexts(TransitionContext.class);
		}
		public TransitionContext transition(int i) {
			return getRuleContext(TransitionContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(UP2COParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(UP2COParser.OR, i);
		}
		public When_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_when_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterWhen_block(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitWhen_block(this);
		}
	}

	public final When_blockContext when_block() throws RecognitionException {
		When_blockContext _localctx = new When_blockContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_when_block);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{

					//System.out.println("new when_block!");
					((When_blockContext)_localctx).when =  new When_block();

				
			setState(107);
			match(T__8);
			setState(108);
			((When_blockContext)_localctx).set = clock_conditions_set();
			 
					_localctx.when.addClockSet(((When_blockContext)_localctx).set.condizioni);

				
			setState(118);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(110);
					match(T__3);
					setState(111);
					match(OR);
					setState(112);
					match(T__3);
					setState(113);
					((When_blockContext)_localctx).other_set = clock_conditions_set();
					 
							_localctx.when.addClockSet(((When_blockContext)_localctx).other_set.condizioni);

						
					}
					} 
				}
				setState(120);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(121);
			match(T__9);
			setState(122);
			((When_blockContext)_localctx).transiz = transition();
			setState(123);
			match(T__0);
			setState(129);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(124);
					transition();
					setState(125);
					match(T__0);
					}
					} 
				}
				setState(131);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}

					_localctx.when.setOrigin(((When_blockContext)_localctx).transiz.origin);
					_localctx.when.setTarget(((When_blockContext)_localctx).transiz.target);
					_localctx.when.setTrigger(((When_blockContext)_localctx).transiz.syncro);
				
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_conditions_setContext extends ParserRuleContext {
		public Clock_cond_set condizioni;
		public Clock_conditionContext cond;
		public List<Clock_conditionContext> clock_condition() {
			return getRuleContexts(Clock_conditionContext.class);
		}
		public Clock_conditionContext clock_condition(int i) {
			return getRuleContext(Clock_conditionContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(UP2COParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(UP2COParser.AND, i);
		}
		public Clock_conditions_setContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_conditions_set; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_conditions_set(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_conditions_set(this);
		}
	}

	public final Clock_conditions_setContext clock_conditions_set() throws RecognitionException {
		Clock_conditions_setContext _localctx = new Clock_conditions_setContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_clock_conditions_set);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{

					//System.out.println("new clock condition set");
					((Clock_conditions_setContext)_localctx).condizioni =  new Clock_cond_set();

				
			setState(135);
			match(T__2);
			{
			setState(136);
			((Clock_conditions_setContext)_localctx).cond = clock_condition();
			}

						//System.out.println("new clock condition");
						_localctx.condizioni.addCond(((Clock_conditions_setContext)_localctx).cond.condizione);
					
			setState(146);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(138);
					match(T__3);
					setState(139);
					match(AND);
					setState(140);
					match(T__3);
					setState(141);
					((Clock_conditions_setContext)_localctx).cond = clock_condition();

						 		//System.out.println("other clock condition");
						 		_localctx.condizioni.addCond(((Clock_conditions_setContext)_localctx).cond.condizione);
						 	
					}
					} 
				}
				setState(148);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			setState(149);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_conditionContext extends ParserRuleContext {
		public Clock_cond condizione;
		public Clock_higher_strongContext cond1;
		public Clock_higher_weakContext cond2;
		public Clock_lower_strongContext cond3;
		public Clock_lower_weakContext cond4;
		public Clock_equalContext cond10;
		public Clock_constant_condition_equalityContext cond5;
		public Clock_constant_condition_1_equalityContext cond11;
		public Clock_constant_condition_1_strongContext cond6;
		public Clock_constant_condition_1_weakContext cond7;
		public Clock_constant_condition_2_strongContext cond8;
		public Clock_constant_condition_2_weakContext cond9;
		public Clock_higher_strongContext clock_higher_strong() {
			return getRuleContext(Clock_higher_strongContext.class,0);
		}
		public Clock_higher_weakContext clock_higher_weak() {
			return getRuleContext(Clock_higher_weakContext.class,0);
		}
		public Clock_lower_strongContext clock_lower_strong() {
			return getRuleContext(Clock_lower_strongContext.class,0);
		}
		public Clock_lower_weakContext clock_lower_weak() {
			return getRuleContext(Clock_lower_weakContext.class,0);
		}
		public Clock_equalContext clock_equal() {
			return getRuleContext(Clock_equalContext.class,0);
		}
		public Clock_constant_condition_equalityContext clock_constant_condition_equality() {
			return getRuleContext(Clock_constant_condition_equalityContext.class,0);
		}
		public Clock_constant_condition_1_equalityContext clock_constant_condition_1_equality() {
			return getRuleContext(Clock_constant_condition_1_equalityContext.class,0);
		}
		public Clock_constant_condition_1_strongContext clock_constant_condition_1_strong() {
			return getRuleContext(Clock_constant_condition_1_strongContext.class,0);
		}
		public Clock_constant_condition_1_weakContext clock_constant_condition_1_weak() {
			return getRuleContext(Clock_constant_condition_1_weakContext.class,0);
		}
		public Clock_constant_condition_2_strongContext clock_constant_condition_2_strong() {
			return getRuleContext(Clock_constant_condition_2_strongContext.class,0);
		}
		public Clock_constant_condition_2_weakContext clock_constant_condition_2_weak() {
			return getRuleContext(Clock_constant_condition_2_weakContext.class,0);
		}
		public Clock_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_condition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_condition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_condition(this);
		}
	}

	public final Clock_conditionContext clock_condition() throws RecognitionException {
		Clock_conditionContext _localctx = new Clock_conditionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_clock_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(151);
				((Clock_conditionContext)_localctx).cond1 = clock_higher_strong();

							((Clock_conditionContext)_localctx).condizione =  ((Clock_conditionContext)_localctx).cond1.condo;
							
				}
				break;
			case 2:
				{
				setState(154);
				((Clock_conditionContext)_localctx).cond2 = clock_higher_weak();

							((Clock_conditionContext)_localctx).condizione =  ((Clock_conditionContext)_localctx).cond2.condo;
							
				}
				break;
			case 3:
				{
				setState(157);
				((Clock_conditionContext)_localctx).cond3 = clock_lower_strong();

							((Clock_conditionContext)_localctx).condizione =  ((Clock_conditionContext)_localctx).cond3.condo;
							
				}
				break;
			case 4:
				{
				setState(160);
				((Clock_conditionContext)_localctx).cond4 = clock_lower_weak();

							((Clock_conditionContext)_localctx).condizione =  ((Clock_conditionContext)_localctx).cond4.condo;
							
				}
				break;
			case 5:
				{
				setState(163);
				((Clock_conditionContext)_localctx).cond10 = clock_equal();

							((Clock_conditionContext)_localctx).condizione =  ((Clock_conditionContext)_localctx).cond10.condo;
							
				}
				break;
			case 6:
				{
				setState(166);
				((Clock_conditionContext)_localctx).cond5 = clock_constant_condition_equality();

							((Clock_conditionContext)_localctx).condizione =  ((Clock_conditionContext)_localctx).cond5.condo;
							
				}
				break;
			case 7:
				{
				setState(169);
				((Clock_conditionContext)_localctx).cond11 = clock_constant_condition_1_equality();

							((Clock_conditionContext)_localctx).condizione =  ((Clock_conditionContext)_localctx).cond11.condo;
							
				}
				break;
			case 8:
				{
				setState(172);
				((Clock_conditionContext)_localctx).cond6 = clock_constant_condition_1_strong();

							((Clock_conditionContext)_localctx).condizione =  ((Clock_conditionContext)_localctx).cond6.condo;
							
				}
				break;
			case 9:
				{
				setState(175);
				((Clock_conditionContext)_localctx).cond7 = clock_constant_condition_1_weak();

							((Clock_conditionContext)_localctx).condizione =  ((Clock_conditionContext)_localctx).cond7.condo;
							
				}
				break;
			case 10:
				{
				setState(178);
				((Clock_conditionContext)_localctx).cond8 = clock_constant_condition_2_strong();

							((Clock_conditionContext)_localctx).condizione =  ((Clock_conditionContext)_localctx).cond8.condo;
							
				}
				break;
			case 11:
				{
				setState(181);
				((Clock_conditionContext)_localctx).cond9 = clock_constant_condition_2_weak();

							((Clock_conditionContext)_localctx).condizione =  ((Clock_conditionContext)_localctx).cond9.condo;
							
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_higher_strongContext extends ParserRuleContext {
		public Clock_cond_higher_strong condo;
		public Token val;
		public Token id;
		public TerminalNode SMALLER_STRONG() { return getToken(UP2COParser.SMALLER_STRONG, 0); }
		public TerminalNode INT() { return getToken(UP2COParser.INT, 0); }
		public TerminalNode CLOCK_ID() { return getToken(UP2COParser.CLOCK_ID, 0); }
		public Clock_higher_strongContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_higher_strong; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_higher_strong(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_higher_strong(this);
		}
	}

	public final Clock_higher_strongContext clock_higher_strong() throws RecognitionException {
		Clock_higher_strongContext _localctx = new Clock_higher_strongContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_clock_higher_strong);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			((Clock_higher_strongContext)_localctx).val = match(INT);
			setState(187);
			match(SMALLER_STRONG);
			setState(188);
			((Clock_higher_strongContext)_localctx).id = match(CLOCK_ID);
			((Clock_higher_strongContext)_localctx).condo =  new Clock_cond_higher_strong((((Clock_higher_strongContext)_localctx).id!=null?((Clock_higher_strongContext)_localctx).id.getText():null), (((Clock_higher_strongContext)_localctx).val!=null?((Clock_higher_strongContext)_localctx).val.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_higher_weakContext extends ParserRuleContext {
		public Clock_cond_higher_weak condo;
		public Token val;
		public Token id;
		public TerminalNode SMALLER_WEAK() { return getToken(UP2COParser.SMALLER_WEAK, 0); }
		public TerminalNode INT() { return getToken(UP2COParser.INT, 0); }
		public TerminalNode CLOCK_ID() { return getToken(UP2COParser.CLOCK_ID, 0); }
		public Clock_higher_weakContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_higher_weak; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_higher_weak(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_higher_weak(this);
		}
	}

	public final Clock_higher_weakContext clock_higher_weak() throws RecognitionException {
		Clock_higher_weakContext _localctx = new Clock_higher_weakContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_clock_higher_weak);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			((Clock_higher_weakContext)_localctx).val = match(INT);
			setState(192);
			match(SMALLER_WEAK);
			setState(193);
			((Clock_higher_weakContext)_localctx).id = match(CLOCK_ID);
			((Clock_higher_weakContext)_localctx).condo =  new Clock_cond_higher_weak((((Clock_higher_weakContext)_localctx).id!=null?((Clock_higher_weakContext)_localctx).id.getText():null), (((Clock_higher_weakContext)_localctx).val!=null?((Clock_higher_weakContext)_localctx).val.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_lower_strongContext extends ParserRuleContext {
		public Clock_cond_lower_strong condo;
		public Token id;
		public Token val;
		public TerminalNode SMALLER_STRONG() { return getToken(UP2COParser.SMALLER_STRONG, 0); }
		public TerminalNode CLOCK_ID() { return getToken(UP2COParser.CLOCK_ID, 0); }
		public TerminalNode INT() { return getToken(UP2COParser.INT, 0); }
		public Clock_lower_strongContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_lower_strong; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_lower_strong(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_lower_strong(this);
		}
	}

	public final Clock_lower_strongContext clock_lower_strong() throws RecognitionException {
		Clock_lower_strongContext _localctx = new Clock_lower_strongContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_clock_lower_strong);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			((Clock_lower_strongContext)_localctx).id = match(CLOCK_ID);
			setState(197);
			match(SMALLER_STRONG);
			setState(198);
			((Clock_lower_strongContext)_localctx).val = match(INT);
			((Clock_lower_strongContext)_localctx).condo =  new Clock_cond_lower_strong((((Clock_lower_strongContext)_localctx).id!=null?((Clock_lower_strongContext)_localctx).id.getText():null), (((Clock_lower_strongContext)_localctx).val!=null?((Clock_lower_strongContext)_localctx).val.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_lower_weakContext extends ParserRuleContext {
		public Clock_cond_lower_weak condo;
		public Token id;
		public Token val;
		public TerminalNode SMALLER_WEAK() { return getToken(UP2COParser.SMALLER_WEAK, 0); }
		public TerminalNode CLOCK_ID() { return getToken(UP2COParser.CLOCK_ID, 0); }
		public TerminalNode INT() { return getToken(UP2COParser.INT, 0); }
		public Clock_lower_weakContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_lower_weak; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_lower_weak(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_lower_weak(this);
		}
	}

	public final Clock_lower_weakContext clock_lower_weak() throws RecognitionException {
		Clock_lower_weakContext _localctx = new Clock_lower_weakContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_clock_lower_weak);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			((Clock_lower_weakContext)_localctx).id = match(CLOCK_ID);
			setState(202);
			match(SMALLER_WEAK);
			setState(203);
			((Clock_lower_weakContext)_localctx).val = match(INT);
			((Clock_lower_weakContext)_localctx).condo =  new Clock_cond_lower_weak((((Clock_lower_weakContext)_localctx).id!=null?((Clock_lower_weakContext)_localctx).id.getText():null), (((Clock_lower_weakContext)_localctx).val!=null?((Clock_lower_weakContext)_localctx).val.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_equalContext extends ParserRuleContext {
		public Clock_cond_equality condo;
		public Token id;
		public Token val;
		public TerminalNode EQUALS() { return getToken(UP2COParser.EQUALS, 0); }
		public TerminalNode CLOCK_ID() { return getToken(UP2COParser.CLOCK_ID, 0); }
		public TerminalNode INT() { return getToken(UP2COParser.INT, 0); }
		public Clock_equalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_equal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_equal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_equal(this);
		}
	}

	public final Clock_equalContext clock_equal() throws RecognitionException {
		Clock_equalContext _localctx = new Clock_equalContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_clock_equal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			((Clock_equalContext)_localctx).id = match(CLOCK_ID);
			setState(207);
			match(EQUALS);
			setState(208);
			((Clock_equalContext)_localctx).val = match(INT);
			((Clock_equalContext)_localctx).condo =  new Clock_cond_equality((((Clock_equalContext)_localctx).id!=null?((Clock_equalContext)_localctx).id.getText():null), (((Clock_equalContext)_localctx).val!=null?((Clock_equalContext)_localctx).val.getText():null));
					//this condition is ognored in all forther generation
				
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_constant_condition_equalityContext extends ParserRuleContext {
		public Clock_cond_constant_equality condo;
		public Token id1;
		public Token id2;
		public TerminalNode EQUALS() { return getToken(UP2COParser.EQUALS, 0); }
		public List<TerminalNode> CLOCK_ID() { return getTokens(UP2COParser.CLOCK_ID); }
		public TerminalNode CLOCK_ID(int i) {
			return getToken(UP2COParser.CLOCK_ID, i);
		}
		public Clock_constant_condition_equalityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_constant_condition_equality; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_constant_condition_equality(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_constant_condition_equality(this);
		}
	}

	public final Clock_constant_condition_equalityContext clock_constant_condition_equality() throws RecognitionException {
		Clock_constant_condition_equalityContext _localctx = new Clock_constant_condition_equalityContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_clock_constant_condition_equality);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			((Clock_constant_condition_equalityContext)_localctx).id1 = match(CLOCK_ID);
			setState(212);
			match(EQUALS);
			setState(213);
			((Clock_constant_condition_equalityContext)_localctx).id2 = match(CLOCK_ID);
			((Clock_constant_condition_equalityContext)_localctx).condo =  new Clock_cond_constant_equality((((Clock_constant_condition_equalityContext)_localctx).id1!=null?((Clock_constant_condition_equalityContext)_localctx).id1.getText():null), (((Clock_constant_condition_equalityContext)_localctx).id2!=null?((Clock_constant_condition_equalityContext)_localctx).id2.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_constant_condition_1_equalityContext extends ParserRuleContext {
		public Clock_cond_constant_1_equality condo;
		public Token id1;
		public Token id2;
		public Token value;
		public TerminalNode EQUALS() { return getToken(UP2COParser.EQUALS, 0); }
		public List<TerminalNode> CLOCK_ID() { return getTokens(UP2COParser.CLOCK_ID); }
		public TerminalNode CLOCK_ID(int i) {
			return getToken(UP2COParser.CLOCK_ID, i);
		}
		public TerminalNode INT() { return getToken(UP2COParser.INT, 0); }
		public Clock_constant_condition_1_equalityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_constant_condition_1_equality; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_constant_condition_1_equality(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_constant_condition_1_equality(this);
		}
	}

	public final Clock_constant_condition_1_equalityContext clock_constant_condition_1_equality() throws RecognitionException {
		Clock_constant_condition_1_equalityContext _localctx = new Clock_constant_condition_1_equalityContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_clock_constant_condition_1_equality);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			((Clock_constant_condition_1_equalityContext)_localctx).id1 = match(CLOCK_ID);
			setState(217);
			match(T__10);
			setState(218);
			((Clock_constant_condition_1_equalityContext)_localctx).id2 = match(CLOCK_ID);
			setState(219);
			match(EQUALS);
			setState(220);
			((Clock_constant_condition_1_equalityContext)_localctx).value = match(INT);
			((Clock_constant_condition_1_equalityContext)_localctx).condo =  new Clock_cond_constant_1_equality((((Clock_constant_condition_1_equalityContext)_localctx).id1!=null?((Clock_constant_condition_1_equalityContext)_localctx).id1.getText():null), (((Clock_constant_condition_1_equalityContext)_localctx).id2!=null?((Clock_constant_condition_1_equalityContext)_localctx).id2.getText():null), (((Clock_constant_condition_1_equalityContext)_localctx).value!=null?((Clock_constant_condition_1_equalityContext)_localctx).value.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_constant_condition_1_strongContext extends ParserRuleContext {
		public Clock_cond_constant_1_strong condo;
		public Token id1;
		public Token id2;
		public Token value;
		public TerminalNode SMALLER_STRONG() { return getToken(UP2COParser.SMALLER_STRONG, 0); }
		public List<TerminalNode> CLOCK_ID() { return getTokens(UP2COParser.CLOCK_ID); }
		public TerminalNode CLOCK_ID(int i) {
			return getToken(UP2COParser.CLOCK_ID, i);
		}
		public TerminalNode INT() { return getToken(UP2COParser.INT, 0); }
		public Clock_constant_condition_1_strongContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_constant_condition_1_strong; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_constant_condition_1_strong(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_constant_condition_1_strong(this);
		}
	}

	public final Clock_constant_condition_1_strongContext clock_constant_condition_1_strong() throws RecognitionException {
		Clock_constant_condition_1_strongContext _localctx = new Clock_constant_condition_1_strongContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_clock_constant_condition_1_strong);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			((Clock_constant_condition_1_strongContext)_localctx).id1 = match(CLOCK_ID);
			setState(224);
			match(T__10);
			setState(225);
			((Clock_constant_condition_1_strongContext)_localctx).id2 = match(CLOCK_ID);
			setState(226);
			match(SMALLER_STRONG);
			setState(227);
			((Clock_constant_condition_1_strongContext)_localctx).value = match(INT);
			((Clock_constant_condition_1_strongContext)_localctx).condo =  new Clock_cond_constant_1_strong((((Clock_constant_condition_1_strongContext)_localctx).id1!=null?((Clock_constant_condition_1_strongContext)_localctx).id1.getText():null), (((Clock_constant_condition_1_strongContext)_localctx).id2!=null?((Clock_constant_condition_1_strongContext)_localctx).id2.getText():null), (((Clock_constant_condition_1_strongContext)_localctx).value!=null?((Clock_constant_condition_1_strongContext)_localctx).value.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_constant_condition_1_weakContext extends ParserRuleContext {
		public Clock_cond_constant_1_weak condo;
		public Token id1;
		public Token id2;
		public Token value;
		public TerminalNode SMALLER_WEAK() { return getToken(UP2COParser.SMALLER_WEAK, 0); }
		public List<TerminalNode> CLOCK_ID() { return getTokens(UP2COParser.CLOCK_ID); }
		public TerminalNode CLOCK_ID(int i) {
			return getToken(UP2COParser.CLOCK_ID, i);
		}
		public TerminalNode INT() { return getToken(UP2COParser.INT, 0); }
		public Clock_constant_condition_1_weakContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_constant_condition_1_weak; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_constant_condition_1_weak(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_constant_condition_1_weak(this);
		}
	}

	public final Clock_constant_condition_1_weakContext clock_constant_condition_1_weak() throws RecognitionException {
		Clock_constant_condition_1_weakContext _localctx = new Clock_constant_condition_1_weakContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_clock_constant_condition_1_weak);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(230);
			((Clock_constant_condition_1_weakContext)_localctx).id1 = match(CLOCK_ID);
			setState(231);
			match(T__10);
			setState(232);
			((Clock_constant_condition_1_weakContext)_localctx).id2 = match(CLOCK_ID);
			setState(233);
			match(SMALLER_WEAK);
			setState(234);
			((Clock_constant_condition_1_weakContext)_localctx).value = match(INT);
			((Clock_constant_condition_1_weakContext)_localctx).condo =  new Clock_cond_constant_1_weak((((Clock_constant_condition_1_weakContext)_localctx).id1!=null?((Clock_constant_condition_1_weakContext)_localctx).id1.getText():null), (((Clock_constant_condition_1_weakContext)_localctx).id2!=null?((Clock_constant_condition_1_weakContext)_localctx).id2.getText():null), (((Clock_constant_condition_1_weakContext)_localctx).value!=null?((Clock_constant_condition_1_weakContext)_localctx).value.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_constant_condition_2_strongContext extends ParserRuleContext {
		public Clock_cond_constant_2_strong condo;
		public Token id1;
		public Token id2;
		public TerminalNode SMALLER_STRONG() { return getToken(UP2COParser.SMALLER_STRONG, 0); }
		public List<TerminalNode> CLOCK_ID() { return getTokens(UP2COParser.CLOCK_ID); }
		public TerminalNode CLOCK_ID(int i) {
			return getToken(UP2COParser.CLOCK_ID, i);
		}
		public Clock_constant_condition_2_strongContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_constant_condition_2_strong; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_constant_condition_2_strong(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_constant_condition_2_strong(this);
		}
	}

	public final Clock_constant_condition_2_strongContext clock_constant_condition_2_strong() throws RecognitionException {
		Clock_constant_condition_2_strongContext _localctx = new Clock_constant_condition_2_strongContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_clock_constant_condition_2_strong);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			((Clock_constant_condition_2_strongContext)_localctx).id1 = match(CLOCK_ID);
			setState(238);
			match(SMALLER_STRONG);
			setState(239);
			((Clock_constant_condition_2_strongContext)_localctx).id2 = match(CLOCK_ID);
			((Clock_constant_condition_2_strongContext)_localctx).condo =  new Clock_cond_constant_2_strong((((Clock_constant_condition_2_strongContext)_localctx).id1!=null?((Clock_constant_condition_2_strongContext)_localctx).id1.getText():null), (((Clock_constant_condition_2_strongContext)_localctx).id2!=null?((Clock_constant_condition_2_strongContext)_localctx).id2.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clock_constant_condition_2_weakContext extends ParserRuleContext {
		public Clock_cond_constant_2_weak condo;
		public Token id1;
		public Token id2;
		public TerminalNode SMALLER_WEAK() { return getToken(UP2COParser.SMALLER_WEAK, 0); }
		public List<TerminalNode> CLOCK_ID() { return getTokens(UP2COParser.CLOCK_ID); }
		public TerminalNode CLOCK_ID(int i) {
			return getToken(UP2COParser.CLOCK_ID, i);
		}
		public Clock_constant_condition_2_weakContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clock_constant_condition_2_weak; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterClock_constant_condition_2_weak(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitClock_constant_condition_2_weak(this);
		}
	}

	public final Clock_constant_condition_2_weakContext clock_constant_condition_2_weak() throws RecognitionException {
		Clock_constant_condition_2_weakContext _localctx = new Clock_constant_condition_2_weakContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_clock_constant_condition_2_weak);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			((Clock_constant_condition_2_weakContext)_localctx).id1 = match(CLOCK_ID);
			setState(243);
			match(SMALLER_WEAK);
			setState(244);
			((Clock_constant_condition_2_weakContext)_localctx).id2 = match(CLOCK_ID);
			((Clock_constant_condition_2_weakContext)_localctx).condo =  new Clock_cond_constant_2_weak((((Clock_constant_condition_2_weakContext)_localctx).id1!=null?((Clock_constant_condition_2_weakContext)_localctx).id1.getText():null), (((Clock_constant_condition_2_weakContext)_localctx).id2!=null?((Clock_constant_condition_2_weakContext)_localctx).id2.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TransitionContext extends ParserRuleContext {
		public Status origin;
		public Status target;
		public Set<String> clocks;
		public String syncro;
		public Automa_stateContext origine;
		public Automa_stateContext targeto;
		public Token sync;
		public Token synch;
		public Token clock;
		public PreconditionsContext preconditions() {
			return getRuleContext(PreconditionsContext.class,0);
		}
		public List<Automa_stateContext> automa_state() {
			return getRuleContexts(Automa_stateContext.class);
		}
		public Automa_stateContext automa_state(int i) {
			return getRuleContext(Automa_stateContext.class,i);
		}
		public TerminalNode SYNC_MASTER() { return getToken(UP2COParser.SYNC_MASTER, 0); }
		public TerminalNode SYNC_SLAVE() { return getToken(UP2COParser.SYNC_SLAVE, 0); }
		public List<TerminalNode> INT() { return getTokens(UP2COParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(UP2COParser.INT, i);
		}
		public List<TerminalNode> POSITION_ID() { return getTokens(UP2COParser.POSITION_ID); }
		public TerminalNode POSITION_ID(int i) {
			return getToken(UP2COParser.POSITION_ID, i);
		}
		public List<TerminalNode> ASSIGNMENT() { return getTokens(UP2COParser.ASSIGNMENT); }
		public TerminalNode ASSIGNMENT(int i) {
			return getToken(UP2COParser.ASSIGNMENT, i);
		}
		public List<TerminalNode> STATE_ID() { return getTokens(UP2COParser.STATE_ID); }
		public TerminalNode STATE_ID(int i) {
			return getToken(UP2COParser.STATE_ID, i);
		}
		public List<TerminalNode> CLOCK_ID() { return getTokens(UP2COParser.CLOCK_ID); }
		public TerminalNode CLOCK_ID(int i) {
			return getToken(UP2COParser.CLOCK_ID, i);
		}
		public TransitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_transition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterTransition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitTransition(this);
		}
	}

	public final TransitionContext transition() throws RecognitionException {
		TransitionContext _localctx = new TransitionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_transition);

				((TransitionContext)_localctx).clocks =  new HashSet<String>();
				((TransitionContext)_localctx).syncro =  new String();
			
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			((TransitionContext)_localctx).origine = automa_state();
			setState(248);
			match(T__11);
			setState(249);
			((TransitionContext)_localctx).targeto = automa_state();
			setState(250);
			match(T__3);
			setState(251);
			match(T__12);
			setState(252);
			match(T__3);
			setState(253);
			preconditions();
			setState(254);
			match(T__3);
			setState(261);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SYNC_MASTER:
				{
				setState(255);
				((TransitionContext)_localctx).sync = match(SYNC_MASTER);

									((TransitionContext)_localctx).syncro =  (((TransitionContext)_localctx).sync!=null?((TransitionContext)_localctx).sync.getText():null);
								
				}
				break;
			case SYNC_SLAVE:
				{
				setState(257);
				((TransitionContext)_localctx).synch = match(SYNC_SLAVE);

									((TransitionContext)_localctx).syncro =  "undefined"; //decision for now to treat slave syncs as undefined, trated by observer
								
				}
				break;
			case T__13:
				{
				setState(259);
				match(T__13);

									((TransitionContext)_localctx).syncro =  "tau";
								
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(279);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(263);
					match(T__14);
					setState(264);
					match(T__3);
					setState(275);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case POSITION_ID:
						{
						{
						setState(265);
						match(POSITION_ID);
						setState(266);
						match(ASSIGNMENT);
						setState(267);
						match(INT);
						}
						}
						break;
					case STATE_ID:
						{
						{
						setState(268);
						match(STATE_ID);
						setState(269);
						match(ASSIGNMENT);
						setState(270);
						match(INT);
						}
						}
						break;
					case CLOCK_ID:
						{
						{
						setState(271);
						((TransitionContext)_localctx).clock = match(CLOCK_ID);
						setState(272);
						match(ASSIGNMENT);
						setState(273);
						match(INT);
						}
						}
						break;
					case INT:
						{
						setState(274);
						match(INT);
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					} 
				}
				setState(281);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			}
			setState(282);
			match(T__3);
			setState(283);
			match(T__15);

					((TransitionContext)_localctx).origin =  ((TransitionContext)_localctx).origine.stat;
					((TransitionContext)_localctx).target =  ((TransitionContext)_localctx).targeto.stat;
				
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PreconditionsContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(UP2COParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(UP2COParser.INT, i);
		}
		public TerminalNode CLOCK_ID() { return getToken(UP2COParser.CLOCK_ID, 0); }
		public List<TerminalNode> AND() { return getTokens(UP2COParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(UP2COParser.AND, i);
		}
		public List<TerminalNode> EQUALS() { return getTokens(UP2COParser.EQUALS); }
		public TerminalNode EQUALS(int i) {
			return getToken(UP2COParser.EQUALS, i);
		}
		public List<TerminalNode> POSITION_ID() { return getTokens(UP2COParser.POSITION_ID); }
		public TerminalNode POSITION_ID(int i) {
			return getToken(UP2COParser.POSITION_ID, i);
		}
		public List<TerminalNode> STATE_ID() { return getTokens(UP2COParser.STATE_ID); }
		public TerminalNode STATE_ID(int i) {
			return getToken(UP2COParser.STATE_ID, i);
		}
		public PreconditionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preconditions; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterPreconditions(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitPreconditions(this);
		}
	}

	public final PreconditionsContext preconditions() throws RecognitionException {
		PreconditionsContext _localctx = new PreconditionsContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_preconditions);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(304);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CLOCK_ID:
				{
				{
				{
				setState(286);
				match(CLOCK_ID);
				setState(287);
				match(T__16);
				setState(288);
				match(INT);
				}
				setState(300);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
				while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1+1 ) {
						{
						{
						setState(290);
						match(T__3);
						setState(291);
						match(AND);
						setState(292);
						match(T__3);
						setState(293);
						_la = _input.LA(1);
						if ( !(_la==POSITION_ID || _la==STATE_ID) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(294);
						match(T__3);
						setState(295);
						match(EQUALS);
						setState(296);
						match(T__3);
						setState(297);
						_la = _input.LA(1);
						if ( !(_la==POSITION_ID || _la==INT) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						}
						} 
					}
					setState(302);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
				}
				}
				}
				break;
			case INT:
				{
				setState(303);
				match(INT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(306);
			match(T__14);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Automa_stateContext extends ParserRuleContext {
		public Status stat;
		public Token id;
		public Token loc;
		public List<TerminalNode> ID() { return getTokens(UP2COParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(UP2COParser.ID, i);
		}
		public Automa_stateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_automa_state; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterAutoma_state(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitAutoma_state(this);
		}
	}

	public final Automa_stateContext automa_state() throws RecognitionException {
		Automa_stateContext _localctx = new Automa_stateContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_automa_state);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(308);
			((Automa_stateContext)_localctx).id = match(ID);
			}
			setState(309);
			match(T__17);
			setState(311);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__18) {
				{
				setState(310);
				match(T__18);
				}
			}

			{
			setState(313);
			((Automa_stateContext)_localctx).loc = match(ID);
			}

					((Automa_stateContext)_localctx).stat =  new Status((((Automa_stateContext)_localctx).id!=null?((Automa_stateContext)_localctx).id.getText():null),  (((Automa_stateContext)_localctx).loc!=null?((Automa_stateContext)_localctx).loc.getText():null));


				
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class State_variableContext extends ParserRuleContext {
		public Status stat;
		public Token id;
		public Token val;
		public TerminalNode POSITION_ID() { return getToken(UP2COParser.POSITION_ID, 0); }
		public TerminalNode INT() { return getToken(UP2COParser.INT, 0); }
		public TerminalNode STATE_ID() { return getToken(UP2COParser.STATE_ID, 0); }
		public State_variableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_state_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).enterState_variable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2COListener ) ((UP2COListener)listener).exitState_variable(this);
		}
	}

	public final State_variableContext state_variable() throws RecognitionException {
		State_variableContext _localctx = new State_variableContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_state_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case POSITION_ID:
				{
				{
				setState(316);
				((State_variableContext)_localctx).id = match(POSITION_ID);
				}
				setState(317);
				match(T__19);
				{
				setState(318);
				((State_variableContext)_localctx).val = match(INT);
				}
				}
				break;
			case STATE_ID:
				{
				{
				setState(319);
				((State_variableContext)_localctx).id = match(STATE_ID);
				}
				setState(320);
				match(T__19);
				{
				setState(321);
				((State_variableContext)_localctx).val = match(INT);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}

					((State_variableContext)_localctx).stat =  new Status((((State_variableContext)_localctx).id!=null?((State_variableContext)_localctx).id.getText():null),  (((State_variableContext)_localctx).val!=null?((State_variableContext)_localctx).val.getText():null));

				
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%\u0149\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2\3\2\5\2"+
		"\63\n\2\6\2\65\n\2\r\2\16\2\66\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\6\3"+
		"B\n\3\r\3\16\3C\3\4\3\4\3\4\3\4\3\4\3\4\6\4L\n\4\r\4\16\4M\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\6\4V\n\4\r\4\16\4W\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\7\5d\n\5\f\5\16\5g\13\5\5\5i\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\7\6w\n\6\f\6\16\6z\13\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u0082"+
		"\n\6\f\6\16\6\u0085\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\7\7\u0093\n\7\f\7\16\7\u0096\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00bb\n\b\3\t\3\t\3\t\3\t\3\t"+
		"\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r"+
		"\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0108\n\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0116"+
		"\n\24\7\24\u0118\n\24\f\24\16\24\u011b\13\24\3\24\3\24\3\24\3\24\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u012d\n\25"+
		"\f\25\16\25\u0130\13\25\3\25\5\25\u0133\n\25\3\25\3\25\3\26\3\26\3\26"+
		"\5\26\u013a\n\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0145"+
		"\n\27\3\27\3\27\3\27\7x\u0083\u0094\u0119\u012e\2\30\2\4\6\b\n\f\16\20"+
		"\22\24\26\30\32\34\36 \"$&(*,\2\4\3\2\31\32\4\2\31\31\33\33\2\u0151\2"+
		"\64\3\2\2\2\4:\3\2\2\2\6E\3\2\2\2\b[\3\2\2\2\nl\3\2\2\2\f\u0088\3\2\2"+
		"\2\16\u00ba\3\2\2\2\20\u00bc\3\2\2\2\22\u00c1\3\2\2\2\24\u00c6\3\2\2\2"+
		"\26\u00cb\3\2\2\2\30\u00d0\3\2\2\2\32\u00d5\3\2\2\2\34\u00da\3\2\2\2\36"+
		"\u00e1\3\2\2\2 \u00e8\3\2\2\2\"\u00ef\3\2\2\2$\u00f4\3\2\2\2&\u00f9\3"+
		"\2\2\2(\u0132\3\2\2\2*\u0136\3\2\2\2,\u0144\3\2\2\2./\5\4\3\2/\62\b\2"+
		"\1\2\60\63\7\3\2\2\61\63\3\2\2\2\62\60\3\2\2\2\62\61\3\2\2\2\63\65\3\2"+
		"\2\2\64.\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\678\3\2\2\2"+
		"89\b\2\1\29\3\3\2\2\2:;\7\4\2\2;<\5\6\4\2<A\b\3\1\2=B\5\b\5\2>?\5\n\6"+
		"\2?@\b\3\1\2@B\3\2\2\2A=\3\2\2\2A>\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2"+
		"\2D\5\3\2\2\2EF\7\5\2\2FK\7\6\2\2GH\5*\26\2HI\7\6\2\2IJ\b\4\1\2JL\3\2"+
		"\2\2KG\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7\7\2\2PU\7\6"+
		"\2\2QR\5,\27\2RS\7\6\2\2ST\b\4\1\2TV\3\2\2\2UQ\3\2\2\2VW\3\2\2\2WU\3\2"+
		"\2\2WX\3\2\2\2XY\3\2\2\2YZ\7\3\2\2Z\7\3\2\2\2[\\\b\5\1\2\\h\7\b\2\2]i"+
		"\7\t\2\2^e\5\f\7\2_`\7\6\2\2`a\7$\2\2ab\7\6\2\2bd\5\f\7\2c_\3\2\2\2dg"+
		"\3\2\2\2ec\3\2\2\2ef\3\2\2\2fi\3\2\2\2ge\3\2\2\2h]\3\2\2\2h^\3\2\2\2i"+
		"j\3\2\2\2jk\7\n\2\2k\t\3\2\2\2lm\b\6\1\2mn\7\13\2\2no\5\f\7\2ox\b\6\1"+
		"\2pq\7\6\2\2qr\7$\2\2rs\7\6\2\2st\5\f\7\2tu\b\6\1\2uw\3\2\2\2vp\3\2\2"+
		"\2wz\3\2\2\2xy\3\2\2\2xv\3\2\2\2y{\3\2\2\2zx\3\2\2\2{|\7\f\2\2|}\5&\24"+
		"\2}\u0083\7\3\2\2~\177\5&\24\2\177\u0080\7\3\2\2\u0080\u0082\3\2\2\2\u0081"+
		"~\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0084\3\2\2\2\u0083\u0081\3\2\2\2"+
		"\u0084\u0086\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087\b\6\1\2\u0087\13"+
		"\3\2\2\2\u0088\u0089\b\7\1\2\u0089\u008a\7\5\2\2\u008a\u008b\5\16\b\2"+
		"\u008b\u0094\b\7\1\2\u008c\u008d\7\6\2\2\u008d\u008e\7#\2\2\u008e\u008f"+
		"\7\6\2\2\u008f\u0090\5\16\b\2\u0090\u0091\b\7\1\2\u0091\u0093\3\2\2\2"+
		"\u0092\u008c\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0095\3\2\2\2\u0094\u0092"+
		"\3\2\2\2\u0095\u0097\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098\7\7\2\2\u0098"+
		"\r\3\2\2\2\u0099\u009a\5\20\t\2\u009a\u009b\b\b\1\2\u009b\u00bb\3\2\2"+
		"\2\u009c\u009d\5\22\n\2\u009d\u009e\b\b\1\2\u009e\u00bb\3\2\2\2\u009f"+
		"\u00a0\5\24\13\2\u00a0\u00a1\b\b\1\2\u00a1\u00bb\3\2\2\2\u00a2\u00a3\5"+
		"\26\f\2\u00a3\u00a4\b\b\1\2\u00a4\u00bb\3\2\2\2\u00a5\u00a6\5\30\r\2\u00a6"+
		"\u00a7\b\b\1\2\u00a7\u00bb\3\2\2\2\u00a8\u00a9\5\32\16\2\u00a9\u00aa\b"+
		"\b\1\2\u00aa\u00bb\3\2\2\2\u00ab\u00ac\5\34\17\2\u00ac\u00ad\b\b\1\2\u00ad"+
		"\u00bb\3\2\2\2\u00ae\u00af\5\36\20\2\u00af\u00b0\b\b\1\2\u00b0\u00bb\3"+
		"\2\2\2\u00b1\u00b2\5 \21\2\u00b2\u00b3\b\b\1\2\u00b3\u00bb\3\2\2\2\u00b4"+
		"\u00b5\5\"\22\2\u00b5\u00b6\b\b\1\2\u00b6\u00bb\3\2\2\2\u00b7\u00b8\5"+
		"$\23\2\u00b8\u00b9\b\b\1\2\u00b9\u00bb\3\2\2\2\u00ba\u0099\3\2\2\2\u00ba"+
		"\u009c\3\2\2\2\u00ba\u009f\3\2\2\2\u00ba\u00a2\3\2\2\2\u00ba\u00a5\3\2"+
		"\2\2\u00ba\u00a8\3\2\2\2\u00ba\u00ab\3\2\2\2\u00ba\u00ae\3\2\2\2\u00ba"+
		"\u00b1\3\2\2\2\u00ba\u00b4\3\2\2\2\u00ba\u00b7\3\2\2\2\u00bb\17\3\2\2"+
		"\2\u00bc\u00bd\7\33\2\2\u00bd\u00be\7 \2\2\u00be\u00bf\7\30\2\2\u00bf"+
		"\u00c0\b\t\1\2\u00c0\21\3\2\2\2\u00c1\u00c2\7\33\2\2\u00c2\u00c3\7!\2"+
		"\2\u00c3\u00c4\7\30\2\2\u00c4\u00c5\b\n\1\2\u00c5\23\3\2\2\2\u00c6\u00c7"+
		"\7\30\2\2\u00c7\u00c8\7 \2\2\u00c8\u00c9\7\33\2\2\u00c9\u00ca\b\13\1\2"+
		"\u00ca\25\3\2\2\2\u00cb\u00cc\7\30\2\2\u00cc\u00cd\7!\2\2\u00cd\u00ce"+
		"\7\33\2\2\u00ce\u00cf\b\f\1\2\u00cf\27\3\2\2\2\u00d0\u00d1\7\30\2\2\u00d1"+
		"\u00d2\7\"\2\2\u00d2\u00d3\7\33\2\2\u00d3\u00d4\b\r\1\2\u00d4\31\3\2\2"+
		"\2\u00d5\u00d6\7\30\2\2\u00d6\u00d7\7\"\2\2\u00d7\u00d8\7\30\2\2\u00d8"+
		"\u00d9\b\16\1\2\u00d9\33\3\2\2\2\u00da\u00db\7\30\2\2\u00db\u00dc\7\r"+
		"\2\2\u00dc\u00dd\7\30\2\2\u00dd\u00de\7\"\2\2\u00de\u00df\7\33\2\2\u00df"+
		"\u00e0\b\17\1\2\u00e0\35\3\2\2\2\u00e1\u00e2\7\30\2\2\u00e2\u00e3\7\r"+
		"\2\2\u00e3\u00e4\7\30\2\2\u00e4\u00e5\7 \2\2\u00e5\u00e6\7\33\2\2\u00e6"+
		"\u00e7\b\20\1\2\u00e7\37\3\2\2\2\u00e8\u00e9\7\30\2\2\u00e9\u00ea\7\r"+
		"\2\2\u00ea\u00eb\7\30\2\2\u00eb\u00ec\7!\2\2\u00ec\u00ed\7\33\2\2\u00ed"+
		"\u00ee\b\21\1\2\u00ee!\3\2\2\2\u00ef\u00f0\7\30\2\2\u00f0\u00f1\7 \2\2"+
		"\u00f1\u00f2\7\30\2\2\u00f2\u00f3\b\22\1\2\u00f3#\3\2\2\2\u00f4\u00f5"+
		"\7\30\2\2\u00f5\u00f6\7!\2\2\u00f6\u00f7\7\30\2\2\u00f7\u00f8\b\23\1\2"+
		"\u00f8%\3\2\2\2\u00f9\u00fa\5*\26\2\u00fa\u00fb\7\16\2\2\u00fb\u00fc\5"+
		"*\26\2\u00fc\u00fd\7\6\2\2\u00fd\u00fe\7\17\2\2\u00fe\u00ff\7\6\2\2\u00ff"+
		"\u0100\5(\25\2\u0100\u0107\7\6\2\2\u0101\u0102\7\34\2\2\u0102\u0108\b"+
		"\24\1\2\u0103\u0104\7\35\2\2\u0104\u0108\b\24\1\2\u0105\u0106\7\20\2\2"+
		"\u0106\u0108\b\24\1\2\u0107\u0101\3\2\2\2\u0107\u0103\3\2\2\2\u0107\u0105"+
		"\3\2\2\2\u0108\u0119\3\2\2\2\u0109\u010a\7\21\2\2\u010a\u0115\7\6\2\2"+
		"\u010b\u010c\7\31\2\2\u010c\u010d\7\37\2\2\u010d\u0116\7\33\2\2\u010e"+
		"\u010f\7\32\2\2\u010f\u0110\7\37\2\2\u0110\u0116\7\33\2\2\u0111\u0112"+
		"\7\30\2\2\u0112\u0113\7\37\2\2\u0113\u0116\7\33\2\2\u0114\u0116\7\33\2"+
		"\2\u0115\u010b\3\2\2\2\u0115\u010e\3\2\2\2\u0115\u0111\3\2\2\2\u0115\u0114"+
		"\3\2\2\2\u0116\u0118\3\2\2\2\u0117\u0109\3\2\2\2\u0118\u011b\3\2\2\2\u0119"+
		"\u011a\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u0119\3\2"+
		"\2\2\u011c\u011d\7\6\2\2\u011d\u011e\7\22\2\2\u011e\u011f\b\24\1\2\u011f"+
		"\'\3\2\2\2\u0120\u0121\7\30\2\2\u0121\u0122\7\23\2\2\u0122\u0123\7\33"+
		"\2\2\u0123\u012e\3\2\2\2\u0124\u0125\7\6\2\2\u0125\u0126\7#\2\2\u0126"+
		"\u0127\7\6\2\2\u0127\u0128\t\2\2\2\u0128\u0129\7\6\2\2\u0129\u012a\7\""+
		"\2\2\u012a\u012b\7\6\2\2\u012b\u012d\t\3\2\2\u012c\u0124\3\2\2\2\u012d"+
		"\u0130\3\2\2\2\u012e\u012f\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0133\3\2"+
		"\2\2\u0130\u012e\3\2\2\2\u0131\u0133\7\33\2\2\u0132\u0120\3\2\2\2\u0132"+
		"\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0135\7\21\2\2\u0135)\3\2\2\2"+
		"\u0136\u0137\7\27\2\2\u0137\u0139\7\24\2\2\u0138\u013a\7\25\2\2\u0139"+
		"\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\7\27"+
		"\2\2\u013c\u013d\b\26\1\2\u013d+\3\2\2\2\u013e\u013f\7\31\2\2\u013f\u0140"+
		"\7\26\2\2\u0140\u0145\7\33\2\2\u0141\u0142\7\32\2\2\u0142\u0143\7\26\2"+
		"\2\u0143\u0145\7\33\2\2\u0144\u013e\3\2\2\2\u0144\u0141\3\2\2\2\u0145"+
		"\u0146\3\2\2\2\u0146\u0147\b\27\1\2\u0147-\3\2\2\2\25\62\66ACMWehx\u0083"+
		"\u0094\u00ba\u0107\u0115\u0119\u012e\u0132\u0139\u0144";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}