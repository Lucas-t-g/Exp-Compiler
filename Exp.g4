grammar Exp;

/*---------------- PARSER INTERNALS ----------------*/

@parser::header
{
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

}


/*---------------- LEXER RULES ----------------*/

COMMENT: '#' ~('\n')*          -> skip ;
SPACE : (' '|'\t'|'\r'|'\n')+  -> skip ;

PLUS  : '+' ;
TIMES : '*' ;
MINUS : '-' ;
OVER  : '/' ;
REM   : '%' ;
OP_PAR: '(' ;
CL_PAR: ')' ;
ATTRIB: '=' ;
COMMA : ',' ;
OP_CUR: '{' ;
CL_CUR: '}' ;
EQ    : '==' ;
NE    : '!=' ;
GT    : '>'  ;
GE    : '>=' ;
LT    : '<'  ;
LE    : '<=' ;

PRINT   : 'print' ;
READ_INT: 'read_int';
IF      : 'if';

NUMBER: '0'..'9'+ ;

NAME  : 'a'..'z'+ ;


/*---------------- PARSER RULES ----------------*/

program:
    {
print('.source Test.src')
print('.class  public Test')
print('.super  java/lang/Object\n')
print('.method public <init>()V')
print('    aload_0')
print('    invokenonvirtual java/lang/Object/<init>()V')
print('    return')
print('.end method\n')
    }
    main ;

main:
    {
print('.method public static main([Ljava/lang/String;)V\n')
symbol_table.append('args')
symbol_table_use.append(1)
    }
    (statement )+
    {
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
    ;

statement: st_print | st_attrib | st_if;

st_print: PRINT OP_PAR
    {
emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
    }
    expression 
    {
emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
    }
    ( COMMA
    {
emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
    }
    expression
    {
emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
    }
    )*
    CL_PAR
    {
emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
emit('invokevirtual java/io/PrintStream/println()V\n', -1)
    }
    ;

st_attrib: NAME ATTRIB expression
    {
# 1. testar se a varialvel name já existe:  se não existir inclui $NAME.text na symbol_table
if $NAME.text not in symbol_table:
    symbol_table.append($NAME.text)
    symbol_table_use.append(0)

# 2. encontrar o índice de $NAME.text e gerar o bytecode 'istore index'
index = symbol_table.index($NAME.text)
emit("istore "+ str(index) + '\n', -1)
    }
    ;

st_if: IF comparison 
    {
global if_counter
if_counter_local = if_counter
if_counter += 1
emit("NOT_IF_" + str(if_counter_local), -2, initLN='')
    }
    OP_CUR (statement)+ CL_CUR
    {
emit("NOT_IF_" + str(if_counter_local)  + ':\n' )
    }
    ;

comparison: expression op = ( EQ | NE | GT | GE | LT | LE ) expression
    {
# usa a comparação inversa para o desvio
if $op.type == ExpParser.NE  : emit("if_icmpeq ", -2, endLN='')
if $op.type == ExpParser.GT  : emit("if_icmple ", -2, endLN='')
if $op.type == ExpParser.GE  : emit("if_icmplt ", -2, endLN='')
if $op.type == ExpParser.LT  : emit("if_icmpge ", -2, endLN='')
if $op.type == ExpParser.EQ  : emit("if_icmpne ", -2, endLN='')
if $op.type == ExpParser.LE  : emit("if_icmpgt ", -2, endLN='')
    }
    ;

expression: term ( op = (PLUS | MINUS) term
    {
if $op.type == ExpParser.PLUS  : emit('iadd', -1)
if $op.type == ExpParser.MINUS : emit('isub', -1)
    }
    )*
    ;

term: factor ( op = (TIMES | OVER | REM ) factor
    {
if $op.type == ExpParser.TIMES : emit('imul', -1)
if $op.type == ExpParser.OVER  : emit('idiv', -1)
if $op.type == ExpParser.REM   : emit('irem', -1)
    }
    )*
    ;

factor: NUMBER
    {
emit('ldc ' + $NUMBER.text, +1)
    }
    | OP_PAR expression CL_PAR
    | NAME
    {
# encontrar o index de $NAME.text e gerar o bytecode 'iload index'
if $NAME.text not in symbol_table:
    # print("fatal error", file=sys.stderr)
    print("error: variable '"+ $NAME.text+"' is not declared", file=sys.stderr)
    sys.exit(1)
else:
    index = symbol_table.index($NAME.text)
    symbol_table_use[index] += 1
    emit("iload "+ str(index), +1)
    }
    | READ_INT OP_PAR CL_PAR
    {
emit("invokestatic Runtime/readInt()I", +1)
    }
    ;