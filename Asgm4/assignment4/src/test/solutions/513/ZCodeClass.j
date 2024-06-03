.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public <init>()V
Label0:
.var 0 is this LZCodeClass; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	return
Label1:
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [F from Label2 to Label3
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 1.0000
	fastore
	dup
	iconst_1
	ldc 2.0000
	fastore
	dup
	iconst_2
	ldc 3.0000
	fastore
	astore_1
	aload_1
	ldc 0.0000
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_1
	ldc 1.0000
	f2i
	faload
	invokestatic io/writeNumber(F)V
	aload_1
	ldc 2.0000
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 5
.limit locals 2
.end method
