# Generated from Exp.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("\\\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\7\2$\n\2\f\2\16\2\'")
        buf.write("\13\2\3\2\3\2\3\3\6\3,\n\3\r\3\16\3-\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\6\17T\n\17\r\17\16\17U")
        buf.write("\3\20\6\20Y\n\20\r\20\16\20Z\2\2\21\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21\3\2\4\3\2\f\f\5\2\13\f\17\17\"\"\2_\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\3!\3\2\2\2\5+\3\2\2\2\7\61\3\2\2\2\t\63")
        buf.write("\3\2\2\2\13\65\3\2\2\2\r\67\3\2\2\2\179\3\2\2\2\21;\3")
        buf.write("\2\2\2\23=\3\2\2\2\25?\3\2\2\2\27A\3\2\2\2\31C\3\2\2\2")
        buf.write("\33I\3\2\2\2\35S\3\2\2\2\37X\3\2\2\2!%\7%\2\2\"$\n\2\2")
        buf.write("\2#\"\3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2")
        buf.write("\'%\3\2\2\2()\b\2\2\2)\4\3\2\2\2*,\t\3\2\2+*\3\2\2\2,")
        buf.write("-\3\2\2\2-+\3\2\2\2-.\3\2\2\2./\3\2\2\2/\60\b\3\2\2\60")
        buf.write("\6\3\2\2\2\61\62\7-\2\2\62\b\3\2\2\2\63\64\7,\2\2\64\n")
        buf.write("\3\2\2\2\65\66\7*\2\2\66\f\3\2\2\2\678\7+\2\28\16\3\2")
        buf.write("\2\29:\7/\2\2:\20\3\2\2\2;<\7\61\2\2<\22\3\2\2\2=>\7\'")
        buf.write("\2\2>\24\3\2\2\2?@\7?\2\2@\26\3\2\2\2AB\7.\2\2B\30\3\2")
        buf.write("\2\2CD\7r\2\2DE\7t\2\2EF\7k\2\2FG\7p\2\2GH\7v\2\2H\32")
        buf.write("\3\2\2\2IJ\7t\2\2JK\7g\2\2KL\7c\2\2LM\7f\2\2MN\7a\2\2")
        buf.write("NO\7k\2\2OP\7p\2\2PQ\7v\2\2Q\34\3\2\2\2RT\4\62;\2SR\3")
        buf.write("\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2V\36\3\2\2\2WY\4c")
        buf.write("|\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[ \3\2\2\2")
        buf.write("\7\2%-UZ\3\b\2\2")
        return buf.getvalue()


class ExpLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    SPACE = 2
    PLUS = 3
    TIMES = 4
    OP_PAR = 5
    CL_PAR = 6
    MINUS = 7
    OVER = 8
    REM = 9
    ATTRIB = 10
    COMMA = 11
    PRINT = 12
    READ_INT = 13
    NUMBER = 14
    NAME = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'('", "')'", "'-'", "'/'", "'%'", "'='", "','", 
            "'print'", "'read_int'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "SPACE", "PLUS", "TIMES", "OP_PAR", "CL_PAR", "MINUS", 
            "OVER", "REM", "ATTRIB", "COMMA", "PRINT", "READ_INT", "NUMBER", 
            "NAME" ]

    ruleNames = [ "COMMENT", "SPACE", "PLUS", "TIMES", "OP_PAR", "CL_PAR", 
                  "MINUS", "OVER", "REM", "ATTRIB", "COMMA", "PRINT", "READ_INT", 
                  "NUMBER", "NAME" ]

    grammarFileName = "Exp.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


