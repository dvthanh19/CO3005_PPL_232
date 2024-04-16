
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test0(self):
        input = """
            string DVT_testcase
        """
        expect = str(Program([
                VarDecl(Id("DVT_testcase"), StringType())
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 300))
    
    def test1(self):
        input = """
            number ppl
        """
        expect = str(Program([
                VarDecl(Id("ppl"), NumberType())
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 301))
    
    
    def test2(self):
        input = """
            string ppl <- 10
        """
        expect = str(Program([
                VarDecl(Id("ppl"), StringType(), None, NumberLiteral(10.0))
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 302))
    
    
    def test3(self):
        input = """
            string ppl
            bool ppl
            string ppl <- 1
            bool ppl <- 1
        """
        expect = str(Program([
                VarDecl(Id("ppl"), StringType()),
                VarDecl(Id("ppl"), BoolType()),
                VarDecl(Id("ppl"), StringType(), None, NumberLiteral(1.0)),
                VarDecl(Id("ppl"), BoolType(), None, NumberLiteral(1.0))
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 303))
    
    
    def test4(self):
        input = """
            string ppl[5] <- 1
            string ppl[5]
        """
        expect = str(Program([
                VarDecl(Id("ppl"), ArrayType([5.0], StringType()), None, NumberLiteral(1.0)),
                VarDecl(Id("ppl"), ArrayType([5.0], StringType()))
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 304))
        
        
    def test5(self):
        input = """
            number ppl[5,3,4.2] <- 1
            bool ppl[2,3,4]
        """
        expect = str(Program([
                VarDecl(Id("ppl"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, NumberLiteral(1.0)),
                VarDecl(Id("ppl"), ArrayType([2.0, 3.0, 4.0], BoolType()))
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 305))
        
        
    def test6(self):
        input = """
            dynamic ppl <- 1
            dynamic ppl
        """
        expect = str(Program([
                    VarDecl(Id("ppl"), None, "dynamic", NumberLiteral(1.0)),
                    VarDecl(Id("ppl"), None, "dynamic")
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 306))
        
        
    def test7(self):
        input = """
            var ppl <- 1
        """
        expect = str(Program([
                    VarDecl(Id("ppl"), None, "var", NumberLiteral(1.0))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 307))
        
        
    def test8(self):
        input = """
            func main()
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], None)
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 308))
        
        
    def test9(self):
        input = """
            func main()
                begin
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 309))


    def test10(self):
        input = """
            func main()
                begin
                break
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Break()]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 310))
         
         
    def test11(self):       
        input = """
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number ppl[1,2])
                return
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("ppl"), ArrayType([1.0, 2.0], NumberType()))], Return(None))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 311))
    
    
    def test12(self):
        input = """
            var x <- 1
            var x <- "123"
            var x <- true
            var x <- false
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  NumberLiteral(1.0)),
                    VarDecl(Id("x"), None, "var",  StringLiteral("123")),
                    VarDecl(Id("x"), None, "var",  BooleanLiteral(True)),
                    VarDecl(Id("x"), None, "var",  BooleanLiteral(False))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 312))
        
        
    def test13(self):
        input = """
            var x <- [1, "a", true, false]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 313))   
        
        
    def test14(self):
        input = """
            var x <- [[1], [1]]
            var x <- [[1]]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)]), ArrayLiteral([NumberLiteral(1.0)])])),
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)])]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 314))  
        
        
    def test15(self):
        input = """
            var x <- 1 ... "2"
            var x <- 1 <= "2"
            var x <- 1 and 2 or 3
            var x <- 1 + 2 - 3
            var x <- 1 * 2 / 3 % 4
            var x <- ---1
            var x <- not not 1
            var x <- x 
            var x <- a[1,2,3]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("<=", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("or", BinaryOp("and", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("%", BinaryOp("/", BinaryOp("*", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0))),
                    VarDecl(Id("x"), None, "var",  UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0))))),
                    VarDecl(Id("x"), None, "var",  UnaryOp("not", UnaryOp("not", NumberLiteral(1.0)))),
                    VarDecl(Id("x"), None, "var",  Id("x")),
                    VarDecl(Id("x"), None, "var",  ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 315))  
        
        
    def test16(self):
        input = """
            var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(1.0)), NumberLiteral(2.0)), BinaryOp("<=", NumberLiteral(4.0), BinaryOp("+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(5.0), BinaryOp("*", Id("a"), NumberLiteral(3.0))), Id("c")), UnaryOp("-", NumberLiteral(1.0))), UnaryOp("not", UnaryOp("-", NumberLiteral(2.0)))))))
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 316))  
        
        
    def test17(self):
        input = """
            var x <- -a[1+2] ... 2
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", UnaryOp("-", ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))])), NumberLiteral(2.0)))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 317))  
        
        
    def test18(self):
        input = """
            var x <- fun()
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), []))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 318)) 
        
        
    def test19(self):
        input = """
            var x <- fun(1+1, "a")
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), StringLiteral("a")]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 319)) 
        
        
    def test20(self):
        input = """
            var x <- fun(fun())
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [CallExpr(Id("fun"), [])]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 320)) 
        
        
    def test21(self):
        input = """
            var x <- (2 ... 3) ... 4
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("...", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(4.0)))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 321)) 
    
    
    def test22(self):
        input = """
            func main()
                begin
                    continue
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue()]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 322))


    def test23(self):
        input = """
            func main()
                begin
                    continue
                    continue
                    break
                    begin
                        continue
                        continue
                        break                    
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue(),
                    Continue(),
                    Break(),
                        Block([
                        Continue(),
                        Continue(),
                        Break()])]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 323))
        
        
    def test24(self):
        input = """
            func main()
                begin
                    return  1 + 1
                    return
                end
            func main()
                return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0))),
                    Return()])),
                    FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 324))


    def test25(self):
        input = """
            func main()
                begin
                    main(a)
                    main(1,1)
                end
            func main()
                begin
                main()
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    CallStmt(Id("main"), [Id("a")]),
                    CallStmt(Id("main"), [NumberLiteral(1.0), NumberLiteral(1.0)])])),
                    FuncDecl(Id("main"), [], Block([
                    CallStmt(Id("main"), [])]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 325))
        
        
    def test26(self):
        input = """
            func main()
                begin
                    a <- 1
                    a[1] <- 2
                    a[3,2] <- 4 + 2
                end
            func main()
                begin
                a[1+1, 3] <- 1
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Assign(Id("a"), NumberLiteral(1.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(1.0)]), NumberLiteral(2.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(3.0), NumberLiteral(2.0)]), BinaryOp("+", NumberLiteral(4.0), NumberLiteral(2.0)))])),
                    FuncDecl(Id("main"), [], Block([
                    Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), NumberLiteral(3.0)]), NumberLiteral(1.0))]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 326))
        
        
    def test27(self):
        input = """
            func main()
                begin
                    for i until i > 2 by 1 + 1
                        print(1)
                end
            func main()
                begin
                    for i until i by [1]
                    begin
                        print(1)
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), BinaryOp(">", Id("i"), NumberLiteral(2.0)), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), CallStmt(Id("print"), [NumberLiteral(1.0)]))])),
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), Id("i"), ArrayLiteral([NumberLiteral(1.0)]), Block([
                    CallStmt(Id("print"), [NumberLiteral(1.0)])]))]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 327))
        
        
    def test28(self):
        input = """
            func main()
                begin
                    if (true) return 1
                end
            func main()
                begin
                    if (true) return 2
                    else return 3
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [] , None)])),
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(2.0)), [] ,Return(NumberLiteral(3.0)))]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 328))
        

    def test29(self):
        input = """
            func main()
                begin
                    if (true) return 1
                    elif (true) return 1
                    elif (true) return 1
                    else return 1
                end

        """
        expect =str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1.0)), 
                       [(BooleanLiteral(True),Return(NumberLiteral(1.0))),
                        (BooleanLiteral(True),Return(NumberLiteral(1.0)))] 
                    ,Return(NumberLiteral(1.0)))]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 329))     
        
        
    def test30(self):
        input = """
            var c <- a[1,2]
            var c <- fun()[1,2]
            var c <- fun(1,2)[1,3]
        """
        expect = str(Program([
            VarDecl(Id("c"), None, "var", ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("fun"), []), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("fun"), [NumberLiteral(1.0), NumberLiteral(2.0)]), [NumberLiteral(1.0), NumberLiteral(3.0)]))
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 330))    
        
        
    def test31(self):
        input = """
            func main()
            begin
                var c <- 2e5
                dynamic c <- 2.56
                dynamic c
                number c[2e2, 2] <- 3.6
                string c[3.823]
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block(
                [VarDecl(Id("c"), None, "var", NumberLiteral(200000.0)), 
                 VarDecl(Id("c"), None, "dynamic", NumberLiteral(2.56)), 
                 VarDecl(Id("c"), None, "dynamic"),
                 VarDecl(Id("c"), ArrayType([200.0, 2.0], NumberType()), None, NumberLiteral(3.6)),
                 VarDecl(Id("c"), ArrayType([3.823], StringType()), None)
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 331))    
        
             
    def test32(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        else return 1
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(1.0))), [], None)
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 332))     
        
        
    def test33(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        else return 1
                    else return 1
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(1.0))), 
               [], Return(NumberLiteral(1.0)))
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 333))   
        
        
    def test34(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 1
                        else return 1
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0))), [], None)
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 334))   
        
        
    def test35(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 1
                        elif (true) return 1
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))]), [], None)
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 335))
        
    
    def test36(self):
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
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
            , [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 336))   
        

    def test37(self):
        input = """
            func main()
            begin
                if (true) return 1
                elif (false) return 2  
                else return 3
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), Return(NumberLiteral(1.0)), 
               [(BooleanLiteral(False),Return(NumberLiteral(2.0)))], 
               Return(NumberLiteral(3.0))
               )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 337))
    
    
    def test38(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (false) return 1.2
                    else return 1.3
                elif (false) return 2  
                else return 3
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(False), Return(NumberLiteral(1.2)))],
                    Return(NumberLiteral(1.3))), 
               [(BooleanLiteral(False), Return(NumberLiteral(2.0)))], 
               Return(NumberLiteral(3.0))
               )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 338))
        
    
    def test39(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (false) return 1.2
                    elif (false) return 1.3
                else return 1.4
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(False), Return(NumberLiteral(1.2))), (BooleanLiteral(False), Return(NumberLiteral(1.3)))], 
                    Return(NumberLiteral(1.4)))
                )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 339))
    
    
    def test40(self):
        input = """
            func main()
                begin
                    if (1)
                        b()
                    elif (2)
                        if (3)
                            c()
                        elif (4)
                            d()
                        else
                            e()
                end

        """

        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(NumberLiteral(1.0), CallStmt(Id("b"), []), 
               [[NumberLiteral(2.0), If(NumberLiteral(3.0), CallStmt(Id("c"), []), [[NumberLiteral(4.0), CallStmt(Id("d"), [])]], CallStmt(Id("e"), []))]], None)
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 340))
    
    
    def test41(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (false) return 1.2
                    elif (false) return 1.3
                    else return 1.4
                else return 2
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(False), Return(NumberLiteral(1.2))), (BooleanLiteral(False), Return(NumberLiteral(1.3)))], 
                    Return(NumberLiteral(1.4))),
                [],
                Return(NumberLiteral(2.0))
                )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 341))
    
    
    def test42(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (false) return 1.2
                    elif (false) return 1.3
                    else return 1.4
                elif (true) return 2
                elif (false) return 3
                else return 4
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(False), Return(NumberLiteral(1.2))), (BooleanLiteral(False), Return(NumberLiteral(1.3)))], 
                    Return(NumberLiteral(1.4))),
                [(BooleanLiteral(True), Return(NumberLiteral(2.0))), (BooleanLiteral(False), Return(NumberLiteral(3.0)))],
                Return(NumberLiteral(4.0))
                )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 342))
    
    
    def test43(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (true) 
                        if (true) return 1.21
                        elif (true) return 1.22
                        else return 1.23
                    elif (true) return 1.3
                    else return 1.4
                elif (true) return 2
                elif (true) return 3
                else return 4
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(True), 
                        If(BooleanLiteral(True), Return(NumberLiteral(1.21)), 
                        [(BooleanLiteral(True), Return(NumberLiteral(1.22)))],
                        Return(NumberLiteral(1.23)))), 
                    (BooleanLiteral(True), Return(NumberLiteral(1.3)))], 
                    Return(NumberLiteral(1.4))),
                [(BooleanLiteral(True), Return(NumberLiteral(2.0))), (BooleanLiteral(True), Return(NumberLiteral(3.0)))],
                Return(NumberLiteral(4.0))
                )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 343))
    
    
    def test44(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (true) 
                        if (true) return 1.21
                        elif (true) return 1.22
                        else return 1.23
                    elif (true) return 1.3
                    else return 1.4
                elif (true) return 2
                elif (true) return 3
                else 
                    if (true) return 4.1
                    elif (true) return 4.2
                    elif (true) return 4.3
                    else return 4.4
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(True), 
                        If(BooleanLiteral(True), Return(NumberLiteral(1.21)), 
                        [(BooleanLiteral(True), Return(NumberLiteral(1.22)))],
                        Return(NumberLiteral(1.23)))), 
                    (BooleanLiteral(True), Return(NumberLiteral(1.3)))], 
                    Return(NumberLiteral(1.4))),
                [(BooleanLiteral(True), Return(NumberLiteral(2.0))), (BooleanLiteral(True), Return(NumberLiteral(3.0)))],
                If(BooleanLiteral(True), Return(NumberLiteral(4.1)), 
                    [(BooleanLiteral(True), Return(NumberLiteral(4.2))), (BooleanLiteral(True), Return(NumberLiteral(4.3)))],
                    Return(NumberLiteral(4.4)))
                )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 344))
    
    
    def test45(self):
        input = """
            func main(number a, string a, bool a[2])
            func main(number arr[1,2])
                return 
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("arr"), ArrayType([1.0, 2.0], NumberType()))], Return(None))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 345))
    
    
    def test46(self):
        input = """
            func foo(number a, string a, bool a[2])
            func foo(number arr[1, 2], string arr[1, 9])
                return 
        """
        expect = str(Program([
                    FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("foo"), [VarDecl(Id("arr"), ArrayType([1.0, 2.0], NumberType())),
                                        VarDecl(Id("arr"), ArrayType([1.0, 9.0], StringType()))], Return(None))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 346))
    
    
    def test47(self):
        input = """
            func foo(number a, string a, bool a[2])
            begin
                for i until 0 by 1
                    for j until 0 by -1
                    begin
                    end
            end
            
            
            func foo(number arr[1, 2], string arr[1, 9])
                return 
        """
        expect = str(Program([
                    FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()), 
                                        VarDecl(Id("a"), StringType()), 
                                        VarDecl(Id("a"), ArrayType([2.0], BoolType()))], Block([
                                            For(Id("i"), NumberLiteral(0.0), NumberLiteral(1.0), 
                                                For(Id("j"), NumberLiteral(0.0), UnaryOp('-', NumberLiteral(1.0)), Block([]))),
                                            ])),
                    FuncDecl(Id("foo"), [VarDecl(Id("arr"), ArrayType([1.0, 2.0], NumberType())),
                                        VarDecl(Id("arr"), ArrayType([1.0, 9.0], StringType()))], Return(None))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 347))
    
    
    def test48(self):
        input = """
            var a <- foo(1 + 1, foo(100)[2, 1 + 1], foo([1, 9], [0, 9]))
        """
        expect = str(Program([
                    VarDecl(Id("a"), None, "var", CallExpr(Id("foo"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), 
                                                                       ArrayCell(CallExpr(Id("foo"), [NumberLiteral(100.0)]), [NumberLiteral(2.0), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0))]), 
                                                                       CallExpr(Id("foo"), [ArrayLiteral([NumberLiteral(1.0), NumberLiteral(9.0)]), ArrayLiteral([NumberLiteral(0.0), NumberLiteral(9.0)])])]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 348))
    
    def test49(self):
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
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 349))
    
    
    def test50(self):
        input = input = """
            func main()
            begin
            if ("p" ... "p" == "L") gpa <- 10.0
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                If(
                    BinaryOp("...", StringLiteral("p"),
                             BinaryOp("==", StringLiteral("p"), 
                                      StringLiteral("L"))),
                    Assign(Id("gpa"), NumberLiteral(10.0)), [], None
                )
            ]))
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 350))
    
    
    def test51(self):
        input = """
            func inc(number ppl) return ppl + 1
            func main()
            begin
                var ppl <- 10
                inc(ppl)
                writeNumber(ppl)
            end
        """
        expect = str(Program([
            FuncDecl(Id("inc"), [VarDecl(Id("ppl"), NumberType())], Return(BinaryOp("+", Id("ppl"), NumberLiteral(1.0)))),
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("ppl"), None, "var", NumberLiteral(10.0)),
                CallStmt(Id("inc"), [Id("ppl")]),
                CallStmt(Id("writeNumber"), [Id("ppl")])
            ]))
        ]))
        
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 351))
        
    
    def test52(self):
        input = """
            var x <- foo()[1,2]
        """
        expect = str(Program([
           VarDecl(Id("x"), None, "var", ArrayCell(CallExpr(Id("foo"), []), [NumberLiteral(1.0), NumberLiteral(2.0)]))
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 352))
        
    
    def test53(self):
        input = """
            number x <- [foo(1), foo(true), foo("ppl")]
        """
        expect = str(Program([
           VarDecl(Id("x"), NumberType(), None, ArrayLiteral([
               CallExpr(Id("foo"), [NumberLiteral(1.0)]), 
               CallExpr(Id("foo"), [BooleanLiteral(True)]), 
               CallExpr(Id("foo"), [StringLiteral("ppl")])]))
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 353))
        
    
    def test54(self):
        input = """
            bool x <- "M10" > "Cr7"
        """
        expect = str(Program([VarDecl(Id("x"), BoolType(), None, BinaryOp(">", StringLiteral("M10"), StringLiteral("Cr7")))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 354))
    
    
    def test55(self):
        input = """
            var x <- e and y or a and n or l
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var", 
                   BinaryOp("or", 
                            BinaryOp("and", 
                                     BinaryOp("or", 
                                              BinaryOp("and", Id("e"), Id("y")), 
                                              Id("a")), 
                                     Id("n")),
                            Id("l"))
                   )
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 355))
    
    
    def test56(self):
        input = """
            var fun <- -10 and not b
        """
        expect = str(Program([
                VarDecl(Id("fun"), None, "var", 
                   BinaryOp("and", 
                            UnaryOp("-", NumberLiteral(10.0)),
                            UnaryOp("not", Id("b"))
                            )
                   )
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 356))
    
    
    def test57(self):
        input = """
		number arr[2,3] <- [1,2,3,[4,5]]
		func main()
begin
	if (a<2) return true
	else return false
end
		"""
        expect = str(Program([
            VarDecl(Id("arr"), ArrayType([2.0, 3.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0)])])),
            FuncDecl(Id("main"), [], Block([
                If(BinaryOp("<", Id("a"), NumberLiteral(2.0)), Return(BooleanLiteral(True)), [], Return(BooleanLiteral(False)))
            ]))
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 357))
    
    
    def test58(self):
        input = """
        number arr[2,3] <- [1,2,3,[4,5]]
        func main()
        begin
            if (a<2) return 1
            if (a<3) return 2
            elif (b == 3) return 4
            elif (c / 3 == 1) return 5
            else return 3
        end
        """
        expect = str(Program([VarDecl(Id("arr"),ArrayType([2.0,3.0],NumberType()),None,ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),ArrayLiteral([NumberLiteral(4.0),NumberLiteral(5.0)])])),
							FuncDecl(Id("main"),[],Block([
								If(BinaryOp("<",Id("a"),NumberLiteral(2.0)),Return(NumberLiteral(1.0))),
								If(BinaryOp("<",Id("a"),NumberLiteral(3.0)),Return(NumberLiteral(2.0)),
								   [(BinaryOp("==",Id("b"),NumberLiteral(3.0)),Return(NumberLiteral(4.0))),
									(BinaryOp("==",BinaryOp("/",Id("c"),NumberLiteral(3.0)),NumberLiteral(1.0)),Return(NumberLiteral(5.0)))],
								   Return(NumberLiteral(3.0)))]))]))
		
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 358))
    
    
    def test59(self):
        input = input = """
		bool a[0] <- [[2,3],[4,5],1+2] 
		"""
        expect = str(Program(
		   [VarDecl(Id("a"),ArrayType([0.0],BoolType()),None,
					ArrayLiteral([ArrayLiteral([NumberLiteral(2.0),NumberLiteral(3.0)]),ArrayLiteral([NumberLiteral(4.0),NumberLiteral(5.0)]),BinaryOp("+",NumberLiteral(1.0),NumberLiteral(2.0))]))]
		   )
			)
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 359))
    
    
    def test60(self):
        input = """
		bool a[1,2,3] <- [[true, false, true],["true","false",true]]
		"""
        expect = str(Program(
		   [VarDecl(Id("a"),ArrayType([1.0,2.0,3.0],BoolType()),None,ArrayLiteral([ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)]),ArrayLiteral([StringLiteral("true"),StringLiteral("false"),BooleanLiteral(True)])]))]
		   )
			)
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 360))
    
    
    def test61(self):
        input = """
		func main()
					begin
						a <- main()[1+2,3] / a[2,3,4,5,6,7] + func_call(func_call[1,2])[1,2]
					end
		"""
        expect ="""Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(+, BinaryOp(/, ArrayCell(CallExpr(Id(main), []), [BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0)]), ArrayCell(Id(a), [NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), NumLit(6.0), NumLit(7.0)])), ArrayCell(CallExpr(Id(func_call), [ArrayCell(Id(func_call), [NumLit(1.0), NumLit(2.0)])]), [NumLit(1.0), NumLit(2.0)])))]))])"""
			
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 361))
    
    
    def test62(self):
        input = """
		func main()
					begin
						a[2,3] <- 2<a ... b > 2
					end
		"""
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0), NumLit(3.0)]), BinaryOp(..., BinaryOp(<, NumLit(2.0), Id(a)), BinaryOp(>, Id(b), NumLit(2.0))))]))])"""
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 362))
    
    
    def test63(self):
        input = """
		func main()
					begin
						a <- ( "hello" > 3 ) - (a <= 2) - (true == 3)
						a[3] <- hehe[1,2] + - "happy" + not true 
						var a <- [1,2,3] + - [a+1,3>2] - [[1-2%3,a > a], [true, false]]
					end 
		"""
		
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(-, BinaryOp(-, BinaryOp(>, StringLit(hello), NumLit(3.0)), BinaryOp(<=, Id(a), NumLit(2.0))), BinaryOp(==, BooleanLit(True), NumLit(3.0)))), AssignStmt(ArrayCell(Id(a), [NumLit(3.0)]), BinaryOp(+, BinaryOp(+, ArrayCell(Id(hehe), [NumLit(1.0), NumLit(2.0)]), UnaryOp(-, StringLit(happy))), UnaryOp(not, BooleanLit(True)))), VarDecl(Id(a), None, var, BinaryOp(-, BinaryOp(+, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), UnaryOp(-, ArrayLit(BinaryOp(+, Id(a), NumLit(1.0)), BinaryOp(>, NumLit(3.0), NumLit(2.0))))), ArrayLit(ArrayLit(BinaryOp(-, NumLit(1.0), BinaryOp(%, NumLit(2.0), NumLit(3.0))), BinaryOp(>, Id(a), Id(a))), ArrayLit(BooleanLit(True), BooleanLit(False)))))]))])"""
		# print(expect)
        self.assertTrue(TestAST.test(input, expect, 363))
    
    
    def test64(self):
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
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 364))
    
    
    def test65(self):
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
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 365))
    
    
    def test66(self):
        input = """
            func gcd(number a, number b)
                begin
                    return a
                end

            func main()
                begin
                    var num1 <- readNumber()
                    var num2 <- readNumber()
                    print(gcd(num1, num2))
                end
        """
        expect = str(Program([FuncDecl(Id("gcd"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Block([Return(Id("a"))])), FuncDecl(Id("main"), [], Block([VarDecl(Id("num1"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("num2"), None, "var", CallExpr(Id("readNumber"), [])), CallStmt(Id("print"), [CallExpr(Id("gcd"), [Id("num1"), Id("num2")])])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 366))
    
    
    def test67(self):
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
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 367))
    
    
    def test68(self):
        input = """
            func isPrime(number num)
                begin
                    if (num < 2) 
                        return false
                    for i until i * i > num by 1
                            if (num % i = 0) 
                                return false
                    return true
                end

            func main()
                begin
                    var x <- readNumber()
                    if (isPrime(x)) 
                        printString("Prime")
                    else printString("Not Prime")
                end
        """
        expect = str(Program([FuncDecl(Id("isPrime"), 
        [VarDecl(Id("num"), NumberType(), None, None)], 
        Block([
            If(BinaryOp("<", Id("num"), NumberLiteral(2.0)),
                Return(BooleanLiteral(False)), [], None),
                For(Id("i"),
                    BinaryOp(">", BinaryOp("*", Id("i"), Id("i")), Id("num")), NumberLiteral(1.0), 
                        If(BinaryOp("=", BinaryOp("%", Id("num"), Id("i")), NumberLiteral(0.0)), Return(BooleanLiteral(False)), [], None)), 
                        Return(BooleanLiteral(True))])), FuncDecl(Id("main"), [], 
        Block([VarDecl(Id("x"), None, "var", CallExpr(Id("readNumber"), [])), 
            If(CallExpr(Id("isPrime"), [Id("x")]), CallStmt(Id("printString"), [StringLiteral("Prime")]), [], CallStmt(Id("printString"), [StringLiteral("Not Prime")]))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 368))
    
    
    def test69(self):
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
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 369))
    
    
    def test70(self):
        input = """
        func isEven(number n)
        begin
            return n % 2 = 0
        end

        func main()
        begin
            var num <- readNumber()
            var result <- isEven(num)
            print(result)
        end
        """
        expect = str(Program([FuncDecl(Id("isEven"), [VarDecl(Id("n"), NumberType(), None, None)], Block([Return(BinaryOp("=", BinaryOp("%", Id("n"), NumberLiteral(2.0)), NumberLiteral(0.0)))])), FuncDecl(Id("main"), [], Block([VarDecl(Id("num"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("result"), None, "var", CallExpr(Id("isEven"), [Id("num")])), CallStmt(Id("print"), [Id("result")])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 370))
    
    
    def test71(self):
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
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 371))
    
    
    def test72(self):
        input = """
            func printMultiplicationTable(number n)
                begin
                    var i <- 1
                    for i until i <= 10 by 1
                        var result <- n * i
                        print(n, " * ", i, " = ", result)
                end

            func main()
                begin
                    var numberToPrint <- readNumber()
                    print("Multiplication Table for", numberToPrint)
                    printMultiplicationTable(numberToPrint)
                end
        """
        expect = str(Program([FuncDecl(Id("printMultiplicationTable"), [VarDecl(Id("n"), NumberType(), None, None)], Block([VarDecl(Id("i"), None, "var", NumberLiteral(1.0)), For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), VarDecl(Id("result"), None, "var", BinaryOp("*", Id("n"), Id("i")))), CallStmt(Id("print"), [Id("n"), StringLiteral(" * "), Id("i"), StringLiteral(" = "), Id("result")])])), FuncDecl(Id("main"), [], Block([VarDecl(Id("numberToPrint"), None, "var", CallExpr(Id("readNumber"), [])), CallStmt(Id("print"), [StringLiteral("Multiplication Table for"), Id("numberToPrint")]), CallStmt(Id("printMultiplicationTable"), [Id("numberToPrint")])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 372))
    
    
    def test73(self):
        input = """
        ## This is a comment
        func square(number x)
            ## Calculate the square of a number
            return x * x

        func cube(number x)
            ## Calculate the cube of a number
            return x * x * x

        func main()
            begin
                var value <- 4
                var squared <- square(value)
                var cubed <- cube(value)
                print("Square:", squared, " Cube:", cubed)
            end
        """
        expect = str(Program([FuncDecl(Id("square"), [VarDecl(Id("x"), NumberType(), None, None)], Return(BinaryOp("*", Id("x"), Id("x")))), FuncDecl(Id("cube"), [VarDecl(Id("x"), NumberType(), None, None)], Return(BinaryOp("*", BinaryOp("*", Id("x"), Id("x")), Id("x")))), FuncDecl(Id("main"), [], Block([VarDecl(Id("value"), None, "var", NumberLiteral(4.0)), VarDecl(Id("squared"), None, "var", CallExpr(Id("square"), [Id("value")])), VarDecl(Id("cubed"), None, "var", CallExpr(Id("cube"), [Id("value")])), CallStmt(Id("print"), [StringLiteral("Square:"), Id("squared"), StringLiteral(" Cube:"), Id("cubed")])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 373))
    
    
    def test74(self):
        input = """
                func multiply(number a, number b)
            begin
                return a * b
            end

        func calculate(number x, number y)
            begin
                var result <- multiply(x, y) + multiply(x + y, y - x)
                return result
            end
        """
        expect = str(Program([FuncDecl(Id("multiply"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Block([Return(BinaryOp("*", Id("a"), Id("b")))])), FuncDecl(Id("calculate"), [VarDecl(Id("x"), NumberType(), None, None), VarDecl(Id("y"), NumberType(), None, None)], Block([VarDecl(Id("result"), None, "var", BinaryOp("+", CallExpr(Id("multiply"), [Id("x"), Id("y")]), CallExpr(Id("multiply"), [BinaryOp("+", Id("x"), Id("y")), BinaryOp("-", Id("y"), Id("x"))]))), Return(Id("result"))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 374))
    
    
    def test75(self):
        input = """
        func calculateAverage(number arr)
            begin
                var total <- 0
                for i until len by 1
                    total <- total + arr[i]
                return total / len
            end
        func main() return calculateAverage([1, 2, 3, 4, 5])
        """
        expect = str(Program([FuncDecl(Id("calculateAverage"), [VarDecl(Id("arr"), NumberType(), None, None)], Block([VarDecl(Id("total"), None, "var", NumberLiteral(0.0)), For(Id("i"), Id("len"), NumberLiteral(1.0), Assign(Id("total"), BinaryOp("+", Id("total"), ArrayCell(Id("arr"), [Id("i")])))), Return(BinaryOp("/", Id("total"), Id("len")))])), FuncDecl(Id("main"), [], Return(CallExpr(Id("calculateAverage"), [ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0), NumberLiteral(5.0)])])))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 375))
    
    
    def test76(self):
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
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 376))
    
    
    def test77(self):
        input = """
        func main()
                begin
                    number a ## This comment is not allowed in ZCode.
                    ###### Hello
                    #### How are you
                    ## Nice to meet you
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("a"), NumberType())
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 377))
    
    
    def test78(self):
        input = """
            number a
            string b
            bool c
        """
        expect = str(Program([VarDecl(Id("a"), NumberType()), VarDecl(
            Id("b"), StringType()), VarDecl(Id("c"), BoolType())]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 378))

    
    def test79(self):
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
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 379))
    
    
    def test80(self):
        input = """
            string a <- "hello"
            number b <- 1
            bool c <- true 
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, StringLiteral("hello")), VarDecl(
            Id("b"), NumberType(), None, NumberLiteral(1.0)), VarDecl(Id("c"), BoolType(), None, BooleanLiteral(True))
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 380))

    
    def test81(self):
        input = """ 
            string a <- "hello"
            number b <- 1
            bool c <- true
            number d
            string e
            bool f
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, StringLiteral("hello")), VarDecl(
            Id("b"), NumberType(),
            None, NumberLiteral(1.0)), VarDecl(Id("c"), BoolType(), None, BooleanLiteral(True)), VarDecl(Id("d"), NumberType()),
            VarDecl(Id("e"),
                    StringType()), VarDecl(Id("f"), BoolType())]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 381))

    
    def test82(self):
        input = """
            number a[4,5]
            number b[2,3] <- [[1,2,3],[4,5,6]] 
        """
        expect = str(
            Program([VarDecl(Id("a"), ArrayType([4.0, 5.0], NumberType()), None, None), VarDecl(Id("b"), ArrayType([2.0, 3.0], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 382))

    
    def test83(self):
        input = """
            number a[1.2,3.4]<-"hello"
            bool b[1,2]
            string c[2,3]<-[[1,2,3],[4,5,6]]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([1.2, 3.4], NumberType()), None, StringLiteral("hello")), VarDecl(Id("b"), ArrayType([1.0, 2.0], BoolType())), VarDecl(Id("c"), ArrayType(
            [2.0, 3.0], StringType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 383))


    def test84(self):
        input = """
            var a <- 1
            dynamic b <- "hello"
            var c <- true 
        """
        expect = str(Program([VarDecl(Id("a"), None, "var", NumberLiteral(1.0)), VarDecl(
            Id("b"), None, "dynamic", StringLiteral("hello")), VarDecl(Id("c"), None, "var", BooleanLiteral(True))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 384))

    
    def test85(self):
        input = """ 
            dynamic b
        """
        expect = str(Program([VarDecl(Id("b"), None, "dynamic", None)]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 385))

    
    def test86(self):
        input = """
            func main() 
        """
        expect = str(Program([FuncDecl(Id("main"), [], None)]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 386))

    
    def test87(self):
        input = """ 
            func main() begin
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 387))

    
    def test88(self):
        input = """
            func main() return 0
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return(NumberLiteral(0.0)))])
                     )
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 388))

    
    def test89(self):
        input = """ 
            func main()
                begin 
                    break
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Break()]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 389))

    
    def test90(self):
        input = """ 
            func swap(number a, number b)
                begin
                    var temp <- a
                    a <- b
                    b <- temp
                end
            func main()
                begin
                    number a <- 1
                    number b <- 2
                    swap(a, b)
                    return 0
                end
        """
        expect = str(Program([FuncDecl(Id("swap"), [VarDecl(Id("a"), NumberType()), VarDecl(Id("b"), NumberType())], Block([VarDecl(Id("temp"), None, "var", Id("a")), Assign(Id("a"), Id("b")), Assign(Id("b"), Id("temp"))])), FuncDecl(
            Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)), VarDecl(Id("b"), NumberType(), None, NumberLiteral(2.0)), CallStmt(Id("swap"), [Id("a"), Id("b")]), Return(NumberLiteral(0.0))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 390))
    

    def test91(self):
        input = """
            var a <- [1,"hello",true]
        """
        expect = str(Program([VarDecl(Id("a"), None, "var", ArrayLiteral(
            [NumberLiteral(1.0), StringLiteral("hello"), BooleanLiteral(True)]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 391))


    def test92(self):
        input = """
            var x <- 1 ... "2"
            var x <- 1 <= "2"
            var x <- 1 and 2 or 3
            var x <- 1 + 2 - 3
            var x <- 1 * 2 / 3 % 4
            var x <- ---1
            var x <- not not 1
            var x <- x 
            var x <- a[1,2,3]
        """
        expect = str(
            Program([VarDecl(Id("x"), None, "var", BinaryOp("...", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp(
                        "<=", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("or", BinaryOp(
                        "and", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp(
                        "-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("%", BinaryOp(
                        "/", BinaryOp("*", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0))),
                    VarDecl(Id("x"), None, "var",  UnaryOp(
                        "-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0))))),
                    VarDecl(Id("x"), None, "var",  UnaryOp(
                        "not", UnaryOp("not", NumberLiteral(1.0)))),
                    VarDecl(Id("x"), None, "var",  Id("x")),
                    VarDecl(Id("x"), None, "var",  ArrayCell(
                        Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
                     ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 392))


    def test93(self):
        input = """
            var a <- ppl()
        """
        expect = str(
            Program([VarDecl(Id("a"), None, "var", CallExpr(Id("ppl"), []))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 393))


    def test94(self):
        input = """
            func main()
                begin
                    if (true)
                        print("Hello")
                    else
                        print("World") 
                end 
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(BooleanLiteral(True), CallStmt(
            Id("print"), [StringLiteral("Hello")]), [], CallStmt(Id("print"), [StringLiteral("World")]))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 394))

    
    def test95(self):
        input = """
            func main()
                begin
                    for i until i < 10 by i=i+1
                        print(i) 
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)),
                                                                  BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), NumberLiteral(1.0))), CallStmt(Id("print"), [Id("i")]))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 395))

    
    def test96(self):
        input = """
            func main()
                begin
                    a <- b
                    continue
                end
        """
        expect = str(Program(
            [FuncDecl(Id("main"), [], Block([Assign(Id("a"), Id("b")), Continue()]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 396))


    def test97(self):
        input = """
            func quickSort(number arr[10], number low, number high)
                begin
                    hongconho <- 1
                    return 0
                end
            func main()
                begin
                    number arr[10] <- [4, 3, 2, 1, 5, 7, 6, 8, 9, 0]
                    quickSort(arr, 0, 9)
                    print(arr)
                    return 0
                end
        """
        expect = str(Program([FuncDecl(Id("quickSort"), [VarDecl(Id("arr"), ArrayType([10.0], NumberType())), VarDecl(Id("low"), NumberType()), VarDecl(Id("high"), NumberType())], Block([Assign(Id("hongconho"), NumberLiteral(1.0)), Return(NumberLiteral(0.0))])), FuncDecl(Id("main"), [], Block([VarDecl(Id("arr"), ArrayType([10.0], NumberType()), None, ArrayLiteral(
            [NumberLiteral(4.0), NumberLiteral(3.0), NumberLiteral(2.0), NumberLiteral(1.0), NumberLiteral(5.0), NumberLiteral(7.0), NumberLiteral(6.0), NumberLiteral(8.0), NumberLiteral(9.0), NumberLiteral(0.0)])), CallStmt(Id("quickSort"), [Id("arr"), NumberLiteral(0.0), NumberLiteral(9.0)]), CallStmt(Id("print"), [Id("arr")]), Return(NumberLiteral(0.0))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 397))

    
    def test98(self):
        input = """
            func main()
                begin
                    var a <- 1
                    var b <- 2
                    var c <- 3
                    if (a < b)
                        print("a < b")
                    elif (a > b)
                        print("a > b")
                    else
                        print("a = b")
                    return 0
                end 
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "var", NumberLiteral(1.0)),
                                                             VarDecl(
                                                                 Id("b"), None, "var", NumberLiteral(2.0)),
                                                              VarDecl(
                                                                  Id("c"), None, "var", NumberLiteral(3.0)),
                                                              If(BinaryOp("<", Id("a"), Id("b")), CallStmt(Id("print"), [StringLiteral("a < b")]),
                                                                 [(BinaryOp(">", Id("a"), Id("b")), CallStmt(Id("print"), [StringLiteral("a > b")]))], CallStmt(Id("print"), [StringLiteral("a = b")])), Return(NumberLiteral(0.0))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 398))

    
    def test99(self):
        input = """ 
            func call()
                begin
                    continue
                    continue
                    break 
                    break
                    no <- yes
                    begin
                        return 0
                    end
                    for i until i < 10 by i=i+1
                        print(i)
                    return 0 
                end
            func main()
                begin
                    call() 
                end 
        """
        expect = str(Program([FuncDecl(Id("call"), [], Block([Continue(), Continue(), Break(), Break(), Assign(Id("no"), Id("yes")),
                                                              Block([Return(NumberLiteral(0.0))]), For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)),
                                                                                                       BinaryOp("=", Id("i"), BinaryOp(
                                                                                                           "+", Id("i"), NumberLiteral(1.0))),
                                                                                                       CallStmt(Id("print"), [Id("i")])), Return(NumberLiteral(0.0))])), FuncDecl(Id("main"), [], Block([CallStmt(Id("call"), [])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 399))
    
   
#     def test_400(self):
#         input = """
#         func loop(string a[1, 2, 3, 3], number _112_[0], bool cc_c)
#         begin
#             if (a > b)
#                 for a until a + 1 by b + 1 if (a > b)
#                         if (a > b) number c
#                         elif (a > b) number c
#                         elif (a > b) number c
#                         else number c
#                     else
#                         break
#             else
#                 if (a < b)
#                     if (a == b) number c
#                 else number c
#         end
# """
#         expect = str(Program([
#             FuncDecl(Id("loop"), [VarDecl(Id("a"), ArrayType([1.0, 2.0, 3.0, 3.0], StringType())), VarDecl(Id("_112_"), ArrayType([0.0], NumberType())), VarDecl(Id("cc_c"), BoolType())], Block([
#                 If(BinaryOp(">", Id("a"), Id("b")),
#                 For(Id("a"), BinaryOp("+", Id("a"), NumberLiteral(1.0)), BinaryOp("+", Id("b"), NumberLiteral(1.0)),
#                     If(BinaryOp(">", Id("a"), Id("b")),
#                         If(BinaryOp(">", Id("a"), Id("b")), VarDecl(Id("c"), NumberType()), [
#                             (BinaryOp(">", Id("a"), Id("b")), VarDecl(Id("c"), NumberType())), 
#                             (BinaryOp(">", Id("a"), Id("b")), VarDecl(Id("c"), NumberType()))
#                             ], VarDecl(Id("c"), NumberType())  
#                         ), [], Break()
#                     )
#                 ), [], If(BinaryOp("<", Id("a"), Id("b")), If(BinaryOp("==", Id("a"), Id("b")), VarDecl(Id("c"), NumberType()), [], VarDecl(Id("c"), NumberType())), [])
#             )
#         ]))]))
#         # print(expect)
#         self.assertTrue(TestAST.test(input, expect, 400))