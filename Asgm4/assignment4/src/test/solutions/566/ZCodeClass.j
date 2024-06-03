.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static b [Z

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
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	putstatic ZCodeClass.b [Z
	return
Label1:
.limit stack 5
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [[Z from Label2 to Label3
	iconst_2
	anewarray [Z
	dup
	iconst_0
	iconst_1
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	aastore
	dup
	iconst_1
	iconst_1
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	aastore
	astore_1
	aload_1
	ldc 1.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
	aload_1
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
	getstatic ZCodeClass.b [Z
	ldc 0.0000
	f2i
	baload
	invokestatic io/writeBool(Z)V
Label3:
Label1:
	return
.limit stack 11
.limit locals 2
.end method
