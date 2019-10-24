// Generated from UP2CO.g4 by ANTLR 4.7.1

   package se.cth.pursue;
   import java.util.Set;
   import java.util.HashSet;

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class UP2COLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
		"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
		"T__17", "T__18", "T__19", "ID", "CLOCK_ID", "POSITION_ID", "STATE_ID", 
		"INT", "SYNC_MASTER", "SYNC_SLAVE", "ACCEPTED_CHARACTER", "ASSIGNMENT", 
		"SMALLER_STRONG", "SMALLER_WEAK", "EQUALS", "AND", "OR", "LETTER", "LOWER", 
		"UPPER", "DIGIT", "ACCEPTED_SYMBOL", "NON_ACCEPTED_SYMBOL", "WS"
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


	public UP2COLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "UP2CO.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2%\u010d\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b"+
		"\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3"+
		"\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3"+
		"\22\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\5\26\u00c5"+
		"\n\26\3\26\7\26\u00c8\n\26\f\26\16\26\u00cb\13\26\3\27\3\27\3\27\3\30"+
		"\3\30\3\30\3\31\3\31\3\31\3\32\5\32\u00d7\n\32\3\32\6\32\u00da\n\32\r"+
		"\32\16\32\u00db\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\5\35\u00e7"+
		"\n\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\""+
		"\3#\3#\3#\3$\3$\5$\u00fe\n$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3"+
		"*\2\2+\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17"+
		"\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35"+
		"9\36;\37= ?!A\"C#E$G\2I\2K\2M\2O\2Q\2S%\3\2\4\b\2##%\61<B]`bb}\u0080\4"+
		"\2\13\13\17\17\2\u010d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2"+
		"\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2"+
		"\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3"+
		"\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2"+
		"\2\2E\3\2\2\2\2S\3\2\2\2\3U\3\2\2\2\5W\3\2\2\2\7_\3\2\2\2\ta\3\2\2\2\13"+
		"c\3\2\2\2\re\3\2\2\2\17w\3\2\2\2\21|\3\2\2\2\23\u0085\3\2\2\2\25\u0096"+
		"\3\2\2\2\27\u00a9\3\2\2\2\31\u00ab\3\2\2\2\33\u00ae\3\2\2\2\35\u00b0\3"+
		"\2\2\2\37\u00b4\3\2\2\2!\u00b6\3\2\2\2#\u00b8\3\2\2\2%\u00bc\3\2\2\2\'"+
		"\u00be\3\2\2\2)\u00c0\3\2\2\2+\u00c4\3\2\2\2-\u00cc\3\2\2\2/\u00cf\3\2"+
		"\2\2\61\u00d2\3\2\2\2\63\u00d6\3\2\2\2\65\u00dd\3\2\2\2\67\u00e0\3\2\2"+
		"\29\u00e6\3\2\2\2;\u00e8\3\2\2\2=\u00ed\3\2\2\2?\u00ef\3\2\2\2A\u00f2"+
		"\3\2\2\2C\u00f5\3\2\2\2E\u00f8\3\2\2\2G\u00fd\3\2\2\2I\u00ff\3\2\2\2K"+
		"\u0101\3\2\2\2M\u0103\3\2\2\2O\u0105\3\2\2\2Q\u0107\3\2\2\2S\u0109\3\2"+
		"\2\2UV\7\f\2\2V\4\3\2\2\2WX\7U\2\2XY\7v\2\2YZ\7c\2\2Z[\7v\2\2[\\\7g\2"+
		"\2\\]\7<\2\2]^\7\"\2\2^\6\3\2\2\2_`\7*\2\2`\b\3\2\2\2ab\7\"\2\2b\n\3\2"+
		"\2\2cd\7+\2\2d\f\3\2\2\2ef\7Y\2\2fg\7j\2\2gh\7k\2\2hi\7n\2\2ij\7g\2\2"+
		"jk\7\"\2\2kl\7{\2\2lm\7q\2\2mn\7w\2\2no\7\"\2\2op\7c\2\2pq\7t\2\2qr\7"+
		"g\2\2rs\7\"\2\2st\7k\2\2tu\7p\2\2uv\7\"\2\2v\16\3\2\2\2wx\7v\2\2xy\7t"+
		"\2\2yz\7w\2\2z{\7g\2\2{\20\3\2\2\2|}\7.\2\2}~\7\"\2\2~\177\7y\2\2\177"+
		"\u0080\7c\2\2\u0080\u0081\7k\2\2\u0081\u0082\7v\2\2\u0082\u0083\7\60\2"+
		"\2\u0083\u0084\7\f\2\2\u0084\22\3\2\2\2\u0085\u0086\7Y\2\2\u0086\u0087"+
		"\7j\2\2\u0087\u0088\7g\2\2\u0088\u0089\7p\2\2\u0089\u008a\7\"\2\2\u008a"+
		"\u008b\7{\2\2\u008b\u008c\7q\2\2\u008c\u008d\7w\2\2\u008d\u008e\7\"\2"+
		"\2\u008e\u008f\7c\2\2\u008f\u0090\7t\2\2\u0090\u0091\7g\2\2\u0091\u0092"+
		"\7\"\2\2\u0092\u0093\7k\2\2\u0093\u0094\7p\2\2\u0094\u0095\7\"\2\2\u0095"+
		"\24\3\2\2\2\u0096\u0097\7.\2\2\u0097\u0098\7\"\2\2\u0098\u0099\7v\2\2"+
		"\u0099\u009a\7c\2\2\u009a\u009b\7m\2\2\u009b\u009c\7g\2\2\u009c\u009d"+
		"\7\"\2\2\u009d\u009e\7v\2\2\u009e\u009f\7t\2\2\u009f\u00a0\7c\2\2\u00a0"+
		"\u00a1\7p\2\2\u00a1\u00a2\7u\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4\7v\2\2"+
		"\u00a4\u00a5\7k\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8"+
		"\7\"\2\2\u00a8\26\3\2\2\2\u00a9\u00aa\7/\2\2\u00aa\30\3\2\2\2\u00ab\u00ac"+
		"\7/\2\2\u00ac\u00ad\7@\2\2\u00ad\32\3\2\2\2\u00ae\u00af\7}\2\2\u00af\34"+
		"\3\2\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3\7w\2\2\u00b3"+
		"\36\3\2\2\2\u00b4\u00b5\7.\2\2\u00b5 \3\2\2\2\u00b6\u00b7\7\177\2\2\u00b7"+
		"\"\3\2\2\2\u00b8\u00b9\7\"\2\2\u00b9\u00ba\7@\2\2\u00ba\u00bb\7\"\2\2"+
		"\u00bb$\3\2\2\2\u00bc\u00bd\7\60\2\2\u00bd&\3\2\2\2\u00be\u00bf\7a\2\2"+
		"\u00bf(\3\2\2\2\u00c0\u00c1\7?\2\2\u00c1*\3\2\2\2\u00c2\u00c5\7Q\2\2\u00c3"+
		"\u00c5\5I%\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c9\3\2\2"+
		"\2\u00c6\u00c8\59\35\2\u00c7\u00c6\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7"+
		"\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca,\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc"+
		"\u00cd\7E\2\2\u00cd\u00ce\5+\26\2\u00ce.\3\2\2\2\u00cf\u00d0\7R\2\2\u00d0"+
		"\u00d1\5+\26\2\u00d1\60\3\2\2\2\u00d2\u00d3\7U\2\2\u00d3\u00d4\5+\26\2"+
		"\u00d4\62\3\2\2\2\u00d5\u00d7\7/\2\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7\3"+
		"\2\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00da\5M\'\2\u00d9\u00d8\3\2\2\2\u00da"+
		"\u00db\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\64\3\2\2"+
		"\2\u00dd\u00de\5+\26\2\u00de\u00df\7#\2\2\u00df\66\3\2\2\2\u00e0\u00e1"+
		"\5+\26\2\u00e1\u00e2\7A\2\2\u00e28\3\2\2\2\u00e3\u00e7\5G$\2\u00e4\u00e7"+
		"\5M\'\2\u00e5\u00e7\5O(\2\u00e6\u00e3\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6"+
		"\u00e5\3\2\2\2\u00e7:\3\2\2\2\u00e8\u00e9\7\"\2\2\u00e9\u00ea\7<\2\2\u00ea"+
		"\u00eb\7?\2\2\u00eb\u00ec\7\"\2\2\u00ec<\3\2\2\2\u00ed\u00ee\7>\2\2\u00ee"+
		">\3\2\2\2\u00ef\u00f0\7>\2\2\u00f0\u00f1\7?\2\2\u00f1@\3\2\2\2\u00f2\u00f3"+
		"\7?\2\2\u00f3\u00f4\7?\2\2\u00f4B\3\2\2\2\u00f5\u00f6\7(\2\2\u00f6\u00f7"+
		"\7(\2\2\u00f7D\3\2\2\2\u00f8\u00f9\7~\2\2\u00f9\u00fa\7~\2\2\u00faF\3"+
		"\2\2\2\u00fb\u00fe\5I%\2\u00fc\u00fe\5K&\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc"+
		"\3\2\2\2\u00feH\3\2\2\2\u00ff\u0100\4c|\2\u0100J\3\2\2\2\u0101\u0102\4"+
		"C\\\2\u0102L\3\2\2\2\u0103\u0104\4\62;\2\u0104N\3\2\2\2\u0105\u0106\7"+
		"a\2\2\u0106P\3\2\2\2\u0107\u0108\t\2\2\2\u0108R\3\2\2\2\u0109\u010a\t"+
		"\3\2\2\u010a\u010b\3\2\2\2\u010b\u010c\b*\2\2\u010cT\3\2\2\2\t\2\u00c4"+
		"\u00c9\u00d6\u00db\u00e6\u00fd\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}