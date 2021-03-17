grammar Exp;

/*---------------- PARSER INTERNALS ----------------*/

@parser::header
{
import sys

symbol_table = []
symbol_table_use = []
}


/*---------------- LEXER RULES ----------------*/

COMMENT: '#' ~('\n')*          -> skip ;
SPACE : (' '|'\t'|'\r'|'\n')+  -> skip ;

PLUS  : '+' ;
TIMES : '*' ;
OP_PAR: '(' ;
CL_PAR: ')' ;
MINUS : '-' ;
OVER  : '/' ;
REM   : '%' ;
ATTRIB : '=' ;

PRINT : 'print' ;

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
print('.limit stack 10')
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

statement: st_print | st_attrib ;

st_print: PRINT OP_PAR
    {
print('    getstatic java/lang/System/out Ljava/io/PrintStream;')
    }
    expression CL_PAR
    {
print('    invokevirtual java/io/PrintStream/println(I)V\n')
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
print("    istore", index, '\n')
    }
    ;

expression: term ( op = (PLUS | MINUS) term
    {
if $op.type == ExpParser.PLUS  : print('    iadd')
if $op.type == ExpParser.MINUS : print('    isub')
    }
    )*
    ;

term: factor ( op = (TIMES | OVER | REM ) factor
    {
if $op.type == ExpParser.TIMES : print('    imul')
if $op.type == ExpParser.OVER  : print('    idiv')
if $op.type == ExpParser.REM   : print('    irem')
    }
    )*
    ;

factor: NUMBER
    {
print('    ldc ' + $NUMBER.text)
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
    print("    iload ", index)
    }
    ;