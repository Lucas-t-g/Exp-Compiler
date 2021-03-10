# Generated from Exp.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("B\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\7\2")
        buf.write("\34\n\2\f\2\16\2\37\13\2\3\2\3\2\3\3\6\3$\n\3\r\3\16\3")
        buf.write("%\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\6\f?\n")
        buf.write("\f\r\f\16\f@\2\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\3\2\4\3\2\f\f\5\2\13\f\17\17\"\"\2D\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2\5#\3\2\2\2")
        buf.write("\7)\3\2\2\2\t+\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\61\3")
        buf.write("\2\2\2\21\63\3\2\2\2\23\65\3\2\2\2\25\67\3\2\2\2\27>\3")
        buf.write("\2\2\2\31\35\7%\2\2\32\34\n\2\2\2\33\32\3\2\2\2\34\37")
        buf.write("\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36 \3\2\2\2\37\35")
        buf.write("\3\2\2\2 !\b\2\2\2!\4\3\2\2\2\"$\t\3\2\2#\"\3\2\2\2$%")
        buf.write("\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\b\3\2\2(\6")
        buf.write("\3\2\2\2)*\7-\2\2*\b\3\2\2\2+,\7,\2\2,\n\3\2\2\2-.\7*")
        buf.write("\2\2.\f\3\2\2\2/\60\7+\2\2\60\16\3\2\2\2\61\62\7/\2\2")
        buf.write("\62\20\3\2\2\2\63\64\7\61\2\2\64\22\3\2\2\2\65\66\7\'")
        buf.write("\2\2\66\24\3\2\2\2\678\7r\2\289\7t\2\29:\7k\2\2:;\7p\2")
        buf.write("\2;<\7v\2\2<\26\3\2\2\2=?\4\62;\2>=\3\2\2\2?@\3\2\2\2")
        buf.write("@>\3\2\2\2@A\3\2\2\2A\30\3\2\2\2\6\2\35%@\3\b\2\2")
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
    PRINT = 10
    NUMBER = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'('", "')'", "'-'", "'/'", "'%'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "SPACE", "PLUS", "TIMES", "OP_PAR", "CL_PAR", "MINUS", 
            "OVER", "REM", "PRINT", "NUMBER" ]

    ruleNames = [ "COMMENT", "SPACE", "PLUS", "TIMES", "OP_PAR", "CL_PAR", 
                  "MINUS", "OVER", "REM", "PRINT", "NUMBER" ]

    grammarFileName = "Exp.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


