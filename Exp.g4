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

def error(line = 0, msg = "", fatal = False):

    global has_error
    has_error = True
    if line != 0: msg = "in line " + str(line) + " " + msg

    if not fatal:   print("ERROR: " + msg, file=sys.stderr)
    else: print("FATAL ERROR: inernal error", file=sys.stderr)
}



/*---------------- LEXER RULES ----------------*/

COMMENT : '#' ~('\n')*          -> skip ;
SPACE   : (' '|'\t'|'\r'|'\n')+  -> skip ;

PLUS    : '+' ;
TIMES   : '*' ;
MINUS   : '-' ;
OVER    : '/' ;
REM     : '%' ;
ATTRIB  : '=' ;
COMMA   : ',' ;
OP_PAR  : '(' ;
CL_PAR  : ')' ;
OP_CUR  : '{' ;
CL_CUR  : '}' ;
OP_SB   : '[' ;
CL_SB   : ']' ;
EQ      : '==' ;
NE      : '!=' ;
GT      : '>'  ;
GE      : '>=' ;
LT      : '<'  ;
LE      : '<=' ;
DOT     : '.'  ;

PUSH    : 'push';
LENGTH  : 'length';

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

statement: st_print | st_if | st_while | st_break | st_continue | st_array_new | st_array_set | st_array_push | st_attrib;

st_print: PRINT OP_PAR
    {
emit('getstatic java/lang/System/out Ljava/io/PrintStream;', stack_att = +1)
    }
    e1 = expression 
    {
if $e1.type == 'i':
    emit('invokevirtual java/io/PrintStream/print(I)V\n', stack_att = -2)
elif $e1.type == 's':
    emit('invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n', stack_att = -2)
elif $e1.type == 'a':
    emit("invokevirtual Array/string()Ljava/lang/String;")
    emit("invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n", stack_att = -2)
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
elif $e1.type == 'a':
    emit("invokevirtual Array/string()Ljava/lang/String;")
    emit("invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V\n", stack_att = -2)
else:
    error(fatal = True)
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
    if my_type == "i":
        error(line = $NAME.line, msg = "'" + $NAME.text + "' must be an " + "integer")
    elif my_type == "s":
        error(line = $NAME.line, msg = "'" + $NAME.text + "' must be an " + "string")
    elif my_type == "a":
        error(line = $NAME.line, msg = "'" + $NAME.text + "' must be an " + "array")
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
    error(line = $CONTINUE.line, msg = "the 'continue' command must be in a loop escope")
    }
    ;

st_array_new: NAME ATTRIB OP_SB CL_SB
    {
# 1. testar se a varialvel name já existe:  se não existir inclui $NAME.text na symbol_table
if $NAME.text not in symbol_table:
    symbol_table.append($NAME.text)
    symbol_table_use.append(0)
    type_table.append('a')
else:
    error(line = $NAME.line, msg = "'" + $NAME.text + "' is already declared")

# 2. encontrar o índice de $NAME.text e gerar o bytecode 'istore index'
index = symbol_table.index($NAME.text)
emit("new Array", stack_att=+1)
emit("dup", stack_att=+1)
emit("invokespecial Array/<init>()V", stack_att=-1)
emit("astore "+str(index),endLN='\n\n', stack_att=-1)
    }
    ;

st_array_push: NAME DOT PUSH
    {
index = symbol_table.index($NAME.text)  
emit("aload " + str(index), stack_att=+1)
    }
    OP_PAR expression CL_PAR
    {
#emit("ldc " + str(expression.text), stack_att=+1)
emit("invokevirtual Array/push(I)V\n", stack_att=-2)

    }
    ;

st_array_set: NAME 
    { 
if $NAME.text in symbol_table:
    index = symbol_table.index($NAME.text)
    emit("aload " + str(index), stack_att = +1)
else:
    error(line = $NAME.line, msg = "'" + $NAME.text + "' is not declared")
    }
        OP_SB ex1 = expression CL_SB ATTRIB ex2 = expression
    {
if $NAME.text in symbol_table:
    my_type = type_table[index]
    if my_type == 'a':
        if $ex1.type == 'i':
            if $ex2.type == 'i':
                emit("invokevirtual Array/set(II)V\n", stack_att = -3)
            else:
                error(line = $NAME.line, msg = "arrays can store only integers and '" + $ex2.text + "' is an " + ('array' if $ex2.type == 'a' else 'string') )
        else:
            error(line = $NAME.line, msg = "array index must be integer")
    else:
        error(line = $NAME.line, msg = "only arrays can be indexable")
    }
    ;

comparison: e1 = expression op = ( EQ | NE | GT | GE | LT | LE ) e2 = expression
    {
# usa a comparação inversa para o desvio

if $e1.type == 'i' and $e2.type == 'i':
    if $op.type == ExpParser.GT  : emit("if_icmple ", stack_att=-2, endLN='')
    if $op.type == ExpParser.NE  : emit("if_icmpeq ", stack_att=-2, endLN='')
    if $op.type == ExpParser.GE  : emit("if_icmplt ", stack_att=-2, endLN='')
    if $op.type == ExpParser.LT  : emit("if_icmpge ", stack_att=-2, endLN='')
    if $op.type == ExpParser.EQ  : emit("if_icmpne ", stack_att=-2, endLN='')
    if $op.type == ExpParser.LE  : emit("if_icmpgt ", stack_att=-2, endLN='')
else:
    error(line = $op.line, msg = "cannot mix types")
    }
    ;

expression returns [type] : t1 = term ( op = (PLUS | MINUS) t2 = term
    {
if $op.type == ExpParser.PLUS  : emit('iadd', -1)
if $op.type == ExpParser.MINUS : emit('isub', -1)
if $t1.type != $t2.type:
    error(line = $op.line, msg = "cannot mix types")
elif $t1.type != 'i' or $t2.type != 'i':
    error(line = $op.line, msg = "math operations is only for integers" )
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

factor returns [type] : 
    
    NUMBER
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
    error(line = $NAME.line, msg = "variable '" + $NAME.text + "' is not declared")
else:
    index = symbol_table.index($NAME.text)
    symbol_table_use[index] += 1
    my_type = type_table[index]
    if my_type == 'i':
        emit("iload "+ str(index), +1)
        $type = my_type
    elif my_type == 's' or my_type == 'a':
        emit("aload "+ str(index), +1)
        $type = my_type
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

    | NAME 
    {
if $NAME.text in symbol_table:
    index = symbol_table.index($NAME.text)
    my_type = type_table[index]
    if my_type == 'a':
        emit("aload " + str(index), stack_att = +1)
    else:
        error(line = $NAME.line, msg = " only arrays can be indexable")
else:
    error(line = $NAME.line, msg = " '" + $NAME.text + "' is not declared" )
    }
    OP_SB expression CL_SB
    {
emit("invokevirtual Array/get(I)I", stack_att = -1)
$type = 'i'
    }

    | NAME DOT LENGTH 
    {
if $NAME.text in symbol_table:
    index = symbol_table.index($NAME.text)
    my_type = type_table[index]
    if my_type == 'a':
        emit("aload " + str(index), +1)
        emit("invokevirtual Array/length()I"    )
        $type = 'i'
    else :
        error(line = $NAME.line, msg = "'" + $NAME.text + "' is not an array")
else:
    error(line = $NAME.line, msg = " '" + $NAME.text + "' is not declared" )
$type = 'i'
    }
    ;