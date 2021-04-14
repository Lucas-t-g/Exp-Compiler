// Generated from /home/lucas_t_g/Documentos/E-Comp/Matérias/Compiladores/Exp-Compiler/Exp.g4 by ANTLR 4.8

import sys

symbol_table = []
symbol_table_use = []

stack_cur = 0
stack_max = 0
if_counter = 0
while_counter = 0
current_begin_while = []
current_end_while = []

def emit(comand, stack_att=0, initLN="    ", endLN='\n'):
    global stack_cur, stack_max
    stack_cur += stack_att
    if stack_cur > stack_max:
        stack_max = stack_cur
    print(initLN + comand, end=endLN)


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
		COMMENT=1, SPACE=2, PLUS=3, TIMES=4, MINUS=5, OVER=6, REM=7, OP_PAR=8, 
		CL_PAR=9, ATTRIB=10, COMMA=11, OP_CUR=12, CL_CUR=13, EQ=14, NE=15, GT=16, 
		GE=17, LT=18, LE=19, PRINT=20, READ_INT=21, IF=22, WHILE=23, BREAK=24, 
		CONTINUE=25, NUMBER=26, NAME=27;
	public static final int
		RULE_program = 0, RULE_main = 1, RULE_statement = 2, RULE_st_print = 3, 
		RULE_st_attrib = 4, RULE_st_if = 5, RULE_st_while = 6, RULE_st_break = 7, 
		RULE_st_continue = 8, RULE_comparison = 9, RULE_expression = 10, RULE_term = 11, 
		RULE_factor = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main", "statement", "st_print", "st_attrib", "st_if", "st_while", 
			"st_break", "st_continue", "comparison", "expression", "term", "factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'+'", "'*'", "'-'", "'/'", "'%'", "'('", "')'", "'='", 
			"','", "'{'", "'}'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'print'", 
			"'read_int'", "'if'", "'while'", "'break'", "'continue'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COMMENT", "SPACE", "PLUS", "TIMES", "MINUS", "OVER", "REM", "OP_PAR", 
			"CL_PAR", "ATTRIB", "COMMA", "OP_CUR", "CL_CUR", "EQ", "NE", "GT", "GE", 
			"LT", "LE", "PRINT", "READ_INT", "IF", "WHILE", "BREAK", "CONTINUE", 
			"NUMBER", "NAME"
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
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
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
			    
			setState(27);
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
		enterRule(_localctx, 2, RULE_main);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{

			print('.method public static main([Ljava/lang/String;)V\n')
			symbol_table.append('args')
			symbol_table_use.append(1)
			    
			setState(31); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(30);
				statement();
				}
				}
				setState(33); 
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
			            print("error: variable '" + symbol + "' is defined but never used", file=sys.stderr)

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
		public St_attribContext st_attrib() {
			return getRuleContext(St_attribContext.class,0);
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
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		try {
			setState(43);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
				enterOuterAlt(_localctx, 1);
				{
				setState(37);
				st_print();
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(38);
				st_attrib();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 3);
				{
				setState(39);
				st_if();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 4);
				{
				setState(40);
				st_while();
				}
				break;
			case BREAK:
				enterOuterAlt(_localctx, 5);
				{
				setState(41);
				st_break();
				}
				break;
			case CONTINUE:
				enterOuterAlt(_localctx, 6);
				{
				setState(42);
				st_continue();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
		public TerminalNode PRINT() { return getToken(ExpParser.PRINT, 0); }
		public TerminalNode OP_PAR() { return getToken(ExpParser.OP_PAR, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode CL_PAR() { return getToken(ExpParser.CL_PAR, 0); }
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
		enterRule(_localctx, 6, RULE_st_print);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(PRINT);
			setState(46);
			match(OP_PAR);

			emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
			    
			setState(48);
			expression();

			emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
			    
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(50);
				match(COMMA);

				emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
				    
				setState(52);
				expression();

				emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
				    
				}
				}
				setState(59);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(60);
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
		enterRule(_localctx, 8, RULE_st_attrib);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			((St_attribContext)_localctx).NAME = match(NAME);
			setState(64);
			match(ATTRIB);
			setState(65);
			expression();

			# 1. testar se a varialvel name já existe:  se não existir inclui (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) na symbol_table
			if (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) not in symbol_table:
			    symbol_table.append((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null))
			    symbol_table_use.append(0)

			# 2. encontrar o índice de (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) e gerar o bytecode 'istore index'
			index = symbol_table.index((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null))
			emit("istore "+ str(index) + '\n', -1)
			    
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
		public TerminalNode OP_CUR() { return getToken(ExpParser.OP_CUR, 0); }
		public TerminalNode CL_CUR() { return getToken(ExpParser.CL_CUR, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public St_ifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_if; }
	}

	public final St_ifContext st_if() throws RecognitionException {
		St_ifContext _localctx = new St_ifContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_st_if);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(IF);
			setState(69);
			comparison();

			global if_counter
			if_counter_local = if_counter
			if_counter += 1
			emit("NOT_IF_" + str(if_counter_local), initLN='')
			    
			setState(71);
			match(OP_CUR);
			setState(73); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(72);
				statement();
				}
				}
				setState(75); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << IF) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << NAME))) != 0) );
			setState(77);
			match(CL_CUR);

			emit("NOT_IF_" + str(if_counter_local)  + ':\n' )
			    
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
		enterRule(_localctx, 12, RULE_st_while);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
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
			    
			setState(82);
			comparison();

			emit(end_while, initLN='')
			    
			setState(84);
			match(OP_CUR);
			setState(86); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(85);
				statement();
				}
				}
				setState(88); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << IF) | (1L << WHILE) | (1L << BREAK) | (1L << CONTINUE) | (1L << NAME))) != 0) );
			setState(90);
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
		public TerminalNode BREAK() { return getToken(ExpParser.BREAK, 0); }
		public St_breakContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_break; }
	}

	public final St_breakContext st_break() throws RecognitionException {
		St_breakContext _localctx = new St_breakContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_st_break);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(BREAK);

			global current_end_while
			if len(current_end_while) > 0:
			    emit("goto " + current_end_while[-1] + " ;break")
			else:
			    print("error: The 'break' command must be in a loop escope", file=sys.stderr)
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

	public static class St_continueContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(ExpParser.CONTINUE, 0); }
		public St_continueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_continue; }
	}

	public final St_continueContext st_continue() throws RecognitionException {
		St_continueContext _localctx = new St_continueContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_st_continue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(CONTINUE);

			global current_begin_while
			if len(current_begin_while) > 0:
			    emit("goto " + current_begin_while[-1] + " ;continue")
			else:
			    print("error: The 'continue' command must be in a loop escope", file=sys.stderr)
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

	public static class ComparisonContext extends ParserRuleContext {
		public Token op;
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
		enterRule(_localctx, 18, RULE_comparison);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			expression();
			setState(100);
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
			setState(101);
			expression();

			# usa a comparação inversa para o desvio
			if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.GT  : emit("if_icmple ", stack_att=-2, endLN='')
			if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.NE  : emit("if_icmpeq ", stack_att=-2, endLN='')
			if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.GE  : emit("if_icmplt ", stack_att=-2, endLN='')
			if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.LT  : emit("if_icmpge ", stack_att=-2, endLN='')
			if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.EQ  : emit("if_icmpne ", stack_att=-2, endLN='')
			if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == ExpParser.LE  : emit("if_icmpgt ", stack_att=-2, endLN='')
			    
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
		public Token op;
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
		enterRule(_localctx, 20, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			term();
			setState(111);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(105);
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
				setState(106);
				term();

				if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == ExpParser.PLUS  : emit('iadd', -1)
				if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == ExpParser.MINUS : emit('isub', -1)
				    
				}
				}
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	public static class TermContext extends ParserRuleContext {
		public Token op;
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
		enterRule(_localctx, 22, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			factor();
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) {
				{
				{
				setState(115);
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
				setState(116);
				factor();

				if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == ExpParser.TIMES : emit('imul', -1)
				if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == ExpParser.OVER  : emit('idiv', -1)
				if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == ExpParser.REM   : emit('irem', -1)
				    
				}
				}
				setState(123);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	public static class FactorContext extends ParserRuleContext {
		public Token NUMBER;
		public Token NAME;
		public TerminalNode NUMBER() { return getToken(ExpParser.NUMBER, 0); }
		public TerminalNode OP_PAR() { return getToken(ExpParser.OP_PAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode CL_PAR() { return getToken(ExpParser.CL_PAR, 0); }
		public TerminalNode NAME() { return getToken(ExpParser.NAME, 0); }
		public TerminalNode READ_INT() { return getToken(ExpParser.READ_INT, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_factor);
		try {
			setState(136);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(124);
				((FactorContext)_localctx).NUMBER = match(NUMBER);

				emit('ldc ' + (((FactorContext)_localctx).NUMBER!=null?((FactorContext)_localctx).NUMBER.getText():null), +1)
				    
				}
				break;
			case OP_PAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(126);
				match(OP_PAR);
				setState(127);
				expression();
				setState(128);
				match(CL_PAR);
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 3);
				{
				setState(130);
				((FactorContext)_localctx).NAME = match(NAME);

				# encontrar o index de (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) e gerar o bytecode 'iload index'
				if (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) not in symbol_table:
				    # print("fatal error", file=sys.stderr)
				    print("error: variable '"+ (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null)+"' is not declared", file=sys.stderr)
				    sys.exit(1)
				else:
				    index = symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))
				    symbol_table_use[index] += 1
				    emit("iload "+ str(index), +1)
				    
				}
				break;
			case READ_INT:
				enterOuterAlt(_localctx, 4);
				{
				setState(132);
				match(READ_INT);
				setState(133);
				match(OP_PAR);
				setState(134);
				match(CL_PAR);

				emit("invokestatic Runtime/readInt()I", +1)
				    
				}
				break;
			default:
				throw new NoViableAltException(this);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35\u008d\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\3\2\3\2\3\2\3\3\3\3\6\3\"\n\3\r\3\16\3"+
		"#\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4.\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\7\5:\n\5\f\5\16\5=\13\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3"+
		"\7\3\7\3\7\3\7\3\7\6\7L\n\7\r\7\16\7M\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\6\bY\n\b\r\b\16\bZ\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13"+
		"\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\7\fp\n\f\f\f\16\fs\13\f\3\r\3\r\3"+
		"\r\3\r\3\r\7\rz\n\r\f\r\16\r}\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\5\16\u008b\n\16\3\16\2\2\17\2\4\6\b\n\f\16\20"+
		"\22\24\26\30\32\2\5\3\2\20\25\4\2\5\5\7\7\4\2\6\6\b\t\2\u008d\2\34\3\2"+
		"\2\2\4\37\3\2\2\2\6-\3\2\2\2\b/\3\2\2\2\nA\3\2\2\2\fF\3\2\2\2\16R\3\2"+
		"\2\2\20_\3\2\2\2\22b\3\2\2\2\24e\3\2\2\2\26j\3\2\2\2\30t\3\2\2\2\32\u008a"+
		"\3\2\2\2\34\35\b\2\1\2\35\36\5\4\3\2\36\3\3\2\2\2\37!\b\3\1\2 \"\5\6\4"+
		"\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\b\3\1\2&\5\3\2"+
		"\2\2\'.\5\b\5\2(.\5\n\6\2).\5\f\7\2*.\5\16\b\2+.\5\20\t\2,.\5\22\n\2-"+
		"\'\3\2\2\2-(\3\2\2\2-)\3\2\2\2-*\3\2\2\2-+\3\2\2\2-,\3\2\2\2.\7\3\2\2"+
		"\2/\60\7\26\2\2\60\61\7\n\2\2\61\62\b\5\1\2\62\63\5\26\f\2\63;\b\5\1\2"+
		"\64\65\7\r\2\2\65\66\b\5\1\2\66\67\5\26\f\2\678\b\5\1\28:\3\2\2\29\64"+
		"\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3\2\2\2>?\7\13\2\2"+
		"?@\b\5\1\2@\t\3\2\2\2AB\7\35\2\2BC\7\f\2\2CD\5\26\f\2DE\b\6\1\2E\13\3"+
		"\2\2\2FG\7\30\2\2GH\5\24\13\2HI\b\7\1\2IK\7\16\2\2JL\5\6\4\2KJ\3\2\2\2"+
		"LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7\17\2\2PQ\b\7\1\2Q\r\3\2\2"+
		"\2RS\7\31\2\2ST\b\b\1\2TU\5\24\13\2UV\b\b\1\2VX\7\16\2\2WY\5\6\4\2XW\3"+
		"\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\7\17\2\2]^\b\b\1\2"+
		"^\17\3\2\2\2_`\7\32\2\2`a\b\t\1\2a\21\3\2\2\2bc\7\33\2\2cd\b\n\1\2d\23"+
		"\3\2\2\2ef\5\26\f\2fg\t\2\2\2gh\5\26\f\2hi\b\13\1\2i\25\3\2\2\2jq\5\30"+
		"\r\2kl\t\3\2\2lm\5\30\r\2mn\b\f\1\2np\3\2\2\2ok\3\2\2\2ps\3\2\2\2qo\3"+
		"\2\2\2qr\3\2\2\2r\27\3\2\2\2sq\3\2\2\2t{\5\32\16\2uv\t\4\2\2vw\5\32\16"+
		"\2wx\b\r\1\2xz\3\2\2\2yu\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\31\3\2"+
		"\2\2}{\3\2\2\2~\177\7\34\2\2\177\u008b\b\16\1\2\u0080\u0081\7\n\2\2\u0081"+
		"\u0082\5\26\f\2\u0082\u0083\7\13\2\2\u0083\u008b\3\2\2\2\u0084\u0085\7"+
		"\35\2\2\u0085\u008b\b\16\1\2\u0086\u0087\7\27\2\2\u0087\u0088\7\n\2\2"+
		"\u0088\u0089\7\13\2\2\u0089\u008b\b\16\1\2\u008a~\3\2\2\2\u008a\u0080"+
		"\3\2\2\2\u008a\u0084\3\2\2\2\u008a\u0086\3\2\2\2\u008b\33\3\2\2\2\n#-"+
		";MZq{\u008a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}