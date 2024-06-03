.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a [[[[F

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
	iconst_1
	anewarray [[[F
	dup
	iconst_0
	iconst_1
	anewarray [[F
	dup
	iconst_0
	iconst_1
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
	aastore
	aastore
	putstatic ZCodeClass.a [[[[F
	return
Label1:
.limit stack 28
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is b [[[F from Label2 to Label3
	getstatic ZCodeClass.a [[[[F
	ldc 0.0000
	f2i
	aaload
	astore_1
.var 2 is c [[F from Label2 to Label3
	aload_1
	ldc 0.0000
	f2i
	aaload
	astore_2
.var 3 is d [F from Label2 to Label3
	aload_2
	ldc 0.0000
	f2i
	aaload
	astore_3
	getstatic ZCodeClass.a [[[[F
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	ldc 4.0000
	fastore
	aload_3
	ldc 0.0000
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 4
.end method
