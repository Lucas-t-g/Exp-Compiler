// Generated from /home/lucas_t_g/Documentos/E-Comp/Matérias/Compiladores/Exp-Compiler/Exp.g4 by ANTLR 4.8

import sys

symbol_table = []
symbol_table_use = []
type_table = []
func_table = []
has_error = False

stack_cur = 0
stack_max = 0
if_counter = 0
while_counter = 0
current_begin_while = []
current_end_while = []

tab_count = 1
def emit(comand, stack_att=0, initLN="    ", endLN='\n'):
    global stack_cur, stack_max, tab_count
    stack_cur += stack_att
    if stack_cur > stack_max:
        stack_max = stack_cur
    print(initLN*(tab_count) + comand, end=endLN)

def error(line = 0, msg = "", fatal = False):

    global has_error
    has_error = True
    if line != 0: msg = "in line " + str(line) + " " + msg

    if not fatal:
        print("ERROR: " + msg, file=sys.stderr)
    else:
        print("FATAL ERROR: inernal error", file=sys.stderr)
        sys.exit(1)

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExpParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMMENT=1, SPACE=2, PLUS=3, TIMES=4, MINUS=5, OVER=6, REM=7, ATTRIB=8, 
		COMMA=9, OP_PAR=10, CL_PAR=11, OP_CUR=12, CL_CUR=13, OP_SB=14, CL_SB=15, 
		EQ=16, NE=17, GT=18, GE=19, LT=20, LE=21, DOT=22, PUSH=23, LENGTH=24, 
		PRINT=25, READ_INT=26, READ_STR=27, IF=28, WHILE=29, BREAK=30, CONTINUE=31, 
		ELSE=32, DEF=33, NUMBER=34, STRING=35, NAME=36;
	public static final int
		RULE_program = 0, RULE_function = 1, RULE_main = 2, RULE_statement = 3, 
		RULE_st_call = 4, RULE_st_print = 5, RULE_st_attrib = 6, RULE_st_if = 7, 
		RULE_st_while = 8, RULE_st_break = 9, RULE_st_continue = 10, RULE_st_array_new = 11, 
		RULE_st_array_push = 12, RULE_st_array_set = 13, RULE_comparison = 14, 
		RULE_expression = 15, RULE_term = 16, RULE_factor = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "function", "main", "statement", "st_call", "st_print", "st_attrib", 
			"st_if", "st_while", "st_break", "st_continue", "st_array_new", "st_array_push", 
			"st_array_set", "comparison", "expression", "term", "factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'+'", "'*'", "'-'", "'/'", "'%'", "'='", "','", "'('", 
			"')'", "'{'", "'}'", "'['", "']'", "'=='", "'!='", "'>'", "'>='", "'<'", 
			"'<='", "'.'", "'push'", "'length'", "'print'", "'read_int'", "'read_str'", 
			"'if'", "'while'", "'break'", "'continue'", "'else'", "'def'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COMMENT", "SPACE", "PLUS", "TIMES", "MINUS", "OVER", "REM", "ATTRIB", 
			"COMMA", "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "OP_SB", "CL_SB", "EQ", 
			"NE", "GT", "GE", "LT", "LE", "DOT", "PUSH", "LENGTH", "PRINT", "READ_INT", 
			"READ_STR", "IF", "WHILE", "BREAK", "CONTINUE", "ELSE", "DEF", "NUMBER", 
			"STRING", "NAME"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
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
	public String getGrammarFileName() { return "Exp.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExpParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{

			print('.source Test.src')
			print('.class  public Test')
			print('.super  java/lang/Object\n')
			print('.method public <init>()V')
			print('    aload_0')
			print('    invokenonvirtual java/lang/Object/<init>()V')
			print('    return')
			print('.end method\n')
			    
			setState(40);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DEF) {
				{
				{
				setState(37);
				function();
				}
				}
				setState(42);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(43);
			main();
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

	public static class FunctionContext extends ParserRuleContext {
		public Token NAME;
		public TerminalNode DEF() { return getToken(ExpParser.DEF, 0); }
		public TerminalNode NAME() { return getToken(ExpParser.NAME, 0); }
		public TerminalNode OP_PAR() { return getToken(ExpParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(ExpParser.CL_PAR, 0); }
		public TerminalNode OP_CUR() { return getToken(ExpParser.OP_CUR, 0); }
		public TerminalNode CL_CUR() { return getToken(ExpParser.CL_CUR, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(DEF);
			setState(46);
			((FunctionContext)_localctx).NAME = match(NAME);
			setState(47);
			match(OP_PAR);
			setState(48);
			match(CL_PAR);

			global tab_count, symbol_table, type_table, symbol_table_use, func_table
			if (((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null) not in func_table:
			    tab_count = 0
			    emit(".method public static {}()V".format((((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null)))
			    tab_count = 1
			else:
			    error(line = (((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getLine():0), msg = "function '{}' is already declared".format((((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null)) )
			    
			setState(50);
			match(OP_CUR);
			setState(54);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << IF) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << NAME))) != 0)) {
				{
				{
				setState(51);
				statement();
				}
				}
				setState(56);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(57);
			match(CL_CUR);

			emit('return')
			tab_count = 0
			if len(symbol_table) > 0 : emit('.limit locals '+ str(len(symbol_table)) )
			emit('.limit stack '+ str(stack_max))
			emit('.end method')
			emit('; symbol_table: '+ str(symbol_table))
			symbol_table = []
			symbol_table_use = []
			type_table = []
			func_table.append((((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null))
			emit("")
			tab_count = 1
			    
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

	public static class MainContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_main);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{

			print('.method public static main([Ljava/lang/String;)V\n')
			    
			setState(62); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(61);
				statement();
				}
				}
				setState(64); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << IF) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << NAME))) != 0) );


			print('    return')
			print('.limit stack', stack_max)
			if len(symbol_table) > 0 : print('.limit locals', len(symbol_table))
			print('.end method')
			print('\n; symbol_table:', symbol_table)

			if 0 in symbol_table_use:
			    for index, symbol in enumerate(symbol_table):
			        if symbol_table_use[index] == 0:
			            error(msg = "variable '" + symbol + "' is defined but never used")

			if has_error:
			    sys.exit(1)
			    
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

	public static class StatementContext extends ParserRuleContext {
		public St_printContext st_print() {
			return getRuleContext(St_printContext.class,0);
		}
		public St_ifContext st_if() {
			return getRuleContext(St_ifContext.class,0);
		}
		public St_whileContext st_while() {
			return getRuleContext(St_whileContext.class,0);
		}
		public St_breakContext st_break() {
			return getRuleContext(St_breakContext.class,0);
		}
		public St_continueContext st_continue() {
			return getRuleContext(St_continueContext.class,0);
		}
		public St_array_newContext st_array_new() {
			return getRuleContext(St_array_newContext.class,0);
		}
		public St_array_setContext st_array_set() {
			return getRuleContext(St_array_setContext.class,0);
		}
		public St_array_pushContext st_array_push() {
			return getRuleContext(St_array_pushContext.class,0);
		}
		public St_attribContext st_attrib() {
			return getRuleContext(St_attribContext.class,0);
		}
		public St_callContext st_call() {
			return getRuleContext(St_callContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_statement);
		try {
			setState(78);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(68);
				st_print();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				st_if();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(70);
				st_while();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(71);
				st_break();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(72);
				st_continue();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(73);
				st_array_new();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(74);
				st_array_set();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(75);
				st_array_push();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(76);
				st_attrib();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(77);
				st_call();
				}
				break;
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

	public static class St_callContext extends ParserRuleContext {
		public Token NAME;
		public TerminalNode NAME() { return getToken(ExpParser.NAME, 0); }
		public TerminalNode OP_PAR() { return getToken(ExpParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(ExpParser.CL_PAR, 0); }
		public St_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_call; }
	}

	public final St_callContext st_call() throws RecognitionException {
		St_callContext _localctx = new St_callContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_st_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			((St_callContext)_localctx).NAME = match(NAME);
			setState(81);
			match(OP_PAR);
			setState(82);
			match(CL_PAR);

			if (((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getText():null) in func_table:
			    emit("invokestatic Test/{}()V".format((((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getText():null)))
			else:
			    error(line = (((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getLine():0), msg="function '{}' is not declared".format((((St_callContext)_localctx).NAME!=null?((St_callContext)_localctx).NAME.getText():null)))
			    
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

	public static class St_printContext extends ParserRuleContext {
		public ExpressionContext e1;
		public ExpressionContext e2;
		public TerminalNode PRINT() { return getToken(ExpParser.PRINT, 0); }
		public TerminalNode OP_PAR() { return getToken(ExpParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(ExpParser.CL_PAR, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ExpParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ExpParser.COMMA, i);
		}
		public St_printContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_print; }
	}

	public final St_printContext st_print() throws RecognitionException {
		St_printContext _localctx = new St_printContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_st_print);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(PRINT);
			setState(86);
			match(OP_PAR);

			emit('getstatic java/lang/System/out Ljava/io/PrintStream;', stack_att = +1)
			    
			setState(88);
			((St_printContext)_localctx).e1 = expression();

			if ((St_printContext)_localctx).e1.type == 'i':
			    emit('invokevirtual java/io/PrintStream/print(I)V\n', stack_att = -2)
			elif ((St_printContext)_localctx).e1.type == 's':
			    emit('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', stack_att = -2)
			elif ((St_printContext)_localctx).e1.type == 'a':
			    emit("invokevirtual Array/string()Ljava/lang/String;")
			    emit("invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n", stack_att = -2)
			else:
			    error(fatal = True)
			    
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(90);
				match(COMMA);

				emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
				    
				setState(92);
				((St_printContext)_localctx).e2 = expression();

				if ((St_printContext)_localctx).e2.type == 'i':
				    emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
				elif ((St_printContext)_localctx).e2.type == 's':
				    emit('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
				elif ((St_printContext)_localctx).e1.type == 'a':
				    emit("invokevirtual Array/string()Ljava/lang/String;")
				    emit("invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n", stack_att = -2)
				else:
				    error(fatal = True)
				    
				}
				}
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(100);
			match(CL_PAR);

			emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
			emit('invokevirtual java/io/PrintStream/println()V\n', -1)
			    
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

	public static class St_attribContext extends ParserRuleContext {
		public Token NAME;
		public ExpressionContext expression;
		public TerminalNode NAME() { return getToken(ExpParser.NAME, 0); }
		public TerminalNode ATTRIB() { return getToken(ExpParser.ATTRIB, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public St_attribContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_attrib; }
	}

	public final St_attribContext st_attrib() throws RecognitionException {
		St_attribContext _localctx = new St_attribContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_st_attrib);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			((St_attribContext)_localctx).NAME = match(NAME);
			setState(104);
			match(ATTRIB);
			setState(105);
			((St_attribContext)_localctx).expression = expression();

			# 1. testar se a varialvel name já existe:  se não existir inclui (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) na symbol_table
			if (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) not in symbol_table:
			    symbol_table.append((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null))
			    symbol_table_use.append(0)
			    type_table.append(((St_attribContext)_localctx).expression.type)

			# 2. encontrar o índice de (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) e gerar o bytecode 'istore index'
			index = symbol_table.index((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null))
			my_type = type_table[index]
			if my_type == ((St_attribContext)_localctx).expression.type:
			    if my_type == 'i':
			        emit("istore "+ str(index) + '\n', -1)
			    elif my_type == 's':
			        emit("astore "+ str(index) + '\n', -1)
			    else:
			        error(fatal = True)
			else:
			    if my_type == "i":
			        error(line = (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getLine():0), msg = "'" + (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) + "' must be an " + "integer")
			    elif my_type == "s":
			        error(line = (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getLine():0), msg = "'" + (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) + "' must be an " + "string")
			    elif my_type == "a":
			        error(line = (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getLine():0), msg = "'" + (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) + "' must be an " + "array")
			    
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

	public static class St_ifContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(ExpParser.IF, 0); }
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public List<TerminalNode> OP_CUR() { return getTokens(ExpParser.OP_CUR); }
		public TerminalNode OP_CUR(int i) {
			return getToken(ExpParser.OP_CUR, i);
		}
		public List<TerminalNode> CL_CUR() { return getTokens(ExpParser.CL_CUR); }
		public TerminalNode CL_CUR(int i) {
			return getToken(ExpParser.CL_CUR, i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(ExpParser.ELSE, 0); }
		public St_ifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_if; }
	}

	public final St_ifContext st_if() throws RecognitionException {
		St_ifContext _localctx = new St_ifContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_st_if);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(IF);
			setState(109);
			comparison();

			have_else = False
			global if_counter
			if_counter_local = if_counter
			not_if_local = "NOT_IF_" + str(if_counter_local)
			if_counter += 1
			emit(not_if_local, initLN='')
			    
			setState(111);
			match(OP_CUR);
			setState(113); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(112);
				statement();
				}
				}
				setState(115); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << IF) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << NAME))) != 0) );
			setState(117);
			match(CL_CUR);
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{

				have_else = True
				end_else = "END_ELSE_"+str(if_counter_local)
				emit("goto "+end_else)
				emit(not_if_local + ':\n' )
				    
				setState(119);
				match(ELSE);
				setState(120);
				match(OP_CUR);
				setState(122); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(121);
					statement();
					}
					}
					setState(124); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << IF) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << NAME))) != 0) );
				setState(126);
				match(CL_CUR);
				}
			}


			if not have_else: emit(not_if_local + ':\n' )
			else            : emit(end_else + ':\n')
			    
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

	public static class St_whileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(ExpParser.WHILE, 0); }
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public TerminalNode OP_CUR() { return getToken(ExpParser.OP_CUR, 0); }
		public TerminalNode CL_CUR() { return getToken(ExpParser.CL_CUR, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public St_whileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_while; }
	}

	public final St_whileContext st_while() throws RecognitionException {
		St_whileContext _localctx = new St_whileContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_st_while);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(WHILE);

			global while_counter
			begin_while = "BEGIN_WHILE_" + str(while_counter)
			end_while = "END_WHILE_" + str(while_counter)
			emit(begin_while + ':')

			global current_begin_while
			current_begin_while.append(begin_while)

			global current_end_while
			current_end_while.append(end_while)

			while_counter += 1
			    
			setState(134);
			comparison();

			emit(end_while, initLN='')
			    
			setState(136);
			match(OP_CUR);
			setState(138); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(137);
				statement();
				}
				}
				setState(140); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << IF) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << NAME))) != 0) );
			setState(142);
			match(CL_CUR);

			emit("goto "+begin_while)
			emit(end_while+':\n')
			current_begin_while.pop()
			current_end_while.pop()
			    
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

	public static class St_breakContext extends ParserRuleContext {
		public Token BREAK;
		public TerminalNode BREAK() { return getToken(ExpParser.BREAK, 0); }
		public St_breakContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_break; }
	}

	public final St_breakContext st_break() throws RecognitionException {
		St_breakContext _localctx = new St_breakContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_st_break);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			((St_breakContext)_localctx).BREAK = match(BREAK);

			global current_end_while
			if len(current_end_while) > 0:
			    emit("goto " + current_end_while[-1] + " ;break")
			else:
			    error(line = (((St_breakContext)_localctx).BREAK!=null?((St_breakContext)_localctx).BREAK.getLine():0), msg = "the 'break' command must be in a loop escope")
			    
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

	public static class St_continueContext extends ParserRuleContext {
		public Token CONTINUE;
		public TerminalNode CONTINUE() { return getToken(ExpParser.CONTINUE, 0); }
		public St_continueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_continue; }
	}

	public final St_continueContext st_continue() throws RecognitionException {
		St_continueContext _localctx = new St_continueContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_st_continue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			((St_continueContext)_localctx).CONTINUE = match(CONTINUE);

			global current_begin_while
			if len(current_begin_while) > 0:
			    emit("goto " + current_begin_while[-1] + " ;continue")
			else:
			    error(line = (((St_continueContext)_localctx).CONTINUE!=null?((St_continueContext)_localctx).CONTINUE.getLine():0), msg = "the 'continue' command must be in a loop escope")
			    
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

	public static class St_array_newContext extends ParserRuleContext {
		public Token NAME;
		public TerminalNode NAME() { return getToken(ExpParser.NAME, 0); }
		public TerminalNode ATTRIB() { return getToken(ExpParser.ATTRIB, 0); }
		public TerminalNode OP_SB() { return getToken(ExpParser.OP_SB, 0); }
		public TerminalNode CL_SB() { return getToken(ExpParser.CL_SB, 0); }
		public St_array_newContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_array_new; }
	}

	public final St_array_newContext st_array_new() throws RecognitionException {
		St_array_newContext _localctx = new St_array_newContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_st_array_new);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			((St_array_newContext)_localctx).NAME = match(NAME);
			setState(152);
			match(ATTRIB);
			setState(153);
			match(OP_SB);
			setState(154);
			match(CL_SB);

			# 1. testar se a varialvel name já existe:  se não existir inclui (((St_array_newContext)_localctx).NAME!=null?((St_array_newContext)_localctx).NAME.getText():null) na symbol_table
			if (((St_array_newContext)_localctx).NAME!=null?((St_array_newContext)_localctx).NAME.getText():null) not in symbol_table:
			    symbol_table.append((((St_array_newContext)_localctx).NAME!=null?((St_array_newContext)_localctx).NAME.getText():null))
			    symbol_table_use.append(0)
			    type_table.append('a')
			else:
			    error(line = (((St_array_newContext)_localctx).NAME!=null?((St_array_newContext)_localctx).NAME.getLine():0), msg = "'" + (((St_array_newContext)_localctx).NAME!=null?((St_array_newContext)_localctx).NAME.getText():null) + "' is already declared")

			# 2. encontrar o índice de (((St_array_newContext)_localctx).NAME!=null?((St_array_newContext)_localctx).NAME.getText():null) e gerar o bytecode 'istore index'
			index = symbol_table.index((((St_array_newContext)_localctx).NAME!=null?((St_array_newContext)_localctx).NAME.getText():null))
			emit("new Array", stack_att=+1)
			emit("dup", stack_att=+1)
			emit("invokespecial Array/<init>()V", stack_att=-1)
			emit("astore "+str(index),endLN='\n\n', stack_att=-1)
			    
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

	public static class St_array_pushContext extends ParserRuleContext {
		public Token NAME;
		public TerminalNode NAME() { return getToken(ExpParser.NAME, 0); }
		public TerminalNode DOT() { return getToken(ExpParser.DOT, 0); }
		public TerminalNode PUSH() { return getToken(ExpParser.PUSH, 0); }
		public TerminalNode OP_PAR() { return getToken(ExpParser.OP_PAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode CL_PAR() { return getToken(ExpParser.CL_PAR, 0); }
		public St_array_pushContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_array_push; }
	}

	public final St_array_pushContext st_array_push() throws RecognitionException {
		St_array_pushContext _localctx = new St_array_pushContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_st_array_push);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			((St_array_pushContext)_localctx).NAME = match(NAME);
			setState(158);
			match(DOT);
			setState(159);
			match(PUSH);

			index = symbol_table.index((((St_array_pushContext)_localctx).NAME!=null?((St_array_pushContext)_localctx).NAME.getText():null))  
			emit("aload " + str(index), stack_att=+1)
			    
			setState(161);
			match(OP_PAR);
			setState(162);
			expression();
			setState(163);
			match(CL_PAR);

			#emit("ldc " + str(expression.text), stack_att=+1)
			emit("invokevirtual Array/push(I)V\n", stack_att=-2)

			    
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

	public static class St_array_setContext extends ParserRuleContext {
		public Token NAME;
		public ExpressionContext ex1;
		public ExpressionContext ex2;
		public TerminalNode NAME() { return getToken(ExpParser.NAME, 0); }
		public TerminalNode OP_SB() { return getToken(ExpParser.OP_SB, 0); }
		public TerminalNode CL_SB() { return getToken(ExpParser.CL_SB, 0); }
		public TerminalNode ATTRIB() { return getToken(ExpParser.ATTRIB, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public St_array_setContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_array_set; }
	}

	public final St_array_setContext st_array_set() throws RecognitionException {
		St_array_setContext _localctx = new St_array_setContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_st_array_set);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			((St_array_setContext)_localctx).NAME = match(NAME);
			 
			if (((St_array_setContext)_localctx).NAME!=null?((St_array_setContext)_localctx).NAME.getText():null) in symbol_table:
			    index = symbol_table.index((((St_array_setContext)_localctx).NAME!=null?((St_array_setContext)_localctx).NAME.getText():null))
			    emit("aload " + str(index), stack_att = +1)
			else:
			    error(line = (((St_array_setContext)_localctx).NAME!=null?((St_array_setContext)_localctx).NAME.getLine():0), msg = "'" + (((St_array_setContext)_localctx).NAME!=null?((St_array_setContext)_localctx).NAME.getText():null) + "' is not declared")
			    
			setState(168);
			match(OP_SB);
			setState(169);
			((St_array_setContext)_localctx).ex1 = expression();
			setState(170);
			match(CL_SB);
			setState(171);
			match(ATTRIB);
			setState(172);
			((St_array_setContext)_localctx).ex2 = expression();

			if (((St_array_setContext)_localctx).NAME!=null?((St_array_setContext)_localctx).NAME.getText():null) in symbol_table:
			    my_type = type_table[index]
			    if my_type == 'a':
			        if ((St_array_setContext)_localctx).ex1.type == 'i':
			            if ((St_array_setContext)_localctx).ex2.type == 'i':
			                emit("invokevirtual Array/set(II)V\n", stack_att = -3)
			            else:
			                error(line = (((St_array_setContext)_localctx).NAME!=null?((St_array_setContext)_localctx).NAME.getLine():0), msg = "arrays can store only integers and '" + (((St_array_setContext)_localctx).ex2!=null?_input.getText(((St_array_setContext)_localctx).ex2.start,((St_array_setContext)_localctx).ex2.stop):null) + "' is an " + ('array' if ((St_array_setContext)_localctx).ex2.type == 'a' else 'string') )
			        else:
			            error(line = (((St_array_setContext)_localctx).NAME!=null?((St_array_setContext)_localctx).NAME.getLine():0), msg = "array index must be integer")
			    else:
			        error(line = (((St_array_setContext)_localctx).NAME!=null?((St_array_setContext)_localctx).NAME.getLine():0), msg = "only arrays can be indexable")
			    
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

	public static class ComparisonContext extends ParserRuleContext {
		public ExpressionContext e1;
		public Token op;
		public ExpressionContext e2;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQ() { return getToken(ExpParser.EQ, 0); }
		public TerminalNode NE() { return getToken(ExpParser.NE, 0); }
		public TerminalNode GT() { return getToken(ExpParser.GT, 0); }
		public TerminalNode GE() { return getToken(ExpParser.GE, 0); }
		public TerminalNode LT() { return getToken(ExpParser.LT, 0); }
		public TerminalNode LE() { return getToken(ExpParser.LE, 0); }
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_comparison);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			((ComparisonContext)_localctx).e1 = expression();
			setState(176);
			((ComparisonContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQ) | (1L << NE) | (1L << GT) | (1L << GE) | (1L << LT) | (1L << LE))) != 0)) ) {
				((ComparisonContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(177);
			((ComparisonContext)_localctx).e2 = expression();

			# usa a comparação inversa para o desvio

			if ((ComparisonContext)_localctx).e1.type == 'i' and ((ComparisonContext)_localctx).e2.type == 'i':
			    if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.GT  : emit("if_icmple ", stack_att=-2, endLN='')
			    if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.NE  : emit("if_icmpeq ", stack_att=-2, endLN='')
			    if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.GE  : emit("if_icmplt ", stack_att=-2, endLN='')
			    if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.LT  : emit("if_icmpge ", stack_att=-2, endLN='')
			    if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.EQ  : emit("if_icmpne ", stack_att=-2, endLN='')
			    if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.LE  : emit("if_icmpgt ", stack_att=-2, endLN='')
			else:
			    error(line = (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getLine():0), msg = "cannot mix types")
			    
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

	public static class ExpressionContext extends ParserRuleContext {
		public  type;
		public TermContext t1;
		public Token op;
		public TermContext t2;
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(ExpParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(ExpParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(ExpParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(ExpParser.MINUS, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			((ExpressionContext)_localctx).t1 = term();
			setState(187);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(181);
				((ExpressionContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
					((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(182);
				((ExpressionContext)_localctx).t2 = term();

				if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == ExpParser.PLUS  : emit('iadd', -1)
				if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == ExpParser.MINUS : emit('isub', -1)
				if ((ExpressionContext)_localctx).t1.type != 'err' and ((ExpressionContext)_localctx).t2.type != 'err':
				    if ((ExpressionContext)_localctx).t1.type != ((ExpressionContext)_localctx).t2.type:
				        error(line = (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getLine():0), msg = "cannot mix types")
				    elif ((ExpressionContext)_localctx).t1.type != 'i' or ((ExpressionContext)_localctx).t2.type != 'i':
				        error(line = (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getLine():0), msg = "math operations is only for integers" )
				        
				}
				}
				setState(189);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}

			_localctx.type = ((ExpressionContext)_localctx).t1.type
			    
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

	public static class TermContext extends ParserRuleContext {
		public  type;
		public FactorContext f1;
		public Token op;
		public FactorContext f2;
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> TIMES() { return getTokens(ExpParser.TIMES); }
		public TerminalNode TIMES(int i) {
			return getToken(ExpParser.TIMES, i);
		}
		public List<TerminalNode> OVER() { return getTokens(ExpParser.OVER); }
		public TerminalNode OVER(int i) {
			return getToken(ExpParser.OVER, i);
		}
		public List<TerminalNode> REM() { return getTokens(ExpParser.REM); }
		public TerminalNode REM(int i) {
			return getToken(ExpParser.REM, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			((TermContext)_localctx).f1 = factor();
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) {
				{
				{
				setState(193);
				((TermContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) ) {
					((TermContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(194);
				((TermContext)_localctx).f2 = factor();

				if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == ExpParser.TIMES : emit('imul', -1)
				if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == ExpParser.OVER  : emit('idiv', -1)
				if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == ExpParser.REM   : emit('irem', -1)
				if ((TermContext)_localctx).f1.type != ((TermContext)_localctx).f2.type:
				    error(line = (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getLine():0), msg = "cannot mix types")
				elif ((TermContext)_localctx).f1.type != 'i' or ((TermContext)_localctx).f2.type != 'i':
				    error(msg = "in line " + str((((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getLine():0)) + " math operations is only for integers" )
				    
				}
				}
				setState(201);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}

			_localctx.type = ((TermContext)_localctx).f1.type
			    
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

	public static class FactorContext extends ParserRuleContext {
		public  type;
		public Token NUMBER;
		public ExpressionContext f1;
		public ExpressionContext expression;
		public Token NAME;
		public Token STRING;
		public TerminalNode NUMBER() { return getToken(ExpParser.NUMBER, 0); }
		public TerminalNode OP_PAR() { return getToken(ExpParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(ExpParser.CL_PAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NAME() { return getToken(ExpParser.NAME, 0); }
		public TerminalNode READ_INT() { return getToken(ExpParser.READ_INT, 0); }
		public TerminalNode STRING() { return getToken(ExpParser.STRING, 0); }
		public TerminalNode READ_STR() { return getToken(ExpParser.READ_STR, 0); }
		public TerminalNode OP_SB() { return getToken(ExpParser.OP_SB, 0); }
		public TerminalNode CL_SB() { return getToken(ExpParser.CL_SB, 0); }
		public TerminalNode DOT() { return getToken(ExpParser.DOT, 0); }
		public TerminalNode LENGTH() { return getToken(ExpParser.LENGTH, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_factor);
		try {
			setState(234);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(204);
				((FactorContext)_localctx).NUMBER = match(NUMBER);

				emit('ldc ' + (((FactorContext)_localctx).NUMBER!=null?((FactorContext)_localctx).NUMBER.getText():null), +1)
				_localctx.type = 'i'
				    
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				match(OP_PAR);
				setState(207);
				((FactorContext)_localctx).f1 = ((FactorContext)_localctx).expression = expression();
				setState(208);
				match(CL_PAR);

				_localctx.type = ((FactorContext)_localctx).expression.type
				    
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(211);
				((FactorContext)_localctx).NAME = match(NAME);

				# encontrar o index de (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) e gerar o bytecode 'iload index'
				if (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) not in symbol_table:
				    error(line = (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getLine():0), msg = "variable '" + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + "' is not declared")
				    _localctx.type = 'err'
				else:
				    index = symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))
				    symbol_table_use[index] += 1
				    my_type = type_table[index]
				    if my_type == 'i':
				        emit("iload "+ str(index), +1)
				        _localctx.type = my_type
				    elif my_type == 's' or my_type == 'a':
				        emit("aload "+ str(index), +1)
				        _localctx.type = my_type
				    else:
				        error(fatal = True)
				    
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(213);
				match(READ_INT);
				setState(214);
				match(OP_PAR);
				setState(215);
				match(CL_PAR);

				emit("invokestatic Runtime/readInt()I", +1)
				_localctx.type = 'i'
				    
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(217);
				((FactorContext)_localctx).STRING = match(STRING);

				emit('ldc '+ (((FactorContext)_localctx).STRING!=null?((FactorContext)_localctx).STRING.getText():null), +1)
				_localctx.type = 's'
				    
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(219);
				match(READ_STR);
				setState(220);
				match(OP_PAR);
				setState(221);
				match(CL_PAR);

				emit("invokestatic Runtime/readString()Ljava/lang/String;", +1)
				_localctx.type = 's'
				    
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(223);
				((FactorContext)_localctx).NAME = match(NAME);

				if (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) in symbol_table:
				    index = symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))
				    my_type = type_table[index]
				    if my_type == 'a':
				        emit("aload " + str(index), stack_att = +1)
				    else:
				        error(line = (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getLine():0), msg = " only arrays can be indexable")
				else:
				    error(line = (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getLine():0), msg = " '" + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + "' is not declared" )
				    
				setState(225);
				match(OP_SB);
				setState(226);
				expression();
				setState(227);
				match(CL_SB);

				emit("invokevirtual Array/get(I)I", stack_att = -1)
				_localctx.type = 'i'
				    
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(230);
				((FactorContext)_localctx).NAME = match(NAME);
				setState(231);
				match(DOT);
				setState(232);
				match(LENGTH);

				if (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) in symbol_table:
				    index = symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))
				    my_type = type_table[index]
				    if my_type == 'a':
				        emit("aload " + str(index), +1)
				        emit("invokevirtual Array/length()I"    )
				        _localctx.type = 'i'
				    else :
				        error(line = (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getLine():0), msg = "'" + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + "' is not an array")
				else:
				    error(line = (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getLine():0), msg = " '" + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + "' is not declared" )
				_localctx.type = 'i'
				    
				}
				break;
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3&\u00ef\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\3\2\7\2)\n\2\f\2\16\2,\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\7\3\67\n\3\f\3\16\3:\13\3\3\3\3\3\3\3\3\4\3\4\6\4A\n\4\r\4\16"+
		"\4B\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5Q\n\5\3\6\3\6\3"+
		"\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7b\n\7\f\7\16\7e"+
		"\13\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\6\tt\n\t\r\t"+
		"\16\tu\3\t\3\t\3\t\3\t\3\t\6\t}\n\t\r\t\16\t~\3\t\3\t\5\t\u0083\n\t\3"+
		"\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\6\n\u008d\n\n\r\n\16\n\u008e\3\n\3\n\3"+
		"\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\7\21\u00bc\n\21"+
		"\f\21\16\21\u00bf\13\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\7\22\u00c8"+
		"\n\22\f\22\16\22\u00cb\13\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3"+
		"\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3"+
		"\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00ed\n\23\3\23"+
		"\2\2\24\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\5\3\2\22\27\4\2\5"+
		"\5\7\7\4\2\6\6\b\t\2\u00f6\2&\3\2\2\2\4/\3\2\2\2\6>\3\2\2\2\bP\3\2\2\2"+
		"\nR\3\2\2\2\fW\3\2\2\2\16i\3\2\2\2\20n\3\2\2\2\22\u0086\3\2\2\2\24\u0093"+
		"\3\2\2\2\26\u0096\3\2\2\2\30\u0099\3\2\2\2\32\u009f\3\2\2\2\34\u00a8\3"+
		"\2\2\2\36\u00b1\3\2\2\2 \u00b6\3\2\2\2\"\u00c2\3\2\2\2$\u00ec\3\2\2\2"+
		"&*\b\2\1\2\')\5\4\3\2(\'\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+-\3\2\2"+
		"\2,*\3\2\2\2-.\5\6\4\2.\3\3\2\2\2/\60\7#\2\2\60\61\7&\2\2\61\62\7\f\2"+
		"\2\62\63\7\r\2\2\63\64\b\3\1\2\648\7\16\2\2\65\67\5\b\5\2\66\65\3\2\2"+
		"\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29;\3\2\2\2:8\3\2\2\2;<\7\17\2\2<="+
		"\b\3\1\2=\5\3\2\2\2>@\b\4\1\2?A\5\b\5\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2"+
		"BC\3\2\2\2CD\3\2\2\2DE\b\4\1\2E\7\3\2\2\2FQ\5\f\7\2GQ\5\20\t\2HQ\5\22"+
		"\n\2IQ\5\24\13\2JQ\5\26\f\2KQ\5\30\r\2LQ\5\34\17\2MQ\5\32\16\2NQ\5\16"+
		"\b\2OQ\5\n\6\2PF\3\2\2\2PG\3\2\2\2PH\3\2\2\2PI\3\2\2\2PJ\3\2\2\2PK\3\2"+
		"\2\2PL\3\2\2\2PM\3\2\2\2PN\3\2\2\2PO\3\2\2\2Q\t\3\2\2\2RS\7&\2\2ST\7\f"+
		"\2\2TU\7\r\2\2UV\b\6\1\2V\13\3\2\2\2WX\7\33\2\2XY\7\f\2\2YZ\b\7\1\2Z["+
		"\5 \21\2[c\b\7\1\2\\]\7\13\2\2]^\b\7\1\2^_\5 \21\2_`\b\7\1\2`b\3\2\2\2"+
		"a\\\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2df\3\2\2\2ec\3\2\2\2fg\7\r\2"+
		"\2gh\b\7\1\2h\r\3\2\2\2ij\7&\2\2jk\7\n\2\2kl\5 \21\2lm\b\b\1\2m\17\3\2"+
		"\2\2no\7\36\2\2op\5\36\20\2pq\b\t\1\2qs\7\16\2\2rt\5\b\5\2sr\3\2\2\2t"+
		"u\3\2\2\2us\3\2\2\2uv\3\2\2\2vw\3\2\2\2w\u0082\7\17\2\2xy\b\t\1\2yz\7"+
		"\"\2\2z|\7\16\2\2{}\5\b\5\2|{\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2\2"+
		"\177\u0080\3\2\2\2\u0080\u0081\7\17\2\2\u0081\u0083\3\2\2\2\u0082x\3\2"+
		"\2\2\u0082\u0083\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\b\t\1\2\u0085"+
		"\21\3\2\2\2\u0086\u0087\7\37\2\2\u0087\u0088\b\n\1\2\u0088\u0089\5\36"+
		"\20\2\u0089\u008a\b\n\1\2\u008a\u008c\7\16\2\2\u008b\u008d\5\b\5\2\u008c"+
		"\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2"+
		"\2\2\u008f\u0090\3\2\2\2\u0090\u0091\7\17\2\2\u0091\u0092\b\n\1\2\u0092"+
		"\23\3\2\2\2\u0093\u0094\7 \2\2\u0094\u0095\b\13\1\2\u0095\25\3\2\2\2\u0096"+
		"\u0097\7!\2\2\u0097\u0098\b\f\1\2\u0098\27\3\2\2\2\u0099\u009a\7&\2\2"+
		"\u009a\u009b\7\n\2\2\u009b\u009c\7\20\2\2\u009c\u009d\7\21\2\2\u009d\u009e"+
		"\b\r\1\2\u009e\31\3\2\2\2\u009f\u00a0\7&\2\2\u00a0\u00a1\7\30\2\2\u00a1"+
		"\u00a2\7\31\2\2\u00a2\u00a3\b\16\1\2\u00a3\u00a4\7\f\2\2\u00a4\u00a5\5"+
		" \21\2\u00a5\u00a6\7\r\2\2\u00a6\u00a7\b\16\1\2\u00a7\33\3\2\2\2\u00a8"+
		"\u00a9\7&\2\2\u00a9\u00aa\b\17\1\2\u00aa\u00ab\7\20\2\2\u00ab\u00ac\5"+
		" \21\2\u00ac\u00ad\7\21\2\2\u00ad\u00ae\7\n\2\2\u00ae\u00af\5 \21\2\u00af"+
		"\u00b0\b\17\1\2\u00b0\35\3\2\2\2\u00b1\u00b2\5 \21\2\u00b2\u00b3\t\2\2"+
		"\2\u00b3\u00b4\5 \21\2\u00b4\u00b5\b\20\1\2\u00b5\37\3\2\2\2\u00b6\u00bd"+
		"\5\"\22\2\u00b7\u00b8\t\3\2\2\u00b8\u00b9\5\"\22\2\u00b9\u00ba\b\21\1"+
		"\2\u00ba\u00bc\3\2\2\2\u00bb\u00b7\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb"+
		"\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0"+
		"\u00c1\b\21\1\2\u00c1!\3\2\2\2\u00c2\u00c9\5$\23\2\u00c3\u00c4\t\4\2\2"+
		"\u00c4\u00c5\5$\23\2\u00c5\u00c6\b\22\1\2\u00c6\u00c8\3\2\2\2\u00c7\u00c3"+
		"\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca"+
		"\u00cc\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\b\22\1\2\u00cd#\3\2\2\2"+
		"\u00ce\u00cf\7$\2\2\u00cf\u00ed\b\23\1\2\u00d0\u00d1\7\f\2\2\u00d1\u00d2"+
		"\5 \21\2\u00d2\u00d3\7\r\2\2\u00d3\u00d4\b\23\1\2\u00d4\u00ed\3\2\2\2"+
		"\u00d5\u00d6\7&\2\2\u00d6\u00ed\b\23\1\2\u00d7\u00d8\7\34\2\2\u00d8\u00d9"+
		"\7\f\2\2\u00d9\u00da\7\r\2\2\u00da\u00ed\b\23\1\2\u00db\u00dc\7%\2\2\u00dc"+
		"\u00ed\b\23\1\2\u00dd\u00de\7\35\2\2\u00de\u00df\7\f\2\2\u00df\u00e0\7"+
		"\r\2\2\u00e0\u00ed\b\23\1\2\u00e1\u00e2\7&\2\2\u00e2\u00e3\b\23\1\2\u00e3"+
		"\u00e4\7\20\2\2\u00e4\u00e5\5 \21\2\u00e5\u00e6\7\21\2\2\u00e6\u00e7\b"+
		"\23\1\2\u00e7\u00ed\3\2\2\2\u00e8\u00e9\7&\2\2\u00e9\u00ea\7\30\2\2\u00ea"+
		"\u00eb\7\32\2\2\u00eb\u00ed\b\23\1\2\u00ec\u00ce\3\2\2\2\u00ec\u00d0\3"+
		"\2\2\2\u00ec\u00d5\3\2\2\2\u00ec\u00d7\3\2\2\2\u00ec\u00db\3\2\2\2\u00ec"+
		"\u00dd\3\2\2\2\u00ec\u00e1\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ed%\3\2\2\2"+
		"\16*8BPcu~\u0082\u008e\u00bd\u00c9\u00ec";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}