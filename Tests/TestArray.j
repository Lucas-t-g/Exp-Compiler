.source TestArray.src
.class  public TestArray
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static main([Ljava/lang/String;)V

    new Array                                                        ; a = []
    dup
    invokespecial Array/<init>()V
    astore 0

    aload 0                                                          ; a.push(123)
    ldc 123
    invokevirtual Array/push(I)V

    getstatic java/lang/System/out Ljava/io/PrintStream;             ; print(a.length)
    aload 0
    invokevirtual Array/length()I
    invokevirtual java/io/PrintStream/print(I)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    getstatic java/lang/System/out Ljava/io/PrintStream;             ; print(a)
    aload 0
    invokevirtual Array/string()Ljava/lang/String;
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    aload 0                                                          ; a[0] = 456
    ldc 0
    ldc 456
    invokevirtual Array/set(II)V

    getstatic java/lang/System/out Ljava/io/PrintStream;             ; print(a[0])
    aload 0
    ldc 0
    invokevirtual Array/get(I)I
    invokevirtual java/io/PrintStream/print(I)V
    
    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V

    return
    .limit stack 3
    .limit locals 1
.end method

