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
.var 1 is a F from Label2 to Label3
	ldc 2.0000
	fstore_1
	fload_1
	ldc 0.0000
	fcmpl
	ifeq Label4
	iconst_0
	goto Label5
Label4:
	iconst_1
Label5:
	ifle Label6
	ldc 1.0000
	invokestatic io/writeNumber(F)V
	goto Label7
Label6:
	fload_1
	ldc 1.0000
	fcmpl
	ifeq Label8
	iconst_0
	goto Label9
Label8:
	iconst_1
Label9:
	ifle Label10
	ldc 2.0000
	invokestatic io/writeNumber(F)V
	goto Label7
Label10:
	fload_1
	ldc 2.0000
	fcmpl
	ifeq Label11
	iconst_0
	goto Label12
Label11:
	iconst_1
Label12:
	ifle Label13
	ldc 3.0000
	invokestatic io/writeNumber(F)V
	goto Label7
Label13:
Label7:
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method
