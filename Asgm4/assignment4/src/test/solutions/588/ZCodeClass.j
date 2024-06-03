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
.var 1 is i F from Label2 to Label3
	ldc 0.0000
	fstore_1
	fload_1
Label6:
	fload_1
	ldc 3.0000
	fcmpl
	iflt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label5
Label9:
	fload_1
	invokestatic io/writeNumber(F)V
	goto Label5
Label10:
Label4:
	fload_1
	ldc 1.0000
	fadd
	fstore_1
	goto Label6
Label5:
	fstore_1
	fload_1
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 3
.end method
