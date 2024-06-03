.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a [[Ljava/lang/String;

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
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_1
	anewarray java/lang/String
	dup
	iconst_0
	ldc "v"
	aastore
	aastore
	dup
	iconst_1
	iconst_1
	anewarray java/lang/String
	dup
	iconst_0
	ldc "o"
	aastore
	aastore
	putstatic ZCodeClass.a [[Ljava/lang/String;
	return
Label1:
.limit stack 11
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is b [Ljava/lang/String; from Label2 to Label3
	iconst_1
	anewarray java/lang/String
	dup
	iconst_0
	ldc "tien"
	aastore
	astore_1
	getstatic ZCodeClass.a [[Ljava/lang/String;
	ldc 1.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	aaload
	invokestatic io/writeString(Ljava/lang/String;)V
	getstatic ZCodeClass.a [[Ljava/lang/String;
	ldc 0.0000
	f2i
	aaload
	ldc 0.0000
	f2i
	aaload
	invokestatic io/writeString(Ljava/lang/String;)V
	aload_1
	ldc 0.0000
	f2i
	aaload
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 5
.limit locals 2
.end method
