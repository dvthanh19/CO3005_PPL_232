import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """number a
        number b <- 5
        """
        expect = str(Program([VarDecl(Id("a"), NumberType()), VarDecl(Id("b"), NumberType(), None, NumberLiteral(5.0))]))
        self.assertTrue(TestAST.test(input, expect, 301))
    def test2(self):
        input = """bool a
        bool b <- true
        bool c <- false
        """
        expect = str(Program([VarDecl(Id("a"), BoolType()), VarDecl(Id("b"), BoolType(), None, BooleanLiteral(True)), VarDecl(Id("c"), BoolType(), None, BooleanLiteral(False))]))
        self.assertTrue(TestAST.test(input, expect, 302))
    
    def test3(self):
        input = """string a
        string b <- "NTV"
        """
        expect = str(Program([VarDecl(Id("a"), StringType()), VarDecl(Id("b"), StringType(), None, StringLiteral("NTV"))]))
        self.assertTrue(TestAST.test(input, expect, 303))
        
    def test4(self):
        input = """var a <- d
        """
        expect = str(Program([VarDecl(Id("a"), None, "var", Id("d"))]))
        self.assertTrue(TestAST.test(input, expect, 304))
    
    def test5(self):
        input = """dynamic a <- d
        dynamic b
        """
        expect = str(Program([VarDecl(Id("a"), None, "dynamic", Id("d")), VarDecl(Id("b"), None, "dynamic")]))
        self.assertTrue(TestAST.test(input, expect, 305))
    
    def test6(self):
        input = """func main()
        """
        expect = str(Program([FuncDecl(Id("main"), [], None)]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test7(self):
        input = """func add(number a, number b)
            return a + b
        """
        expect = str(Program([FuncDecl(Id("add"), [VarDecl(Id("a"), NumberType()), VarDecl(Id("b"), NumberType())], Return(BinaryOp("+", Id("a"),Id("b"))))]))
        self.assertTrue(TestAST.test(input, expect, 307))
    def test8(self):
        input = """func check(bool flag, number a, number b)
            begin
                if (flag) return a
                else return b
            end
        """
        expect = str(Program([FuncDecl(Id("check"), [VarDecl(Id("flag"), BoolType()),VarDecl(Id("a"), NumberType()), VarDecl(Id("b"), NumberType())], Block([If(Id("flag"), Return(Id("a")), [], Return(Id("b")))]))]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test9(self):
        input = """func main() return 1
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 309))
    def test10(self):
        input = """func main() begin
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 310))
    def test11(self): # expression
        input = """var a <- -3 + 1 * 0 and 20 = 3
                """
        expect = str(
            Program([
                VarDecl(
                    Id("a"),
                    None,
                    "var",
                    BinaryOp("=", 
                            BinaryOp("and", 
                                    BinaryOp("+",
                                            UnaryOp("-", NumberLiteral(3.0)),
                                            BinaryOp("*",
                                                    NumberLiteral(1.0),
                                                    NumberLiteral(0.0))
                                    ),
                                    NumberLiteral(20.0)), 
                            NumberLiteral(3.0))
                )
            ])
        )
        self.assertTrue(TestAST.test(input, expect, 311))

    def test12(self): # var declaration
        input = """string name <- "trung" ... "vuong"
                """
        expect = str(
            Program([
                VarDecl(
                    Id("name"),
                    "StringType",
                    None,
                    BinaryOp("...", StringLiteral("trung"), StringLiteral("vuong"))
                )
            ])
        )
        self.assertTrue(TestAST.test(input, expect, 312))
    def test13(self):
        input = """
        func areDivisors(number num1, number num2)
                    return ((num1 % num2 = 0) or (num2 % num1 = 0))
                """
        expect = str(
            Program(
                [
                    FuncDecl(Id("areDivisors"),
                            [
                                VarDecl(Id("num1"), "NumberType"),
                                VarDecl(Id("num2"), "NumberType")
                            ], 
                            Return(
                                BinaryOp(
                                    "or",
                                    BinaryOp("=",
                                            BinaryOp("%", 
                                                    Id("num1"),
                                                    Id("num2")),
                                            NumberLiteral(0.0)
                                            
                                    ),
                                    BinaryOp("=",
                                            BinaryOp("%", 
                                                    Id("num2"), 
                                                    Id("num1")), 
                                            NumberLiteral(0.0)
                                            
                                    )
                                )
                            ))
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 313))
    def test14(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 1
                        elif (true) return 1
                        else return 1
                    elif (true) return 1
                    elif (true) return 1                        
                    else return 1
                end

        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
            , [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
            ]))]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test15(self):
        input = """
                func main()
                begin
                number i <- 5
                i <- false + 1
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("i"), NumberType(), None, NumberLiteral(5.0)), 
                                           Assign(Id("i"), BinaryOp("+", BooleanLiteral(False), NumberLiteral(1.0)))
                                           ]))]))
        self.assertTrue(TestAST.test(input, expect, 315))
    
    def test16(self):
        input = """number a[5] <- [1, 2, 3, 4, 5]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, ArrayLiteral([
            NumberLiteral(1.0),
            NumberLiteral(2.0),
            NumberLiteral(3.0),
            NumberLiteral(4.0),
            NumberLiteral(5.0)
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17(self):
        input = """
                func foo(number a[5], number n)
                    return a[0] < n
        """
        expect = str(Program([FuncDecl(Id("foo"), 
                                       [VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, None),
                                        VarDecl(Id("n"), NumberType())
                                        ],
                                        Return(BinaryOp("<", ArrayCell(Id("a"), [NumberLiteral(0.0)]), Id("n")))
                )]))
        self.assertTrue(TestAST.test(input, expect, 317))
    def test18(self):
        input = """
                func foo(number a[5], number n)
                begin
                    break
                end
        """
        expect = str(Program([FuncDecl(Id("foo"), 
                                       [VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, None),
                                        VarDecl(Id("n"), NumberType())
                                        ],
                                        Block([Break()])
                )]))
        self.assertTrue(TestAST.test(input, expect, 318))
    def test19(self):
        input = """
                func foo()
                begin
                    continue
                end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([Continue()])
                )]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test20(self):
        input = """
                func foo()
                begin
                    for i until i > 10 by 1
                        a <- i
                end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([For(Id("i"), 
                                                                BinaryOp(">", Id("i"), 
                                                                NumberLiteral(10.0)), 
                                                                NumberLiteral(1.0), 
                                                                Assign(Id("a"), Id("i")))])
                )]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test21(self):
        """testcase 205"""
        input = """
            func main()
            begin
                number a[2, 3] <- [[1, 2, 3], [4, 5, 6]]
                ## array a
                string b <- "Hello world"
                var i <- 1
                for i until i >= 10 by 1
                begin
                    printString(b)
                    if (i > 309) break
                    else continue

                end
                number e
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                    Block([
                                        VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0),NumberLiteral(5.0),NumberLiteral(6.0)])])),
                                        VarDecl(Id("b"), StringType(), None, StringLiteral("Hello world")),
                                        VarDecl(Id("i"), None, "var", NumberLiteral(1.0)),
                                        For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), 
                                                Block([
                                                    CallStmt(Id("printString"), [Id("b")]),
                                                    If(BinaryOp(">", Id("i"), NumberLiteral(309.0)), Break(), [], Continue())
                                                ])
                                        ),
                                        VarDecl(Id("e"), NumberType())
                                        ]))]))

        self.assertTrue(TestAST.test(input,expect,321))

    def test22(self):
        """testcase 221"""
        input = """
            func main()
            begin
            if ("a" ... "b" == "H") a <- 5
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                If(
                    BinaryOp("...", StringLiteral("a"),
                             BinaryOp("==", StringLiteral("b"), 
                                      StringLiteral("H"))),
                    Assign(Id("a"), NumberLiteral(5.0)), [], None
                )
            ]))
        ]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test23(self):
        input = """
            func main() begin
            if (1)
                if (2)
                    b()
                elif (3)
                    if (4)
                        c()
                    elif (5)
                        d()
                    else e()
                elif(6)
                    f()
                else g()
            elif (7) h()
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"),[],Block([
                If(NumberLiteral(1.0),
                    If(NumberLiteral(2.0),
                       CallStmt(Id("b"),[]),
                        [(NumberLiteral(3.0),If(NumberLiteral(4.0),
                                                CallStmt(Id("c"),[]),
                                                [(NumberLiteral(5.0),CallStmt(Id("d"),[]))],
                                                CallStmt(Id("e"),[])
                                                )),
                         (NumberLiteral(6.0),CallStmt(Id("f"),[]))
                         ],
                        CallStmt(Id("g"),[])
                    ),
                    [(NumberLiteral(7.0),CallStmt(Id("h"),[]))]
                )
            ]))
        ]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test24(self):
        input = """
            func inc(number a) return a + 1
                func main() begin
                var a <- 1
                inc(a)
                writeNumber(a)
                end
        """
        expect = str(Program([
            FuncDecl(Id("inc"), [VarDecl(Id("a"), NumberType())], Return(BinaryOp("+", Id("a"), NumberLiteral(1.0)))),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, "var", NumberLiteral(1.0)),
                CallStmt(Id("inc"), [Id("a")]),
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test25(self):
        input = """
            func inc(number a) return a + 1
                func main() begin
                var a <- 1
                inc(a)
                writeNumber(a)
                end
        """
        expect = str(Program([
            FuncDecl(Id("inc"), [VarDecl(Id("a"), NumberType())], Return(BinaryOp("+", Id("a"), NumberLiteral(1.0)))),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), None, "var", NumberLiteral(1.0)),
                CallStmt(Id("inc"), [Id("a")]),
                CallStmt(Id("writeNumber"), [Id("a")])
            ]))
        ]))
        self.assertTrue(TestAST.test(input,expect,325))
    
    def test26(self):
        input = """
            var x <- foo()[1,2]
        """
        expect = str(Program([
           VarDecl(Id("x"), None, "var", ArrayCell(CallExpr(Id("foo"), []), [NumberLiteral(1.0), NumberLiteral(2.0)]))
        ]))
        self.assertTrue(TestAST.test(input,expect,326))
    
    def test27(self):
        input = """
            var x <- foo(a, "vuong", 1, true)[1,2]
        """
        expect = str(Program([
           VarDecl(Id("x"), None, "var", ArrayCell(CallExpr(
                                                        Id("foo"), [Id("a"), StringLiteral("vuong"), NumberLiteral(1.0), BooleanLiteral(True)]), 
                                                        [NumberLiteral(1.0), NumberLiteral(2.0)]))
        ]))
        self.assertTrue(TestAST.test(input,expect,327))
    
    def test28(self):
        input = """
            number x <- [foo(1), foo(true), foo("vun")]
        """
        expect = str(Program([
           VarDecl(Id("x"), NumberType(), None, ArrayLiteral([
               CallExpr(Id("foo"), [NumberLiteral(1.0)]), 
               CallExpr(Id("foo"), [BooleanLiteral(True)]), 
               CallExpr(Id("foo"), [StringLiteral("vun")])]))
        ]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test29(self):
        input = """
            bool x <- "vun" == "vuong"
        """
        expect = str(Program([
           VarDecl(Id("x"), BoolType(), None, BinaryOp("==", StringLiteral("vun"), StringLiteral("vuong")))
        ]))
        self.assertTrue(TestAST.test(input,expect,329))
    
    def test30(self):
        input = """
            bool x <- "vuong" >= "vun"
        """
        expect = str(Program([
           VarDecl(Id("x"), BoolType(), None, BinaryOp(">=", StringLiteral("vuong"), StringLiteral("vun")))
        ]))
        self.assertTrue(TestAST.test(input,expect,330))
    
    def test31(self):
        input = """
            bool x <- "vuong" <= "vun"
        """
        expect = str(Program([
           VarDecl(Id("x"), BoolType(), None, BinaryOp("<=", StringLiteral("vuong"), StringLiteral("vun")))
        ]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test32(self):
        input = """
            bool x <- "vuong" > "vun"
        """
        expect = str(Program([
           VarDecl(Id("x"), BoolType(), None, BinaryOp(">", StringLiteral("vuong"), StringLiteral("vun")))
        ]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test33(self):
        input = """
            bool x <- "bia" != 333
        """
        expect = str(Program([
           VarDecl(Id("x"), BoolType(), None, BinaryOp("!=", StringLiteral("bia"), NumberLiteral(333.0)))
        ]))
        self.assertTrue(TestAST.test(input,expect,333))
    
    def test34(self):
        input = """
            func main()
            begin 
                for i until i < 10 by 1
                    print(i)
            end
        """
        expect = str(Program([
           FuncDecl(Id("main"), [], Block([
               For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), CallStmt(Id("print"), [Id("i")]))
           ]))
        ]))
        self.assertTrue(TestAST.test(input,expect,334))
    
    def test35(self):
        input = """
            func main()
            begin 
                for i until i < 10 by inc
                    print(i)
            end
        """
        expect = str(Program([
           FuncDecl(Id("main"), [], Block([
               For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)), Id("inc"), CallStmt(Id("print"), [Id("i")]))
           ]))
        ]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test36(self):
        input = """
            func concat(string a, string b)
                return a ... b
        """
        expect = str(Program([
           FuncDecl(Id("concat"), 
                    [VarDecl(Id("a"), StringType()),
                     VarDecl(Id("b"), StringType())
                     ], 
                    Return(BinaryOp("...", Id("a"), Id("b"))))
        ]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test37(self):
        input = """
            func concat(string a, string b)
                return 
        """
        expect = str(Program([
           FuncDecl(Id("concat"), 
                    [VarDecl(Id("a"), StringType()),
                     VarDecl(Id("b"), StringType())
                     ], 
                    Return())
        ]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test38(self):
        input = """
            var x <- a and b or c and d or e
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var", 
                   BinaryOp("or", 
                            BinaryOp("and", 
                                     BinaryOp("or", 
                                              BinaryOp("and", Id("a"), Id("b")), 
                                              Id("c")), 
                                     Id("d")),
                            Id("e"))
                   )
        ]))
        self.assertTrue(TestAST.test(input,expect,338))
    
    def test39(self):
        input = """
            var x <- 5 / 2 % 3 * 10 / 2
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var", 
                   BinaryOp("/", 
                            BinaryOp("*", 
                                     BinaryOp("%", 
                                              BinaryOp("/", NumberLiteral(5.0), NumberLiteral(2.0)), 
                                              NumberLiteral(3.0)), 
                                     NumberLiteral(10.0)),
                            NumberLiteral(2.0))
                   )
        ]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test40(self):
        input = """
            var x <- -5 and not b
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var", 
                   BinaryOp("and", 
                            UnaryOp("-", NumberLiteral(5.0)),
                            UnaryOp("not", Id("b"))
                            )
                   )
        ]))
        self.assertTrue(TestAST.test(input,expect,340))  
    
    def test41(self):
        input = """
            var x <- (5 - 2) * 2
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var", 
                   BinaryOp("*", 
                            BinaryOp("-", NumberLiteral(5.0), NumberLiteral(2.0)),
                            NumberLiteral(2.0)
                            )
                   )
        ]))
        self.assertTrue(TestAST.test(input,expect,341)) 

    def test42(self):
        input = """
            var x <- foo(2) * foo(3)
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var", 
                   BinaryOp("*", 
                            CallExpr(Id("foo"), [NumberLiteral(2.0)]),
                            CallExpr(Id("foo"), [NumberLiteral(3.0)])
                            )
                   )
        ]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test43(self):
        input = """
            var x <- foo(2) * foo(3)
            number x1 <- 5 - -2 * 10
            string x2 <- "vun" ... "ngyn"
            bool x3 <- true and false or not true and (b == a) and (c >= d) and (c <= d)
            dynamic x <- 5 * 10 
        """
        expect = str(Program([VarDecl(Id("x"), None, "var", 
                                      BinaryOp("*", CallExpr(Id("foo"), [NumberLiteral(2.0)]), CallExpr(Id("foo"), [NumberLiteral(3.0)]))), 
                                      VarDecl(Id("x1"), NumberType(), None, BinaryOp("-", NumberLiteral(5.0), BinaryOp("*", UnaryOp("-", NumberLiteral(2.0)), NumberLiteral(10.0)))), 
                                      VarDecl(Id("x2"), StringType(), None, BinaryOp("...", StringLiteral("vun"), StringLiteral("ngyn"))), 
                                      VarDecl(Id("x3"), BoolType(), None, BinaryOp("and", BinaryOp("and", BinaryOp("and", BinaryOp("or", BinaryOp("and", BooleanLiteral(True), BooleanLiteral(False)), UnaryOp("not", BooleanLiteral(True))), BinaryOp("==", Id("b"), Id("a"))), BinaryOp(">=", Id("c"), Id("d"))), BinaryOp("<=", Id("c"), Id("d")))),
                                    VarDecl(Id("x"), None, "dynamic", BinaryOp("*", NumberLiteral(5.0), NumberLiteral(10.0)))]))
        self.assertTrue(TestAST.test(input,expect,343))
    
    def test44(self):
        input = """
                func main() return 1
                func main1() return 1 + 1
                func main2() return 1 + 2
                func main3() return 1 + 3
                func main4() return 1 + 4
                func main5() return 1 + 5 
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Return(NumberLiteral(1.0))), 
            FuncDecl(Id("main1"), [], Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)))), 
            FuncDecl(Id("main2"), [], Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)))), 
            FuncDecl(Id("main3"), [], Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(3.0)))),
            FuncDecl(Id("main4"), [], Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(4.0)))), 
            FuncDecl(Id("main5"), [], Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(5.0))))]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test45(self):
        input = """
                func main()
                begin
                    var x <- foo(1, 2)
                    if (x > 5) return x
                    else return x + 1
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                    Block([
                        VarDecl(Id("x"), None, "var", CallExpr(Id("foo"), [NumberLiteral(1.0), NumberLiteral(2.0)])), 
                        If(BinaryOp(">", Id("x"), NumberLiteral(5.0)), Return(Id("x")), [], Return(BinaryOp("+", Id("x"), NumberLiteral(1.0))))
                        ]))]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test46(self):
        input = """
                func main()
                begin
                    a[5,2,foo(2)] <- foo1()[1,2,3,4] + foo2[1,2]
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                    Block([
                        Assign(
                            ArrayCell(Id("a"), [NumberLiteral(5.0), NumberLiteral(2.0), CallExpr(Id("foo"), [NumberLiteral(2.0)])]),
                            BinaryOp("+",
                                     ArrayCell(CallExpr(Id("foo1"), []), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0)]),
                                     ArrayCell(Id("foo2"), [NumberLiteral(1.0), NumberLiteral(2.0)])
                                     )
                            )
                        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,346))

    def test47(self):
        input = """
                func main()
                begin
                    if(1) return 1
                    if(2) return 2
                    elif(3) return 3
                    elif(4) return 4
                    else return 5
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                    Block([
                        If(NumberLiteral(1.0), Return(NumberLiteral(1.0)), [], None),
                        If(NumberLiteral(2.0), Return(NumberLiteral(2.0)), [(NumberLiteral(3.0), Return(NumberLiteral(3.0))), (NumberLiteral(4.0), Return(NumberLiteral(4.0)))], Return(NumberLiteral(5.0)))
                        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,347))

    
    def test48(self):
        input = """
        func foo(number a[5], string b)
        begin
            var i <- 0
            for i until i >= 5 by 1
            begin
            a[i] <- i * i + 5
            end
            return -1
        end
        """
        expect = str(Program([FuncDecl(Id("foo"), 
                    [VarDecl(Id("a"), ArrayType([5.0], NumberType())),
                     VarDecl(Id("b"), StringType())
                     ], 
                    Block([
                        VarDecl(Id("i"), None, "var", NumberLiteral(0.0)),
                        For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), 
                            Block([
                                Assign(ArrayCell(Id("a"), [Id("i")]),
                                       BinaryOp("+", 
                                                BinaryOp("*", Id("i"), Id("i")),
                                                NumberLiteral(5.0)
                                                ))
                                ])),
                        Return(UnaryOp("-", NumberLiteral(1.0)))
                        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,348))
    
    def test49(self):
        input = """
      func isPrime(number x)
        """
        expect = str(Program([FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType())], None)]))
        
        self.assertTrue(TestAST.test(input,expect,349))

    def test50(self):
        input = """
     func main()
        begin
            number a <- 0 
            bool flag <- true
            if (flag) a <- a + 1
            else 
                if (not flag) a <- a + 2
                else a <- a + 3
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                Block([
                    VarDecl(Id("a"), NumberType(), None, NumberLiteral(0.0)),
                    VarDecl(Id("flag"), BoolType(), None, BooleanLiteral(True)),
                    If(Id("flag"), Assign(Id("a"), BinaryOp("+", Id("a"), NumberLiteral(1.0))), [], 
                       If(UnaryOp("not", Id("flag")), Assign(Id("a"), BinaryOp("+", Id("a"), NumberLiteral(2.0))), [], 
                          Assign(Id("a"), BinaryOp("+", Id("a"), NumberLiteral(3.0))))
                       )
                ])    
                )]))
        
        self.assertTrue(TestAST.test(input,expect,350))
         
    def test51(self):
        input = """
            func add(number a, number b)
                return a + b
            func main()
            begin
                number a <- 10
                number b <- 3
                number sum <- add(a, b)
                print(sum)
            end
        """
        expect = str(Program([
            FuncDecl(Id("add"), 
                    [VarDecl(Id("a"), NumberType()),
                      VarDecl(Id("b"), NumberType())
                    ],
                    Return(BinaryOp("+", Id("a"), Id("b")))  
                      ),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("a"), NumberType(), None, NumberLiteral(10.0)),
                VarDecl(Id("b"), NumberType(), None, NumberLiteral(3.0)),
                VarDecl(Id("sum"), NumberType(), None, CallExpr(Id("add"), [Id("a"), Id("b")])),
                CallStmt(Id("print"), [Id("sum")])
            ]))]))
        
        self.assertTrue(TestAST.test(input,expect,351))

    def test52(self):
        input = """var str <- "Hello world!"
                """
        expect = str(Program([VarDecl(Id("str"), None, "var", StringLiteral("Hello world!"))]))
        
        self.assertTrue(TestAST.test(input,expect,352))

    def test53(self):
        input = """
      string a[5] <- ["nguyen", "trung", "vuong"]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([5.0], StringType()), None, ArrayLiteral([StringLiteral("nguyen"), StringLiteral("trung"), StringLiteral("vuong")]))]))
        
        self.assertTrue(TestAST.test(input,expect,353))
 
    def test54(self):
        input = """
      bool a[2,3] <- [[true, false, true], [false, true, true]]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([2.0, 3.0], BoolType()), None, ArrayLiteral(
            [ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(True)]),
             ArrayLiteral([BooleanLiteral(False), BooleanLiteral(True), BooleanLiteral(True)])
             ]
        ))]))
        
        self.assertTrue(TestAST.test(input,expect,354))
 
    def test55(self):
        input = """
      number a <- 001
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0))]))
        
        self.assertTrue(TestAST.test(input,expect,355))
 
    def test56(self):
        input = """
      number a <- 001.e1
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(10.0))]))
        
        self.assertTrue(TestAST.test(input,expect,356))
 
    def test57(self):
        input = """
      number a <- 001.e-1
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(0.1))]))
        
        self.assertTrue(TestAST.test(input,expect,357))
 
    def test58(self):
        input = """
      number a <- -001.e-1
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, UnaryOp("-", NumberLiteral(0.1)))]))
        self.assertTrue(TestAST.test(input,expect,358))
 
    def test59(self):
        input = """
       number a <- -001.12e-1
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, UnaryOp("-", NumberLiteral(0.112)))]))
        
        self.assertTrue(TestAST.test(input,expect,359))
 
    def test60(self):
        input = """
      func optional(number a)
      begin
        if (a = 1) 
        begin
            number sum <- 0
            number i <- 1
            for i until i <= 10 by 1
            begin
                sum <- sum + i
                return (sum)
            end
        end
        else 
        begin
            number product <- 1
            number i <- 1
            for i until i <= 10 by 1
                product <- product * i
            return product
        end
      end
        """
        expect = str(Program([FuncDecl(Id("optional"), [VarDecl(Id("a"), NumberType())], 
                                       Block([
                                           If(BinaryOp("=", Id("a"), NumberLiteral(1.0)), 
                                              Block([
                                                VarDecl(Id("sum"), NumberType(), None, NumberLiteral(0.0)),
                                                VarDecl(Id("i"), NumberType(), None, NumberLiteral(1.0)),
                                                For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), 
                                                    Block([
                                                        Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i"))),
                                                        Return(Id("sum"))
                                                    ]))
                                                ]),
                                                [],
                                                Block([
                                                    VarDecl(Id("product"), NumberType(), None, NumberLiteral(1.0)),
                                                    VarDecl(Id("i"), NumberType(), None, NumberLiteral(1.0)),
                                                    For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0),
                                                            Assign(Id("product"), BinaryOp("*", Id("product"), Id("i")))
                                                        ),
                                                    Return(Id("product"))
                                                ])

                                              )
                                       ]))]))
        self.assertTrue(TestAST.test(input,expect,360))
 
    def test61(self):
        input = """
      func isPrime(number x)
      begin
        if (x <= 1) return false
        number i <- 2
        for i until i < x by 1
            if (x % i = 0) return false
        return true 
      end
        """
        expect = str(Program([FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType())], Block([
            If(BinaryOp("<=", Id("x"), NumberLiteral(1.0)), Return(BooleanLiteral(False)), [], None),
            VarDecl(Id("i"), NumberType(), None, NumberLiteral(2.0)),
            For(Id("i"), BinaryOp("<", Id("i"), Id("x")), NumberLiteral(1.0), 
                If(BinaryOp("=", BinaryOp("%", Id("x"),Id("i")), NumberLiteral(0.0)), Return(BooleanLiteral(False)))
                ),
            Return(BooleanLiteral(True))
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,361))
 
    def test62(self):
        input = """
      func isEven(number x)
      begin
        if (x % 2 = 0) return true
        return false
      end
        """
        expect = str(Program([FuncDecl(Id("isEven"), [VarDecl(Id("x"), NumberType())], Block([
            If(BinaryOp("=", BinaryOp("%", Id("x"), NumberLiteral(2.0)), NumberLiteral(0.0)), Return(BooleanLiteral(True))),
            Return(BooleanLiteral(False))
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,362))
 
    def test63(self):
        input = """
      func isPalindrome(string str)
      begin
            number i <- 0
            for i until i < len(str) by 1
                if (str[i] != str[len(str) - i - 1])
                    return false
            return true
      end
        """
        expect = str(Program([FuncDecl(Id("isPalindrome"), [VarDecl(Id("str"), StringType())], Block(
            [
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(0.0)),
                For(Id("i"), BinaryOp("<", Id("i"), CallExpr(Id("len"), [Id("str")])), NumberLiteral(1.0), 
                    If(BinaryOp("!=", 
                                ArrayCell(Id("str"), [Id("i")]), 
                                ArrayCell(Id("str"), [BinaryOp("-", 
                                                               BinaryOp("-", 
                                                                        CallExpr(Id("len"), [Id("str")]), 
                                                                        Id("i")), 
                                                               NumberLiteral(1.0))
                                ])), 
                        Return(BooleanLiteral(False)))),
                Return(BooleanLiteral(True))
            ]
        ))]))
        
        self.assertTrue(TestAST.test(input,expect,363))
 
    def test64(self):
        input = """
        func main() 
        begin
            bool a <- foo((x < 5) and ("a" == "a'""))[3,2]
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("a"), BoolType(), None,
                    ArrayCell(CallExpr(Id("foo"), [BinaryOp("and", 
                                                            BinaryOp("<", Id("x"), NumberLiteral(5.0)),
                                                            BinaryOp("==", StringLiteral("a"), StringLiteral("a'\""))
                                                            )]),
                              [NumberLiteral(3.0), NumberLiteral(2.0)])
                    )
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,364))
 
    def test65(self):
        input = """
          func main() 
        begin
            bool a <- foo((x < 5) and ("a" == "a'""), 3 + 2, "vun" ... "ngyn")[3,2]
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("a"), BoolType(), None,
                    ArrayCell(CallExpr(Id("foo"), [BinaryOp("and", 
                                                            BinaryOp("<", Id("x"), NumberLiteral(5.0)),
                                                            BinaryOp("==", StringLiteral("a"), StringLiteral("a'\""))
                                                            ),
                                                    BinaryOp("+", NumberLiteral(3.0), NumberLiteral(2.0)),
                                                    BinaryOp("...", StringLiteral("vun"), StringLiteral("ngyn"))
                                                    ]),
                              [NumberLiteral(3.0), NumberLiteral(2.0)])
                    )
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,365))
 
    def test66(self):
        input = """
            func main() 
            begin 
            number a <- readNumber()
            if (1) 
                if (2) 
                    return
                else if (3) return
                    elif (4) return
                    else return 
            elif (5) 
                return
            else return
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("a"), NumberType(), None, CallExpr(Id("readNumber"), [])),
                                           If(NumberLiteral(1.0), 
                                              If(NumberLiteral(2.0), Return(), [], 
                                                 If(NumberLiteral(3.0), Return(), [(NumberLiteral(4.0), Return())], Return())),
                                            [(NumberLiteral(5.0), Return())],
                                            Return()
                                            )
            
                    ]))]))
        self.assertTrue(TestAST.test(input,expect,366))
 
    def test67(self):
        input = """
    func initArrValue() 
            return [1, [1,2], ["a","b","c"] , [1,2,3,4], [true, false]]
        """
        expect = str(Program([FuncDecl(Id("initArrValue"), [], 
                        Return(
                            ArrayLiteral([
                                NumberLiteral(1.0),
                                ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]),
                                ArrayLiteral([StringLiteral("a"), StringLiteral("b"), StringLiteral("c")]),
                                ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0)]),
                                ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])
                            ])
                        ))]))
        self.assertTrue(TestAST.test(input,expect,367))
 
    def test68(self):
        input = """
        func main()
        begin
            number x <- "str"
            string r <- 5
            bool c <- value * aPi
            var s <- 2.0*5 +6
            r <- 2.0*5 +6
            number a[5]
            number b[5, 2]
        end 
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("x"), NumberType(), None, StringLiteral("str")),
                                           VarDecl(Id("r"), StringType(), None, NumberLiteral(5.0)),
                                           VarDecl(Id("c"), BoolType(), None, BinaryOp("*", Id("value"), Id("aPi"))),
                                           VarDecl(Id("s"), None, "var", BinaryOp("+", BinaryOp("*", NumberLiteral(2.0), NumberLiteral(5.0)), NumberLiteral(6.0))),
                                           Assign(Id("r"), BinaryOp("+", BinaryOp("*", NumberLiteral(2.0), NumberLiteral(5.0)), NumberLiteral(6.0))),
                                           VarDecl(Id("a"), ArrayType([5.0], NumberType())),
                                           VarDecl(Id("b"), ArrayType([5.0, 2.0], NumberType())),
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,368))
 
    def test69(self):
        input = """
     func main()
                begin
                    number a ## This comment is not allowed in ZCode.
                    #############################
                    ############################
                    ###########################
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("a"), NumberType())
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,369))
 
    def test70(self):
        input = """
    func main()
                begin
                bool a123a_ABC
                bool _a123a_AB____1C
                end 
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("a123a_ABC"), BoolType()),
            VarDecl(Id("_a123a_AB____1C"), BoolType())
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,370))
 
    def test71(self):
        input = """
     func main()
                begin
                    begin
                        begin
                            number i <- 0
                            for i until i > 10 by 1
                            begin
                                if (i > 5) 
                                    continue
                            end
                        end
                    end
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                            Block([
                                                Block([
                                                    VarDecl(Id("i"), NumberType(), None, NumberLiteral(0.0)),
                                                    For(Id("i"), BinaryOp(">", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), 
                                                        Block([
                                                            If(BinaryOp(">", Id("i"), NumberLiteral(5.0)), Continue())
                                                        ]))
                                                ])
                                            ])
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,371))
 
    def test72(self):
        input = """
      func main()
                begin
                    bool gggg_g[2] <- [false, false]
                    bool jjjj <- not (false and gggg_g[1])
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("gggg_g"), ArrayType([2.0], BoolType()), None, ArrayLiteral([BooleanLiteral(False), BooleanLiteral(False)])),
            VarDecl(Id("jjjj"),  BoolType(), None, UnaryOp("not", BinaryOp("and", BooleanLiteral(False), ArrayCell(Id("gggg_g"), [NumberLiteral(1.0)]))))
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,372))
 
    def test73(self):
        input = """
      func calculateAverage(number num1, number num2, number num3) 
                return (num1 + num2 + num3) / 3

                func main()
                begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                var num3 <- readNumber()

                var average <- calculateAverage(num1, num2, num3)

                writeNumber(average)
                end
        """
        expect = str(Program([FuncDecl(Id("calculateAverage"), 
                                       [VarDecl(Id("num1"), NumberType(), None, None), 
                                        VarDecl(Id("num2"), NumberType(), None, None), 
                                        VarDecl(Id("num3"), NumberType(), None, None)], 
                                        Return(BinaryOp("/", BinaryOp("+", 
                                                                      BinaryOp("+", Id("num1"), Id("num2")), 
                                                                      Id("num3")), 
                                                NumberLiteral(3.0)))), 
                            FuncDecl(Id("main"), [], 
                                     Block([
                                         VarDecl(Id("num1"), None, "var", CallExpr(Id("readNumber"), [])), 
                                         VarDecl(Id("num2"), None, "var", CallExpr(Id("readNumber"), [])), 
                                         VarDecl(Id("num3"), None, "var", CallExpr(Id("readNumber"), [])), 
                                         VarDecl(Id("average"), None, "var", CallExpr(Id("calculateAverage"), [Id("num1"), Id("num2"), Id("num3")])), 
                                         CallStmt(Id("writeNumber"), [Id("average")])]))]))
        
        self.assertTrue(TestAST.test(input,expect,373))
 
    def test74(self):
        input = """
        func main()
                begin
                number a <- 0
                if (1 < 2) 
                if (2 < 3) a <- 5
                elif (3 > 2) a <- 2
                elif (3 > 3) 
                    if (a == b) a <- 5
                    else a <- 3
                else a <- 4
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([VarDecl(Id("a"), NumberType(), None, NumberLiteral(0.0)), 
                                              If(BinaryOp("<", NumberLiteral(1.0), NumberLiteral(2.0)),
                                                 If(BinaryOp("<", NumberLiteral(2.0), NumberLiteral(3.0)), 
                                                    Assign(Id("a"), NumberLiteral(5.0)),
                                                    [(BinaryOp(">", NumberLiteral(3.0), NumberLiteral(2.0)),  Assign(Id("a"), NumberLiteral(2.0))),
                                                     (BinaryOp(">", NumberLiteral(3.0), NumberLiteral(3.0)), 
                                                            If(BinaryOp("==", Id("a"), Id("b")),  Assign(Id("a"), NumberLiteral(5.0)), [],  Assign(Id("a"), NumberLiteral(3.0))))],
                                                     Assign(Id("a"), NumberLiteral(4.0))
                                                    ) 
                                              )]))]))
        self.assertTrue(TestAST.test(input,expect,374))
 
    def test75(self):
        input = """
                    func main()
                begin
                bool flag <- "'"'"*"
                foo()
                foo(a, b, 123, "str", false, 1+1 - 2)
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("flag"), BoolType(), None, StringLiteral("'\"'\"*")), CallStmt(Id("foo"), []), CallStmt(Id("foo"), [Id("a"), Id("b"), NumberLiteral(123.0), StringLiteral("str"), BooleanLiteral(False), BinaryOp("-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), NumberLiteral(2.0))])]))]))
        
        self.assertTrue(TestAST.test(input,expect,375))
 
    def test76(self):
        input = """
                   func main()
                begin
                var i <- readNumber()
                if (i = 0) writeString("car")
                elif (i = 1) writeString("air plane")
                elif (i = 2) writeString("air plane 2")
                elif (i = 3) writeString("air plane 3")
                elif (i = 4) writeString("air plane 4")
                else writeString("unknown")
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("i"), None, "var", CallExpr(Id("readNumber"), [])), 
                                           If(BinaryOp("=", Id("i"), NumberLiteral(0.0)), CallStmt(Id("writeString"), [StringLiteral("car")]), 
                                              [
                                                  (BinaryOp("=", Id("i"), NumberLiteral(1.0)), CallStmt(Id("writeString"), [StringLiteral("air plane")])),
                                                  (BinaryOp("=", Id("i"), NumberLiteral(2.0)), CallStmt(Id("writeString"), [StringLiteral("air plane 2")])),
                                                  (BinaryOp("=", Id("i"), NumberLiteral(3.0)), CallStmt(Id("writeString"), [StringLiteral("air plane 3")])),
                                                  (BinaryOp("=", Id("i"), NumberLiteral(4.0)), CallStmt(Id("writeString"), [StringLiteral("air plane 4")]))
                                              ], 
                                              CallStmt(Id("writeString"), [StringLiteral("unknown")])
                                           )]))]))
        
        self.assertTrue(TestAST.test(input,expect,376))

    def test77(self):
        input = """
            func main()
                begin
                number i <- "str" or "rts"
                i <- false + 1
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([VarDecl(Id("i"), NumberType(), None, BinaryOp("or", StringLiteral("str"), StringLiteral("rts"))), 
                                              Assign(Id("i"), BinaryOp("+", BooleanLiteral(False), NumberLiteral(1.0)))]))]))
        
        self.assertTrue(TestAST.test(input,expect,377))
 
    def test78(self):
        input = """
     ##      cmt0
        func main()
                ##   cmt1
                ## cmt2
                ##cmt3
                ## comment
        """
        expect = str(Program([FuncDecl(Id("main"), [], None)]))
        
        self.assertTrue(TestAST.test(input,expect,378))
 
    def test79(self):
        input = """
               func foo()
                    return 1

                func foo1()
                    return
                func foo2()
                    return foo1()
                func foo3()return foo

                func foo4()
                    return 1 + 2

                func main()
                    return
        """
        expect = str(Program([
            FuncDecl(Id("foo"), [], Return(NumberLiteral(1.0))), FuncDecl(Id("foo1"), [], Return()), 
            FuncDecl(Id("foo2"), [], Return(CallExpr(Id("foo1"), []))), 
            FuncDecl(Id("foo3"), [], Return(Id("foo"))), 
            FuncDecl(Id("foo4"), [], Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)))), 
            FuncDecl(Id("main"), [], Return())]))
        
        self.assertTrue(TestAST.test(input,expect,379))
 
    def test80(self):
        input = """
        func main()
                begin
                var a <- [1,2]
                dynamic b <- [2,  3]
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("a"), None, "var", ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("b"), None, "dynamic", ArrayLiteral([NumberLiteral(2.0), NumberLiteral(3.0)]))
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,380))
 
    def test81(self):
        input = """
      func main()
                begin
                var a <- [1, "str", false]
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("a"), None, "var", ArrayLiteral([NumberLiteral(1.0), StringLiteral("str"), BooleanLiteral(False)]))
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,381))
 
    def test82(self):
        input = """
        func inc(number x) return x + 1
        number a <-  inc(inc(inc(inc(inc(1e-1)))))
        """
        expect = str(Program([FuncDecl(Id("inc"), [VarDecl(Id("x"), NumberType())], Return(BinaryOp("+", Id("x"), NumberLiteral(1.0)))),
                              VarDecl(Id("a"), NumberType(), None, 
                                      CallExpr(Id("inc"), 
                                               [CallExpr(Id("inc"), 
                                                         [CallExpr(Id("inc"), 
                                                                   [CallExpr(Id("inc"), [
                                                                       CallExpr(Id("inc"), [NumberLiteral(0.1)])
                                                                   ])])])])
                                      )
                              ]))
        self.assertTrue(TestAST.test(input,expect,382))
 
    def test83(self):
        input = """
         func areDivisors(number num1, number num2)
                    return ((num1 % num2 = 0) or (num2 % num1 = 0))
                func main()
                    begin
                        var num1 <- readNumber()
                        var num2 <- readNumber()
                        if (areDivisors(num1, num2)) printString("Yes")
                        elif (a > 5) print(a)
                        elif (a < 5) print(5)
                        else printString("No")
                    end
        """
        expect = str(Program([FuncDecl(Id("areDivisors"), 
                                       [VarDecl(Id("num1"), NumberType(), None, None), 
                                        VarDecl(Id("num2"), NumberType(), None, None)
                                        ],
                                     Return(BinaryOp("or", 
                                                    BinaryOp("=", 
                                                            BinaryOp("%", Id("num1"), Id("num2")),
                                                            NumberLiteral(0.0)), 
                                                    BinaryOp("=", BinaryOp("%", Id("num2"), Id("num1")), NumberLiteral(0.0))))), 
                            FuncDecl(Id("main"), [] , 
                                     Block([
                                         VarDecl(Id("num1"),None, "var",  CallExpr(Id("readNumber"), [])),
                                         VarDecl(Id("num2"),None, "var", CallExpr(Id("readNumber"), [])),
                                         If(CallExpr(Id("areDivisors"), [Id("num1"), Id("num2")]), 
                                            CallStmt(Id("printString"), [StringLiteral("Yes")]),
                                            [(BinaryOp(">", Id("a"), NumberLiteral(5.0)), CallStmt(Id("print"), [Id("a")])),
                                             (BinaryOp("<", Id("a"), NumberLiteral(5.0)), CallStmt(Id("print"), [NumberLiteral(5.0)]))
                                             ],
                                             CallStmt(Id("printString"), [StringLiteral("No")])
                                            )
                                     ]))
        ]))
        self.assertTrue(TestAST.test(input,expect,383))
 
    def test84(self):
        input = """
    func main()
                begin
                string abc <- ""
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) printString("Yes")
                else printString(2)
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("abc"), StringType(), None, StringLiteral("")), 
                                           VarDecl(Id("num1"), None, "var", CallExpr(Id("readNumber"), [])), 
                                           VarDecl(Id("num2"), None, "var", CallExpr(Id("readNumber"), [])), 
                                           If(CallExpr(Id("areDivisors"), [Id("num1"), Id("num2")]), 
                                               CallStmt(Id("printString"), [StringLiteral("Yes")]), 
                                              [], CallStmt(Id("printString"), [NumberLiteral(2.0)])
                                              )]))]))
        
        self.assertTrue(TestAST.test(input,expect,384))
 
    def test85(self):
        input = """
      func main()
                begin
                ##int a <- 0 ## this is a comment
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([]))]))
        
        self.assertTrue(TestAST.test(input,expect,385))
 
    def test86(self):
        input = """
     func isPrime(number x)

                func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end

                func isPrime(number x)
                begin
                if (x <= 1) return false
                var i <- 2
                for i until i > x / 2 by 1
                begin
                if (x % i = 0) return false
                end
                return true
                end
        """
        expect = str(Program([FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType(), None, None)], None), 
                              FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("x"), NumberType(), None, CallExpr(Id("readNumber"), [])), 
                                           If(CallExpr(Id("isPrime"), [Id("x")]),
                                                CallStmt(Id("printString"), [StringLiteral("Yes")]),
                                                  [],
                                                CallStmt(Id("printString"), [StringLiteral("No")]))])), 
                              FuncDecl(Id("isPrime"), 
                                       [VarDecl(Id("x"), NumberType(), None, None)], 
                                       Block([
                                            If(BinaryOp("<=", Id("x"), NumberLiteral(1.0)), 
                                                Return(BooleanLiteral(False)), [], None), 
                                            VarDecl(Id("i"), None, "var", NumberLiteral(2.0)), 
                                            For(Id("i"), BinaryOp(">", Id("i"), BinaryOp("/", Id("x"), NumberLiteral(2.0))), NumberLiteral(1.0), 
                                                Block([
                                                    If(BinaryOp("=", 
                                                                 BinaryOp("%", Id("x"), Id("i")), 
                                                                NumberLiteral(0.0)), 
                                                        Return(BooleanLiteral(False)), 
                                                        [], None)])), 
                                                        Return(BooleanLiteral(True))]))]))
        
        self.assertTrue(TestAST.test(input,expect,386))
 
    def test87(self):
        input = """
      func main()
                begin
                a[3 + foo(2)] <- arr[5,6, 5,b[90,8], d[7,8,9]] + a[4,5] + 6*7/90
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                            Assign(ArrayCell(Id("a"), [BinaryOp("+", 
                                                                             NumberLiteral(3.0), 
                                                                             CallExpr(Id("foo"), [NumberLiteral(2.0)]))]), 
                                                    BinaryOp("+", 
                                                             BinaryOp("+", 
                                                                      ArrayCell(Id("arr"), [NumberLiteral(5.0), NumberLiteral(6.0), NumberLiteral(5.0), 
                                                                                            ArrayCell(Id("b"), [NumberLiteral(90.0), NumberLiteral(8.0)]), 
                                                                                            ArrayCell(Id("d"), [NumberLiteral(7.0), NumberLiteral(8.0), NumberLiteral(9.0)])]), 
                                                                    ArrayCell(Id("a"), [NumberLiteral(4.0), NumberLiteral(5.0)])), 
                                                             BinaryOp("/", 
                                                                      BinaryOp("*", NumberLiteral(6.0), NumberLiteral(7.0)), 
                                                                      NumberLiteral(90.0))))]))]))
        
        self.assertTrue(TestAST.test(input,expect,387))
 
    def test88(self):
        input = """
     func main() 
                begin
                bool a <- ((167E-5 >= 5) and (5.7e5 - 6e+67 < 90)) or "str" == "huhu" and 5 - 2
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("a"), BoolType(), None, 
                                                   BinaryOp("==", 
                                                            BinaryOp("or", 
                                                                     BinaryOp("and", 
                                                                              BinaryOp(">=", NumberLiteral(0.00167), NumberLiteral(5.0)), 
                                                                              BinaryOp("<", 
                                                                                       BinaryOp("-", NumberLiteral(570000.0), NumberLiteral(6e+67)), 
                                                                                       NumberLiteral(90.0))), 
                                                                    StringLiteral("str")), 
                                                            BinaryOp("and", 
                                                                     StringLiteral("huhu"),
                                                                    BinaryOp("-", NumberLiteral(5.0), NumberLiteral(2.0)))))]))]))
        
        self.assertTrue(TestAST.test(input,expect,388))
 
    def test89(self):
        input = """
   func main()
                begin
                number b <- ---1-2-(-3)-(4+56) ---- a[1,2,3,b[8,9],b[9,0,1]]* 9 / 10 % 100
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("b"), NumberType(), None, 
                                                   BinaryOp("-", BinaryOp("-", BinaryOp("-", BinaryOp("-", UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0)))), NumberLiteral(2.0)), UnaryOp("-", NumberLiteral(3.0))), BinaryOp("+", NumberLiteral(4.0), NumberLiteral(56.0))), BinaryOp("%", BinaryOp("/", BinaryOp("*", UnaryOp("-", UnaryOp("-", UnaryOp("-", ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), ArrayCell(Id("b"), [NumberLiteral(8.0), NumberLiteral(9.0)]), ArrayCell(Id("b"), [NumberLiteral(9.0), NumberLiteral(0.0), NumberLiteral(1.0)])])))), NumberLiteral(9.0)), NumberLiteral(10.0)), NumberLiteral(100.0))))]))]))
        
        self.assertTrue(TestAST.test(input,expect,389))
 
    def test90(self):
        input = """
     func main()
                begin
                var i <- 0
                for i until i - 10 by 1 + (9)
                    writeNumber(i)
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), 
                                           For(Id("i"), BinaryOp("-", Id("i"), NumberLiteral(10.0)), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(9.0)), 
                                               CallStmt(Id("writeNumber"), [Id("i")]))]))]))
        
        self.assertTrue(TestAST.test(input,expect,390))
 
    def test91(self):
        input = """
   func main()
                begin
                    for i until str == char by -100
                    dynamic a <- 0
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [],
                                        Block([
                                            For(Id("i"), BinaryOp("==", Id("str"), Id("char")), UnaryOp("-", NumberLiteral(100.0)), 
                                            VarDecl(Id("a"), None, "dynamic", NumberLiteral(0.0)))]))]))
        
        self.assertTrue(TestAST.test(input,expect,391))
 
    def test92(self):
        input = """
            func foo(number a[5], string b)
                begin
                var i <- 0
                for i until i >= 5 by 1
                begin
                a[i] <- i * i + 5
                end
                return -1
                end

                func main()
                begin
                foo(a[HH_h[1,2,3], uio[4,5 , 6]], "abc")
                end
        """
        expect = str(Program([
            FuncDecl(Id("foo"), [
                    VarDecl(Id("a"), ArrayType([5.0], NumberType())),
                    VarDecl(Id("b"), StringType())
                    ], 
                        Block([
                            VarDecl(Id("i"), None, "var", NumberLiteral(0.0)),
                            For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), 
                                Block([
                                    Assign(ArrayCell(Id("a"), [Id("i")]), BinaryOp("+", BinaryOp("*", Id("i"), Id("i")), NumberLiteral(5.0)))])),
                            Return(UnaryOp("-", NumberLiteral(1.0)))])), 
            FuncDecl(Id("main"), [], 
                     Block([
                            CallStmt(Id("foo"), [
                                ArrayCell(Id("a"), [ArrayCell(Id("HH_h"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), 
                                ArrayCell(Id("uio"), [NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]), 
                                StringLiteral("abc")])]))]))
        
        self.assertTrue(TestAST.test(input,expect,392))
 
    def test93(self):
        input = """
func main()
                begin
                    number u <- 1e4
                    for u until u < 0 by -1
                    begin
                        if (u % 5 = 0) writeString(u ... " is even")
                        elif ((u % 5 >= 1) and (u % 5 <= 3)) writeString(u ... " is odd")
                    end
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("u"), NumberType(), None, NumberLiteral(10000.0)), 
                                           For(Id("u"), BinaryOp("<", Id("u"), NumberLiteral(0.0)), UnaryOp("-", NumberLiteral(1.0)), 
                                               Block([
                                                   If(BinaryOp("=", BinaryOp("%", Id("u"), NumberLiteral(5.0)), NumberLiteral(0.0)),
                                                       CallStmt(Id("writeString"), [BinaryOp("...", Id("u"), StringLiteral(" is even"))]),
                                                         [(BinaryOp("and", BinaryOp(">=", BinaryOp("%", Id("u"), NumberLiteral(5.0)), NumberLiteral(1.0)), BinaryOp("<=", BinaryOp("%", Id("u"), NumberLiteral(5.0)), NumberLiteral(3.0))), CallStmt(Id("writeString"), [BinaryOp("...", Id("u"), StringLiteral(" is odd"))]))], None)]))]))]))
        
        self.assertTrue(TestAST.test(input,expect,393))
 
    def test94(self):
        input = """
dynamic a<- (("a"...s) == "as") or false and true or not (2 + 3 * sin(x) / cos(x) / (3 % 2) / -4 >= 5) or (1 >= 2)
        """
        expect = str(Program([
            VarDecl(Id("a"), None, "dynamic", BinaryOp("or", BinaryOp("or", BinaryOp("and", BinaryOp("or", BinaryOp("==", BinaryOp("...", StringLiteral("a"), Id("s")), StringLiteral("as")), BooleanLiteral(False)), BooleanLiteral(True)), UnaryOp("not", BinaryOp(">=", BinaryOp("+", NumberLiteral(2.0), BinaryOp("/", BinaryOp("/", BinaryOp("/", BinaryOp("*", NumberLiteral(3.0), CallExpr(Id("sin"), [Id("x")])), CallExpr(Id("cos"), [Id("x")])), BinaryOp("%", NumberLiteral(3.0), NumberLiteral(2.0))), UnaryOp("-", NumberLiteral(4.0)))), NumberLiteral(5.0)))), BinaryOp(">=", NumberLiteral(1.0), NumberLiteral(2.0))))]))
        
        self.assertTrue(TestAST.test(input,expect,394))
 
    def test95(self):
        input = """
  func main()
                begin
                    bool flag
                    flag <- false or not true
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("flag"), BoolType()),
            Assign(Id("flag"), BinaryOp("or", BooleanLiteral(False), UnaryOp("not", BooleanLiteral(True))))
        ]))]))
        
        self.assertTrue(TestAST.test(input,expect,395))
 
    def test96(self):
        input = """
      func main()
                begin
                bool flag <- "'"'"*"
                foo()
                foo(a, b, 123, "str", false, 1+1 - 2)
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("flag"), BoolType(), None, StringLiteral("'\"'\"*")),
                                            CallStmt(Id("foo"), []), 
                                            CallStmt(Id("foo"), [Id("a"), Id("b"), NumberLiteral(123.0), StringLiteral("str"), BooleanLiteral(False), BinaryOp("-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), NumberLiteral(2.0))])]))]))
        
        self.assertTrue(TestAST.test(input,expect,396))
 
    def test97(self):
        input = """
        func fibo(number x) 
        begin 
            if (x = 0) return 1
            if (x = 1) return 2
            return fibo(x - 1) + fibo(x - 2)
        end
        func main() 
        begin 
            writeNumber(fibo(5))
        end
        """
        expect = str(Program([FuncDecl(Id("fibo"), 
                                       [VarDecl(Id("x"), NumberType())], 
                                       Block([
                                           If(BinaryOp("=", Id("x"), NumberLiteral(0.0)), Return(NumberLiteral(1.0))), 
                                           If(BinaryOp("=", Id("x"), NumberLiteral(1.0)), Return(NumberLiteral(2.0))),
                                            Return(BinaryOp("+", 
                                                            CallExpr(Id("fibo"), [BinaryOp("-", Id("x"), NumberLiteral(1.0))]),
                                                            CallExpr(Id("fibo"), [BinaryOp("-", Id("x"), NumberLiteral(2.0))])))])), 
                            FuncDecl(Id("main"), [], Block([
                                CallStmt(Id("writeNumber"), [CallExpr(Id("fibo"), [NumberLiteral(5.0)])])]))]))
        
        self.assertTrue(TestAST.test(input,expect,397))
 
    def test98(self):
        input = """
     number arr[0, 199, 12., 12.3, 12.3e3, 12e3, 12.3e-30]
        """
        expect = str(Program([VarDecl(Id("arr"), ArrayType([0.0, 199.0, 12.0, 12.3, 12300.0, 12000.0, 1.23e-29], NumberType()))]))
        
        self.assertTrue(TestAST.test(input,expect,398))
 
    def test99(self):
        input = """
      func main ()
            begin
            begin
            begin
            begin
            begin
            begin
            end
            end
            end
            end
            end
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Block([Block([Block([Block([Block([])])])])])]))]))
        
        self.assertTrue(TestAST.test(input,expect,399))
 
    def test100(self):
        input = """
func main()
begin 
    dynamic for_ 
    var var_  <- for_ 
    if(var_) for_ <- 1
end
        """
        expect = str(Program([FuncDecl(Id("main"), [], 
                                       Block([
                                           VarDecl(Id("for_"), None, "dynamic", None),
                                            VarDecl(Id("var_"), None, "var", Id("for_")), 
                                            If(Id("var_"), Assign(Id("for_"), NumberLiteral(1.0)))]))]))
        
        self.assertTrue(TestAST.test(input,expect,400))
 
