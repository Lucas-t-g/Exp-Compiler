grammar Exp;

/*---------------- PARSER INTERNALS ----------------*/

@parser::header
{
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
READ_STR: 'read_str';
IF      : 'if';
WHILE   : 'while';
BREAK   : 'break';
CONTINUE: 'continue';
ELSE    : 'else';

NUMBER  : '0'..'9'+ ;
STRING  : '"'~('"')*'"';

NAME    : 'a'..'z'+ ;


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
    }
    ;

statement: st_print | st_attrib | st_if | st_while | st_break | st_continue;

st_print: PRINT OP_PAR
    {
emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
    }
    e1 = expression 
    {
if $e1.type == 'i':
    emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
elif $e1.type == 's':
    emit('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
else:
    error(fatal = True)
    }
    ( COMMA
    {
emit('getstatic java/lang/System/out Ljava/io/PrintStream;', +1)
    }
    e2 = expression
    {
if $e2.type == 'i':
    emit('invokevirtual java/io/PrintStream/print(I)V\n', -2)
elif $e2.type == 's':
    emit('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', -2)
else:
    error(msg = "in line" + str($COMMA.line) + "The 'break' command must be in a loop escope")
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
    type_table.append($expression.type)

# 2. encontrar o índice de $NAME.text e gerar o bytecode 'istore index'
index = symbol_table.index($NAME.text)
my_type = type_table[index]
if my_type == $expression.type:
    if my_type == 'i':
        emit("istore "+ str(index) + '\n', -1)
    elif my_type == 's':
        emit("astore "+ str(index) + '\n', -1)
    else:
        error(fatal = True)
else:
    error(msg = "in line " + str($NAME.line) + " '"+$NAME.text+"' must be an " + ("integer" if my_type == 'i' else "string") )
    }

    ;

st_if: IF comparison 
    {
have_else = False
global if_counter
if_counter_local = if_counter
not_if_local = "NOT_IF_" + str(if_counter_local)
if_counter += 1
emit(not_if_local, initLN='')
    }
    OP_CUR (statement)+ CL_CUR
    (
    {
have_else = True
end_else = "END_ELSE_"+str(if_counter_local)
emit("goto "+end_else)
emit(not_if_local + ':\n' )
    }
    ELSE OP_CUR (statement)+ CL_CUR
    )?
    {
if not have_else: emit(not_if_local + ':\n' )
else            : emit(end_else + ':\n')
    }
    ;

st_while: WHILE 
    {
global while_counter
begin_while = "BEGIN_WHILE_" + str(while_counter)
end_while = "END_WHILE_" + str(while_counter)
emit(begin_while + ':')

global current_begin_while
current_begin_while.append(begin_while)

global current_end_while
current_end_while.append(end_while)

while_counter += 1
    }
    comparison
    {
emit(end_while, initLN='')
    }
    OP_CUR (statement)+ CL_CUR
    {
emit("goto "+begin_while)
emit(end_while+':\n')
current_begin_while.pop()
current_end_while.pop()
    }
    ;

st_break: BREAK
    {
global current_end_while
if len(current_end_while) > 0:
    emit("goto " + current_end_while[-1] + " ;break")
else:
    error(msg = "in line " + str($BREAK.line) + "The 'break' command must be in a loop escope")
    }
    ;

st_continue: CONTINUE
    {
global current_begin_while
if len(current_begin_while) > 0:
    emit("goto " + current_begin_while[-1] + " ;continue")
else:
    error(msg = "in line" + str($CONTINUE.line) + "the 'continue' command must be in a loop escope")
    }
    ;

comparison: e1 = expression op = ( EQ | NE | GT | GE | LT | LE ) e2 = expression
    {
# usa a comparação inversa para o desvio

if $e1.type == 'i' and $e2.type == 'i':
    if $op.type == ExpParser.GT  :emit("if_icmple ", stack_att=-2, endLN='')
    if $op.type == ExpParser.NE  : emit("if_icmpeq ", stack_att=-2, endLN='')
    if $op.type == ExpParser.GE  : emit("if_icmplt ", stack_att=-2, endLN='')
    if $op.type == ExpParser.LT  : emit("if_icmpge ", stack_att=-2, endLN='')
    if $op.type == ExpParser.EQ  : emit("if_icmpne ", stack_att=-2, endLN='')
    if $op.type == ExpParser.LE  : emit("if_icmpgt ", stack_att=-2, endLN='')
else:
    error(msg = "in line " + str($op.line) + " cannot mix types")
    }
    ;

expression returns [type] : t1 = term ( op = (PLUS | MINUS) t2 = term
    {
if $op.type == ExpParser.PLUS  : emit('iadd', -1)
if $op.type == ExpParser.MINUS : emit('isub', -1)
if $t1.type != $t2.type:
    error(msg = "in line " + str($op.line) + " cannot mix types")
    }
    )*
    {
$type = $t1.type
    }
    ;

term returns [type]: f1 = factor ( op = (TIMES | OVER | REM ) f2 = factor
    {
if $op.type == ExpParser.TIMES : emit('imul', -1)
if $op.type == ExpParser.OVER  : emit('idiv', -1)
if $op.type == ExpParser.REM   : emit('irem', -1)
if $f1.type != $f2.type:
    error(msg = "in line " + str($op.line) + " cannot mix types")
elif $f1.type != 'i' or $f2.type != 'i':
    error(msg = "in line " + str($op.line) + " math operations is only for integers" )
    }
    )*
    {
$type = $f1.type
    }
    ;

factor returns [type] : NUMBER
    {
emit('ldc ' + $NUMBER.text, +1)
$type = 'i'
    }

    | OP_PAR f1 = expression CL_PAR
    {
$type = $expression.type
    }

    | NAME
    {
# encontrar o index de $NAME.text e gerar o bytecode 'iload index'
if $NAME.text not in symbol_table:
    error(msg =  "in line " + str($NAME.line) + "variable '" + $NAME.text + "' is not declared")

else:
    index = symbol_table.index($NAME.text)
    symbol_table_use[index] += 1
    my_type = type_table[index]
    if my_type == 'i':
        emit("iload "+ str(index), +1)
        $type = 'i'
    elif my_type == 's':
        emit("aload "+ str(index), +1)
        $type = 's'
    else:
        error(fatal = True)
    }
    | READ_INT OP_PAR CL_PAR
    {
emit("invokestatic Runtime/readInt()I", +1)
$type = 'i'
    }

    | STRING
    {
emit('ldc '+ $STRING.text, +1)
$type = 's'
    }

    | READ_STR OP_PAR CL_PAR
    {
emit("invokestatic Runtime/readString()Ljava/lang/String;", +1)
$type = 's'
    }
    ;