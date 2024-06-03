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

.method public static areDivisors(FF)Z
.var 0 is num1 F from Label0 to Label1
.var 1 is num2 F from Label0 to Label1
Label0:
	fload_0
	fload_1
	frem
	ldc 0.0000
	fcmpl
	ifeq Label2
	iconst_0
	goto Label3
Label2:
	iconst_1
Label3:
	fload_1
	fload_0
	frem
	ldc 0.0000
	fcmpl
	ifeq Label4
	iconst_0
	goto Label5
Label4:
	iconst_1
Label5:
	ior
	ireturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is num1 F from Label2 to Label3
	ldc 3.0000
	fstore_1
.var 2 is num2 F from Label2 to Label3
	ldc 4.0000
	fstore_2
	fload_1
	fload_2
	invokestatic ZCodeClass/areDivisors(FF)Z
	ifle Label4
	ldc "Yes"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label5
Label4:
	ldc "No"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label5
Label5:
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method
