.source SimpleFunction.src
.class  public SimpleFunction
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static cube()V
    ; n = 4
    ldc 4
    istore 0

    ; print(n * n * n)
    getstatic java/lang/System/out Ljava/io/PrintStream;
    iload 0
    iload 0
    imul
    iload 0
    imul
    invokevirtual java/io/PrintStream/print(I)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    return
.limit locals 1
.limit stack  3
.end method

.method public static main([Ljava/lang/String;)V
    ; n = "abc"
    ldc "abc"
    astore 0

    ; cube()
    invokestatic SimpleFunction/cube()V

    ; print(n)
    
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload 0
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    return
    .limit locals 1
    .limit stack  2
.end method

