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
func_table = []
func_num_args = []

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


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3&")
        buf.write("\u0112\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\7\2-\n\2\f\2\16\2\60\13\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\38\n\3\3\3\3\3\3\3\3\3\7\3")
        buf.write(">\n\3\f\3\16\3A\13\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\7")
        buf.write("\4K\n\4\f\4\16\4N\13\4\3\5\3\5\6\5R\n\5\r\5\16\5S\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6b\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\5\7i\n\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\7\bt\n\b\f\b\16\bw\13\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u0085\n\t\f\t\16\t")
        buf.write("\u0088\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\6\13\u0097\n\13\r\13\16\13\u0098\3\13")
        buf.write("\3\13\3\13\3\13\3\13\6\13\u00a0\n\13\r\13\16\13\u00a1")
        buf.write("\3\13\3\13\5\13\u00a6\n\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\6\f\u00b0\n\f\r\f\16\f\u00b1\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\7\23\u00df\n\23\f\23\16")
        buf.write("\23\u00e2\13\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\7\24")
        buf.write("\u00eb\n\24\f\24\16\24\u00ee\13\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0110\n\25\3\25\2")
        buf.write("\2\26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(\2\5")
        buf.write("\3\2\22\27\4\2\5\5\7\7\4\2\6\6\b\t\2\u011b\2*\3\2\2\2")
        buf.write("\4\63\3\2\2\2\6E\3\2\2\2\bO\3\2\2\2\na\3\2\2\2\fc\3\2")
        buf.write("\2\2\16m\3\2\2\2\20z\3\2\2\2\22\u008c\3\2\2\2\24\u0091")
        buf.write("\3\2\2\2\26\u00a9\3\2\2\2\30\u00b6\3\2\2\2\32\u00b9\3")
        buf.write("\2\2\2\34\u00bc\3\2\2\2\36\u00c2\3\2\2\2 \u00cb\3\2\2")
        buf.write("\2\"\u00d4\3\2\2\2$\u00d9\3\2\2\2&\u00e5\3\2\2\2(\u010f")
        buf.write("\3\2\2\2*.\b\2\1\2+-\5\4\3\2,+\3\2\2\2-\60\3\2\2\2.,\3")
        buf.write("\2\2\2./\3\2\2\2/\61\3\2\2\2\60.\3\2\2\2\61\62\5\b\5\2")
        buf.write("\62\3\3\2\2\2\63\64\7#\2\2\64\65\7&\2\2\65\67\7\f\2\2")
        buf.write("\668\5\6\4\2\67\66\3\2\2\2\678\3\2\2\289\3\2\2\29:\7\r")
        buf.write("\2\2:;\b\3\1\2;?\7\16\2\2<>\5\n\6\2=<\3\2\2\2>A\3\2\2")
        buf.write("\2?=\3\2\2\2?@\3\2\2\2@B\3\2\2\2A?\3\2\2\2BC\7\17\2\2")
        buf.write("CD\b\3\1\2D\5\3\2\2\2EF\7&\2\2FL\b\4\1\2GH\7\13\2\2HI")
        buf.write("\7&\2\2IK\b\4\1\2JG\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2")
        buf.write("\2\2M\7\3\2\2\2NL\3\2\2\2OQ\b\5\1\2PR\5\n\6\2QP\3\2\2")
        buf.write("\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\b\5\1\2V")
        buf.write("\t\3\2\2\2Wb\5\20\t\2Xb\5\24\13\2Yb\5\26\f\2Zb\5\30\r")
        buf.write("\2[b\5\32\16\2\\b\5\34\17\2]b\5 \21\2^b\5\36\20\2_b\5")
        buf.write("\22\n\2`b\5\f\7\2aW\3\2\2\2aX\3\2\2\2aY\3\2\2\2aZ\3\2")
        buf.write("\2\2a[\3\2\2\2a\\\3\2\2\2a]\3\2\2\2a^\3\2\2\2a_\3\2\2")
        buf.write("\2a`\3\2\2\2b\13\3\2\2\2cd\7&\2\2dh\7\f\2\2ef\5\16\b\2")
        buf.write("fg\b\7\1\2gi\3\2\2\2he\3\2\2\2hi\3\2\2\2ij\3\2\2\2jk\7")
        buf.write("\r\2\2kl\b\7\1\2l\r\3\2\2\2mn\5$\23\2nu\b\b\1\2op\7\13")
        buf.write("\2\2pq\5$\23\2qr\b\b\1\2rt\3\2\2\2so\3\2\2\2tw\3\2\2\2")
        buf.write("us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wu\3\2\2\2xy\b\b\1\2y\17")
        buf.write("\3\2\2\2z{\7\33\2\2{|\7\f\2\2|}\b\t\1\2}~\5$\23\2~\u0086")
        buf.write("\b\t\1\2\177\u0080\7\13\2\2\u0080\u0081\b\t\1\2\u0081")
        buf.write("\u0082\5$\23\2\u0082\u0083\b\t\1\2\u0083\u0085\3\2\2\2")
        buf.write("\u0084\177\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2")
        buf.write("\2\2\u0086\u0087\3\2\2\2\u0087\u0089\3\2\2\2\u0088\u0086")
        buf.write("\3\2\2\2\u0089\u008a\7\r\2\2\u008a\u008b\b\t\1\2\u008b")
        buf.write("\21\3\2\2\2\u008c\u008d\7&\2\2\u008d\u008e\7\n\2\2\u008e")
        buf.write("\u008f\5$\23\2\u008f\u0090\b\n\1\2\u0090\23\3\2\2\2\u0091")
        buf.write("\u0092\7\36\2\2\u0092\u0093\5\"\22\2\u0093\u0094\b\13")
        buf.write("\1\2\u0094\u0096\7\16\2\2\u0095\u0097\5\n\6\2\u0096\u0095")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u00a5\7\17\2")
        buf.write("\2\u009b\u009c\b\13\1\2\u009c\u009d\7\"\2\2\u009d\u009f")
        buf.write("\7\16\2\2\u009e\u00a0\5\n\6\2\u009f\u009e\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\u00a3\3\2\2\2\u00a3\u00a4\7\17\2\2\u00a4\u00a6")
        buf.write("\3\2\2\2\u00a5\u009b\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a7\u00a8\b\13\1\2\u00a8\25\3\2\2\2\u00a9")
        buf.write("\u00aa\7\37\2\2\u00aa\u00ab\b\f\1\2\u00ab\u00ac\5\"\22")
        buf.write("\2\u00ac\u00ad\b\f\1\2\u00ad\u00af\7\16\2\2\u00ae\u00b0")
        buf.write("\5\n\6\2\u00af\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00b4\7\17\2\2\u00b4\u00b5\b\f\1\2\u00b5\27\3\2")
        buf.write("\2\2\u00b6\u00b7\7 \2\2\u00b7\u00b8\b\r\1\2\u00b8\31\3")
        buf.write("\2\2\2\u00b9\u00ba\7!\2\2\u00ba\u00bb\b\16\1\2\u00bb\33")
        buf.write("\3\2\2\2\u00bc\u00bd\7&\2\2\u00bd\u00be\7\n\2\2\u00be")
        buf.write("\u00bf\7\20\2\2\u00bf\u00c0\7\21\2\2\u00c0\u00c1\b\17")
        buf.write("\1\2\u00c1\35\3\2\2\2\u00c2\u00c3\7&\2\2\u00c3\u00c4\7")
        buf.write("\30\2\2\u00c4\u00c5\7\31\2\2\u00c5\u00c6\b\20\1\2\u00c6")
        buf.write("\u00c7\7\f\2\2\u00c7\u00c8\5$\23\2\u00c8\u00c9\7\r\2\2")
        buf.write("\u00c9\u00ca\b\20\1\2\u00ca\37\3\2\2\2\u00cb\u00cc\7&")
        buf.write("\2\2\u00cc\u00cd\b\21\1\2\u00cd\u00ce\7\20\2\2\u00ce\u00cf")
        buf.write("\5$\23\2\u00cf\u00d0\7\21\2\2\u00d0\u00d1\7\n\2\2\u00d1")
        buf.write("\u00d2\5$\23\2\u00d2\u00d3\b\21\1\2\u00d3!\3\2\2\2\u00d4")
        buf.write("\u00d5\5$\23\2\u00d5\u00d6\t\2\2\2\u00d6\u00d7\5$\23\2")
        buf.write("\u00d7\u00d8\b\22\1\2\u00d8#\3\2\2\2\u00d9\u00e0\5&\24")
        buf.write("\2\u00da\u00db\t\3\2\2\u00db\u00dc\5&\24\2\u00dc\u00dd")
        buf.write("\b\23\1\2\u00dd\u00df\3\2\2\2\u00de\u00da\3\2\2\2\u00df")
        buf.write("\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e3\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\b")
        buf.write("\23\1\2\u00e4%\3\2\2\2\u00e5\u00ec\5(\25\2\u00e6\u00e7")
        buf.write("\t\4\2\2\u00e7\u00e8\5(\25\2\u00e8\u00e9\b\24\1\2\u00e9")
        buf.write("\u00eb\3\2\2\2\u00ea\u00e6\3\2\2\2\u00eb\u00ee\3\2\2\2")
        buf.write("\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ef\3")
        buf.write("\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\b\24\1\2\u00f0")
        buf.write("\'\3\2\2\2\u00f1\u00f2\7$\2\2\u00f2\u0110\b\25\1\2\u00f3")
        buf.write("\u00f4\7\f\2\2\u00f4\u00f5\5$\23\2\u00f5\u00f6\7\r\2\2")
        buf.write("\u00f6\u00f7\b\25\1\2\u00f7\u0110\3\2\2\2\u00f8\u00f9")
        buf.write("\7&\2\2\u00f9\u0110\b\25\1\2\u00fa\u00fb\7\34\2\2\u00fb")
        buf.write("\u00fc\7\f\2\2\u00fc\u00fd\7\r\2\2\u00fd\u0110\b\25\1")
        buf.write("\2\u00fe\u00ff\7%\2\2\u00ff\u0110\b\25\1\2\u0100\u0101")
        buf.write("\7\35\2\2\u0101\u0102\7\f\2\2\u0102\u0103\7\r\2\2\u0103")
        buf.write("\u0110\b\25\1\2\u0104\u0105\7&\2\2\u0105\u0106\b\25\1")
        buf.write("\2\u0106\u0107\7\20\2\2\u0107\u0108\5$\23\2\u0108\u0109")
        buf.write("\7\21\2\2\u0109\u010a\b\25\1\2\u010a\u0110\3\2\2\2\u010b")
        buf.write("\u010c\7&\2\2\u010c\u010d\7\30\2\2\u010d\u010e\7\32\2")
        buf.write("\2\u010e\u0110\b\25\1\2\u010f\u00f1\3\2\2\2\u010f\u00f3")
        buf.write("\3\2\2\2\u010f\u00f8\3\2\2\2\u010f\u00fa\3\2\2\2\u010f")
        buf.write("\u00fe\3\2\2\2\u010f\u0100\3\2\2\2\u010f\u0104\3\2\2\2")
        buf.write("\u010f\u010b\3\2\2\2\u0110)\3\2\2\2\22.\67?LSahu\u0086")
        buf.write("\u0098\u00a1\u00a5\u00b1\u00e0\u00ec\u010f")
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
                     "'continue'", "'else'", "'def'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "SPACE", "PLUS", "TIMES", 
                      "MINUS", "OVER", "REM", "ATTRIB", "COMMA", "OP_PAR", 
                      "CL_PAR", "OP_CUR", "CL_CUR", "OP_SB", "CL_SB", "EQ", 
                      "NE", "GT", "GE", "LT", "LE", "DOT", "PUSH", "LENGTH", 
                      "PRINT", "READ_INT", "READ_STR", "IF", "WHILE", "BREAK", 
                      "CONTINUE", "ELSE", "DEF", "NUMBER", "STRING", "NAME" ]

    RULE_program = 0
    RULE_function = 1
    RULE_parameters = 2
    RULE_main = 3
    RULE_statement = 4
    RULE_st_call = 5
    RULE_arguments = 6
    RULE_st_print = 7
    RULE_st_attrib = 8
    RULE_st_if = 9
    RULE_st_while = 10
    RULE_st_break = 11
    RULE_st_continue = 12
    RULE_st_array_new = 13
    RULE_st_array_push = 14
    RULE_st_array_set = 15
    RULE_comparison = 16
    RULE_expression = 17
    RULE_term = 18
    RULE_factor = 19

    ruleNames =  [ "program", "function", "parameters", "main", "statement", 
                   "st_call", "arguments", "st_print", "st_attrib", "st_if", 
                   "st_while", "st_break", "st_continue", "st_array_new", 
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
    DEF=33
    NUMBER=34
    STRING=35
    NAME=36

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


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.FunctionContext)
            else:
                return self.getTypedRuleContext(ExpParser.FunctionContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_program




    def program(self):

        localctx = ExpParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
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
                
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.DEF:
                self.state = 41
                self.function()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token

        def DEF(self):
            return self.getToken(ExpParser.DEF, 0)

        def NAME(self):
            return self.getToken(ExpParser.NAME, 0)

        def OP_PAR(self):
            return self.getToken(ExpParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(ExpParser.CL_PAR, 0)

        def OP_CUR(self):
            return self.getToken(ExpParser.OP_CUR, 0)

        def CL_CUR(self):
            return self.getToken(ExpParser.CL_CUR, 0)

        def parameters(self):
            return self.getTypedRuleContext(ExpParser.ParametersContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExpParser.StatementContext,i)


        def getRuleIndex(self):
            return ExpParser.RULE_function




    def function(self):

        localctx = ExpParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(ExpParser.DEF)
            self.state = 50
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 51
            self.match(ExpParser.OP_PAR)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ExpParser.NAME:
                self.state = 52
                self.parameters()


            self.state = 55
            self.match(ExpParser.CL_PAR)

            global tab_count, symbol_table, type_table, symbol_table_use, func_table, func_num_args
            if (None if localctx._NAME is None else localctx._NAME.text) not in func_table:
                tab_count = 0
                func_table.append((None if localctx._NAME is None else localctx._NAME.text))
                num_args = len(symbol_table)
                func_num_args.append(num_args)
                emit(".method public static {}({})V".format((None if localctx._NAME is None else localctx._NAME.text), "I"*num_args))
                tab_count = 1
                #for i in range(len(symbol_table)):
                #    emit("istore "+ str(i) + '\n', -1)
            else:
                error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "function '{}' is already declared".format((None if localctx._NAME is None else localctx._NAME.text)) )
                
            self.state = 57
            self.match(ExpParser.OP_CUR)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0):
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(ExpParser.CL_CUR)

            emit('return')
            tab_count = 0
            if len(symbol_table) > 0 : emit('.limit locals '+ str(len(symbol_table)) )
            emit('.limit stack '+ str(stack_max))
            emit('.end method')
            emit('; symbol_table: '+ str(symbol_table))
            symbol_table = []
            symbol_table_use = []
            type_table = []
            emit("")
            tab_count = 1
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.NAME)
            else:
                return self.getToken(ExpParser.NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExpParser.COMMA)
            else:
                return self.getToken(ExpParser.COMMA, i)

        def getRuleIndex(self):
            return ExpParser.RULE_parameters




    def parameters(self):

        localctx = ExpParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            localctx._NAME = self.match(ExpParser.NAME)

            if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                symbol_table_use.append(0)
                type_table.append('i')
            else:
                error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "parameter names must be unique")
                
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.COMMA:
                self.state = 69
                self.match(ExpParser.COMMA)
                self.state = 70
                localctx._NAME = self.match(ExpParser.NAME)

                if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                    symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                    symbol_table_use.append(0)
                    type_table.append('i')
                else:
                    error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "parameter names must be unique")
                    
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 6, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)

            print('.method public static main([Ljava/lang/String;)V\n')
                
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self.statement()
                self.state = 81 
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


        def st_call(self):
            return self.getTypedRuleContext(ExpParser.St_callContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_statement




    def statement(self):

        localctx = ExpParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.st_print()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.st_if()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.st_while()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.st_break()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.st_continue()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
                self.st_array_new()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 91
                self.st_array_set()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 92
                self.st_array_push()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 93
                self.st_attrib()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 94
                self.st_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token
            self.args = None # ArgumentsContext

        def NAME(self):
            return self.getToken(ExpParser.NAME, 0)

        def OP_PAR(self):
            return self.getToken(ExpParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(ExpParser.CL_PAR, 0)

        def arguments(self):
            return self.getTypedRuleContext(ExpParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_st_call




    def st_call(self):

        localctx = ExpParser.St_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_st_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 98
            self.match(ExpParser.OP_PAR)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.OP_PAR) | (1 << ExpParser.READ_INT) | (1 << ExpParser.READ_STR) | (1 << ExpParser.NUMBER) | (1 << ExpParser.STRING) | (1 << ExpParser.NAME))) != 0):
                self.state = 99
                localctx.args = self.arguments()

                if localctx.args.types.count('i') != len(localctx.args.types):
                    error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "all arguments must be integer")
                    


            self.state = 104
            self.match(ExpParser.CL_PAR)

            if (None if localctx._NAME is None else localctx._NAME.text) in func_table:
                try:
                    args_count = len(localctx.args.types)
                except:
                    args_count = 0
                index = func_table.index((None if localctx._NAME is None else localctx._NAME.text))
                if args_count != func_num_args[index]:
                    error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "wrong number of arguments")
                emit("invokestatic Test/{}({})V".format((None if localctx._NAME is None else localctx._NAME.text), "I"*func_num_args[index]))
            else:
                error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg="function '{}' is not declared".format((None if localctx._NAME is None else localctx._NAME.text)))
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.types = None
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

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
            return ExpParser.RULE_arguments




    def arguments(self):

        localctx = ExpParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            localctx.e1 = self.expression()

            types = [localctx.e1.type]
                
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.COMMA:
                self.state = 109
                self.match(ExpParser.COMMA)
                self.state = 110
                localctx.e2 = self.expression()

                types.append(localctx.e2.type)
                    
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.types = types
                
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
        self.enterRule(localctx, 14, self.RULE_st_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(ExpParser.PRINT)
            self.state = 121
            self.match(ExpParser.OP_PAR)

            emit('getstatic java/lang/System/out Ljava/io/PrintStream;', stack_att = +1)
                
            self.state = 123
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
                
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.COMMA:
                self.state = 125
                self.match(ExpParser.COMMA)

                emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    
                self.state = 127
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
                    
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
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
        self.enterRule(localctx, 16, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 139
            self.match(ExpParser.ATTRIB)
            self.state = 140
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
        self.enterRule(localctx, 18, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(ExpParser.IF)
            self.state = 144
            self.comparison()

            have_else = False
            global if_counter
            if_counter_local = if_counter
            not_if_local = "NOT_IF_" + str(if_counter_local)
            if_counter += 1
            emit(not_if_local, initLN='')
                
            self.state = 146
            self.match(ExpParser.OP_CUR)
            self.state = 148 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 147
                self.statement()
                self.state = 150 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                    break

            self.state = 152
            self.match(ExpParser.CL_CUR)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ExpParser.ELSE:

                have_else = True
                end_else = "END_ELSE_"+str(if_counter_local)
                emit("goto "+end_else)
                emit(not_if_local + ':\n' )
                    
                self.state = 154
                self.match(ExpParser.ELSE)
                self.state = 155
                self.match(ExpParser.OP_CUR)
                self.state = 157 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 156
                    self.statement()
                    self.state = 159 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                        break

                self.state = 161
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
        self.enterRule(localctx, 20, self.RULE_st_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
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
                
            self.state = 169
            self.comparison()

            emit(end_while, initLN='')
                
            self.state = 171
            self.match(ExpParser.OP_CUR)
            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.statement()
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                    break

            self.state = 177
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
        self.enterRule(localctx, 22, self.RULE_st_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            localctx._BREAK = self.match(ExpParser.BREAK)

            global current_end_while
            if len(current_end_while) > 0:
                emit("goto " + current_end_while[-1] + " ;break")
            else:
                error(line = (0 if localctx._BREAK is None else localctx._BREAK.line), msg = "the 'break' command must be in a loop escope")
                
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
        self.enterRule(localctx, 24, self.RULE_st_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
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
        self.enterRule(localctx, 26, self.RULE_st_array_new)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 187
            self.match(ExpParser.ATTRIB)
            self.state = 188
            self.match(ExpParser.OP_SB)
            self.state = 189
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
        self.enterRule(localctx, 28, self.RULE_st_array_push)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 193
            self.match(ExpParser.DOT)
            self.state = 194
            self.match(ExpParser.PUSH)

            index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))  
            emit("aload " + str(index), stack_att=+1)
                
            self.state = 196
            self.match(ExpParser.OP_PAR)
            self.state = 197
            self.expression()
            self.state = 198
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
        self.enterRule(localctx, 30, self.RULE_st_array_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            localctx._NAME = self.match(ExpParser.NAME)
             
            if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                emit("aload " + str(index), stack_att = +1)
            else:
                error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "'" + (None if localctx._NAME is None else localctx._NAME.text) + "' is not declared")
                
            self.state = 203
            self.match(ExpParser.OP_SB)
            self.state = 204
            localctx.ex1 = self.expression()
            self.state = 205
            self.match(ExpParser.CL_SB)
            self.state = 206
            self.match(ExpParser.ATTRIB)
            self.state = 207
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
        self.enterRule(localctx, 32, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            localctx.e1 = self.expression()
            self.state = 211
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.EQ) | (1 << ExpParser.NE) | (1 << ExpParser.GT) | (1 << ExpParser.GE) | (1 << ExpParser.LT) | (1 << ExpParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 212
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
        self.enterRule(localctx, 34, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            localctx.t1 = self.term()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.PLUS or _la==ExpParser.MINUS:
                self.state = 216
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ExpParser.PLUS or _la==ExpParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 217
                localctx.t2 = self.term()

                if (0 if localctx.op is None else localctx.op.type) == ExpParser.PLUS  : emit('iadd', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.MINUS : emit('isub', -1)
                if localctx.t1.type != 'err' and localctx.t2.type != 'err':
                    if localctx.t1.type != localctx.t2.type:
                        error(line = (0 if localctx.op is None else localctx.op.line), msg = "cannot mix types")
                    elif localctx.t1.type != 'i' or localctx.t2.type != 'i':
                        error(line = (0 if localctx.op is None else localctx.op.line), msg = "math operations is only for integers" )
                        
                self.state = 224
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
        self.enterRule(localctx, 36, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            localctx.f1 = self.factor()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.TIMES) | (1 << ExpParser.OVER) | (1 << ExpParser.REM))) != 0):
                self.state = 228
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.TIMES) | (1 << ExpParser.OVER) | (1 << ExpParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 229
                localctx.f2 = self.factor()

                if (0 if localctx.op is None else localctx.op.type) == ExpParser.TIMES : emit('imul', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.OVER  : emit('idiv', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.REM   : emit('irem', -1)
                if localctx.f1.type != localctx.f2.type:
                    error(line = (0 if localctx.op is None else localctx.op.line), msg = "cannot mix types")
                elif localctx.f1.type != 'i' or localctx.f2.type != 'i':
                    error(msg = "in line " + str((0 if localctx.op is None else localctx.op.line)) + " math operations is only for integers" )
                    
                self.state = 236
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
        self.enterRule(localctx, 38, self.RULE_factor)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                localctx._NUMBER = self.match(ExpParser.NUMBER)

                emit('ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text), +1)
                localctx.type = 'i'
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(ExpParser.OP_PAR)
                self.state = 242
                localctx.f1 = localctx._expression = self.expression()
                self.state = 243
                self.match(ExpParser.CL_PAR)

                localctx.type = localctx._expression.type
                    
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                localctx._NAME = self.match(ExpParser.NAME)

                # encontrar o index de (None if localctx._NAME is None else localctx._NAME.text) e gerar o bytecode 'iload index'
                if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                    error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "variable '" + (None if localctx._NAME is None else localctx._NAME.text) + "' is not declared")
                    localctx.type = 'err'
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
                self.state = 248
                self.match(ExpParser.READ_INT)
                self.state = 249
                self.match(ExpParser.OP_PAR)
                self.state = 250
                self.match(ExpParser.CL_PAR)

                emit("invokestatic Runtime/readInt()I", +1)
                localctx.type = 'i'
                    
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 252
                localctx._STRING = self.match(ExpParser.STRING)

                emit('ldc '+ (None if localctx._STRING is None else localctx._STRING.text), +1)
                localctx.type = 's'
                    
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 254
                self.match(ExpParser.READ_STR)
                self.state = 255
                self.match(ExpParser.OP_PAR)
                self.state = 256
                self.match(ExpParser.CL_PAR)

                emit("invokestatic Runtime/readString()Ljava/lang/String;", +1)
                localctx.type = 's'
                    
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 258
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
                    
                self.state = 260
                self.match(ExpParser.OP_SB)
                self.state = 261
                self.expression()
                self.state = 262
                self.match(ExpParser.CL_SB)

                emit("invokevirtual Array/get(I)I", stack_att = -1)
                localctx.type = 'i'
                    
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 265
                localctx._NAME = self.match(ExpParser.NAME)
                self.state = 266
                self.match(ExpParser.DOT)
                self.state = 267
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





