# Generated from Exp.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import sys

symbol_table = []
symbol_table_use = []
type_table = []
has_error = False

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

def error(line = 0, msg = "", fatal = False):

    global has_error
    has_error = True
    if line != 0: msg = "in line " + str(line) + " " + msg

    if not fatal:   print("ERROR: " + msg, file=sys.stderr)
    else: print("FATAL ERROR: inernal error", file=sys.stderr)


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%")
        buf.write("\u00d0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\3\3")
        buf.write("\3\6\3(\n\3\r\3\16\3)\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\5\4\67\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\7\5C\n\5\f\5\16\5F\13\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\6\7U\n\7\r\7\16\7V\3")
        buf.write("\7\3\7\3\7\3\7\3\7\6\7^\n\7\r\7\16\7_\3\7\3\7\5\7d\n\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\6\bn\n\b\r\b\16\bo\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\7\17\u009d\n\17\f\17\16\17\u00a0")
        buf.write("\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\7\20\u00a9\n")
        buf.write("\20\f\20\16\20\u00ac\13\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u00ce\n\21\3\21\2\2\22")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \2\5\3\2\22\27")
        buf.write("\4\2\5\5\7\7\4\2\6\6\b\t\2\u00d6\2\"\3\2\2\2\4%\3\2\2")
        buf.write("\2\6\66\3\2\2\2\b8\3\2\2\2\nJ\3\2\2\2\fO\3\2\2\2\16g\3")
        buf.write("\2\2\2\20t\3\2\2\2\22w\3\2\2\2\24z\3\2\2\2\26\u0080\3")
        buf.write("\2\2\2\30\u0089\3\2\2\2\32\u0092\3\2\2\2\34\u0097\3\2")
        buf.write("\2\2\36\u00a3\3\2\2\2 \u00cd\3\2\2\2\"#\b\2\1\2#$\5\4")
        buf.write("\3\2$\3\3\2\2\2%\'\b\3\1\2&(\5\6\4\2\'&\3\2\2\2()\3\2")
        buf.write("\2\2)\'\3\2\2\2)*\3\2\2\2*+\3\2\2\2+,\b\3\1\2,\5\3\2\2")
        buf.write("\2-\67\5\b\5\2.\67\5\f\7\2/\67\5\16\b\2\60\67\5\20\t\2")
        buf.write("\61\67\5\22\n\2\62\67\5\24\13\2\63\67\5\30\r\2\64\67\5")
        buf.write("\26\f\2\65\67\5\n\6\2\66-\3\2\2\2\66.\3\2\2\2\66/\3\2")
        buf.write("\2\2\66\60\3\2\2\2\66\61\3\2\2\2\66\62\3\2\2\2\66\63\3")
        buf.write("\2\2\2\66\64\3\2\2\2\66\65\3\2\2\2\67\7\3\2\2\289\7\33")
        buf.write("\2\29:\7\f\2\2:;\b\5\1\2;<\5\34\17\2<D\b\5\1\2=>\7\13")
        buf.write("\2\2>?\b\5\1\2?@\5\34\17\2@A\b\5\1\2AC\3\2\2\2B=\3\2\2")
        buf.write("\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2FD\3\2\2\2G")
        buf.write("H\7\r\2\2HI\b\5\1\2I\t\3\2\2\2JK\7%\2\2KL\7\n\2\2LM\5")
        buf.write("\34\17\2MN\b\6\1\2N\13\3\2\2\2OP\7\36\2\2PQ\5\32\16\2")
        buf.write("QR\b\7\1\2RT\7\16\2\2SU\5\6\4\2TS\3\2\2\2UV\3\2\2\2VT")
        buf.write("\3\2\2\2VW\3\2\2\2WX\3\2\2\2Xc\7\17\2\2YZ\b\7\1\2Z[\7")
        buf.write("\"\2\2[]\7\16\2\2\\^\5\6\4\2]\\\3\2\2\2^_\3\2\2\2_]\3")
        buf.write("\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7\17\2\2bd\3\2\2\2cY\3\2")
        buf.write("\2\2cd\3\2\2\2de\3\2\2\2ef\b\7\1\2f\r\3\2\2\2gh\7\37\2")
        buf.write("\2hi\b\b\1\2ij\5\32\16\2jk\b\b\1\2km\7\16\2\2ln\5\6\4")
        buf.write("\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2pq\3\2\2\2q")
        buf.write("r\7\17\2\2rs\b\b\1\2s\17\3\2\2\2tu\7 \2\2uv\b\t\1\2v\21")
        buf.write("\3\2\2\2wx\7!\2\2xy\b\n\1\2y\23\3\2\2\2z{\7%\2\2{|\7\n")
        buf.write("\2\2|}\7\20\2\2}~\7\21\2\2~\177\b\13\1\2\177\25\3\2\2")
        buf.write("\2\u0080\u0081\7%\2\2\u0081\u0082\7\30\2\2\u0082\u0083")
        buf.write("\7\31\2\2\u0083\u0084\b\f\1\2\u0084\u0085\7\f\2\2\u0085")
        buf.write("\u0086\5\34\17\2\u0086\u0087\7\r\2\2\u0087\u0088\b\f\1")
        buf.write("\2\u0088\27\3\2\2\2\u0089\u008a\7%\2\2\u008a\u008b\b\r")
        buf.write("\1\2\u008b\u008c\7\20\2\2\u008c\u008d\5\34\17\2\u008d")
        buf.write("\u008e\7\21\2\2\u008e\u008f\7\n\2\2\u008f\u0090\5\34\17")
        buf.write("\2\u0090\u0091\b\r\1\2\u0091\31\3\2\2\2\u0092\u0093\5")
        buf.write("\34\17\2\u0093\u0094\t\2\2\2\u0094\u0095\5\34\17\2\u0095")
        buf.write("\u0096\b\16\1\2\u0096\33\3\2\2\2\u0097\u009e\5\36\20\2")
        buf.write("\u0098\u0099\t\3\2\2\u0099\u009a\5\36\20\2\u009a\u009b")
        buf.write("\b\17\1\2\u009b\u009d\3\2\2\2\u009c\u0098\3\2\2\2\u009d")
        buf.write("\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a2\b")
        buf.write("\17\1\2\u00a2\35\3\2\2\2\u00a3\u00aa\5 \21\2\u00a4\u00a5")
        buf.write("\t\4\2\2\u00a5\u00a6\5 \21\2\u00a6\u00a7\b\20\1\2\u00a7")
        buf.write("\u00a9\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a9\u00ac\3\2\2\2")
        buf.write("\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ad\3")
        buf.write("\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\b\20\1\2\u00ae")
        buf.write("\37\3\2\2\2\u00af\u00b0\7#\2\2\u00b0\u00ce\b\21\1\2\u00b1")
        buf.write("\u00b2\7\f\2\2\u00b2\u00b3\5\34\17\2\u00b3\u00b4\7\r\2")
        buf.write("\2\u00b4\u00b5\b\21\1\2\u00b5\u00ce\3\2\2\2\u00b6\u00b7")
        buf.write("\7%\2\2\u00b7\u00ce\b\21\1\2\u00b8\u00b9\7\34\2\2\u00b9")
        buf.write("\u00ba\7\f\2\2\u00ba\u00bb\7\r\2\2\u00bb\u00ce\b\21\1")
        buf.write("\2\u00bc\u00bd\7$\2\2\u00bd\u00ce\b\21\1\2\u00be\u00bf")
        buf.write("\7\35\2\2\u00bf\u00c0\7\f\2\2\u00c0\u00c1\7\r\2\2\u00c1")
        buf.write("\u00ce\b\21\1\2\u00c2\u00c3\7%\2\2\u00c3\u00c4\b\21\1")
        buf.write("\2\u00c4\u00c5\7\20\2\2\u00c5\u00c6\5\34\17\2\u00c6\u00c7")
        buf.write("\7\21\2\2\u00c7\u00c8\b\21\1\2\u00c8\u00ce\3\2\2\2\u00c9")
        buf.write("\u00ca\7%\2\2\u00ca\u00cb\7\30\2\2\u00cb\u00cc\7\32\2")
        buf.write("\2\u00cc\u00ce\b\21\1\2\u00cd\u00af\3\2\2\2\u00cd\u00b1")
        buf.write("\3\2\2\2\u00cd\u00b6\3\2\2\2\u00cd\u00b8\3\2\2\2\u00cd")
        buf.write("\u00bc\3\2\2\2\u00cd\u00be\3\2\2\2\u00cd\u00c2\3\2\2\2")
        buf.write("\u00cd\u00c9\3\2\2\2\u00ce!\3\2\2\2\f)\66DV_co\u009e\u00aa")
        buf.write("\u00cd")
        return buf.getvalue()


class ExpParser ( Parser ):

    grammarFileName = "Exp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'*'", 
                     "'-'", "'/'", "'%'", "'='", "','", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'=='", "'!='", "'>'", "'>='", 
                     "'<'", "'<='", "'.'", "'push'", "'length'", "'print'", 
                     "'read_int'", "'read_str'", "'if'", "'while'", "'break'", 
                     "'continue'", "'else'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "SPACE", "PLUS", "TIMES", 
                      "MINUS", "OVER", "REM", "ATTRIB", "COMMA", "OP_PAR", 
                      "CL_PAR", "OP_CUR", "CL_CUR", "OP_SB", "CL_SB", "EQ", 
                      "NE", "GT", "GE", "LT", "LE", "DOT", "PUSH", "LENGTH", 
                      "PRINT", "READ_INT", "READ_STR", "IF", "WHILE", "BREAK", 
                      "CONTINUE", "ELSE", "NUMBER", "STRING", "NAME" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_st_attrib = 4
    RULE_st_if = 5
    RULE_st_while = 6
    RULE_st_break = 7
    RULE_st_continue = 8
    RULE_st_array_new = 9
    RULE_st_array_push = 10
    RULE_st_array_set = 11
    RULE_comparison = 12
    RULE_expression = 13
    RULE_term = 14
    RULE_factor = 15

    ruleNames =  [ "program", "main", "statement", "st_print", "st_attrib", 
                   "st_if", "st_while", "st_break", "st_continue", "st_array_new", 
                   "st_array_push", "st_array_set", "comparison", "expression", 
                   "term", "factor" ]

    EOF = Token.EOF
    COMMENT=1
    SPACE=2
    PLUS=3
    TIMES=4
    MINUS=5
    OVER=6
    REM=7
    ATTRIB=8
    COMMA=9
    OP_PAR=10
    CL_PAR=11
    OP_CUR=12
    CL_CUR=13
    OP_SB=14
    CL_SB=15
    EQ=16
    NE=17
    GT=18
    GE=19
    LT=20
    LE=21
    DOT=22
    PUSH=23
    LENGTH=24
    PRINT=25
    READ_INT=26
    READ_STR=27
    IF=28
    WHILE=29
    BREAK=30
    CONTINUE=31
    ELSE=32
    NUMBER=33
    STRING=34
    NAME=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(ExpParser.MainContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_program




    def program(self):

        localctx = ExpParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)

            print('.source Test.src')
            print('.class  public Test')
            print('.super  java/lang/Object\n')
            print('.method public <init>()V')
            print('    aload_0')
            print('    invokenonvirtual java/lang/Object/<init>()V')
            print('    return')
            print('.end method\n')
                
            self.state = 33
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExpParser.StatementContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_main




    def main(self):

        localctx = ExpParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)

            print('.method public static main([Ljava/lang/String;)V\n')
                
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.statement()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                    break



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
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def st_print(self):
            return self.getTypedRuleContext(ExpParser.St_printContext,0)


        def st_if(self):
            return self.getTypedRuleContext(ExpParser.St_ifContext,0)


        def st_while(self):
            return self.getTypedRuleContext(ExpParser.St_whileContext,0)


        def st_break(self):
            return self.getTypedRuleContext(ExpParser.St_breakContext,0)


        def st_continue(self):
            return self.getTypedRuleContext(ExpParser.St_continueContext,0)


        def st_array_new(self):
            return self.getTypedRuleContext(ExpParser.St_array_newContext,0)


        def st_array_set(self):
            return self.getTypedRuleContext(ExpParser.St_array_setContext,0)


        def st_array_push(self):
            return self.getTypedRuleContext(ExpParser.St_array_pushContext,0)


        def st_attrib(self):
            return self.getTypedRuleContext(ExpParser.St_attribContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_statement




    def statement(self):

        localctx = ExpParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.st_print()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.st_if()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.st_while()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.st_break()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.st_continue()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.st_array_new()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 49
                self.st_array_set()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 50
                self.st_array_push()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 51
                self.st_attrib()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

        def PRINT(self):
            return self.getToken(ExpParser.PRINT, 0)

        def OP_PAR(self):
            return self.getToken(ExpParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(ExpParser.CL_PAR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.COMMA)
            else:
                return self.getToken(ExpParser.COMMA, i)

        def getRuleIndex(self):
            return ExpParser.RULE_st_print




    def st_print(self):

        localctx = ExpParser.St_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_st_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ExpParser.PRINT)
            self.state = 55
            self.match(ExpParser.OP_PAR)

            emit('getstatic java/lang/System/out Ljava/io/PrintStream;', stack_att = +1)
                
            self.state = 57
            localctx.e1 = self.expression()

            if localctx.e1.type == 'i':
                emit('invokevirtual java/io/PrintStream/print(I)V\n', stack_att = -2)
            elif localctx.e1.type == 's':
                emit('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', stack_att = -2)
            elif localctx.e1.type == 'a':
                emit("invokevirtual Array/string()Ljava/lang/String;")
                emit("invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n", stack_att = -2)
            else:
                error(fatal = True)
                
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.COMMA:
                self.state = 59
                self.match(ExpParser.COMMA)

                emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    
                self.state = 61
                localctx.e2 = self.expression()

                if localctx.e2.type == 'i':
                    emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
                elif localctx.e2.type == 's':
                    emit('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
                elif localctx.e1.type == 'a':
                    emit("invokevirtual Array/string()Ljava/lang/String;")
                    emit("invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n", stack_att = -2)
                else:
                    error(fatal = True)
                    
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(ExpParser.CL_PAR)

            emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
            emit('invokevirtual java/io/PrintStream/println()V\n', -1)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_attribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token
            self._expression = None # ExpressionContext

        def NAME(self):
            return self.getToken(ExpParser.NAME, 0)

        def ATTRIB(self):
            return self.getToken(ExpParser.ATTRIB, 0)

        def expression(self):
            return self.getTypedRuleContext(ExpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_st_attrib




    def st_attrib(self):

        localctx = ExpParser.St_attribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 73
            self.match(ExpParser.ATTRIB)
            self.state = 74
            localctx._expression = self.expression()

            # 1. testar se a varialvel name já existe:  se não existir inclui (None if localctx._NAME is None else localctx._NAME.text) na symbol_table
            if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                symbol_table_use.append(0)
                type_table.append(localctx._expression.type)

            # 2. encontrar o índice de (None if localctx._NAME is None else localctx._NAME.text) e gerar o bytecode 'istore index'
            index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
            my_type = type_table[index]
            if my_type == localctx._expression.type:
                if my_type == 'i':
                    emit("istore "+ str(index) + '\n', -1)
                elif my_type == 's':
                    emit("astore "+ str(index) + '\n', -1)
                else:
                    error(fatal = True)
            else:
                if my_type == "i":
                    error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "'" + (None if localctx._NAME is None else localctx._NAME.text) + "' must be an " + "integer")
                elif my_type == "s":
                    error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "'" + (None if localctx._NAME is None else localctx._NAME.text) + "' must be an " + "string")
                elif my_type == "a":
                    error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "'" + (None if localctx._NAME is None else localctx._NAME.text) + "' must be an " + "array")
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExpParser.IF, 0)

        def comparison(self):
            return self.getTypedRuleContext(ExpParser.ComparisonContext,0)


        def OP_CUR(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.OP_CUR)
            else:
                return self.getToken(ExpParser.OP_CUR, i)

        def CL_CUR(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.CL_CUR)
            else:
                return self.getToken(ExpParser.CL_CUR, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExpParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(ExpParser.ELSE, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_st_if




    def st_if(self):

        localctx = ExpParser.St_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(ExpParser.IF)
            self.state = 78
            self.comparison()

            have_else = False
            global if_counter
            if_counter_local = if_counter
            not_if_local = "NOT_IF_" + str(if_counter_local)
            if_counter += 1
            emit(not_if_local, initLN='')
                
            self.state = 80
            self.match(ExpParser.OP_CUR)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.statement()
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                    break

            self.state = 86
            self.match(ExpParser.CL_CUR)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ExpParser.ELSE:

                have_else = True
                end_else = "END_ELSE_"+str(if_counter_local)
                emit("goto "+end_else)
                emit(not_if_local + ':\n' )
                    
                self.state = 88
                self.match(ExpParser.ELSE)
                self.state = 89
                self.match(ExpParser.OP_CUR)
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 90
                    self.statement()
                    self.state = 93 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                        break

                self.state = 95
                self.match(ExpParser.CL_CUR)



            if not have_else: emit(not_if_local + ':\n' )
            else            : emit(end_else + ':\n')
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ExpParser.WHILE, 0)

        def comparison(self):
            return self.getTypedRuleContext(ExpParser.ComparisonContext,0)


        def OP_CUR(self):
            return self.getToken(ExpParser.OP_CUR, 0)

        def CL_CUR(self):
            return self.getToken(ExpParser.CL_CUR, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExpParser.StatementContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_st_while




    def st_while(self):

        localctx = ExpParser.St_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_st_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(ExpParser.WHILE)

            global while_counter
            begin_while = "BEGIN_WHILE_" + str(while_counter)
            end_while = "END_WHILE_" + str(while_counter)
            emit(begin_while + ':')

            global current_begin_while
            current_begin_while.append(begin_while)

            global current_end_while
            current_end_while.append(end_while)

            while_counter += 1
                
            self.state = 103
            self.comparison()

            emit(end_while, initLN='')
                
            self.state = 105
            self.match(ExpParser.OP_CUR)
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.statement()
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                    break

            self.state = 111
            self.match(ExpParser.CL_CUR)

            emit("goto "+begin_while)
            emit(end_while+':\n')
            current_begin_while.pop()
            current_end_while.pop()
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._BREAK = None # Token

        def BREAK(self):
            return self.getToken(ExpParser.BREAK, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_st_break




    def st_break(self):

        localctx = ExpParser.St_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_st_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            localctx._BREAK = self.match(ExpParser.BREAK)

            global current_end_while
            if len(current_end_while) > 0:
                emit("goto " + current_end_while[-1] + " ;break")
            else:
                error(msg = "in line " + str((0 if localctx._BREAK is None else localctx._BREAK.line)) + "The 'break' command must be in a loop escope")
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_continueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CONTINUE = None # Token

        def CONTINUE(self):
            return self.getToken(ExpParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_st_continue




    def st_continue(self):

        localctx = ExpParser.St_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_st_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            localctx._CONTINUE = self.match(ExpParser.CONTINUE)

            global current_begin_while
            if len(current_begin_while) > 0:
                emit("goto " + current_begin_while[-1] + " ;continue")
            else:
                error(line = (0 if localctx._CONTINUE is None else localctx._CONTINUE.line), msg = "the 'continue' command must be in a loop escope")
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_array_newContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token

        def NAME(self):
            return self.getToken(ExpParser.NAME, 0)

        def ATTRIB(self):
            return self.getToken(ExpParser.ATTRIB, 0)

        def OP_SB(self):
            return self.getToken(ExpParser.OP_SB, 0)

        def CL_SB(self):
            return self.getToken(ExpParser.CL_SB, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_st_array_new




    def st_array_new(self):

        localctx = ExpParser.St_array_newContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_st_array_new)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 121
            self.match(ExpParser.ATTRIB)
            self.state = 122
            self.match(ExpParser.OP_SB)
            self.state = 123
            self.match(ExpParser.CL_SB)

            # 1. testar se a varialvel name já existe:  se não existir inclui (None if localctx._NAME is None else localctx._NAME.text) na symbol_table
            if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                symbol_table_use.append(0)
                type_table.append('a')
            else:
                error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "'" + (None if localctx._NAME is None else localctx._NAME.text) + "' is already declared")

            # 2. encontrar o índice de (None if localctx._NAME is None else localctx._NAME.text) e gerar o bytecode 'istore index'
            index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
            emit("new Array", stack_att=+1)
            emit("dup", stack_att=+1)
            emit("invokespecial Array/<init>()V", stack_att=-1)
            emit("astore "+str(index),endLN='\n\n', stack_att=-1)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_array_pushContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token

        def NAME(self):
            return self.getToken(ExpParser.NAME, 0)

        def DOT(self):
            return self.getToken(ExpParser.DOT, 0)

        def PUSH(self):
            return self.getToken(ExpParser.PUSH, 0)

        def OP_PAR(self):
            return self.getToken(ExpParser.OP_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(ExpParser.ExpressionContext,0)


        def CL_PAR(self):
            return self.getToken(ExpParser.CL_PAR, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_st_array_push




    def st_array_push(self):

        localctx = ExpParser.St_array_pushContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_st_array_push)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 127
            self.match(ExpParser.DOT)
            self.state = 128
            self.match(ExpParser.PUSH)

            index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))  
            emit("aload " + str(index), stack_att=+1)
                
            self.state = 130
            self.match(ExpParser.OP_PAR)
            self.state = 131
            self.expression()
            self.state = 132
            self.match(ExpParser.CL_PAR)

            #emit("ldc " + str(expression.text), stack_att=+1)
            emit("invokevirtual Array/push(I)V\n", stack_att=-2)

                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_array_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token
            self.ex1 = None # ExpressionContext
            self.ex2 = None # ExpressionContext

        def NAME(self):
            return self.getToken(ExpParser.NAME, 0)

        def OP_SB(self):
            return self.getToken(ExpParser.OP_SB, 0)

        def CL_SB(self):
            return self.getToken(ExpParser.CL_SB, 0)

        def ATTRIB(self):
            return self.getToken(ExpParser.ATTRIB, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_st_array_set




    def st_array_set(self):

        localctx = ExpParser.St_array_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_st_array_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            localctx._NAME = self.match(ExpParser.NAME)
             
            if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                emit("aload " + str(index), stack_att = +1)
            else:
                error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "'" + (None if localctx._NAME is None else localctx._NAME.text) + "' is not declared")
                
            self.state = 137
            self.match(ExpParser.OP_SB)
            self.state = 138
            localctx.ex1 = self.expression()
            self.state = 139
            self.match(ExpParser.CL_SB)
            self.state = 140
            self.match(ExpParser.ATTRIB)
            self.state = 141
            localctx.ex2 = self.expression()

            if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                my_type = type_table[index]
                if my_type == 'a':
                    if localctx.ex1.type == 'i':
                        if localctx.ex2.type == 'i':
                            emit("invokevirtual Array/set(II)V\n", stack_att = -3)
                        else:
                            error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "arrays can store only integers and '" + (None if localctx.ex2 is None else self._input.getText(localctx.ex2.start,localctx.ex2.stop)) + "' is an " + ('array' if localctx.ex2.type == 'a' else 'string') )
                    else:
                        error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "array index must be integer")
                else:
                    error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "only arrays can be indexable")
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.e1 = None # ExpressionContext
            self.op = None # Token
            self.e2 = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpressionContext,i)


        def EQ(self):
            return self.getToken(ExpParser.EQ, 0)

        def NE(self):
            return self.getToken(ExpParser.NE, 0)

        def GT(self):
            return self.getToken(ExpParser.GT, 0)

        def GE(self):
            return self.getToken(ExpParser.GE, 0)

        def LT(self):
            return self.getToken(ExpParser.LT, 0)

        def LE(self):
            return self.getToken(ExpParser.LE, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_comparison




    def comparison(self):

        localctx = ExpParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            localctx.e1 = self.expression()
            self.state = 145
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.EQ) | (1 << ExpParser.NE) | (1 << ExpParser.GT) | (1 << ExpParser.GE) | (1 << ExpParser.LT) | (1 << ExpParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 146
            localctx.e2 = self.expression()

            # usa a comparação inversa para o desvio

            if localctx.e1.type == 'i' and localctx.e2.type == 'i':
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.GT  : emit("if_icmple ", stack_att=-2, endLN='')
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.NE  : emit("if_icmpeq ", stack_att=-2, endLN='')
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.GE  : emit("if_icmplt ", stack_att=-2, endLN='')
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.LT  : emit("if_icmpge ", stack_att=-2, endLN='')
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.EQ  : emit("if_icmpne ", stack_att=-2, endLN='')
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.LE  : emit("if_icmpgt ", stack_att=-2, endLN='')
            else:
                error(line = (0 if localctx.op is None else localctx.op.line), msg = "cannot mix types")
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.t1 = None # TermContext
            self.op = None # Token
            self.t2 = None # TermContext

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.TermContext)
            else:
                return self.getTypedRuleContext(ExpParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.PLUS)
            else:
                return self.getToken(ExpParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.MINUS)
            else:
                return self.getToken(ExpParser.MINUS, i)

        def getRuleIndex(self):
            return ExpParser.RULE_expression




    def expression(self):

        localctx = ExpParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            localctx.t1 = self.term()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.PLUS or _la==ExpParser.MINUS:
                self.state = 150
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ExpParser.PLUS or _la==ExpParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 151
                localctx.t2 = self.term()

                if (0 if localctx.op is None else localctx.op.type) == ExpParser.PLUS  : emit('iadd', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.MINUS : emit('isub', -1)
                if localctx.t1.type != localctx.t2.type:
                    error(line = (0 if localctx.op is None else localctx.op.line), msg = "cannot mix types")
                elif localctx.t1.type != 'i' or localctx.t2.type != 'i':
                    error(line = (0 if localctx.op is None else localctx.op.line), msg = "math operations is only for integers" )
                    
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.type = localctx.t1.type
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.f1 = None # FactorContext
            self.op = None # Token
            self.f2 = None # FactorContext

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.FactorContext)
            else:
                return self.getTypedRuleContext(ExpParser.FactorContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.TIMES)
            else:
                return self.getToken(ExpParser.TIMES, i)

        def OVER(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.OVER)
            else:
                return self.getToken(ExpParser.OVER, i)

        def REM(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.REM)
            else:
                return self.getToken(ExpParser.REM, i)

        def getRuleIndex(self):
            return ExpParser.RULE_term




    def term(self):

        localctx = ExpParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            localctx.f1 = self.factor()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.TIMES) | (1 << ExpParser.OVER) | (1 << ExpParser.REM))) != 0):
                self.state = 162
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.TIMES) | (1 << ExpParser.OVER) | (1 << ExpParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                localctx.f2 = self.factor()

                if (0 if localctx.op is None else localctx.op.type) == ExpParser.TIMES : emit('imul', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.OVER  : emit('idiv', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.REM   : emit('irem', -1)
                if localctx.f1.type != localctx.f2.type:
                    error(msg = "in line " + str((0 if localctx.op is None else localctx.op.line)) + " cannot mix types")
                elif localctx.f1.type != 'i' or localctx.f2.type != 'i':
                    error(msg = "in line " + str((0 if localctx.op is None else localctx.op.line)) + " math operations is only for integers" )
                    
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.type = localctx.f1.type
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self._NUMBER = None # Token
            self.f1 = None # ExpressionContext
            self._expression = None # ExpressionContext
            self._NAME = None # Token
            self._STRING = None # Token

        def NUMBER(self):
            return self.getToken(ExpParser.NUMBER, 0)

        def OP_PAR(self):
            return self.getToken(ExpParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(ExpParser.CL_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(ExpParser.ExpressionContext,0)


        def NAME(self):
            return self.getToken(ExpParser.NAME, 0)

        def READ_INT(self):
            return self.getToken(ExpParser.READ_INT, 0)

        def STRING(self):
            return self.getToken(ExpParser.STRING, 0)

        def READ_STR(self):
            return self.getToken(ExpParser.READ_STR, 0)

        def OP_SB(self):
            return self.getToken(ExpParser.OP_SB, 0)

        def CL_SB(self):
            return self.getToken(ExpParser.CL_SB, 0)

        def DOT(self):
            return self.getToken(ExpParser.DOT, 0)

        def LENGTH(self):
            return self.getToken(ExpParser.LENGTH, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_factor




    def factor(self):

        localctx = ExpParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_factor)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                localctx._NUMBER = self.match(ExpParser.NUMBER)

                emit('ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text), +1)
                localctx.type = 'i'
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(ExpParser.OP_PAR)
                self.state = 176
                localctx.f1 = localctx._expression = self.expression()
                self.state = 177
                self.match(ExpParser.CL_PAR)

                localctx.type = localctx._expression.type
                    
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                localctx._NAME = self.match(ExpParser.NAME)

                # encontrar o index de (None if localctx._NAME is None else localctx._NAME.text) e gerar o bytecode 'iload index'
                if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                    error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "variable '" + (None if localctx._NAME is None else localctx._NAME.text) + "' is not declared")
                else:
                    index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                    symbol_table_use[index] += 1
                    my_type = type_table[index]
                    if my_type == 'i':
                        emit("iload "+ str(index), +1)
                        localctx.type = my_type
                    elif my_type == 's' or my_type == 'a':
                        emit("aload "+ str(index), +1)
                        localctx.type = my_type
                    else:
                        error(fatal = True)
                    
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                self.match(ExpParser.READ_INT)
                self.state = 183
                self.match(ExpParser.OP_PAR)
                self.state = 184
                self.match(ExpParser.CL_PAR)

                emit("invokestatic Runtime/readInt()I", +1)
                localctx.type = 'i'
                    
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 186
                localctx._STRING = self.match(ExpParser.STRING)

                emit('ldc '+ (None if localctx._STRING is None else localctx._STRING.text), +1)
                localctx.type = 's'
                    
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 188
                self.match(ExpParser.READ_STR)
                self.state = 189
                self.match(ExpParser.OP_PAR)
                self.state = 190
                self.match(ExpParser.CL_PAR)

                emit("invokestatic Runtime/readString()Ljava/lang/String;", +1)
                localctx.type = 's'
                    
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 192
                localctx._NAME = self.match(ExpParser.NAME)

                if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                    index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                    my_type = type_table[index]
                    if my_type == 'a':
                        emit("aload " + str(index), stack_att = +1)
                    else:
                        error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = " only arrays can be indexable")
                else:
                    error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = " '" + (None if localctx._NAME is None else localctx._NAME.text) + "' is not declared" )
                    
                self.state = 194
                self.match(ExpParser.OP_SB)
                self.state = 195
                self.expression()
                self.state = 196
                self.match(ExpParser.CL_SB)

                emit("invokevirtual Array/get(I)I", stack_att = -1)
                localctx.type = 'i'
                    
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 199
                localctx._NAME = self.match(ExpParser.NAME)
                self.state = 200
                self.match(ExpParser.DOT)
                self.state = 201
                self.match(ExpParser.LENGTH)

                if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                    index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                    my_type = type_table[index]
                    if my_type == 'a':
                        emit("aload " + str(index), +1)
                        emit("invokevirtual Array/length()I"    )
                        localctx.type = 'i'
                    else :
                        error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "'" + (None if localctx._NAME is None else localctx._NAME.text) + "' is not an array")
                else:
                    error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = " '" + (None if localctx._NAME is None else localctx._NAME.text) + "' is not declared" )
                localctx.type = 'i'
                    
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





