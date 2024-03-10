import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_0(self):
        input = """ 
            number x
            bool flag <- true
            string message <- "Hello, World!"
            var count <- 0
            dynamic result <- 3.14
            bool isDone <- false
            """
        expect = str(Program([VarDecl(Id("x"), NumberType(), None, None), VarDecl(Id("flag"), BoolType(), None, BooleanLiteral(True)), VarDecl(Id("message"), StringType(), None, StringLiteral("Hello, World!")), VarDecl(Id("count"), None, "var", NumberLiteral(0.0)), VarDecl(Id("result"), None, "dynamic", NumberLiteral(3.14)), VarDecl(Id("isDone"), BoolType(), None, BooleanLiteral(False))]))
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_1(self):
        input = """ 
            var NNKM <- "Khanh My"
            """
        expect = str(Program([VarDecl(Id("NNKM"), None, "var", StringLiteral("Khanh My"))]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_2(self):
        input = """dynamic a <- d
        dynamic b
        """
        expect = str(Program([VarDecl(Id("a"), None, "dynamic", Id("d")), VarDecl(Id("b"), None, "dynamic")]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_3(self):
        input = """ 
            bool invalid[1,2,3]
        """
        expect = str(Program([VarDecl(Id("invalid"), ArrayType([1.0, 2.0, 3.0], BoolType()), None, None)]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4(self):
        input = """string a
        string b <- "NNKM"
        """
        expect = str(Program([VarDecl(Id("a"), StringType()), VarDecl(Id("b"), StringType(), None, StringLiteral("NNKM"))]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5(self):
        input = """func main()
        """
        expect = str(Program([FuncDecl(Id("main"), [], None)]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_6(self):
        input = """##declaration check 
        dynamic abc <-2
        """
        expect = str(Program([VarDecl(Id("abc"), None, "dynamic", NumberLiteral(2.0))]))
        self.assertTrue(TestAST.test(input, expect, 306))
    
    def test_7(self):
        input = """func calculateCircleArea(number radius)
        return 3.14 * radius * radius
        """
        expect = str(Program([FuncDecl(Id("calculateCircleArea"), [VarDecl(Id("radius"), NumberType())], Return(BinaryOp("*", BinaryOp("*", NumberLiteral(3.14), Id("radius")), Id("radius"))))]))
        self.assertTrue(TestAST.test(input, expect, 307))
    
    def test_8(self):
        input = """func checkEvenOdd(number n)
        begin
            if (n % 2 == 0) 
                return "Even"
            else 
                return "Odd"
        end
        """
        expect = str(Program([FuncDecl(Id("checkEvenOdd"), [VarDecl(Id("n"), NumberType())], Block([If(BinaryOp("==", BinaryOp("%", Id("n"), NumberLiteral(2.0)), NumberLiteral(0.0)), Return(StringLiteral("Even")), [], Return(StringLiteral("Odd")))]))]))
        self.assertTrue(TestAST.test(input, expect, 308))
    
    def test_9(self):
        input = """func checkEvenOdd(number n)
        begin
            if (n % 2 == 0) 
                return "Even"
            else 
                return "Odd"
        end
        """
        expect = str(Program([FuncDecl(Id("checkEvenOdd"), [VarDecl(Id("n"), NumberType())], Block([If(BinaryOp("==", BinaryOp("%", Id("n"), NumberLiteral(2.0)), NumberLiteral(0.0)), Return(StringLiteral("Even")), [], Return(StringLiteral("Odd")))]))]))
        self.assertTrue(TestAST.test(input, expect, 309))
    
    def test_10(self):
        input = """func main() 
        return 42
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return(NumberLiteral(42.0)))]))
        self.assertTrue(TestAST.test(input, expect, 310))
    
    def test_11(self):
        input = """func powerOfTwo(number n) begin
        return n * n
        end
        """
        expect = str(Program([FuncDecl(Id("powerOfTwo"), [VarDecl(Id("n"), NumberType())], Block([Return(BinaryOp("*", Id("n"), Id("n")))]))]))
        self.assertTrue(TestAST.test(input, expect, 311))   

    def test_12(self):
        input = """
            number x <- [foo(1), foo(true), foo("vun")]
        """
        expect = str(Program([
           VarDecl(Id("x"), NumberType(), None, ArrayLiteral([
               CallExpr(Id("foo"), [NumberLiteral(1.0)]), 
               CallExpr(Id("foo"), [BooleanLiteral(True)]), 
               CallExpr(Id("foo"), [StringLiteral("vun")])]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 312))    

    def test_13(self):
        input = """ 
            ## Comment before function
            func main(number a) 
                begin 
                    ## Inside block
                    break 
                    ## After break
                end
            ## Comment after function
            func helper(number b)
                ## Helper function body
                begin
                    break
                end
            func anotherFunc()
            ## After another function
        """
        expect = str(Program([FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType(), None, None)], Block(["Break"])), FuncDecl(Id("helper"), [VarDecl(Id("b"), NumberType(), None, None)], Block(["Break"])), FuncDecl(Id("anotherFunc"), [], None)]))
        self.assertTrue(TestAST.test(input, expect, 313))                  

    def test_14(self):
        input = """ var name <- "Khanh" ... "My" 
        """
        expect = str(Program([VarDecl(Id("name"), None, "var", BinaryOp("...", StringLiteral("Khanh"), StringLiteral("My")))]))
        self.assertTrue(TestAST.test(input, expect, 314))
    
    def test_15(self):
        input = """ 
            var result <- true == false
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", BinaryOp("==", BooleanLiteral(True), BooleanLiteral(False)))]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16(self):
        input = """ 
            var result <- (3 > 2) and (5 <= 7)
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", BinaryOp("and", BinaryOp(">", NumberLiteral(3.0), NumberLiteral(2.0)), BinaryOp("<=", NumberLiteral(5.0), NumberLiteral(7.0))))]))
        self.assertTrue(TestAST.test(input, expect, 316))
    
    def test_17(self):
        input = """ 
            var result <- (1 + 2) * (3 and true) or (false or 4)
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", BinaryOp("or", BinaryOp("*", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), BinaryOp("and", NumberLiteral(3.0), BooleanLiteral(True))), BinaryOp("or", BooleanLiteral(False), NumberLiteral(4.0))))]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_18(self):
        input = """ 
            var invalid <- 1 + true and 2
        """
        expect = str(Program([VarDecl(Id("invalid"), None, "var", BinaryOp("and", BinaryOp("+", NumberLiteral(1.0), BooleanLiteral(True)), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_19(self):
        input = """ 
            var result <- fun()[array[1, 2]]
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", ArrayCell(CallExpr(Id("fun"), []), [ArrayCell(Id("array"), [NumberLiteral(1.0), NumberLiteral(2.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20(self):
        input = """var result <- a(array[1, 2])
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", CallExpr(Id("a"), [ArrayCell(Id("array"), [NumberLiteral(1.0), NumberLiteral(2.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21(self):
        input = """ 
            var result <- a(x, array[2])[2]
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", ArrayCell(CallExpr(Id("a"), [Id("x"), ArrayCell(Id("array"), [NumberLiteral(2.0)])]), [NumberLiteral(2.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_22(self):
        input = """ 
            var result <- a(z, k[3] ... 2)[1, 2]
        """
        expect = str(Program([VarDecl(Id("result"), None, "var", ArrayCell(CallExpr(Id("a"), [Id("z"), BinaryOp("...", ArrayCell(Id("k"), [NumberLiteral(3.0)]), NumberLiteral(2.0))]), [NumberLiteral(1.0), NumberLiteral(2.0)]))]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23(self):
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
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_24(self):
        input = """
        func main()
            begin   
                if ((1 + 2) * 3 >= 7) api <- 1
                else api <- 2
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"),[],Block([
                If(BinaryOp(">=",
                        BinaryOp("*",
                            BinaryOp("+",
                                NumberLiteral(1.0),
                                NumberLiteral(2.0)
                            ),
                            NumberLiteral(3.0)
                        ),
                        NumberLiteral(7.0)
                    ),
                    Assign(Id("api"),NumberLiteral(1.0)), 
                    [],
                    Assign(Id("api"), NumberLiteral(2.0)))
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_25(self):
        input ="""func checkNumberSign(number num)
            begin
                if (num > 0)
                    return "Positive"
                elif (num < 0)
                    return "Negative"
                else
                    return "Zero"
            end
                """
        expect =str(Program([FuncDecl(Id("checkNumberSign"), [VarDecl(Id("num"), NumberType(), None, None)], Block([
            If((BinaryOp(">", Id("num"), NumberLiteral(0.0))), 
                Return(StringLiteral("Positive")), 
                [(BinaryOp("<", Id("num"), NumberLiteral(0.0)), Return(StringLiteral("Negative")))], 
                Return(StringLiteral("Zero")))]))]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26(self):
        input = """
        func main()
            begin
            for i until i < 10 by 1
                for j until j < 5 by 1
                    break
                    continue
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), For(Id("j"), BinaryOp("<", Id("j"), NumberLiteral(5.0)), NumberLiteral(1.0), "Break")), "Continue"]))]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27(self):
        input = """
        func main()
            begin
            for i until i < 10 by 1
                if (i == 5) break
                continue
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0),
        If((BinaryOp("==", Id("i"), NumberLiteral(5.0))), Break(), [], None)), Continue()]))]))
        self.assertTrue(TestAST.test(input, expect, 327))

    
    def test_28(self):
        input = """
        func main()
            return (1 + 2) * (3 - 4) / 5
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return(BinaryOp("/", BinaryOp("*", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), BinaryOp("-", NumberLiteral(3.0), NumberLiteral(4.0))), NumberLiteral(5.0))))]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29(self):
        input = """
        func main()
            begin
                return 1 + 2
                return true or false
                return "hello"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))), Return(BinaryOp("or", BooleanLiteral(True), BooleanLiteral(False))), Return(StringLiteral("hello"))]))]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_30(self):
        input = """
        func main()
            return
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return())]))
        self.assertTrue(TestAST.test(input, expect, 330))
    

    def test_31(self):
        input = """
        func addNumbers(number a[1,2,3], number b)
            return a + b
        """
        expect = str(Program([FuncDecl(Id("addNumbers"), [VarDecl(Id("a"), ArrayType([1.0, 2.0, 3.0], NumberType()), None, None), VarDecl(Id("b"), NumberType(), None, None)], Return(BinaryOp("+", Id("a"), Id("b"))))]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_32(self):
        input = """
        func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 ... num2 % num1 = 0)
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
            end
        """
        expect = str(Program([FuncDecl(Id("areDivisors"), [VarDecl(Id("num1"), NumberType(), None, None), VarDecl(Id("num2"), NumberType(), None, None)], Return(BinaryOp("...", BinaryOp("=", BinaryOp("%", Id("num1"), Id("num2")), NumberLiteral(0.0)), BinaryOp("=", BinaryOp("%", Id("num2"), Id("num1")), NumberLiteral(0.0))))), FuncDecl(Id("main"), [], Block([VarDecl(Id("num1"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("num2"), None, "var", CallExpr(Id("readNumber"), [])), 
        If((CallExpr(Id("areDivisors"), [Id("num1"), Id("num2")])), CallStmt(Id("printString"), [StringLiteral("Yes")]), [], CallStmt(Id("printString"), [StringLiteral("No")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 332))
    
    def test_33(self):
        input = """
        func square(number x)
        func main()
            begin
            var a <- 5
            var b <- square(a)
            var c <- a + b
            print(c)
            end
        """
        expect = str(Program([FuncDecl(Id("square"), [VarDecl(Id("x"), NumberType(), None, None)], None), FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "var", NumberLiteral(5.0)), VarDecl(Id("b"), None, "var", CallExpr(Id("square"), [Id("a")])), VarDecl(Id("c"), None, "var", BinaryOp("+", Id("a"), Id("b"))), CallStmt(Id("print"), [Id("c")])]))]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_34(self):
        input = """
        func main()
            begin
                var x <- 10
                if (x > 0) 
                x <- x * 2
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), None, "var", NumberLiteral(10.0)), 
        If((BinaryOp(">", Id("x"), NumberLiteral(0.0))), Assign(Id("x"), BinaryOp("*", Id("x"), NumberLiteral(2.0))), [], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 334))
    
    def test_35(self):
        input = """
        func main()
            begin
                var a <- 3
                var b <- 5
                var result <- a + b
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "var", NumberLiteral(3.0)), VarDecl(Id("b"), None, "var", NumberLiteral(5.0)), VarDecl(Id("result"), None, "var", BinaryOp("+", Id("a"), Id("b")))]))]))
        self.assertTrue(TestAST.test(input, expect, 335))
    
    def test_36(self):
        input = """
        func main()
            begin
                var x <- 15
                if (x > 10) 
                x <- x + 5
                else x <- x - 5
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), None, "var", NumberLiteral(15.0)), 
        If((BinaryOp(">", Id("x"), NumberLiteral(10.0))), Assign(Id("x"), BinaryOp("+", Id("x"), NumberLiteral(5.0))), [], Assign(Id("x"), BinaryOp("-", Id("x"), NumberLiteral(5.0))))]))]))
        self.assertTrue(TestAST.test(input, expect, 336))
    
    def test_37(self):
        input = """
        func main()
            begin
                number arr[5]
                arr[0] <- 1
                arr[1] <- 2
                arr[2] <- 3
                arr[3] <- 4
                arr[4] <- 5
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("arr"), ArrayType([5.0], NumberType()), None, None), Assign(ArrayCell(Id("arr"), [NumberLiteral(0.0)]), NumberLiteral(1.0)), Assign(ArrayCell(Id("arr"), [NumberLiteral(1.0)]), NumberLiteral(2.0)), Assign(ArrayCell(Id("arr"), [NumberLiteral(2.0)]), NumberLiteral(3.0)), Assign(ArrayCell(Id("arr"), [NumberLiteral(3.0)]), NumberLiteral(4.0)), Assign(ArrayCell(Id("arr"), [NumberLiteral(4.0)]), NumberLiteral(5.0))]))]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_38(self):
        input = """
        func main()
            begin
                for i until i < 5 by 1
                    var x <- i * i
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), VarDecl(Id("x"), None, "var", BinaryOp("*", Id("i"), Id("i"))))]))]))
        self.assertTrue(TestAST.test(input, expect, 338))
    
    def test_39(self):
        input = """
        func main()
            begin
                for i until i < 10 by 1
                    if (i > 5) break
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), If((BinaryOp(">", Id("i"), NumberLiteral(5.0))), Break(), [], None))]))]))
        self.assertTrue(TestAST.test(input, expect, 339))
    
    def test_40(self):
        input = """
        func main()
            begin
                number arr[3]
                arr[0] <- 10
                arr[1] <- 20
                arr[2] <- 30
                var sum <- arr[0] + arr[1] + arr[2]
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("arr"), ArrayType([3.0], NumberType()), None, None), Assign(ArrayCell(Id("arr"), [NumberLiteral(0.0)]), NumberLiteral(10.0)), Assign(ArrayCell(Id("arr"), [NumberLiteral(1.0)]), NumberLiteral(20.0)), Assign(ArrayCell(Id("arr"), [NumberLiteral(2.0)]), NumberLiteral(30.0)), VarDecl(Id("sum"), None, "var", BinaryOp("+", BinaryOp("+", ArrayCell(Id("arr"), [NumberLiteral(0.0)]), ArrayCell(Id("arr"), [NumberLiteral(1.0)])), ArrayCell(Id("arr"), [NumberLiteral(2.0)])))]))]))
        self.assertTrue(TestAST.test(input, expect, 340))
    
    def test_41(self):
        input = """
        func main()
            begin
                var x <- 42
                if (x > 50)
                    var result <- "Greater than 50"
                elif (x > 30)
                    var result <- "Greater than 30"
                else var result <- "Less than or equal to 30"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), None, "var", NumberLiteral(42.0)), 
        If((BinaryOp(">", Id("x"), NumberLiteral(50.0))), VarDecl(Id("result"), None, "var", StringLiteral("Greater than 50")), [(BinaryOp(">", Id("x"), NumberLiteral(30.0)), VarDecl(Id("result"), None, "var", StringLiteral("Greater than 30")))], VarDecl(Id("result"), None, "var", StringLiteral("Less than or equal to 30")))]))]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_42(self):
        input = """
        func main()
            begin
                var x <- 42
                if (x > 50)
                    if (x > 60)
                        var result <- "Greater than 60"
                    elif (x > 55)
                        var result <- "Greater than 55"
                    else var result <- "Between 50 and 55"
                elif (x > 30)
                    var result <- "Greater than 30"
                else var result <- "Less than or equal to 30"
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), None, "var", NumberLiteral(42.0)), 
        If((BinaryOp(">", Id("x"), NumberLiteral(50.0))), 
            If((BinaryOp(">", Id("x"), NumberLiteral(60.0))), VarDecl(Id("result"), None, "var", StringLiteral("Greater than 60")), 
            [(BinaryOp(">", Id("x"), NumberLiteral(55.0)), VarDecl(Id("result"), None, "var", StringLiteral("Greater than 55")))], VarDecl(Id("result"), None, "var", StringLiteral("Between 50 and 55"))), 
        [(BinaryOp(">", Id("x"), NumberLiteral(30.0)), VarDecl(Id("result"), None, "var", StringLiteral("Greater than 30")))], VarDecl(Id("result"), None, "var", StringLiteral("Less than or equal to 30")))]))]))
        self.assertTrue(TestAST.test(input, expect, 342))
    
    def test_43(self):
        input = """
        func main()
            begin
                var x <- 10 + 5
                var y <- x * 2
                var z <- true and false or true
                if (z)
                    var result <- "True"
                else var result <- "False"
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("x"), None, "var", BinaryOp("+", NumberLiteral(10.0), NumberLiteral(5.0))),
                VarDecl(Id("y"), None, "var", BinaryOp("*", Id("x"), NumberLiteral(2.0))),
                VarDecl(Id("z"), None, "var", BinaryOp("or", BinaryOp("and", BooleanLiteral(True), BooleanLiteral(False)), BooleanLiteral(True))),
                If(Id("z"),
                   VarDecl(Id("result"),None,"var",StringLiteral("True")),
                   [], 
                   VarDecl(Id("result"),None,"var",StringLiteral("False"))
                )
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 343))
    
    def test_44(self):
        input = """
        func main()
            begin
                for i until i < 5 by 1
                    print(i)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), CallStmt(Id("print"), [Id("i")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 344))
    
    def test_45(self):
        input = """
        func main()
            begin
                number arr[5] <- [1, 2, 3, 4, 5]
                var index <- 2
                print(arr[index] + 3 * (index + 1))
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"),[],Block([
                VarDecl(Id("arr"),ArrayType([5.0],NumberType()),None,ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(4.0),NumberLiteral(5.0)])),
                VarDecl(Id("index"),None,"var",NumberLiteral(2.0)),
                CallStmt(Id("print"),
                         [BinaryOp("+",
                                   ArrayCell(Id("arr"),[Id("index")]),
                                   BinaryOp("*",
                                            NumberLiteral(3.0),
                                            BinaryOp("+",Id("index"),NumberLiteral(1.0))
                                    )
                        )]
                )
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_46(self):
        input = """
        func main()
            begin
                var x <- (1 + 2) * (3 - 4) / (5 % 6)
                print(x)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), None, "var", BinaryOp("/", BinaryOp("*", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), BinaryOp("-", NumberLiteral(3.0), NumberLiteral(4.0))), BinaryOp("%", NumberLiteral(5.0), NumberLiteral(6.0)))), CallStmt(Id("print"), [Id("x")])]))]))
        self.assertTrue(TestAST.test(input, expect, 346))
    
    def test_47(self):
        input = """
            func factorial(number n)
                begin
                    if (n <= 1) 
                        return 1
                    else return n * factorial(n - 1)
                end

            func main()
                begin
                    var x <- readNumber()
                    print(factorial(x))
                end
        """
        expect = str(Program([FuncDecl(Id("factorial"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If(BinaryOp("<=", Id("n"), NumberLiteral(1.0)), Return(NumberLiteral(1.0)), [], Return(BinaryOp("*", Id("n"), CallExpr(Id("factorial"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))]))))])), 
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("x"), None, "var", CallExpr(Id("readNumber"), [])), CallStmt(Id("print"), [CallExpr(Id("factorial"), [Id("x")])])]))]))
        self.assertTrue(TestAST.test(input, expect, 347))
    
    def test_48(self):
        input = """
            func fibonacci(number n)
                begin
                    if (n <= 1)
                        return n
                    else return fibonacci(n - 1) + fibonacci(n - 2)
                end

            func main()
                begin
                    var x <- readNumber()
                    print(fibonacci(x))
                end
        """
        expect = str(Program([FuncDecl(Id("fibonacci"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If(BinaryOp("<=", Id("n"), NumberLiteral(1.0)), Return(Id("n")), [], Return(BinaryOp("+", CallExpr(Id("fibonacci"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))]), CallExpr(Id("fibonacci"), [BinaryOp("-", Id("n"), NumberLiteral(2.0))]))))])), FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), None, "var", CallExpr(Id("readNumber"), [])), CallStmt(Id("print"), [CallExpr(Id("fibonacci"), [Id("x")])])]))]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_49(self):
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
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_50(self):
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
        self.assertTrue(TestAST.test(input, expect, 350))
    
    def test_51(self):
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
        self.assertTrue(TestAST.test(input, expect, 351))


    def test_52(self):
        input = """
            func sumArray(number arr[5])
                begin
                    var sum <- 0
                    var i <- 0
                    for i until i < 5 by 1
                        sum <- sum + arr[i]
                    return sum
                end

            func multiplyArrayBy(number arr[5], number multiplier)
                begin
                    var i <- 0
                    for i until i < 5 by 1
                        arr[i] <- arr[i] * multiplier
                end

            func main()
                begin
                    number myArray[5] <- [1, 2, 3, 4, 5]
                    print("Original Array:", myArray)
                    
                    var arraySum <- sumArray(myArray)
                    print("Sum of Array Elements:", arraySum)
                    
                    multiplyArrayBy(myArray, 2)
                    print("Array after Multiplication by 2:", myArray)
                end
        """
        expect = str(Program([
            FuncDecl(Id("sumArray"), [VarDecl(Id("arr"), ArrayType([5.0], NumberType()), None, None)], Block([VarDecl(Id("sum"), None, "var", NumberLiteral(0.0)), VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("arr"), [Id("i")])))), Return(Id("sum"))])), 

            FuncDecl(Id("multiplyArrayBy"), [VarDecl(Id("arr"), ArrayType([5.0], NumberType()), None, None), VarDecl(Id("multiplier"),
            NumberType(), None, None)], Block([VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Assign(ArrayCell(Id("arr"), [Id("i")]), BinaryOp("*", ArrayCell(Id("arr"), [Id("i")]), Id("multiplier"))))])), 
            
            FuncDecl(Id("main"), [], Block([VarDecl(Id("myArray"), ArrayType([5.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0), NumberLiteral(5.0)])), CallStmt(Id("print"), [StringLiteral("Original Array:"), Id("myArray")]), VarDecl(Id("arraySum"), None, "var", CallExpr(Id("sumArray"), [Id("myArray")])), CallStmt(Id("print"), [StringLiteral("Sum of Array Elements:"), Id("arraySum")]), CallStmt(Id("multiplyArrayBy"), [Id("myArray"), NumberLiteral(2.0)]), CallStmt(Id("print"), [StringLiteral("Array after Multiplication by 2:"), Id("myArray")])]))]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_53(self):
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
        self.assertTrue(TestAST.test(input, expect, 353))


    def test_54(self):
        input = """
        func addNumbers(number a, number b)
            return a + b

        func multiplyNumbers(number x, number y)
            return x * y

        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()

                var sum <- addNumbers(num1, num2)
                var product <- multiplyNumbers(num1, num2)

                print("Sum:", sum)
                print("Product:", product)
            end
        """
        expect = str(Program([FuncDecl(Id("addNumbers"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Return(BinaryOp("+", Id("a"), Id("b")))), FuncDecl(Id("multiplyNumbers"), [VarDecl(Id("x"), NumberType(), None, None), VarDecl(Id("y"), NumberType(), None, None)], Return(BinaryOp("*", Id("x"), Id("y")))), FuncDecl(Id("main"), [], Block([VarDecl(Id("num1"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("num2"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("sum"), None, "var", CallExpr(Id("addNumbers"), [Id("num1"), Id("num2")])), VarDecl(Id("product"), None, "var", CallExpr(Id("multiplyNumbers"), [Id("num1"), Id("num2")])), CallStmt(Id("print"), [StringLiteral("Sum:"), Id("sum")]), CallStmt(Id("print"), [StringLiteral("Product:"), Id("product")])]))]))
        self.assertTrue(TestAST.test(input, expect, 354))
    
    def test_55(self):
        input = """
            var phrase <- "happy" ... " dragon year"
        """
        expect = str(Program([VarDecl(Id("phrase"), None, "var", BinaryOp("...", StringLiteral("happy"), StringLiteral(" dragon year")))]))
        self.assertTrue(TestAST.test(input,expect,355))

    
    def test_56(self):
        input = """
        func generateWish(string occasion)
        return "happy" ... occasion
        var phrase <- generateWish(" dragon year")
        """
        expect = str(Program([FuncDecl(Id("generateWish"), [VarDecl(Id("occasion"), StringType(), None, None)], Return(BinaryOp("...", StringLiteral("happy"), Id("occasion")))), VarDecl(Id("phrase"), None, "var", CallExpr(Id("generateWish"), [StringLiteral(" dragon year")]))]))
        self.assertTrue(TestAST.test(input,expect,356))
    
    def test_57(self):
        input = """
        func repeatLove(string feeling, number times)
            begin
            var result <- ""
            for i until i < times by 1
                result <- result ... feeling
            return result
            end

        var lovePhrase <- repeatLove("love", 3)
        """
        expect = str(Program([FuncDecl(Id("repeatLove"), [VarDecl(Id("feeling"), StringType(), None, None), VarDecl(Id("times"), NumberType(), None, None)], Block([VarDecl(Id("result"), None, "var", StringLiteral("")), For(Id("i"), BinaryOp("<", Id("i"), Id("times")), NumberLiteral(1.0), Assign(Id("result"), BinaryOp("...", Id("result"), Id("feeling")))), Return(Id("result"))])), VarDecl(Id("lovePhrase"), None, "var", CallExpr(Id("repeatLove"), [StringLiteral("love"), NumberLiteral(3.0)]))]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_58(self):
        input = """
        func createGreeting(string name)
        return "Hello, " ... name

        func main()
            begin
                var userName <- "NNKM"
                var greeting <- createGreeting(userName)
                print(greeting)
            end
        """
        expect = str(Program([FuncDecl(Id("createGreeting"), [VarDecl(Id("name"), StringType(), None, None)], Return(BinaryOp("...", StringLiteral("Hello, "), Id("name")))), FuncDecl(Id("main"), [], Block([VarDecl(Id("userName"), None, "var", StringLiteral("NNKM")), VarDecl(Id("greeting"), None, "var", CallExpr(Id("createGreeting"), [Id("userName")])), CallStmt(Id("print"), [Id("greeting")])]))]))
        self.assertTrue(TestAST.test(input,expect,358))
    
    def test_59(self):
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
        self.assertTrue(TestAST.test(input,expect,359))
    
    def test_60(self):
        input = """
        func sayHello()
            return print("Hello, World!")

        func main()
            begin
                sayHello()
            end
        """
        expect = str(Program([FuncDecl(Id("sayHello"), [], Return(CallExpr(Id("print"), [StringLiteral("Hello, World!")]))), FuncDecl(Id("main"), [], Block([CallStmt(Id("sayHello"), [])]))]))
        self.assertTrue(TestAST.test(input,expect,360))
    
    def test_61(self):
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
        self.assertTrue(TestAST.test(input,expect,361))

    def test_62(self):
        input = """
        var arr <- [1, 2, 3, 4, 5]
        var index <- 2
        var value <- arr[index]
        """
        expect = str(Program([VarDecl(Id("arr"), None, "var", ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0), NumberLiteral(5.0)])), VarDecl(Id("index"), None, "var", NumberLiteral(2.0)), VarDecl(Id("value"), None, "var", ArrayCell(Id("arr"), [Id("index")]))]))
        self.assertTrue(TestAST.test(input,expect,362))
    
    def test_63(self):
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
        self.assertTrue(TestAST.test(input,expect,363))

    def test_64(self):
        input = """
        func main()
            begin
                var x <- 10
                var y <- 20
                var z <- x + y
                print("The sum of x and y is: ", z)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), None, "var", NumberLiteral(10.0)), VarDecl(Id("y"), None, "var", NumberLiteral(20.0)), VarDecl(Id("z"), None, "var", BinaryOp("+", Id("x"), Id("y"))), CallStmt(Id("print"), [StringLiteral("The sum of x and y is: "), Id("z")])]))]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_65(self):
        input = """
        func main()
            begin
                var a <- 5
                var b <- 7
                var c <- a + b
                print("The sum of ", a, " and ", b, " is ", c)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "var", NumberLiteral(5.0)), VarDecl(Id("b"), None, "var", NumberLiteral(7.0)), VarDecl(Id("c"), None, "var", BinaryOp("+", Id("a"), Id("b"))), CallStmt(Id("print"), [StringLiteral("The sum of "), Id("a"), StringLiteral(" and "), Id("b"), StringLiteral(" is "), Id("c")])]))]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test_66(self):
        input = """
        func main()
            begin
                var num1 <- 10
                var num2 <- 5
                var sum <- num1 + num2
                var difference <- num1 - num2
                var product <- num1 * num2
                var quotient <- num1 / num2
                print("Sum:", sum)
                print("Difference:", difference)
                print("Product:", product)
                print("Quotient:", quotient)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("num1"), None, "var", NumberLiteral(10.0)), 
            VarDecl(Id("num2"), None, "var", NumberLiteral(5.0)), 
            VarDecl(Id("sum"), None, "var", BinaryOp("+", Id("num1"), Id("num2"))), 
            VarDecl(Id("difference"), None, "var", BinaryOp("-", Id("num1"), Id("num2"))), 
            VarDecl(Id("product"), None, "var", BinaryOp("*", Id("num1"), Id("num2"))), 
            VarDecl(Id("quotient"), None, "var", BinaryOp("/", Id("num1"), Id("num2"))), 
            CallStmt(Id("print"), [StringLiteral("Sum:"), Id("sum")]), 
            CallStmt(Id("print"), [StringLiteral("Difference:"), Id("difference")]), 
            CallStmt(Id("print"), [StringLiteral("Product:"), Id("product")]), 
            CallStmt(Id("print"), [StringLiteral("Quotient:"), Id("quotient")])]))]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_67(self):
        input = """
        func factorial(number n)
            begin
                if (n <= 1)
                    return 1
                else
                    return n * factorial(n - 1)
            end

        func main()
            begin
                var x <- readNumber()
                print("Factorial of", x, "is", factorial(x))
            end
        """
        expect = str(Program([FuncDecl(Id("factorial"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If((BinaryOp("<=", Id("n"), NumberLiteral(1.0))), Return(NumberLiteral(1.0)), [], Return(BinaryOp("*", Id("n"), CallExpr(Id("factorial"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))]))))])), 
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("x"), None, "var", CallExpr(Id("readNumber"), [])), 
                CallStmt(Id("print"), [StringLiteral("Factorial of"), Id("x"), StringLiteral("is"), CallExpr(Id("factorial"), [Id("x")])])]))]))
        self.assertTrue(TestAST.test(input,expect,367))
    
    def test_68(self):
        input = """var str <- "Hello world!"
                """
        expect = str(Program([VarDecl(Id("str"), None, "var", StringLiteral("Hello world!"))]))
        self.assertTrue(TestAST.test(input,expect,368))
    
    def test_69(self):
        input = """
        func fib(number n)
        begin
            if (n <= 1)
                return n
            else
                return fib(n - 1) + fib(n - 2)
        end
        """
        expect = str(Program([FuncDecl(Id("fib"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If((
                BinaryOp("<=", Id("n"), NumberLiteral(1.0))), Return(Id("n")), 
                [], 
                Return(BinaryOp("+", CallExpr(Id("fib"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))]), 
                                    CallExpr(Id("fib"), [BinaryOp("-", Id("n"), NumberLiteral(2.0))]))))]))]))
        self.assertTrue(TestAST.test(input,expect,369))
    
    def test_70(self):
        input = """
        func power(number base, number exponent)
            begin
                var result <- 1
                var i <- 1
                for i until i <= exponent by 1
                    result <- result * base
                return result
            end

        func main()
            begin
                var base <- readNumber()
                var exponent <- readNumber()
                print(base, " raised to the power of ", exponent, " is ", power(base, exponent))
            end
        """
        expect = str(Program([FuncDecl(Id("power"), [VarDecl(Id("base"), NumberType(), None, None), VarDecl(Id("exponent"), NumberType(), None, None)], Block([VarDecl(Id("result"), None, "var", NumberLiteral(1.0)), VarDecl(Id("i"), None, "var", NumberLiteral(1.0)), For(Id("i"), BinaryOp("<=", Id("i"), Id("exponent")), NumberLiteral(1.0), Assign(Id("result"), BinaryOp("*", Id("result"), Id("base")))), Return(Id("result"))])), FuncDecl(Id("main"), [], Block([VarDecl(Id("base"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("exponent"), None, "var", CallExpr(Id("readNumber"), [])), CallStmt(Id("print"), [Id("base"), StringLiteral(" raised to the power of "), Id("exponent"), StringLiteral(" is "), CallExpr(Id("power"), [Id("base"), Id("exponent")])])]))]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_71(self):
        input = """
        func sum_of_squares(number n)
            begin
                if (n == 0)
                    return 0
                else
                    return n * n + sum_of_squares(n - 1)
            end

        func main()
            begin
                var n <- 5
                var result <- sum_of_squares(n)
                print(result)
            end
        """
        expect = str(Program([FuncDecl(Id("sum_of_squares"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If((BinaryOp("==", Id("n"), NumberLiteral(0.0))), Return(NumberLiteral(0.0)), [], Return(BinaryOp("+", BinaryOp("*", Id("n"), Id("n")), CallExpr(Id("sum_of_squares"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))]))))])), FuncDecl(Id("main"), [], Block([VarDecl(Id("n"), None, "var", NumberLiteral(5.0)), VarDecl(Id("result"), None, "var", CallExpr(Id("sum_of_squares"), [Id("n")])), CallStmt(Id("print"), [Id("result")])]))]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_72(self):
        input = """
        func specialCase()
            begin
                var a <- 10 + 5 / 2 - 3
                var b <- 2 * (4 + 6) % 3
                var c <- 2 * 3
                var d <- -5 + 3 * -2
            end
        """
        expect = str(Program([FuncDecl(Id("specialCase"), [], Block([
            VarDecl(Id("a"), None, "var", BinaryOp("-", BinaryOp("+", NumberLiteral(10.0), BinaryOp("/", NumberLiteral(5.0), NumberLiteral(2.0))), NumberLiteral(3.0))), 
            VarDecl(Id("b"), None, "var", BinaryOp("%", BinaryOp("*", NumberLiteral(2.0), BinaryOp("+", NumberLiteral(4.0), NumberLiteral(6.0))), NumberLiteral(3.0))), 
            VarDecl(Id("c"), None, "var", BinaryOp("*", NumberLiteral(2.0), NumberLiteral(3.0))), 
            VarDecl(Id("d"), None, "var", BinaryOp("+", UnaryOp("-", NumberLiteral(5.0)), BinaryOp("*", NumberLiteral(3.0), UnaryOp("-", NumberLiteral(2.0)))))]))]))
        self.assertTrue(TestAST.test(input,expect,372))
    
    def test_73(self):
        input = """
        func specialCase()
            begin
                var e <- 10 / 2 + 5 - 3 * (4 % 3)
                var f <- (2 + 3) * (4 - 1) / (6 / 2)
                var g <- (10 - 2) * ((5 + 3) - 2) / 4
                var h <- 8 - 2 + 5 / (3 % 2)
            end
        """
        expect = str(Program([FuncDecl(Id("specialCase"), [], Block([
            VarDecl(Id("e"), None, "var", BinaryOp("-", BinaryOp("+", BinaryOp("/", NumberLiteral(10.0), NumberLiteral(2.0)), NumberLiteral(5.0)), BinaryOp("*", NumberLiteral(3.0), BinaryOp("%", NumberLiteral(4.0), NumberLiteral(3.0))))), 
            VarDecl(Id("f"), None, "var", BinaryOp("/", BinaryOp("*", BinaryOp("+", NumberLiteral(2.0), NumberLiteral(3.0)), BinaryOp("-", NumberLiteral(4.0), NumberLiteral(1.0))), BinaryOp("/", NumberLiteral(6.0), NumberLiteral(2.0)))), 
            VarDecl(Id("g"), None, "var", BinaryOp("/", BinaryOp("*", BinaryOp("-", NumberLiteral(10.0), NumberLiteral(2.0)), BinaryOp("-", BinaryOp("+", NumberLiteral(5.0), NumberLiteral(3.0)), NumberLiteral(2.0))), NumberLiteral(4.0))), 
            VarDecl(Id("h"), None, "var", BinaryOp("+", BinaryOp("-", NumberLiteral(8.0), NumberLiteral(2.0)), BinaryOp("/", NumberLiteral(5.0), BinaryOp("%", NumberLiteral(3.0), NumberLiteral(2.0)))))]))]))
        self.assertTrue(TestAST.test(input,expect,373))
    
    def test_74(self):
        input = """
            func add(number a, number b) 
                return a + b
            func subtract(number a, number b) 
                return a - b
            func main() 
                return add(5, subtract(8, 3))
        """
        expect = str(Program([FuncDecl(Id("add"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Return(BinaryOp("+", Id("a"), Id("b")))), FuncDecl(Id("subtract"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Return(BinaryOp("-", Id("a"), Id("b")))), FuncDecl(Id("main"), [], Return(CallExpr(Id("add"), [NumberLiteral(5.0), CallExpr(Id("subtract"), [NumberLiteral(8.0), NumberLiteral(3.0)])])))]))
        self.assertTrue(TestAST.test(input,expect,374))
    
    def test_75(self):
        input = """
        func calculate_area(number radius)
            begin
                return 3.14 * radius * radius
            end
        func main() 
            return calculate_area(5)
        """
        expect = str(Program([FuncDecl(Id("calculate_area"), [VarDecl(Id("radius"), NumberType(), None, None)], Block([Return(BinaryOp("*", BinaryOp("*", NumberLiteral(3.14), Id("radius")), Id("radius")))])), FuncDecl(Id("main"), [], Return(CallExpr(Id("calculate_area"), [NumberLiteral(5.0)])))]))
        self.assertTrue(TestAST.test(input,expect,375))

    def test_76(self):
        input = """
        func check_odd_even(number n)
            begin
                if (n % 2)
                    return "Even"
                else
                    return "Odd"
            end
        func main() 
            return check_odd_even(7)
        """
        expect = str(Program([FuncDecl(Id("check_odd_even"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If((BinaryOp("%", Id("n"), NumberLiteral(2.0))), Return(StringLiteral("Even")), [], Return(StringLiteral("Odd")))])), FuncDecl(Id("main"), [], Return(CallExpr(Id("check_odd_even"), [NumberLiteral(7.0)])))]))
        self.assertTrue(TestAST.test(input,expect,376))
    
    def test_77(self):
        input = """
        func maxOfThree(number a, number b, number c)
            begin
                if (a > b)
                    if (a > c)
                        return a
                    else
                        return c
                elif (b > c)
                    return b
                return c
            end
        """
        expect = str(Program([FuncDecl(Id("maxOfThree"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None), VarDecl(Id("c"), NumberType(), None, None)], Block([
            If((BinaryOp(">", Id("a"), Id("b"))), 
                If((BinaryOp(">", Id("a"), Id("c"))), Return(Id("a")), [], Return(Id("c"))), 
            [(BinaryOp(">", Id("b"), Id("c")),                                                                                
            Return(Id("b")))], None), 
        Return(Id("c"))]))]))
        self.assertTrue(TestAST.test(input,expect,377))
    
    def test_78(self):
        input = """
        func sumOfSquares(number a, number b)
            begin
                return a * a + b * b
            end
        func main() return sumOfSquares(3, 4)
        """
        expect = str(Program([FuncDecl(Id("sumOfSquares"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Block([Return(BinaryOp("+", BinaryOp("*", Id("a"), Id("a")), BinaryOp("*", Id("b"), Id("b"))))])), FuncDecl(Id("main"), [], Return(CallExpr(Id("sumOfSquares"), [NumberLiteral(3.0), NumberLiteral(4.0)])))]))
        self.assertTrue(TestAST.test(input,expect,378))
    
    def test_79(self):
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
        self.assertTrue(TestAST.test(input,expect,379))
    
    def test_80(self):
        input = """
        func main()
            begin
                var x <- 10
                var y <- 20
                var sum <- x + y
                if (sum > 30)
                    print("Sum is greater than 30")
                else
                    print("Sum is not greater than 30")
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), None, "var", NumberLiteral(10.0)), VarDecl(Id("y"), None, "var", NumberLiteral(20.0)), VarDecl(Id("sum"), None, "var", BinaryOp("+", Id("x"), Id("y"))), 
        If((BinaryOp(">", Id("sum"), NumberLiteral(30.0))), CallStmt(Id("print"), [StringLiteral("Sum is greater than 30")]), [], CallStmt(Id("print"), [StringLiteral("Sum is not greater than 30")]))]))]))
        self.assertTrue(TestAST.test(input,expect,380))
    
    def test_81(self):
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
        self.assertTrue(TestAST.test(input,expect,381))
    
    def test_82(self):
        input = """
        func main()
            begin
                var num <- readNumber()
                if (num % 2 == 0)
                    print(num, " is even")
                else
                    print(num, " is odd")
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("num"), None, "var", CallExpr(Id("readNumber"), [])), 
        If((BinaryOp("==", BinaryOp("%", Id("num"), NumberLiteral(2.0)), NumberLiteral(0.0))), CallStmt(Id("print"), [Id("num"), StringLiteral(" is even")]), [], CallStmt(Id("print"), [Id("num"), StringLiteral(" is odd")]))]))]))
        self.assertTrue(TestAST.test(input,expect,382))
    
    def test_83(self):
        input = """
        func calculateArea(number radius)
            begin
                var pi <- 3.14
                var area <- pi * radius * radius
                return area
            end
        var r <- readNumber()
        """
        expect = str(Program([FuncDecl(Id("calculateArea"), [VarDecl(Id("radius"), NumberType(), None, None)], Block([VarDecl(Id("pi"), None, "var", NumberLiteral(3.14)), VarDecl(Id("area"), None, "var", BinaryOp("*", BinaryOp("*", Id("pi"), Id("radius")), Id("radius"))), Return(Id("area"))])), VarDecl(Id("r"), None, "var", CallExpr(Id("readNumber"), []))]))
        self.assertTrue(TestAST.test(input,expect,383))
    
    def test_83(self):
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
        self.assertTrue(TestAST.test(input,expect,383))
    
    def test_84(self):
        input = """
        func isPalindrome(string s)
            begin
                var reversed <- ""
                for i until i < len by 1
                    reversed <- s[i] + reversed
                return s = reversed
            end

        var word <- readString()
        """
        expect = str(Program([FuncDecl(Id("isPalindrome"), [VarDecl(Id("s"), StringType(), None, None)], Block([VarDecl(Id("reversed"), None, "var", StringLiteral("")), For(Id("i"), BinaryOp("<", Id("i"), Id("len")), NumberLiteral(1.0), Assign(Id("reversed"), BinaryOp("+", ArrayCell(Id("s"), [Id("i")]), Id("reversed")))), Return(BinaryOp("=", Id("s"), Id("reversed")))])), VarDecl(Id("word"), None, "var", CallExpr(Id("readString"), []))]))
        self.assertTrue(TestAST.test(input,expect,384))
    def test_85(self):
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
        
        self.assertTrue(TestAST.test(input,expect,385))
    
    def test_86(self):
        input ="""func max(number a[100], number length)
        begin
            if (length <= 0)
                return -1e9 ## Represent negative infinity
            var max <- a[0]
            var i <- 0
            for i until i >= length by 1
                if (a[i] > max) max <- a[i]
            return max
        end
                """
        expect =str(Program([FuncDecl(Id("max"), [VarDecl(Id("a"), ArrayType([100.0], NumberType()), None, None), VarDecl(Id("length"), NumberType(), None, None)], Block([
            If((BinaryOp("<=", Id("length"), NumberLiteral(0.0))), Return(UnaryOp("-", NumberLiteral(1000000000.0))), [], None), VarDecl(Id("max"), None, "var", ArrayCell(Id("a"), [NumberLiteral(0.0)])), VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp(">=", Id("i"), Id("length")), NumberLiteral(1.0), 
            If((BinaryOp(">", ArrayCell(Id("a"), [Id("i")]), Id("max"))), Assign(Id("max"), ArrayCell(Id("a"), [Id("i")])), [], None)), Return(Id("max"))]))]))
        self.assertTrue(TestAST.test(input,expect,386))
    
    def test_87(self):
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
        self.assertTrue(TestAST.test(input,expect,387))
    
    def test_88(self):
        input = """func foo(number a[5], string b)
                begin
                    var i <- 0
                    for i until i >= 5 by 1
                        begin
                            a[i] <- i * i + 5
                        end
                    return -1
                end
            """
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, None), VarDecl(Id("b"), StringType(), None, None)], Block([VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([Assign(ArrayCell(Id("a"), [Id("i")]), BinaryOp("+", BinaryOp("*", Id("i"), Id("i")), NumberLiteral(5.0)))])), Return(UnaryOp("-", NumberLiteral(1.0)))]))]))
        self.assertTrue(TestAST.test(input,expect,388))
    
    def test_89(self):
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
        self.assertTrue(TestAST.test(input,expect,389))
    
    def test_90(self):
        input = """
        func calculateSum(number n)
            begin
                if (n <= 0)
                    return 0
                else return n + calculateSum(n - 1)
            end

        var num <- readNumber()
        """
        expect = str(Program([FuncDecl(Id("calculateSum"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If((BinaryOp("<=", Id("n"), NumberLiteral(0.0))), Return(NumberLiteral(0.0)), [], Return(BinaryOp("+", Id("n"), CallExpr(Id("calculateSum"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))]))))])), VarDecl(Id("num"), None, "var", CallExpr(Id("readNumber"), []))]))
        self.assertTrue(TestAST.test(input,expect,390))
    
    def test_91(self):
        input = """
        func findMax(number a, number b)
            begin
                if (a > b)
                    return a
                else return b
            end
        """
        expect = str(Program([FuncDecl(Id("findMax"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Block([If((BinaryOp(">", Id("a"), Id("b"))), Return(Id("a")), [], Return(Id("b")))]))]))
        self.assertTrue(TestAST.test(input,expect,391))
    
    def test_92(self):
        input = """
        func power(number base,number exponent)
            begin
            var result <- 1
            for i until exponent by 1
                result <- result * base
            return result
            end
        """
        expect = str(Program([FuncDecl(Id("power"), [VarDecl(Id("base"), NumberType(), None, None), VarDecl(Id("exponent"), NumberType(), None, None)], Block([VarDecl(Id("result"), None, "var", NumberLiteral(1.0)), For(Id("i"), Id("exponent"), NumberLiteral(1.0), Assign(Id("result"), BinaryOp("*", Id("result"), Id("base")))), Return(Id("result"))]))]))
        self.assertTrue(TestAST.test(input,expect,392))
    
    def test_93(self):
        input = """
        func power(number a,number b)
            begin
            var squareA <- a * a
            var squareB <- b * b
            var sum <- squareA + squareB
            return sum
            end
        """
        expect = str(Program([FuncDecl(Id("power"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Block([VarDecl(Id("squareA"), None, "var", BinaryOp("*", Id("a"), Id("a"))), VarDecl(Id("squareB"), None, "var", BinaryOp("*", Id("b"), Id("b"))), VarDecl(Id("sum"), None, "var", BinaryOp("+", Id("squareA"), Id("squareB"))), Return(Id("sum"))]))]))
        self.assertTrue(TestAST.test(input,expect,393))
    
    def test_94(self):
        input = """
        func calculateHypotenuse(number a,number b)
            begin
            var squareSum <- a * a + b * b
            var hypotenuse <- sqrt(squareSum)
            return hypotenuse
            end
        """
        expect = str(Program([FuncDecl(Id("calculateHypotenuse"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Block([VarDecl(Id("squareSum"), None, "var", BinaryOp("+", BinaryOp("*", Id("a"), Id("a")), BinaryOp("*", Id("b"), Id("b")))), VarDecl(Id("hypotenuse"), None, "var", CallExpr(Id("sqrt"), [Id("squareSum")])), Return(Id("hypotenuse"))]))]))
        self.assertTrue(TestAST.test(input,expect,394))
    
    def test_95(self):
        input = """
        func isPrime(number n)
            begin
            if (n <= 1)
                return false
            for i until n by 1
                if (n % i == 0)
                    return false
            return true
            end
        """
        expect = str(Program([FuncDecl(Id("isPrime"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If((BinaryOp("<=", Id("n"), NumberLiteral(1.0))), Return(BooleanLiteral(False)), [], None), For(Id("i"), Id("n"), NumberLiteral(1.0), 
            If((BinaryOp("==", BinaryOp("%", Id("n"), Id("i")), NumberLiteral(0.0))), Return(BooleanLiteral(False)), [], None)), Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input,expect,395))
    
    def test_96(self):
        input = """
        func main()
            begin
                var a <- 5
                var b <- 3
                var c <- 7
                var d <- a + b
                var e <- c - b
                var result <- d * e
                print("The result is: ", result)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "var", NumberLiteral(5.0)), VarDecl(Id("b"), None, "var", NumberLiteral(3.0)), VarDecl(Id("c"), None, "var", NumberLiteral(7.0)), VarDecl(Id("d"), None, "var", BinaryOp("+", Id("a"), Id("b"))), VarDecl(Id("e"), None, "var", BinaryOp("-", Id("c"), Id("b"))), VarDecl(Id("result"), None, "var", BinaryOp("*", Id("d"), Id("e"))), CallStmt(Id("print"), [StringLiteral("The result is: "), Id("result")])]))]))
        self.assertTrue(TestAST.test(input,expect,396))
    
    def test_97(self):
        input = """
        func calculateArea(number length, number width)
            begin
                var area <- length * width
                return area
            end

        var l <- 10
        var w <- 5
        var result <- calculateArea(l, w)
        """
        expect = str(Program([FuncDecl(Id("calculateArea"), [VarDecl(Id("length"), NumberType(), None, None), VarDecl(Id("width"), NumberType(), None, None)], Block([VarDecl(Id("area"), None, "var", BinaryOp("*", Id("length"), Id("width"))), Return(Id("area"))])), VarDecl(Id("l"), None, "var", NumberLiteral(10.0)), VarDecl(Id("w"), None, "var", NumberLiteral(5.0)), VarDecl(Id("result"), None, "var", CallExpr(Id("calculateArea"), [Id("l"), Id("w")]))]))
        self.assertTrue(TestAST.test(input,expect,397))
    
    def test_98(self):
        input = """
        func main()
            begin
                string result <- "(a * b + c) / (a - b)"
                print("Result: ", result)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("result"), StringType(), None, StringLiteral("(a * b + c) / (a - b)")), CallStmt(Id("print"), [StringLiteral("Result: "), Id("result")])]))]))
        self.assertTrue(TestAST.test(input,expect,398))
    
    def test_99(self):
        input = """
        func main()
            begin
                string result <- "IM FREAKING DONE"
                print("Result: ", result)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("result"), StringType(), None, StringLiteral("IM FREAKING DONE")), CallStmt(Id("print"), [StringLiteral("Result: "), Id("result")])]))]))
        self.assertTrue(TestAST.test(input,expect,399))
    

