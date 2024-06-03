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
	iconst_1
	iconst_1
	iand
	invokestatic io/writeBool(Z)V
	iconst_1
	iconst_0
	iand
	invokestatic io/writeBool(Z)V
	iconst_0
	iconst_1
	iand
	invokestatic io/writeBool(Z)V
	iconst_0
	iconst_0
	iand
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
