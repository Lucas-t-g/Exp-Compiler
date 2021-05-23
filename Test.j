.source Test.src
.class  public Test
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static dragon(II)V
    iload 1
    ldc 0
    if_icmpne NOT_IF_0
    iload 0
    ldc 0
    if_icmpne NOT_IF_1
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    <line x1='0' y1='0' x2='500' y2='0' stroke='blue'/>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    goto END_ELSE_1
    NOT_IF_1:

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    <g transform='scale(0.7071) rotate(-45)'>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    iload 0
    ldc 1
    isub
    ldc 0
    invokestatic Test/dragon(II)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    <g transform='translate(500,0) rotate(90)'>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    iload 0
    ldc 1
    isub
    ldc 1
    invokestatic Test/dragon(II)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    </g></g>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    END_ELSE_1:

    NOT_IF_0:

    iload 1
    ldc 1
    if_icmpne NOT_IF_2
    iload 0
    ldc 0
    if_icmpne NOT_IF_3
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    <line x1='0' y1='0' x2='500' y2='0' stroke='red'/>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    goto END_ELSE_3
    NOT_IF_3:

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    <g transform='scale(0.7071) rotate(45)'>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    iload 0
    ldc 1
    isub
    ldc 0
    invokestatic Test/dragon(II)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    <g transform='translate(500,0) rotate(-90) '>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    iload 0
    ldc 1
    isub
    ldc 1
    invokestatic Test/dragon(II)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    </g></g>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    END_ELSE_3:

    NOT_IF_2:

    return
.limit locals 2
.limit stack 2
.end method
; symbol_table: ['level', 'type']

.method public static random(I)I
    ldc 8121
    iload 0
    imul
    ldc 28411
    iadd
    ldc 134456
    irem
    ireturn
    return
.limit locals 1
.limit stack 2
.end method
; symbol_table: ['last']

.method public static curve(II)V
    iload 0
    ldc 0
    if_icmpne NOT_IF_4
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    <line x1='0' y1='0' x2='500' y2='0' stroke='black'/>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    NOT_IF_4:

    iload 0
    ldc 0
    if_icmpeq NOT_IF_5
    iload 1
    invokestatic Test/random(I)I
    istore 1

    iload 1
    ldc 256
    idiv
    ldc 2
    irem
    istore 2

    iload 2
    ldc 0
    if_icmpne NOT_IF_6
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    <g transform='scale(0.7071) rotate(-45)'>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    iload 0
    ldc 1
    isub
    iload 1
    invokestatic Test/curve(II)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    <g transform='translate(500,0) rotate(90)'>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    iload 0
    ldc 1
    isub
    iload 1
    invokestatic Test/curve(II)V
    goto END_ELSE_6
    NOT_IF_6:

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    <g transform='scale(0.7071) rotate(45)'>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    iload 0
    ldc 1
    isub
    iload 1
    invokestatic Test/curve(II)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    <g transform='translate(500,0) rotate(-90) '>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    iload 0
    ldc 1
    isub
    iload 1
    invokestatic Test/curve(II)V
    END_ELSE_6:

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "    </g></g>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    NOT_IF_5:

    return
.limit locals 3
.limit stack 2
.end method
; symbol_table: ['level', 'last', 'bit']

.method public static main([Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "<?xml version='1.0' encoding='UTF-8'?>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "<svg xmlns='http://www.w3.org/2000/svg' width='1000' height='800' stroke-width='50'>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "  <g transform='translate(300,500)'>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    ldc 0
    istore 0

    ldc 8
    iload 0
    invokestatic Test/curve(II)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "  </g>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "</svg>"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    return
.limit stack 2
.limit locals 1
.end method

; symbol_table: ['seed']
