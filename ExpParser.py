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
        buf.write("\u00ef\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\7\2)\n\2\f\2\16\2,\13\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\7\3\67\n\3\f\3\16\3:\13\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\6\4A\n\4\r\4\16\4B\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5Q\n\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7b\n\7\f\7\16\7")
        buf.write("e\13\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\6\tt\n\t\r\t\16\tu\3\t\3\t\3\t\3\t\3\t\6\t}\n\t\r")
        buf.write("\t\16\t~\3\t\3\t\5\t\u0083\n\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\6\n\u008d\n\n\r\n\16\n\u008e\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\7\21\u00bc\n\21\f\21\16\21\u00bf")
        buf.write("\13\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\7\22\u00c8\n")
        buf.write("\22\f\22\16\22\u00cb\13\22\3\22\3\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u00ed\n\23\3\23\2\2\24")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\5\3\2\22")
        buf.write("\27\4\2\5\5\7\7\4\2\6\6\b\t\2\u00f6\2&\3\2\2\2\4/\3\2")
        buf.write("\2\2\6>\3\2\2\2\bP\3\2\2\2\nR\3\2\2\2\fW\3\2\2\2\16i\3")
        buf.write("\2\2\2\20n\3\2\2\2\22\u0086\3\2\2\2\24\u0093\3\2\2\2\26")
        buf.write("\u0096\3\2\2\2\30\u0099\3\2\2\2\32\u009f\3\2\2\2\34\u00a8")
        buf.write("\3\2\2\2\36\u00b1\3\2\2\2 \u00b6\3\2\2\2\"\u00c2\3\2\2")
        buf.write("\2$\u00ec\3\2\2\2&*\b\2\1\2\')\5\4\3\2(\'\3\2\2\2),\3")
        buf.write("\2\2\2*(\3\2\2\2*+\3\2\2\2+-\3\2\2\2,*\3\2\2\2-.\5\6\4")
        buf.write("\2.\3\3\2\2\2/\60\7#\2\2\60\61\7&\2\2\61\62\7\f\2\2\62")
        buf.write("\63\7\r\2\2\63\64\b\3\1\2\648\7\16\2\2\65\67\5\b\5\2\66")
        buf.write("\65\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29;\3\2\2")
        buf.write("\2:8\3\2\2\2;<\7\17\2\2<=\b\3\1\2=\5\3\2\2\2>@\b\4\1\2")
        buf.write("?A\5\b\5\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2CD\3")
        buf.write("\2\2\2DE\b\4\1\2E\7\3\2\2\2FQ\5\f\7\2GQ\5\20\t\2HQ\5\22")
        buf.write("\n\2IQ\5\24\13\2JQ\5\26\f\2KQ\5\30\r\2LQ\5\34\17\2MQ\5")
        buf.write("\32\16\2NQ\5\16\b\2OQ\5\n\6\2PF\3\2\2\2PG\3\2\2\2PH\3")
        buf.write("\2\2\2PI\3\2\2\2PJ\3\2\2\2PK\3\2\2\2PL\3\2\2\2PM\3\2\2")
        buf.write("\2PN\3\2\2\2PO\3\2\2\2Q\t\3\2\2\2RS\7&\2\2ST\7\f\2\2T")
        buf.write("U\7\r\2\2UV\b\6\1\2V\13\3\2\2\2WX\7\33\2\2XY\7\f\2\2Y")
        buf.write("Z\b\7\1\2Z[\5 \21\2[c\b\7\1\2\\]\7\13\2\2]^\b\7\1\2^_")
        buf.write("\5 \21\2_`\b\7\1\2`b\3\2\2\2a\\\3\2\2\2be\3\2\2\2ca\3")
        buf.write("\2\2\2cd\3\2\2\2df\3\2\2\2ec\3\2\2\2fg\7\r\2\2gh\b\7\1")
        buf.write("\2h\r\3\2\2\2ij\7&\2\2jk\7\n\2\2kl\5 \21\2lm\b\b\1\2m")
        buf.write("\17\3\2\2\2no\7\36\2\2op\5\36\20\2pq\b\t\1\2qs\7\16\2")
        buf.write("\2rt\5\b\5\2sr\3\2\2\2tu\3\2\2\2us\3\2\2\2uv\3\2\2\2v")
        buf.write("w\3\2\2\2w\u0082\7\17\2\2xy\b\t\1\2yz\7\"\2\2z|\7\16\2")
        buf.write("\2{}\5\b\5\2|{\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2")
        buf.write("\2\177\u0080\3\2\2\2\u0080\u0081\7\17\2\2\u0081\u0083")
        buf.write("\3\2\2\2\u0082x\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0085\b\t\1\2\u0085\21\3\2\2\2\u0086\u0087")
        buf.write("\7\37\2\2\u0087\u0088\b\n\1\2\u0088\u0089\5\36\20\2\u0089")
        buf.write("\u008a\b\n\1\2\u008a\u008c\7\16\2\2\u008b\u008d\5\b\5")
        buf.write("\2\u008c\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u0091\7\17\2\2\u0091\u0092\b\n\1\2\u0092\23\3\2\2\2\u0093")
        buf.write("\u0094\7 \2\2\u0094\u0095\b\13\1\2\u0095\25\3\2\2\2\u0096")
        buf.write("\u0097\7!\2\2\u0097\u0098\b\f\1\2\u0098\27\3\2\2\2\u0099")
        buf.write("\u009a\7&\2\2\u009a\u009b\7\n\2\2\u009b\u009c\7\20\2\2")
        buf.write("\u009c\u009d\7\21\2\2\u009d\u009e\b\r\1\2\u009e\31\3\2")
        buf.write("\2\2\u009f\u00a0\7&\2\2\u00a0\u00a1\7\30\2\2\u00a1\u00a2")
        buf.write("\7\31\2\2\u00a2\u00a3\b\16\1\2\u00a3\u00a4\7\f\2\2\u00a4")
        buf.write("\u00a5\5 \21\2\u00a5\u00a6\7\r\2\2\u00a6\u00a7\b\16\1")
        buf.write("\2\u00a7\33\3\2\2\2\u00a8\u00a9\7&\2\2\u00a9\u00aa\b\17")
        buf.write("\1\2\u00aa\u00ab\7\20\2\2\u00ab\u00ac\5 \21\2\u00ac\u00ad")
        buf.write("\7\21\2\2\u00ad\u00ae\7\n\2\2\u00ae\u00af\5 \21\2\u00af")
        buf.write("\u00b0\b\17\1\2\u00b0\35\3\2\2\2\u00b1\u00b2\5 \21\2\u00b2")
        buf.write("\u00b3\t\2\2\2\u00b3\u00b4\5 \21\2\u00b4\u00b5\b\20\1")
        buf.write("\2\u00b5\37\3\2\2\2\u00b6\u00bd\5\"\22\2\u00b7\u00b8\t")
        buf.write("\3\2\2\u00b8\u00b9\5\"\22\2\u00b9\u00ba\b\21\1\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00b7\3\2\2\2\u00bc\u00bf\3\2\2\2")
        buf.write("\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c0\3")
        buf.write("\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c1\b\21\1\2\u00c1")
        buf.write("!\3\2\2\2\u00c2\u00c9\5$\23\2\u00c3\u00c4\t\4\2\2\u00c4")
        buf.write("\u00c5\5$\23\2\u00c5\u00c6\b\22\1\2\u00c6\u00c8\3\2\2")
        buf.write("\2\u00c7\u00c3\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cc\u00cd\b\22\1\2\u00cd#\3\2\2\2\u00ce")
        buf.write("\u00cf\7$\2\2\u00cf\u00ed\b\23\1\2\u00d0\u00d1\7\f\2\2")
        buf.write("\u00d1\u00d2\5 \21\2\u00d2\u00d3\7\r\2\2\u00d3\u00d4\b")
        buf.write("\23\1\2\u00d4\u00ed\3\2\2\2\u00d5\u00d6\7&\2\2\u00d6\u00ed")
        buf.write("\b\23\1\2\u00d7\u00d8\7\34\2\2\u00d8\u00d9\7\f\2\2\u00d9")
        buf.write("\u00da\7\r\2\2\u00da\u00ed\b\23\1\2\u00db\u00dc\7%\2\2")
        buf.write("\u00dc\u00ed\b\23\1\2\u00dd\u00de\7\35\2\2\u00de\u00df")
        buf.write("\7\f\2\2\u00df\u00e0\7\r\2\2\u00e0\u00ed\b\23\1\2\u00e1")
        buf.write("\u00e2\7&\2\2\u00e2\u00e3\b\23\1\2\u00e3\u00e4\7\20\2")
        buf.write("\2\u00e4\u00e5\5 \21\2\u00e5\u00e6\7\21\2\2\u00e6\u00e7")
        buf.write("\b\23\1\2\u00e7\u00ed\3\2\2\2\u00e8\u00e9\7&\2\2\u00e9")
        buf.write("\u00ea\7\30\2\2\u00ea\u00eb\7\32\2\2\u00eb\u00ed\b\23")
        buf.write("\1\2\u00ec\u00ce\3\2\2\2\u00ec\u00d0\3\2\2\2\u00ec\u00d5")
        buf.write("\3\2\2\2\u00ec\u00d7\3\2\2\2\u00ec\u00db\3\2\2\2\u00ec")
        buf.write("\u00dd\3\2\2\2\u00ec\u00e1\3\2\2\2\u00ec\u00e8\3\2\2\2")
        buf.write("\u00ed%\3\2\2\2\16*8BPcu~\u0082\u008e\u00bd\u00c9\u00ec")
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
    RULE_main = 2
    RULE_statement = 3
    RULE_st_call = 4
    RULE_st_print = 5
    RULE_st_attrib = 6
    RULE_st_if = 7
    RULE_st_while = 8
    RULE_st_break = 9
    RULE_st_continue = 10
    RULE_st_array_new = 11
    RULE_st_array_push = 12
    RULE_st_array_set = 13
    RULE_comparison = 14
    RULE_expression = 15
    RULE_term = 16
    RULE_factor = 17

    ruleNames =  [ "program", "function", "main", "statement", "st_call", 
                   "st_print", "st_attrib", "st_if", "st_while", "st_break", 
                   "st_continue", "st_array_new", "st_array_push", "st_array_set", 
                   "comparison", "expression", "term", "factor" ]

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
                
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.DEF:
                self.state = 37
                self.function()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
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
            self.state = 45
            self.match(ExpParser.DEF)
            self.state = 46
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 47
            self.match(ExpParser.OP_PAR)
            self.state = 48
            self.match(ExpParser.CL_PAR)

            global tab_count, symbol_table, type_table, symbol_table_use, func_table
            if (None if localctx._NAME is None else localctx._NAME.text) not in func_table:
                tab_count = 0
                emit(".method public static {}()V".format((None if localctx._NAME is None else localctx._NAME.text)))
                tab_count = 1
            else:
                error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "function '{}' is already declared".format((None if localctx._NAME is None else localctx._NAME.text)) )
                
            self.state = 50
            self.match(ExpParser.OP_CUR)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0):
                self.state = 51
                self.statement()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
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
            func_table.append((None if localctx._NAME is None else localctx._NAME.text))
            emit("")
            tab_count = 1
                
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
        self.enterRule(localctx, 4, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)

            print('.method public static main([Ljava/lang/String;)V\n')
                
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.statement()
                self.state = 64 
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
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.st_print()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.st_if()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.st_while()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.st_break()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.st_continue()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.st_array_new()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.st_array_set()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.st_array_push()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 76
                self.st_attrib()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 77
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

        def NAME(self):
            return self.getToken(ExpParser.NAME, 0)

        def OP_PAR(self):
            return self.getToken(ExpParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(ExpParser.CL_PAR, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_st_call




    def st_call(self):

        localctx = ExpParser.St_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_st_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 81
            self.match(ExpParser.OP_PAR)
            self.state = 82
            self.match(ExpParser.CL_PAR)

            if (None if localctx._NAME is None else localctx._NAME.text) in func_table:
                emit("invokestatic Test/{}()V".format((None if localctx._NAME is None else localctx._NAME.text)))
            else:
                error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg="function '{}' is not declared".format((None if localctx._NAME is None else localctx._NAME.text)))
                
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
        self.enterRule(localctx, 10, self.RULE_st_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(ExpParser.PRINT)
            self.state = 86
            self.match(ExpParser.OP_PAR)

            emit('getstatic java/lang/System/out Ljava/io/PrintStream;', stack_att = +1)
                
            self.state = 88
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
                
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.COMMA:
                self.state = 90
                self.match(ExpParser.COMMA)

                emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    
                self.state = 92
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
                    
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
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
        self.enterRule(localctx, 12, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 104
            self.match(ExpParser.ATTRIB)
            self.state = 105
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
        self.enterRule(localctx, 14, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(ExpParser.IF)
            self.state = 109
            self.comparison()

            have_else = False
            global if_counter
            if_counter_local = if_counter
            not_if_local = "NOT_IF_" + str(if_counter_local)
            if_counter += 1
            emit(not_if_local, initLN='')
                
            self.state = 111
            self.match(ExpParser.OP_CUR)
            self.state = 113 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self.statement()
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                    break

            self.state = 117
            self.match(ExpParser.CL_CUR)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ExpParser.ELSE:

                have_else = True
                end_else = "END_ELSE_"+str(if_counter_local)
                emit("goto "+end_else)
                emit(not_if_local + ':\n' )
                    
                self.state = 119
                self.match(ExpParser.ELSE)
                self.state = 120
                self.match(ExpParser.OP_CUR)
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 121
                    self.statement()
                    self.state = 124 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                        break

                self.state = 126
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
        self.enterRule(localctx, 16, self.RULE_st_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
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
                
            self.state = 134
            self.comparison()

            emit(end_while, initLN='')
                
            self.state = 136
            self.match(ExpParser.OP_CUR)
            self.state = 138 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 137
                self.statement()
                self.state = 140 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                    break

            self.state = 142
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
        self.enterRule(localctx, 18, self.RULE_st_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
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
        self.enterRule(localctx, 20, self.RULE_st_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
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
        self.enterRule(localctx, 22, self.RULE_st_array_new)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 152
            self.match(ExpParser.ATTRIB)
            self.state = 153
            self.match(ExpParser.OP_SB)
            self.state = 154
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
        self.enterRule(localctx, 24, self.RULE_st_array_push)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 158
            self.match(ExpParser.DOT)
            self.state = 159
            self.match(ExpParser.PUSH)

            index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))  
            emit("aload " + str(index), stack_att=+1)
                
            self.state = 161
            self.match(ExpParser.OP_PAR)
            self.state = 162
            self.expression()
            self.state = 163
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
        self.enterRule(localctx, 26, self.RULE_st_array_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            localctx._NAME = self.match(ExpParser.NAME)
             
            if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                emit("aload " + str(index), stack_att = +1)
            else:
                error(line = (0 if localctx._NAME is None else localctx._NAME.line), msg = "'" + (None if localctx._NAME is None else localctx._NAME.text) + "' is not declared")
                
            self.state = 168
            self.match(ExpParser.OP_SB)
            self.state = 169
            localctx.ex1 = self.expression()
            self.state = 170
            self.match(ExpParser.CL_SB)
            self.state = 171
            self.match(ExpParser.ATTRIB)
            self.state = 172
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
        self.enterRule(localctx, 28, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            localctx.e1 = self.expression()
            self.state = 176
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.EQ) | (1 << ExpParser.NE) | (1 << ExpParser.GT) | (1 << ExpParser.GE) | (1 << ExpParser.LT) | (1 << ExpParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 177
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
        self.enterRule(localctx, 30, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            localctx.t1 = self.term()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.PLUS or _la==ExpParser.MINUS:
                self.state = 181
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ExpParser.PLUS or _la==ExpParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 182
                localctx.t2 = self.term()

                if (0 if localctx.op is None else localctx.op.type) == ExpParser.PLUS  : emit('iadd', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.MINUS : emit('isub', -1)
                if localctx.t1.type != 'err' and localctx.t2.type != 'err':
                    if localctx.t1.type != localctx.t2.type:
                        error(line = (0 if localctx.op is None else localctx.op.line), msg = "cannot mix types")
                    elif localctx.t1.type != 'i' or localctx.t2.type != 'i':
                        error(line = (0 if localctx.op is None else localctx.op.line), msg = "math operations is only for integers" )
                        
                self.state = 189
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
        self.enterRule(localctx, 32, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            localctx.f1 = self.factor()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.TIMES) | (1 << ExpParser.OVER) | (1 << ExpParser.REM))) != 0):
                self.state = 193
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.TIMES) | (1 << ExpParser.OVER) | (1 << ExpParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 194
                localctx.f2 = self.factor()

                if (0 if localctx.op is None else localctx.op.type) == ExpParser.TIMES : emit('imul', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.OVER  : emit('idiv', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.REM   : emit('irem', -1)
                if localctx.f1.type != localctx.f2.type:
                    error(line = (0 if localctx.op is None else localctx.op.line), msg = "cannot mix types")
                elif localctx.f1.type != 'i' or localctx.f2.type != 'i':
                    error(msg = "in line " + str((0 if localctx.op is None else localctx.op.line)) + " math operations is only for integers" )
                    
                self.state = 201
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
        self.enterRule(localctx, 34, self.RULE_factor)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                localctx._NUMBER = self.match(ExpParser.NUMBER)

                emit('ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text), +1)
                localctx.type = 'i'
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(ExpParser.OP_PAR)
                self.state = 207
                localctx.f1 = localctx._expression = self.expression()
                self.state = 208
                self.match(ExpParser.CL_PAR)

                localctx.type = localctx._expression.type
                    
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
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
                self.state = 213
                self.match(ExpParser.READ_INT)
                self.state = 214
                self.match(ExpParser.OP_PAR)
                self.state = 215
                self.match(ExpParser.CL_PAR)

                emit("invokestatic Runtime/readInt()I", +1)
                localctx.type = 'i'
                    
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 217
                localctx._STRING = self.match(ExpParser.STRING)

                emit('ldc '+ (None if localctx._STRING is None else localctx._STRING.text), +1)
                localctx.type = 's'
                    
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 219
                self.match(ExpParser.READ_STR)
                self.state = 220
                self.match(ExpParser.OP_PAR)
                self.state = 221
                self.match(ExpParser.CL_PAR)

                emit("invokestatic Runtime/readString()Ljava/lang/String;", +1)
                localctx.type = 's'
                    
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 223
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
                    
                self.state = 225
                self.match(ExpParser.OP_SB)
                self.state = 226
                self.expression()
                self.state = 227
                self.match(ExpParser.CL_SB)

                emit("invokevirtual Array/get(I)I", stack_att = -1)
                localctx.type = 'i'
                    
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 230
                localctx._NAME = self.match(ExpParser.NAME)
                self.state = 231
                self.match(ExpParser.DOT)
                self.state = 232
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





