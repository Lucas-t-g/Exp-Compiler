.source Test.src
.class  public Test
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static test()V
    ldc 1
    istore 0

    return
.limit locals 1
.limit stack 1
.end method
; symbol_table: ['x']

    ldc 1
    istore 0

    return
.limit locals 1
.limit stack 1
.end method
; symbol_table: ['y']

.method public static main([Ljava/lang/String;)V

    invokestatic Test/test()V
    return
.limit stack 1
.end method

; symbol_table: []
