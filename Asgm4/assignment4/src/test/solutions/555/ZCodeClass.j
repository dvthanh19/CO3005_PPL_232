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
.var 1 is a [Z from Label2 to Label3
	iconst_2
	newarray boolean
	astore_1
.var 2 is b [[Z from Label2 to Label3
	iconst_2
	iconst_2
	multianewarray [[Z 2
	astore_2
	aload_1
	ldc 1.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
	aload_2
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
	aload_1
	ldc 0.0000
	f2i
	iconst_1
	bastore
	aload_1
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
	aload_2
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	iconst_1
	bastore
	aload_2
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
.var 3 is c [Z from Label2 to Label3
	aload_2
	ldc 0.0000
	f2i
	aaload
	astore_3
	aload_3
	ldc 1.0000
	f2i
	iconst_1
	bastore
	aload_2
	ldc 0.0000
	f2i
	aaload
	ldc 1.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 4
.end method
