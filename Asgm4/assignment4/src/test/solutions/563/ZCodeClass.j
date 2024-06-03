.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a [[F

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
	iconst_2
	anewarray [F
	dup
	iconst_0
	iconst_1
	newarray float
	dup
	iconst_0
	ldc 1.0000
	fastore
	aastore
	dup
	iconst_1
	iconst_1
	newarray float
	dup
	iconst_0
	ldc 2.0000
	fastore
	aastore
	putstatic ZCodeClass.a [[F
	return
Label1:
.limit stack 11
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic ZCodeClass.a [[F
	ldc 1.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	faload
	invokestatic io/writeNumber(F)V
	getstatic ZCodeClass.a [[F
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
