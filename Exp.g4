grammar Exp;

/*---------------- PARSER INTERNALS ----------------*/

@parser::header
{
# symbol_table = []
}

/*---------------- LEXER RULES ----------------*/

COMMENT: '#' ~('\n')*          -> skip ;
SPACE : (' '|'\t'|'\r'|'\n')+  -> skip ;

PLUS  : '+' ;
TIMES : '*' ;
OP_PAR: '(' ;
CL_PAR: ')' ;
MINUS : '-';
OVER  : '/';
REM   : '%';

PRINT : 'print' ;

NUMBER: '0'..'9'+ ;


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
    }
    (statement )+
    {
print('    return')
print('.limit stack 10')
print('.end method')
# print('\n; symbol_table:', symbol_table)
    }
    ;

statement: st_print;

st_print: PRINT OP_PAR
    {
print('    getstatic java/lang/System/out Ljava/io/PrintStream;')
    }
    expression CL_PAR
    {
print('    invokevirtual java/io/PrintStream/println(I)V\n')
    }
    ;

expression: term ( op = (PLUS | MINUS) term
    {
if $op.type == ExpParser.PLUS  : print('    iadd')
if $op.type == ExpParser.MINUS : print('    isub')
    }
    )* ;

term: factor ( op = (TIMES | OVER | REM ) factor
    {
if $op.type == ExpParser.TIMES : print('    imul')
if $op.type == ExpParser.OVER  : print('    idiv')
if $op.type == ExpParser.REM   : print('    irem')
    }
    )* ;

factor: NUMBER
    {
print('    ldc ' + $NUMBER.text)
# symbol_table.append($NUMBER.text)
    } 
    | OP_PAR expression CL_PAR ;

