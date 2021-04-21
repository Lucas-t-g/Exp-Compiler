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

def error(msg = "", fatal = False):
    global has_error
    has_error = True
    if not fatal:   print("ERROR: " + msg, file=sys.stderr)
    else: print("FATAL ERROR: inernal error", file=sys.stderr)


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("\u00a4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\3\3\3\6\3\"\n\3\r\3\16\3#\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4.\n\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\7\5:\n\5\f\5\16\5=\13\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\6\7L\n\7\r")
        buf.write("\7\16\7M\3\7\3\7\3\7\3\7\3\7\6\7U\n\7\r\7\16\7V\3\7\3")
        buf.write("\7\5\7[\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\6\be\n\b\r")
        buf.write("\b\16\bf\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\7\f|\n\f\f\f\16\f")
        buf.write("\177\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\7\r\u0088\n\r\f")
        buf.write("\r\16\r\u008b\13\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00a2\n\16\3\16\2\2\17\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\2\5\3\2\20\25\4\2\5\5\7\7\4\2")
        buf.write("\6\6\b\t\2\u00a8\2\34\3\2\2\2\4\37\3\2\2\2\6-\3\2\2\2")
        buf.write("\b/\3\2\2\2\nA\3\2\2\2\fF\3\2\2\2\16^\3\2\2\2\20k\3\2")
        buf.write("\2\2\22n\3\2\2\2\24q\3\2\2\2\26v\3\2\2\2\30\u0082\3\2")
        buf.write("\2\2\32\u00a1\3\2\2\2\34\35\b\2\1\2\35\36\5\4\3\2\36\3")
        buf.write("\3\2\2\2\37!\b\3\1\2 \"\5\6\4\2! \3\2\2\2\"#\3\2\2\2#")
        buf.write("!\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\b\3\1\2&\5\3\2\2\2\'.")
        buf.write("\5\b\5\2(.\5\n\6\2).\5\f\7\2*.\5\16\b\2+.\5\20\t\2,.\5")
        buf.write("\22\n\2-\'\3\2\2\2-(\3\2\2\2-)\3\2\2\2-*\3\2\2\2-+\3\2")
        buf.write("\2\2-,\3\2\2\2.\7\3\2\2\2/\60\7\26\2\2\60\61\7\n\2\2\61")
        buf.write("\62\b\5\1\2\62\63\5\26\f\2\63;\b\5\1\2\64\65\7\r\2\2\65")
        buf.write("\66\b\5\1\2\66\67\5\26\f\2\678\b\5\1\28:\3\2\2\29\64\3")
        buf.write("\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3\2\2")
        buf.write("\2>?\7\13\2\2?@\b\5\1\2@\t\3\2\2\2AB\7 \2\2BC\7\f\2\2")
        buf.write("CD\5\26\f\2DE\b\6\1\2E\13\3\2\2\2FG\7\31\2\2GH\5\24\13")
        buf.write("\2HI\b\7\1\2IK\7\16\2\2JL\5\6\4\2KJ\3\2\2\2LM\3\2\2\2")
        buf.write("MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OZ\7\17\2\2PQ\b\7\1\2QR")
        buf.write("\7\35\2\2RT\7\16\2\2SU\5\6\4\2TS\3\2\2\2UV\3\2\2\2VT\3")
        buf.write("\2\2\2VW\3\2\2\2WX\3\2\2\2XY\7\17\2\2Y[\3\2\2\2ZP\3\2")
        buf.write("\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\b\7\1\2]\r\3\2\2\2^_\7\32")
        buf.write("\2\2_`\b\b\1\2`a\5\24\13\2ab\b\b\1\2bd\7\16\2\2ce\5\6")
        buf.write("\4\2dc\3\2\2\2ef\3\2\2\2fd\3\2\2\2fg\3\2\2\2gh\3\2\2\2")
        buf.write("hi\7\17\2\2ij\b\b\1\2j\17\3\2\2\2kl\7\33\2\2lm\b\t\1\2")
        buf.write("m\21\3\2\2\2no\7\34\2\2op\b\n\1\2p\23\3\2\2\2qr\5\26\f")
        buf.write("\2rs\t\2\2\2st\5\26\f\2tu\b\13\1\2u\25\3\2\2\2v}\5\30")
        buf.write("\r\2wx\t\3\2\2xy\5\30\r\2yz\b\f\1\2z|\3\2\2\2{w\3\2\2")
        buf.write("\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0080\3\2\2\2\177")
        buf.write("}\3\2\2\2\u0080\u0081\b\f\1\2\u0081\27\3\2\2\2\u0082\u0089")
        buf.write("\5\32\16\2\u0083\u0084\t\4\2\2\u0084\u0085\5\32\16\2\u0085")
        buf.write("\u0086\b\r\1\2\u0086\u0088\3\2\2\2\u0087\u0083\3\2\2\2")
        buf.write("\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3")
        buf.write("\2\2\2\u008a\u008c\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d")
        buf.write("\b\r\1\2\u008d\31\3\2\2\2\u008e\u008f\7\36\2\2\u008f\u00a2")
        buf.write("\b\16\1\2\u0090\u0091\7\n\2\2\u0091\u0092\5\26\f\2\u0092")
        buf.write("\u0093\7\13\2\2\u0093\u0094\b\16\1\2\u0094\u00a2\3\2\2")
        buf.write("\2\u0095\u0096\7 \2\2\u0096\u00a2\b\16\1\2\u0097\u0098")
        buf.write("\7\27\2\2\u0098\u0099\7\n\2\2\u0099\u009a\7\13\2\2\u009a")
        buf.write("\u00a2\b\16\1\2\u009b\u009c\7\37\2\2\u009c\u00a2\b\16")
        buf.write("\1\2\u009d\u009e\7\30\2\2\u009e\u009f\7\n\2\2\u009f\u00a0")
        buf.write("\7\13\2\2\u00a0\u00a2\b\16\1\2\u00a1\u008e\3\2\2\2\u00a1")
        buf.write("\u0090\3\2\2\2\u00a1\u0095\3\2\2\2\u00a1\u0097\3\2\2\2")
        buf.write("\u00a1\u009b\3\2\2\2\u00a1\u009d\3\2\2\2\u00a2\33\3\2")
        buf.write("\2\2\f#-;MVZf}\u0089\u00a1")
        return buf.getvalue()


class ExpParser ( Parser ):

    grammarFileName = "Exp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'*'", 
                     "'-'", "'/'", "'%'", "'('", "')'", "'='", "','", "'{'", 
                     "'}'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "'print'", "'read_int'", "'read_str'", "'if'", "'while'", 
                     "'break'", "'continue'", "'else'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "SPACE", "PLUS", "TIMES", 
                      "MINUS", "OVER", "REM", "OP_PAR", "CL_PAR", "ATTRIB", 
                      "COMMA", "OP_CUR", "CL_CUR", "EQ", "NE", "GT", "GE", 
                      "LT", "LE", "PRINT", "READ_INT", "READ_STR", "IF", 
                      "WHILE", "BREAK", "CONTINUE", "ELSE", "NUMBER", "STRING", 
                      "NAME" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_st_attrib = 4
    RULE_st_if = 5
    RULE_st_while = 6
    RULE_st_break = 7
    RULE_st_continue = 8
    RULE_comparison = 9
    RULE_expression = 10
    RULE_term = 11
    RULE_factor = 12

    ruleNames =  [ "program", "main", "statement", "st_print", "st_attrib", 
                   "st_if", "st_while", "st_break", "st_continue", "comparison", 
                   "expression", "term", "factor" ]

    EOF = Token.EOF
    COMMENT=1
    SPACE=2
    PLUS=3
    TIMES=4
    MINUS=5
    OVER=6
    REM=7
    OP_PAR=8
    CL_PAR=9
    ATTRIB=10
    COMMA=11
    OP_CUR=12
    CL_CUR=13
    EQ=14
    NE=15
    GT=16
    GE=17
    LT=18
    LE=19
    PRINT=20
    READ_INT=21
    READ_STR=22
    IF=23
    WHILE=24
    BREAK=25
    CONTINUE=26
    ELSE=27
    NUMBER=28
    STRING=29
    NAME=30

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
                
            self.state = 27
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
                
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.statement()
                self.state = 33 
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


        def st_attrib(self):
            return self.getTypedRuleContext(ExpParser.St_attribContext,0)


        def st_if(self):
            return self.getTypedRuleContext(ExpParser.St_ifContext,0)


        def st_while(self):
            return self.getTypedRuleContext(ExpParser.St_whileContext,0)


        def st_break(self):
            return self.getTypedRuleContext(ExpParser.St_breakContext,0)


        def st_continue(self):
            return self.getTypedRuleContext(ExpParser.St_continueContext,0)


        def getRuleIndex(self):
            return ExpParser.RULE_statement




    def statement(self):

        localctx = ExpParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExpParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.st_print()
                pass
            elif token in [ExpParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.st_attrib()
                pass
            elif token in [ExpParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.st_if()
                pass
            elif token in [ExpParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.st_while()
                pass
            elif token in [ExpParser.BREAK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.st_break()
                pass
            elif token in [ExpParser.CONTINUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 42
                self.st_continue()
                pass
            else:
                raise NoViableAltException(self)

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
            self._COMMA = None # Token
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
            self.state = 45
            self.match(ExpParser.PRINT)
            self.state = 46
            self.match(ExpParser.OP_PAR)

            emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                
            self.state = 48
            localctx.e1 = self.expression()

            if localctx.e1.type == 'i':
                emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
            elif localctx.e1.type == 's':
                emit('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
            else:
                error(fatal = True)
                
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.COMMA:
                self.state = 50
                localctx._COMMA = self.match(ExpParser.COMMA)

                emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    
                self.state = 52
                localctx.e2 = self.expression()

                if localctx.e2.type == 'i':
                    emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
                elif localctx.e2.type == 's':
                    emit('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
                else:
                    error(msg = "in line" + str((0 if localctx._COMMA is None else localctx._COMMA.line)) + "The 'break' command must be in a loop escope")
                    
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
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
            self.state = 63
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 64
            self.match(ExpParser.ATTRIB)
            self.state = 65
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
                error(msg = "in line " + str((0 if localctx._NAME is None else localctx._NAME.line)) + " '"+(None if localctx._NAME is None else localctx._NAME.text)+"' must be an " + ("integer" if my_type == 'i' else "string") )
                
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
            self.state = 68
            self.match(ExpParser.IF)
            self.state = 69
            self.comparison()

            have_else = False
            global if_counter
            if_counter_local = if_counter
            not_if_local = "NOT_IF_" + str(if_counter_local)
            if_counter += 1
            emit(not_if_local, initLN='')
                
            self.state = 71
            self.match(ExpParser.OP_CUR)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.statement()
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                    break

            self.state = 77
            self.match(ExpParser.CL_CUR)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ExpParser.ELSE:

                have_else = True
                end_else = "END_ELSE_"+str(if_counter_local)
                emit("goto "+end_else)
                emit(not_if_local + ':\n' )
                    
                self.state = 79
                self.match(ExpParser.ELSE)
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
            self.state = 92
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
                
            self.state = 94
            self.comparison()

            emit(end_while, initLN='')
                
            self.state = 96
            self.match(ExpParser.OP_CUR)
            self.state = 98 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 97
                self.statement()
                self.state = 100 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.WHILE) | (1 << ExpParser.BREAK) | (1 << ExpParser.CONTINUE) | (1 << ExpParser.NAME))) != 0)):
                    break

            self.state = 102
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
            self.state = 105
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
            self.state = 108
            localctx._CONTINUE = self.match(ExpParser.CONTINUE)

            global current_begin_while
            if len(current_begin_while) > 0:
                emit("goto " + current_begin_while[-1] + " ;continue")
            else:
                error(msg = "in line" + str((0 if localctx._CONTINUE is None else localctx._CONTINUE.line)) + "the 'continue' command must be in a loop escope")
                
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
        self.enterRule(localctx, 18, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            localctx.e1 = self.expression()
            self.state = 112
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.EQ) | (1 << ExpParser.NE) | (1 << ExpParser.GT) | (1 << ExpParser.GE) | (1 << ExpParser.LT) | (1 << ExpParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 113
            localctx.e2 = self.expression()

            # usa a comparação inversa para o desvio

            if localctx.e1.type == 'i' and localctx.e2.type == 'i':
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.GT  :emit("if_icmple ", stack_att=-2, endLN='')
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.NE  : emit("if_icmpeq ", stack_att=-2, endLN='')
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.GE  : emit("if_icmplt ", stack_att=-2, endLN='')
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.LT  : emit("if_icmpge ", stack_att=-2, endLN='')
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.EQ  : emit("if_icmpne ", stack_att=-2, endLN='')
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.LE  : emit("if_icmpgt ", stack_att=-2, endLN='')
            else:
                error(msg = "in line " + str((0 if localctx.op is None else localctx.op.line)) + " cannot mix types")
                
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
        self.enterRule(localctx, 20, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            localctx.t1 = self.term()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.PLUS or _la==ExpParser.MINUS:
                self.state = 117
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ExpParser.PLUS or _la==ExpParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 118
                localctx.t2 = self.term()

                if (0 if localctx.op is None else localctx.op.type) == ExpParser.PLUS  : emit('iadd', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.MINUS : emit('isub', -1)
                if localctx.t1.type != localctx.t2.type:
                    error(msg = "in line " + str((0 if localctx.op is None else localctx.op.line)) + " cannot mix types")
                    
                self.state = 125
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
        self.enterRule(localctx, 22, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            localctx.f1 = self.factor()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.TIMES) | (1 << ExpParser.OVER) | (1 << ExpParser.REM))) != 0):
                self.state = 129
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.TIMES) | (1 << ExpParser.OVER) | (1 << ExpParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 130
                localctx.f2 = self.factor()

                if (0 if localctx.op is None else localctx.op.type) == ExpParser.TIMES : emit('imul', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.OVER  : emit('idiv', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.REM   : emit('irem', -1)
                if localctx.f1.type != localctx.f2.type:
                    error(msg = "in line " + str((0 if localctx.op is None else localctx.op.line)) + " cannot mix types")
                elif localctx.f1.type != 'i' or localctx.f2.type != 'i':
                    error(msg = "in line " + str((0 if localctx.op is None else localctx.op.line)) + " math operations is only for integers" )
                    
                self.state = 137
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

        def getRuleIndex(self):
            return ExpParser.RULE_factor




    def factor(self):

        localctx = ExpParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_factor)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExpParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                localctx._NUMBER = self.match(ExpParser.NUMBER)

                emit('ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text), +1)
                localctx.type = 'i'
                    
                pass
            elif token in [ExpParser.OP_PAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(ExpParser.OP_PAR)
                self.state = 143
                localctx.f1 = localctx._expression = self.expression()
                self.state = 144
                self.match(ExpParser.CL_PAR)

                localctx.type = localctx._expression.type
                    
                pass
            elif token in [ExpParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                localctx._NAME = self.match(ExpParser.NAME)

                # encontrar o index de (None if localctx._NAME is None else localctx._NAME.text) e gerar o bytecode 'iload index'
                if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                    error(msg =  "in line " + str((0 if localctx._NAME is None else localctx._NAME.line)) + "variable '" + (None if localctx._NAME is None else localctx._NAME.text) + "' is not declared")

                else:
                    index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                    symbol_table_use[index] += 1
                    my_type = type_table[index]
                    if my_type == 'i':
                        emit("iload "+ str(index), +1)
                        localctx.type = 'i'
                    elif my_type == 's':
                        emit("aload "+ str(index), +1)
                        localctx.type = 's'
                    else:
                        error(fatal = True)
                    
                pass
            elif token in [ExpParser.READ_INT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.match(ExpParser.READ_INT)
                self.state = 150
                self.match(ExpParser.OP_PAR)
                self.state = 151
                self.match(ExpParser.CL_PAR)

                emit("invokestatic Runtime/readInt()I", +1)
                localctx.type = 'i'
                    
                pass
            elif token in [ExpParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 153
                localctx._STRING = self.match(ExpParser.STRING)

                emit('ldc '+ (None if localctx._STRING is None else localctx._STRING.text), +1)
                localctx.type = 's'
                    
                pass
            elif token in [ExpParser.READ_STR]:
                self.enterOuterAlt(localctx, 6)
                self.state = 155
                self.match(ExpParser.READ_STR)
                self.state = 156
                self.match(ExpParser.OP_PAR)
                self.state = 157
                self.match(ExpParser.CL_PAR)

                emit("invokestatic Runtime/readString()Ljava/lang/String;", +1)
                localctx.type = 's'
                    
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





