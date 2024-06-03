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
.var 1 is x F from Label2 to Label3
	ldc 7.0000
	fstore_1
	fload_1
	invokestatic ZCodeClass/isPrime(F)Z
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
.limit stack 1
.limit locals 2
.end method

.method public static isPrime(F)Z
.var 0 is x F from Label0 to Label1
Label0:
Label2:
	fload_0
	ldc 1.0000
	fcmpl
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	iconst_0
	ireturn
Label6:
.var 1 is i F from Label2 to Label3
	ldc 2.0000
	fstore_1
	fload_1
Label9:
	fload_1
	fload_0
	ldc 2.0000
	fdiv
	fcmpl
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label8
Label12:
	fload_0
	fload_1
	frem
	ldc 0.0000
	fcmpl
	ifeq Label14
	iconst_0
	goto Label15
Label14:
	iconst_1
Label15:
	ifle Label16
	iconst_0
	ireturn
Label16:
Label13:
Label7:
	fload_1
	ldc 1.0000
	fadd
	fstore_1
	goto Label9
Label8:
	fstore_1
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 4
.limit locals 3
.end method
