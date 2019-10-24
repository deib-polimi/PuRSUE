// Generated from UP2OB.g4 by ANTLR 4.7.1

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
public class UP2OBParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, CHAN_DEC=38, 
		ID=39, CLOCK_ID=40, COMMA=41, SEMICOLON=42, PAR_OPEN=43, PAR_CLOSE=44, 
		POSITION_ID=45, STATE_ID=46, INT=47, ACCEPTED_CHARACTER=48, ASSIGNMENT=49, 
		SMALLER_WEAK=50, GREATER_STRONG=51, EQUALS=52, AND=53, SYSTEM_DECLARATION=54, 
		WS=55, LINE_COMMENT=56;
	public static final int
		RULE_model = 0, RULE_declaration_block = 1, RULE_machine_block = 2, RULE_location_block = 3, 
		RULE_transition_block = 4;
	public static final String[] ruleNames = {
		"model", "declaration_block", "machine_block", "location_block", "transition_block"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'<nta>'", "'automata_declaration'", "'state_updater'", "'rules'", 
		"'agents'", "'objectives'", "'</nta>'", "'<declaration>'", "'broadcast chan '", 
		"'int '", "'clock '", "'</declaration>'", "'<template>'", "'<name>'", 
		"'</name>'", "'<init ref = '", "'\"'", "'/>'", "'</template>'", "'<location id='", 
		"'<location id = '", "'>'", "'<label kind=\"invariant\">'", "'</label>'", 
		"'</location>'", "'<transition>'", "'<transition controllable=\"false\" >'", 
		"'<source ref='", "'<target ref='", "'<label kind=\"synchronisation\">'", 
		"'!'", "'?'", "'<label'", "'kind'", "'\"assignment\">'", "'\"guard\">'", 
		"'</transition>'", null, null, null, "','", "';'", "'('", "')'", null, 
		null, null, null, "'='", "'&lt;='", "'&gt;'", "'=='", "'&amp;&amp;'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, "CHAN_DEC", "ID", "CLOCK_ID", "COMMA", "SEMICOLON", "PAR_OPEN", 
		"PAR_CLOSE", "POSITION_ID", "STATE_ID", "INT", "ACCEPTED_CHARACTER", "ASSIGNMENT", 
		"SMALLER_WEAK", "GREATER_STRONG", "EQUALS", "AND", "SYSTEM_DECLARATION", 
		"WS", "LINE_COMMENT"
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
	public String getGrammarFileName() { return "UP2OB.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public UP2OBParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ModelContext extends ParserRuleContext {
		public Model mod;
		public Declaration_blockContext declared;
		public Machine_blockContext mac;
		public Machine_blockContext reg;
		public Machine_blockContext agent;
		public Machine_blockContext obj;
		public TerminalNode SYSTEM_DECLARATION() { return getToken(UP2OBParser.SYSTEM_DECLARATION, 0); }
		public TerminalNode EOF() { return getToken(UP2OBParser.EOF, 0); }
		public Declaration_blockContext declaration_block() {
			return getRuleContext(Declaration_blockContext.class,0);
		}
		public List<Machine_blockContext> machine_block() {
			return getRuleContexts(Machine_blockContext.class);
		}
		public Machine_blockContext machine_block(int i) {
			return getRuleContext(Machine_blockContext.class,i);
		}
		public ModelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_model; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2OBListener ) ((UP2OBListener)listener).enterModel(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2OBListener ) ((UP2OBListener)listener).exitModel(this);
		}
	}

	public final ModelContext model() throws RecognitionException {
		ModelContext _localctx = new ModelContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_model);

				String str = "#Model name";
				((ModelContext)_localctx).mod =  new Model(str);
			
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			match(T__0);
			setState(11);
			((ModelContext)_localctx).declared = declaration_block();

					_localctx.mod.setInitialConditions(((ModelContext)_localctx).declared.dichiarazioni);
				
			setState(13);
			match(T__1);
			setState(18);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__2) {
				{
				setState(14);
				match(T__2);
				setState(15);
				((ModelContext)_localctx).mac = machine_block();

						_localctx.mod.addStateUpdater(((ModelContext)_localctx).mac.machine);
					
				}
			}

			setState(20);
			match(T__3);
			setState(26);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(21);
					((ModelContext)_localctx).reg = machine_block();

								_localctx.mod.addRule(((ModelContext)_localctx).reg.machine);
							
					}
					} 
				}
				setState(28);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			setState(29);
			match(T__4);
			setState(35);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(30);
					((ModelContext)_localctx).agent = machine_block();

								_localctx.mod.addAgent(((ModelContext)_localctx).agent.machine);
							
					}
					} 
				}
				setState(37);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			setState(38);
			match(T__5);
			setState(44);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(39);
					((ModelContext)_localctx).obj = machine_block();

								_localctx.mod.addObjective(((ModelContext)_localctx).obj.machine);
							
					}
					} 
				}
				setState(46);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			setState(47);
			match(SYSTEM_DECLARATION);
			setState(48);
			match(T__6);
			setState(49);
			match(EOF);
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

	public static class Declaration_blockContext extends ParserRuleContext {
		public InitialConditions dichiarazioni;
		public Token name;
		public Token value;
		public List<TerminalNode> SEMICOLON() { return getTokens(UP2OBParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(UP2OBParser.SEMICOLON, i);
		}
		public List<TerminalNode> ASSIGNMENT() { return getTokens(UP2OBParser.ASSIGNMENT); }
		public TerminalNode ASSIGNMENT(int i) {
			return getToken(UP2OBParser.ASSIGNMENT, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(UP2OBParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(UP2OBParser.COMMA, i);
		}
		public List<TerminalNode> CLOCK_ID() { return getTokens(UP2OBParser.CLOCK_ID); }
		public TerminalNode CLOCK_ID(int i) {
			return getToken(UP2OBParser.CLOCK_ID, i);
		}
		public List<TerminalNode> ID() { return getTokens(UP2OBParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(UP2OBParser.ID, i);
		}
		public List<TerminalNode> CHAN_DEC() { return getTokens(UP2OBParser.CHAN_DEC); }
		public TerminalNode CHAN_DEC(int i) {
			return getToken(UP2OBParser.CHAN_DEC, i);
		}
		public List<TerminalNode> POSITION_ID() { return getTokens(UP2OBParser.POSITION_ID); }
		public TerminalNode POSITION_ID(int i) {
			return getToken(UP2OBParser.POSITION_ID, i);
		}
		public List<TerminalNode> INT() { return getTokens(UP2OBParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(UP2OBParser.INT, i);
		}
		public List<TerminalNode> STATE_ID() { return getTokens(UP2OBParser.STATE_ID); }
		public TerminalNode STATE_ID(int i) {
			return getToken(UP2OBParser.STATE_ID, i);
		}
		public Declaration_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2OBListener ) ((UP2OBListener)listener).enterDeclaration_block(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2OBListener ) ((UP2OBListener)listener).exitDeclaration_block(this);
		}
	}

	public final Declaration_blockContext declaration_block() throws RecognitionException {
		Declaration_blockContext _localctx = new Declaration_blockContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration_block);

				((Declaration_blockContext)_localctx).dichiarazioni =  new InitialConditions();

			
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(T__7);


				
			setState(53);
			match(T__8);
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CHAN_DEC) | (1L << ID) | (1L << COMMA))) != 0)) {
				{
				{
				setState(54);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CHAN_DEC) | (1L << ID) | (1L << COMMA))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(59);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(60);
			match(SEMICOLON);
			setState(61);
			match(T__8);
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CHAN_DEC) | (1L << ID) | (1L << COMMA))) != 0)) {
				{
				{
				setState(62);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CHAN_DEC) | (1L << ID) | (1L << COMMA))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(67);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(68);
			match(SEMICOLON);
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(69);
				match(T__9);
				setState(76);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA || _la==POSITION_ID) {
					{
					setState(74);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case POSITION_ID:
						{
						setState(70);
						match(POSITION_ID);
						setState(71);
						match(ASSIGNMENT);
						setState(72);
						match(INT);
						}
						break;
					case COMMA:
						{
						setState(73);
						match(COMMA);
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					setState(78);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(79);
				match(SEMICOLON);
				}
			}

			setState(82);
			match(T__10);
			setState(86);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CLOCK_ID || _la==COMMA) {
				{
				{
				setState(83);
				_la = _input.LA(1);
				if ( !(_la==CLOCK_ID || _la==COMMA) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(88);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(89);
			match(SEMICOLON);
			setState(90);
			match(T__9);
			setState(96); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(96);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case POSITION_ID:
					{
					setState(91);
					((Declaration_blockContext)_localctx).name = match(POSITION_ID);
					setState(92);
					match(ASSIGNMENT);
					setState(93);
					((Declaration_blockContext)_localctx).value = match(INT);


							_localctx.dichiarazioni.addInitialPosition((((Declaration_blockContext)_localctx).name!=null?((Declaration_blockContext)_localctx).name.getText():null), (((Declaration_blockContext)_localctx).value!=null?((Declaration_blockContext)_localctx).value.getText():null));

						
					}
					break;
				case COMMA:
					{
					setState(95);
					match(COMMA);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(98); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==COMMA || _la==POSITION_ID );
			setState(100);
			match(SEMICOLON);
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(101);
				match(T__9);
				setState(109);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA || _la==STATE_ID) {
					{
					setState(107);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case STATE_ID:
						{
						setState(102);
						((Declaration_blockContext)_localctx).name = match(STATE_ID);
						setState(103);
						match(ASSIGNMENT);
						setState(104);
						((Declaration_blockContext)_localctx).value = match(INT);

								_localctx.dichiarazioni.addInitialState((((Declaration_blockContext)_localctx).name!=null?((Declaration_blockContext)_localctx).name.getText():null), (((Declaration_blockContext)_localctx).value!=null?((Declaration_blockContext)_localctx).value.getText():null));
								
						}
						break;
					case COMMA:
						{
						setState(106);
						match(COMMA);
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					setState(111);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(112);
				match(SEMICOLON);
				}
			}

			setState(118);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(115);
				match(T__10);
				setState(116);
				match(CLOCK_ID);
				setState(117);
				match(SEMICOLON);
				}
				break;
			}
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__10) {
				{
				setState(120);
				match(T__10);
				setState(121);
				match(CLOCK_ID);
				setState(122);
				match(SEMICOLON);
				}
			}

			setState(125);
			match(T__11);
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

	public static class Machine_blockContext extends ParserRuleContext {
		public Machine machine;
		public Token nome;
		public Location_blockContext loc;
		public Token init;
		public Transition_blockContext tran;
		public List<TerminalNode> ID() { return getTokens(UP2OBParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(UP2OBParser.ID, i);
		}
		public List<Location_blockContext> location_block() {
			return getRuleContexts(Location_blockContext.class);
		}
		public Location_blockContext location_block(int i) {
			return getRuleContext(Location_blockContext.class,i);
		}
		public List<Transition_blockContext> transition_block() {
			return getRuleContexts(Transition_blockContext.class);
		}
		public Transition_blockContext transition_block(int i) {
			return getRuleContext(Transition_blockContext.class,i);
		}
		public Machine_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_machine_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2OBListener ) ((UP2OBListener)listener).enterMachine_block(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2OBListener ) ((UP2OBListener)listener).exitMachine_block(this);
		}
	}

	public final Machine_blockContext machine_block() throws RecognitionException {
		Machine_blockContext _localctx = new Machine_blockContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_machine_block);

				((Machine_blockContext)_localctx).machine =  new Machine();
			
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(T__12);
			setState(128);
			match(T__13);
			setState(129);
			((Machine_blockContext)_localctx).nome = match(ID);
			setState(130);
			match(T__14);

					_localctx.machine.setName((((Machine_blockContext)_localctx).nome!=null?((Machine_blockContext)_localctx).nome.getText():null));
					
			setState(135); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(132);
				((Machine_blockContext)_localctx).loc = location_block();

							_localctx.machine.addLocation(((Machine_blockContext)_localctx).loc.loc);
							
				}
				}
				setState(137); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__19 || _la==T__20 );
			setState(139);
			match(T__15);
			setState(140);
			match(T__16);
			setState(141);
			((Machine_blockContext)_localctx).init = match(ID);
			setState(142);
			match(T__16);
			setState(143);
			match(T__17);

						_localctx.machine.setInitialLocation((((Machine_blockContext)_localctx).init!=null?((Machine_blockContext)_localctx).init.getText():null));
						
			setState(150);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(145);
					((Machine_blockContext)_localctx).tran = transition_block();

								_localctx.machine.addTransition(((Machine_blockContext)_localctx).tran.tran);
								
					}
					} 
				}
				setState(152);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			}
			setState(153);
			match(T__18);
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

	public static class Location_blockContext extends ParserRuleContext {
		public String loc;
		public Token loc_id;
		public List<TerminalNode> ID() { return getTokens(UP2OBParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(UP2OBParser.ID, i);
		}
		public TerminalNode CLOCK_ID() { return getToken(UP2OBParser.CLOCK_ID, 0); }
		public TerminalNode SMALLER_WEAK() { return getToken(UP2OBParser.SMALLER_WEAK, 0); }
		public TerminalNode INT() { return getToken(UP2OBParser.INT, 0); }
		public Location_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_location_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2OBListener ) ((UP2OBListener)listener).enterLocation_block(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2OBListener ) ((UP2OBListener)listener).exitLocation_block(this);
		}
	}

	public final Location_blockContext location_block() throws RecognitionException {
		Location_blockContext _localctx = new Location_blockContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_location_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			_la = _input.LA(1);
			if ( !(_la==T__19 || _la==T__20) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(156);
			match(T__16);
			setState(157);
			((Location_blockContext)_localctx).loc_id = match(ID);
			setState(158);
			match(T__16);
			setState(159);
			match(T__21);

					((Location_blockContext)_localctx).loc =  (((Location_blockContext)_localctx).loc_id!=null?((Location_blockContext)_localctx).loc_id.getText():null);
					
				
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13) {
				{
				setState(161);
				match(T__13);
				setState(162);
				match(ID);
				setState(163);
				match(T__14);
				}
			}

			setState(171);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__22) {
				{
				setState(166);
				match(T__22);
				setState(167);
				match(CLOCK_ID);
				setState(168);
				match(SMALLER_WEAK);
				setState(169);
				match(INT);
				setState(170);
				match(T__23);
				}
			}

			setState(173);
			match(T__24);
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

	public static class Transition_blockContext extends ParserRuleContext {
		public Transition tran;
		public Token source;
		public Token target;
		public Token synch;
		public Token value;
		public Token state_name;
		public List<TerminalNode> ID() { return getTokens(UP2OBParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(UP2OBParser.ID, i);
		}
		public List<TerminalNode> ASSIGNMENT() { return getTokens(UP2OBParser.ASSIGNMENT); }
		public TerminalNode ASSIGNMENT(int i) {
			return getToken(UP2OBParser.ASSIGNMENT, i);
		}
		public List<TerminalNode> CLOCK_ID() { return getTokens(UP2OBParser.CLOCK_ID); }
		public TerminalNode CLOCK_ID(int i) {
			return getToken(UP2OBParser.CLOCK_ID, i);
		}
		public List<TerminalNode> INT() { return getTokens(UP2OBParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(UP2OBParser.INT, i);
		}
		public List<TerminalNode> POSITION_ID() { return getTokens(UP2OBParser.POSITION_ID); }
		public TerminalNode POSITION_ID(int i) {
			return getToken(UP2OBParser.POSITION_ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(UP2OBParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(UP2OBParser.COMMA, i);
		}
		public List<TerminalNode> GREATER_STRONG() { return getTokens(UP2OBParser.GREATER_STRONG); }
		public TerminalNode GREATER_STRONG(int i) {
			return getToken(UP2OBParser.GREATER_STRONG, i);
		}
		public List<TerminalNode> EQUALS() { return getTokens(UP2OBParser.EQUALS); }
		public TerminalNode EQUALS(int i) {
			return getToken(UP2OBParser.EQUALS, i);
		}
		public List<TerminalNode> STATE_ID() { return getTokens(UP2OBParser.STATE_ID); }
		public TerminalNode STATE_ID(int i) {
			return getToken(UP2OBParser.STATE_ID, i);
		}
		public List<TerminalNode> AND() { return getTokens(UP2OBParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(UP2OBParser.AND, i);
		}
		public List<TerminalNode> PAR_OPEN() { return getTokens(UP2OBParser.PAR_OPEN); }
		public TerminalNode PAR_OPEN(int i) {
			return getToken(UP2OBParser.PAR_OPEN, i);
		}
		public List<TerminalNode> PAR_CLOSE() { return getTokens(UP2OBParser.PAR_CLOSE); }
		public TerminalNode PAR_CLOSE(int i) {
			return getToken(UP2OBParser.PAR_CLOSE, i);
		}
		public Transition_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_transition_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof UP2OBListener ) ((UP2OBListener)listener).enterTransition_block(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof UP2OBListener ) ((UP2OBListener)listener).exitTransition_block(this);
		}
	}

	public final Transition_blockContext transition_block() throws RecognitionException {
		Transition_blockContext _localctx = new Transition_blockContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_transition_block);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			_la = _input.LA(1);
			if ( !(_la==T__25 || _la==T__26) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(176);
			match(T__27);
			setState(177);
			match(T__16);
			setState(178);
			((Transition_blockContext)_localctx).source = match(ID);
			setState(179);
			match(T__16);
			setState(180);
			match(T__17);
			setState(181);
			match(T__28);
			setState(182);
			match(T__16);
			setState(183);
			((Transition_blockContext)_localctx).target = match(ID);
			setState(184);
			match(T__16);
			setState(185);
			match(T__17);

					((Transition_blockContext)_localctx).tran =  new Transition((((Transition_blockContext)_localctx).source!=null?((Transition_blockContext)_localctx).source.getText():null), (((Transition_blockContext)_localctx).target!=null?((Transition_blockContext)_localctx).target.getText():null));
				
			setState(245);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					setState(243);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
					case 1:
						{
						{
						setState(187);
						match(T__29);
						setState(192);
						_errHandler.sync(this);
						switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
						case 1:
							{
							setState(188);
							((Transition_blockContext)_localctx).synch = match(ID);
							setState(189);
							match(T__30);
							}
							break;
						case 2:
							{
							setState(190);
							((Transition_blockContext)_localctx).synch = match(ID);
							setState(191);
							match(T__31);
							}
							break;
						}
						setState(194);
						match(T__23);
						}

									_localctx.tran.setSynch((((Transition_blockContext)_localctx).synch!=null?((Transition_blockContext)_localctx).synch.getText():null));
								
						}
						break;
					case 2:
						{
						{
						{
						setState(197);
						match(T__32);
						setState(198);
						match(T__33);
						setState(199);
						match(ASSIGNMENT);
						setState(200);
						match(T__34);
						}
						setState(217);
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
						while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
							if ( _alt==1+1 ) {
								{
								setState(215);
								_errHandler.sync(this);
								switch (_input.LA(1)) {
								case CLOCK_ID:
									{
									setState(202);
									match(CLOCK_ID);
									setState(203);
									match(ASSIGNMENT);
									setState(204);
									match(INT);

													_localctx.tran.clockReset(); //I assume any clock assignment is a reset
												
									}
									break;
								case POSITION_ID:
									{
									setState(206);
									match(POSITION_ID);
									setState(207);
									match(ASSIGNMENT);
									setState(208);
									((Transition_blockContext)_localctx).value = match(INT);

													_localctx.tran.setPositionSet((((Transition_blockContext)_localctx).value!=null?((Transition_blockContext)_localctx).value.getText():null));
												
									}
									break;
								case STATE_ID:
									{
									setState(210);
									((Transition_blockContext)_localctx).state_name = match(STATE_ID);
									setState(211);
									match(ASSIGNMENT);
									setState(212);
									((Transition_blockContext)_localctx).value = match(INT);

													_localctx.tran.setStateSet((((Transition_blockContext)_localctx).state_name!=null?((Transition_blockContext)_localctx).state_name.getText():null), (((Transition_blockContext)_localctx).value!=null?((Transition_blockContext)_localctx).value.getText():null));
												
									}
									break;
								case COMMA:
									{
									setState(214);
									match(COMMA);
									}
									break;
								default:
									throw new NoViableAltException(this);
								}
								} 
							}
							setState(219);
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
						}
						setState(220);
						match(T__23);
						}
						}
						break;
					case 3:
						{
						{
						setState(221);
						match(T__32);
						setState(222);
						match(T__33);
						setState(223);
						match(ASSIGNMENT);
						setState(224);
						match(T__35);
						setState(239);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CLOCK_ID) | (1L << PAR_OPEN) | (1L << PAR_CLOSE) | (1L << POSITION_ID) | (1L << STATE_ID) | (1L << AND))) != 0)) {
							{
							setState(237);
							_errHandler.sync(this);
							switch (_input.LA(1)) {
							case CLOCK_ID:
								{
								setState(225);
								match(CLOCK_ID);
								setState(226);
								match(GREATER_STRONG);
								setState(227);
								match(INT);
								}
								break;
							case POSITION_ID:
								{
								setState(228);
								match(POSITION_ID);
								setState(229);
								match(EQUALS);
								setState(230);
								match(INT);
								}
								break;
							case STATE_ID:
								{
								setState(231);
								match(STATE_ID);
								setState(232);
								match(EQUALS);
								setState(233);
								match(INT);
								}
								break;
							case AND:
								{
								setState(234);
								match(AND);
								}
								break;
							case PAR_OPEN:
								{
								setState(235);
								match(PAR_OPEN);
								}
								break;
							case PAR_CLOSE:
								{
								setState(236);
								match(PAR_CLOSE);
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							}
							setState(241);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						setState(242);
						match(T__23);
						}
						}
						break;
					}
					} 
				}
				setState(247);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
			}
			setState(248);
			match(T__36);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:\u00fd\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\25"+
		"\n\2\3\2\3\2\3\2\3\2\7\2\33\n\2\f\2\16\2\36\13\2\3\2\3\2\3\2\3\2\7\2$"+
		"\n\2\f\2\16\2\'\13\2\3\2\3\2\3\2\3\2\7\2-\n\2\f\2\16\2\60\13\2\3\2\3\2"+
		"\3\2\3\2\3\3\3\3\3\3\3\3\7\3:\n\3\f\3\16\3=\13\3\3\3\3\3\3\3\7\3B\n\3"+
		"\f\3\16\3E\13\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3M\n\3\f\3\16\3P\13\3\3\3\5"+
		"\3S\n\3\3\3\3\3\7\3W\n\3\f\3\16\3Z\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\6"+
		"\3c\n\3\r\3\16\3d\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3n\n\3\f\3\16\3q\13\3"+
		"\3\3\5\3t\n\3\3\3\3\3\3\3\5\3y\n\3\3\3\3\3\3\3\5\3~\n\3\3\3\3\3\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\6\4\u008a\n\4\r\4\16\4\u008b\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\7\4\u0097\n\4\f\4\16\4\u009a\13\4\3\4\3\4\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00a7\n\5\3\5\3\5\3\5\3\5\3\5\5\5\u00ae"+
		"\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\5\6\u00c3\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6\u00da\n\6\f\6\16\6\u00dd\13"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6"+
		"\7\6\u00f0\n\6\f\6\16\6\u00f3\13\6\3\6\7\6\u00f6\n\6\f\6\16\6\u00f9\13"+
		"\6\3\6\3\6\3\6\b\34%.\u0098\u00db\u00f7\2\7\2\4\6\b\n\2\6\4\2()++\3\2"+
		"*+\3\2\26\27\3\2\34\35\2\u011a\2\f\3\2\2\2\4\65\3\2\2\2\6\u0081\3\2\2"+
		"\2\b\u009d\3\2\2\2\n\u00b1\3\2\2\2\f\r\7\3\2\2\r\16\5\4\3\2\16\17\b\2"+
		"\1\2\17\24\7\4\2\2\20\21\7\5\2\2\21\22\5\6\4\2\22\23\b\2\1\2\23\25\3\2"+
		"\2\2\24\20\3\2\2\2\24\25\3\2\2\2\25\26\3\2\2\2\26\34\7\6\2\2\27\30\5\6"+
		"\4\2\30\31\b\2\1\2\31\33\3\2\2\2\32\27\3\2\2\2\33\36\3\2\2\2\34\35\3\2"+
		"\2\2\34\32\3\2\2\2\35\37\3\2\2\2\36\34\3\2\2\2\37%\7\7\2\2 !\5\6\4\2!"+
		"\"\b\2\1\2\"$\3\2\2\2# \3\2\2\2$\'\3\2\2\2%&\3\2\2\2%#\3\2\2\2&(\3\2\2"+
		"\2\'%\3\2\2\2(.\7\b\2\2)*\5\6\4\2*+\b\2\1\2+-\3\2\2\2,)\3\2\2\2-\60\3"+
		"\2\2\2./\3\2\2\2.,\3\2\2\2/\61\3\2\2\2\60.\3\2\2\2\61\62\78\2\2\62\63"+
		"\7\t\2\2\63\64\7\2\2\3\64\3\3\2\2\2\65\66\7\n\2\2\66\67\b\3\1\2\67;\7"+
		"\13\2\28:\t\2\2\298\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;"+
		"\3\2\2\2>?\7,\2\2?C\7\13\2\2@B\t\2\2\2A@\3\2\2\2BE\3\2\2\2CA\3\2\2\2C"+
		"D\3\2\2\2DF\3\2\2\2EC\3\2\2\2FR\7,\2\2GN\7\f\2\2HI\7/\2\2IJ\7\63\2\2J"+
		"M\7\61\2\2KM\7+\2\2LH\3\2\2\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2"+
		"OQ\3\2\2\2PN\3\2\2\2QS\7,\2\2RG\3\2\2\2RS\3\2\2\2ST\3\2\2\2TX\7\r\2\2"+
		"UW\t\3\2\2VU\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y[\3\2\2\2ZX\3\2\2\2"+
		"[\\\7,\2\2\\b\7\f\2\2]^\7/\2\2^_\7\63\2\2_`\7\61\2\2`c\b\3\1\2ac\7+\2"+
		"\2b]\3\2\2\2ba\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2ef\3\2\2\2fs\7,\2"+
		"\2go\7\f\2\2hi\7\60\2\2ij\7\63\2\2jk\7\61\2\2kn\b\3\1\2ln\7+\2\2mh\3\2"+
		"\2\2ml\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2\2pr\3\2\2\2qo\3\2\2\2rt\7,"+
		"\2\2sg\3\2\2\2st\3\2\2\2tx\3\2\2\2uv\7\r\2\2vw\7*\2\2wy\7,\2\2xu\3\2\2"+
		"\2xy\3\2\2\2y}\3\2\2\2z{\7\r\2\2{|\7*\2\2|~\7,\2\2}z\3\2\2\2}~\3\2\2\2"+
		"~\177\3\2\2\2\177\u0080\7\16\2\2\u0080\5\3\2\2\2\u0081\u0082\7\17\2\2"+
		"\u0082\u0083\7\20\2\2\u0083\u0084\7)\2\2\u0084\u0085\7\21\2\2\u0085\u0089"+
		"\b\4\1\2\u0086\u0087\5\b\5\2\u0087\u0088\b\4\1\2\u0088\u008a\3\2\2\2\u0089"+
		"\u0086\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2"+
		"\2\2\u008c\u008d\3\2\2\2\u008d\u008e\7\22\2\2\u008e\u008f\7\23\2\2\u008f"+
		"\u0090\7)\2\2\u0090\u0091\7\23\2\2\u0091\u0092\7\24\2\2\u0092\u0098\b"+
		"\4\1\2\u0093\u0094\5\n\6\2\u0094\u0095\b\4\1\2\u0095\u0097\3\2\2\2\u0096"+
		"\u0093\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0099\3\2\2\2\u0098\u0096\3\2"+
		"\2\2\u0099\u009b\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\7\25\2\2\u009c"+
		"\7\3\2\2\2\u009d\u009e\t\4\2\2\u009e\u009f\7\23\2\2\u009f\u00a0\7)\2\2"+
		"\u00a0\u00a1\7\23\2\2\u00a1\u00a2\7\30\2\2\u00a2\u00a6\b\5\1\2\u00a3\u00a4"+
		"\7\20\2\2\u00a4\u00a5\7)\2\2\u00a5\u00a7\7\21\2\2\u00a6\u00a3\3\2\2\2"+
		"\u00a6\u00a7\3\2\2\2\u00a7\u00ad\3\2\2\2\u00a8\u00a9\7\31\2\2\u00a9\u00aa"+
		"\7*\2\2\u00aa\u00ab\7\64\2\2\u00ab\u00ac\7\61\2\2\u00ac\u00ae\7\32\2\2"+
		"\u00ad\u00a8\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0"+
		"\7\33\2\2\u00b0\t\3\2\2\2\u00b1\u00b2\t\5\2\2\u00b2\u00b3\7\36\2\2\u00b3"+
		"\u00b4\7\23\2\2\u00b4\u00b5\7)\2\2\u00b5\u00b6\7\23\2\2\u00b6\u00b7\7"+
		"\24\2\2\u00b7\u00b8\7\37\2\2\u00b8\u00b9\7\23\2\2\u00b9\u00ba\7)\2\2\u00ba"+
		"\u00bb\7\23\2\2\u00bb\u00bc\7\24\2\2\u00bc\u00f7\b\6\1\2\u00bd\u00c2\7"+
		" \2\2\u00be\u00bf\7)\2\2\u00bf\u00c3\7!\2\2\u00c0\u00c1\7)\2\2\u00c1\u00c3"+
		"\7\"\2\2\u00c2\u00be\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4"+
		"\u00c5\7\32\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00f6\b\6\1\2\u00c7\u00c8\7"+
		"#\2\2\u00c8\u00c9\7$\2\2\u00c9\u00ca\7\63\2\2\u00ca\u00cb\7%\2\2\u00cb"+
		"\u00db\3\2\2\2\u00cc\u00cd\7*\2\2\u00cd\u00ce\7\63\2\2\u00ce\u00cf\7\61"+
		"\2\2\u00cf\u00da\b\6\1\2\u00d0\u00d1\7/\2\2\u00d1\u00d2\7\63\2\2\u00d2"+
		"\u00d3\7\61\2\2\u00d3\u00da\b\6\1\2\u00d4\u00d5\7\60\2\2\u00d5\u00d6\7"+
		"\63\2\2\u00d6\u00d7\7\61\2\2\u00d7\u00da\b\6\1\2\u00d8\u00da\7+\2\2\u00d9"+
		"\u00cc\3\2\2\2\u00d9\u00d0\3\2\2\2\u00d9\u00d4\3\2\2\2\u00d9\u00d8\3\2"+
		"\2\2\u00da\u00dd\3\2\2\2\u00db\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc"+
		"\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00f6\7\32\2\2\u00df\u00e0\7"+
		"#\2\2\u00e0\u00e1\7$\2\2\u00e1\u00e2\7\63\2\2\u00e2\u00f1\7&\2\2\u00e3"+
		"\u00e4\7*\2\2\u00e4\u00e5\7\65\2\2\u00e5\u00f0\7\61\2\2\u00e6\u00e7\7"+
		"/\2\2\u00e7\u00e8\7\66\2\2\u00e8\u00f0\7\61\2\2\u00e9\u00ea\7\60\2\2\u00ea"+
		"\u00eb\7\66\2\2\u00eb\u00f0\7\61\2\2\u00ec\u00f0\7\67\2\2\u00ed\u00f0"+
		"\7-\2\2\u00ee\u00f0\7.\2\2\u00ef\u00e3\3\2\2\2\u00ef\u00e6\3\2\2\2\u00ef"+
		"\u00e9\3\2\2\2\u00ef\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2"+
		"\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2"+
		"\u00f4\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f6\7\32\2\2\u00f5\u00bd\3"+
		"\2\2\2\u00f5\u00c7\3\2\2\2\u00f5\u00df\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7"+
		"\u00f8\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00fa\3\2\2\2\u00f9\u00f7\3\2"+
		"\2\2\u00fa\u00fb\7\'\2\2\u00fb\13\3\2\2\2\36\24\34%.;CLNRXbdmosx}\u008b"+
		"\u0098\u00a6\u00ad\u00c2\u00d9\u00db\u00ef\u00f1\u00f5\u00f7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}