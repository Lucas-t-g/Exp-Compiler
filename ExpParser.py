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

stack_cur = 0
stack_max = 0
if_counter = 0

def emit(comand, stack_att=0, initLN="    ", endLN='\n'):
    global stack_cur, stack_max
    stack_cur += stack_att
    if stack_cur > stack_max:
        stack_max = stack_cur
    print(initLN + comand, end=endLN)



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3\6\3")
        buf.write("\34\n\3\r\3\16\3\35\3\3\3\3\3\4\3\4\3\4\5\4%\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\61\n\5\f\5\16\5")
        buf.write("\64\13\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\6\7C\n\7\r\7\16\7D\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\7\tT\n\t\f\t\16\tW\13\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\7\n^\n\n\f\n\16\na\13\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13o\n")
        buf.write("\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\5\3\2\20\25\4")
        buf.write("\2\5\5\7\7\4\2\6\6\b\t\2p\2\26\3\2\2\2\4\31\3\2\2\2\6")
        buf.write("$\3\2\2\2\b&\3\2\2\2\n8\3\2\2\2\f=\3\2\2\2\16I\3\2\2\2")
        buf.write("\20N\3\2\2\2\22X\3\2\2\2\24n\3\2\2\2\26\27\b\2\1\2\27")
        buf.write("\30\5\4\3\2\30\3\3\2\2\2\31\33\b\3\1\2\32\34\5\6\4\2\33")
        buf.write("\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2")
        buf.write("\36\37\3\2\2\2\37 \b\3\1\2 \5\3\2\2\2!%\5\b\5\2\"%\5\n")
        buf.write("\6\2#%\5\f\7\2$!\3\2\2\2$\"\3\2\2\2$#\3\2\2\2%\7\3\2\2")
        buf.write("\2&\'\7\26\2\2\'(\7\n\2\2()\b\5\1\2)*\5\20\t\2*\62\b\5")
        buf.write("\1\2+,\7\r\2\2,-\b\5\1\2-.\5\20\t\2./\b\5\1\2/\61\3\2")
        buf.write("\2\2\60+\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2")
        buf.write("\2\2\63\65\3\2\2\2\64\62\3\2\2\2\65\66\7\13\2\2\66\67")
        buf.write("\b\5\1\2\67\t\3\2\2\289\7\32\2\29:\7\f\2\2:;\5\20\t\2")
        buf.write(";<\b\6\1\2<\13\3\2\2\2=>\7\30\2\2>?\5\16\b\2?@\b\7\1\2")
        buf.write("@B\7\16\2\2AC\5\6\4\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE")
        buf.write("\3\2\2\2EF\3\2\2\2FG\7\17\2\2GH\b\7\1\2H\r\3\2\2\2IJ\5")
        buf.write("\20\t\2JK\t\2\2\2KL\5\20\t\2LM\b\b\1\2M\17\3\2\2\2NU\5")
        buf.write("\22\n\2OP\t\3\2\2PQ\5\22\n\2QR\b\t\1\2RT\3\2\2\2SO\3\2")
        buf.write("\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V\21\3\2\2\2WU\3\2\2")
        buf.write("\2X_\5\24\13\2YZ\t\4\2\2Z[\5\24\13\2[\\\b\n\1\2\\^\3\2")
        buf.write("\2\2]Y\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\23\3\2\2")
        buf.write("\2a_\3\2\2\2bc\7\31\2\2co\b\13\1\2de\7\n\2\2ef\5\20\t")
        buf.write("\2fg\7\13\2\2go\3\2\2\2hi\7\32\2\2io\b\13\1\2jk\7\27\2")
        buf.write("\2kl\7\n\2\2lm\7\13\2\2mo\b\13\1\2nb\3\2\2\2nd\3\2\2\2")
        buf.write("nh\3\2\2\2nj\3\2\2\2o\25\3\2\2\2\t\35$\62DU_n")
        return buf.getvalue()


class ExpParser ( Parser ):

    grammarFileName = "Exp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'*'", 
                     "'-'", "'/'", "'%'", "'('", "')'", "'='", "','", "'{'", 
                     "'}'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "'print'", "'read_int'", "'if'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "SPACE", "PLUS", "TIMES", 
                      "MINUS", "OVER", "REM", "OP_PAR", "CL_PAR", "ATTRIB", 
                      "COMMA", "OP_CUR", "CL_CUR", "EQ", "NE", "GT", "GE", 
                      "LT", "LE", "PRINT", "READ_INT", "IF", "NUMBER", "NAME" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_st_attrib = 4
    RULE_st_if = 5
    RULE_comparison = 6
    RULE_expression = 7
    RULE_term = 8
    RULE_factor = 9

    ruleNames =  [ "program", "main", "statement", "st_print", "st_attrib", 
                   "st_if", "comparison", "expression", "term", "factor" ]

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
    IF=22
    NUMBER=23
    NAME=24

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
                
            self.state = 21
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
            symbol_table.append('args')
            symbol_table_use.append(1)
                
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.NAME))) != 0)):
                    break


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


        def getRuleIndex(self):
            return ExpParser.RULE_statement




    def statement(self):

        localctx = ExpParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExpParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.st_print()
                pass
            elif token in [ExpParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.st_attrib()
                pass
            elif token in [ExpParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.st_if()
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

        def PRINT(self):
            return self.getToken(ExpParser.PRINT, 0)

        def OP_PAR(self):
            return self.getToken(ExpParser.OP_PAR, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExpParser.ExpressionContext,i)


        def CL_PAR(self):
            return self.getToken(ExpParser.CL_PAR, 0)

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
            self.state = 36
            self.match(ExpParser.PRINT)
            self.state = 37
            self.match(ExpParser.OP_PAR)

            emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                
            self.state = 39
            self.expression()

            emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
                
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.COMMA:
                self.state = 41
                self.match(ExpParser.COMMA)

                emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
                    
                self.state = 43
                self.expression()

                emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
                    
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
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
            self.state = 54
            localctx._NAME = self.match(ExpParser.NAME)
            self.state = 55
            self.match(ExpParser.ATTRIB)
            self.state = 56
            self.expression()

            # 1. testar se a varialvel name já existe:  se não existir inclui (None if localctx._NAME is None else localctx._NAME.text) na symbol_table
            if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                symbol_table_use.append(0)

            # 2. encontrar o índice de (None if localctx._NAME is None else localctx._NAME.text) e gerar o bytecode 'istore index'
            index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
            emit("istore "+ str(index) + '\n', -1)
                
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
            return ExpParser.RULE_st_if




    def st_if(self):

        localctx = ExpParser.St_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ExpParser.IF)
            self.state = 60
            self.comparison()

            global if_counter
            if_counter_local = if_counter
            if_counter += 1
            emit("NOT_IF_" + str(if_counter_local), -2, initLN='')
                
            self.state = 62
            self.match(ExpParser.OP_CUR)
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.statement()
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.PRINT) | (1 << ExpParser.IF) | (1 << ExpParser.NAME))) != 0)):
                    break

            self.state = 68
            self.match(ExpParser.CL_CUR)

            emit("NOT_IF_" + str(if_counter_local)  + ':\n' )
                
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
            self.op = None # Token

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
        self.enterRule(localctx, 12, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.expression()
            self.state = 72
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.EQ) | (1 << ExpParser.NE) | (1 << ExpParser.GT) | (1 << ExpParser.GE) | (1 << ExpParser.LT) | (1 << ExpParser.LE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 73
            self.expression()

            # usa a comparação inversa para o desvio
            if (0 if localctx.op is None else localctx.op.type) == ExpParser.NE  : emit("if_icmpeq ", -2, endLN='')
            if (0 if localctx.op is None else localctx.op.type) == ExpParser.GT  : emit("if_icmple ", -2, endLN='')
            if (0 if localctx.op is None else localctx.op.type) == ExpParser.GE  : emit("if_icmplt ", -2, endLN='')
            if (0 if localctx.op is None else localctx.op.type) == ExpParser.LT  : emit("if_icmpge ", -2, endLN='')
            if (0 if localctx.op is None else localctx.op.type) == ExpParser.EQ  : emit("if_icmpne ", -2, endLN='')
            if (0 if localctx.op is None else localctx.op.type) == ExpParser.LE  : emit("if_icmpgt ", -2, endLN='')
                
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
            self.op = None # Token

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
        self.enterRule(localctx, 14, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.term()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExpParser.PLUS or _la==ExpParser.MINUS:
                self.state = 77
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==ExpParser.PLUS or _la==ExpParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 78
                self.term()

                if (0 if localctx.op is None else localctx.op.type) == ExpParser.PLUS  : emit('iadd', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.MINUS : emit('isub', -1)
                    
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.op = None # Token

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
        self.enterRule(localctx, 16, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.factor()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.TIMES) | (1 << ExpParser.OVER) | (1 << ExpParser.REM))) != 0):
                self.state = 87
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpParser.TIMES) | (1 << ExpParser.OVER) | (1 << ExpParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 88
                self.factor()

                if (0 if localctx.op is None else localctx.op.type) == ExpParser.TIMES : emit('imul', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.OVER  : emit('idiv', -1)
                if (0 if localctx.op is None else localctx.op.type) == ExpParser.REM   : emit('irem', -1)
                    
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self._NUMBER = None # Token
            self._NAME = None # Token

        def NUMBER(self):
            return self.getToken(ExpParser.NUMBER, 0)

        def OP_PAR(self):
            return self.getToken(ExpParser.OP_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(ExpParser.ExpressionContext,0)


        def CL_PAR(self):
            return self.getToken(ExpParser.CL_PAR, 0)

        def NAME(self):
            return self.getToken(ExpParser.NAME, 0)

        def READ_INT(self):
            return self.getToken(ExpParser.READ_INT, 0)

        def getRuleIndex(self):
            return ExpParser.RULE_factor




    def factor(self):

        localctx = ExpParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_factor)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExpParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                localctx._NUMBER = self.match(ExpParser.NUMBER)

                emit('ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text), +1)
                    
                pass
            elif token in [ExpParser.OP_PAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(ExpParser.OP_PAR)
                self.state = 99
                self.expression()
                self.state = 100
                self.match(ExpParser.CL_PAR)
                pass
            elif token in [ExpParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                localctx._NAME = self.match(ExpParser.NAME)

                # encontrar o index de (None if localctx._NAME is None else localctx._NAME.text) e gerar o bytecode 'iload index'
                if (None if localctx._NAME is None else localctx._NAME.text) not in symbol_table:
                    # print("fatal error", file=sys.stderr)
                    print("error: variable '"+ (None if localctx._NAME is None else localctx._NAME.text)+"' is not declared", file=sys.stderr)
                    sys.exit(1)
                else:
                    index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                    symbol_table_use[index] += 1
                    emit("iload "+ str(index), +1)
                    
                pass
            elif token in [ExpParser.READ_INT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.match(ExpParser.READ_INT)
                self.state = 105
                self.match(ExpParser.OP_PAR)
                self.state = 106
                self.match(ExpParser.CL_PAR)

                emit("invokestatic Runtime/readInt()I", +1)
                    
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





