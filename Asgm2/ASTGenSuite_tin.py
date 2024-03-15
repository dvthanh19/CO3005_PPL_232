import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"),NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 301))
    
    def test_2(self):
        input = """number a <- 3 + 4 / 2
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), varInit = BinaryOp("+",NumberLiteral(3.0),BinaryOp("/",NumberLiteral(4.0),NumberLiteral(2.0))))]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_3(self):
        input = """number list[5,6] <- [[[[5,4,3,2,1],[66.78,77.e-4,89.1,50.00]],[5.e-4,65.9E+3,20.6E-3]],[1E-78]]
        bool test[5] <- [[[true,false,true,false,true]]]
        string abc[20] <- [\"abcdefg\",\"\",\"123@\\n\"]
        dynamic dym
        var abc <- \"a string with numbers like \'\"1.123e-3'\", \'\"0.23E-50'\"?\"
        """
        expect = str(Program([VarDecl(Id("list"), ArrayType([5.0,6.0], NumberType()), varInit = ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([NumberLiteral(5.0), NumberLiteral(4.0), NumberLiteral(3.0), NumberLiteral(2.0), NumberLiteral(1.0)]), ArrayLiteral([NumberLiteral(66.78),NumberLiteral(77.e-4),NumberLiteral(89.1),NumberLiteral(50.00)])]), ArrayLiteral([NumberLiteral(5.e-4), NumberLiteral(65.9E+3), NumberLiteral(20.6E-3)])]), ArrayLiteral([NumberLiteral(1e-78)])])),
                                      VarDecl(Id("test"), ArrayType([5.0], BoolType()), varInit = ArrayLiteral([ArrayLiteral([ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(True)])])])),
                                      VarDecl(Id("abc"), ArrayType([20.0], StringType()), varInit = ArrayLiteral([StringLiteral("abcdefg"), StringLiteral(""), StringLiteral("123@\\n")])),
                                      VarDecl(Id("dym"), modifier = "dynamic"),
                                      VarDecl(Id("abc"), varInit = StringLiteral("a string with numbers like \'\"1.123e-3'\", \'\"0.23E-50'\"?"), modifier = "var")]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4(self):
        input = """func isPrime(number n, string a[3])
        func main()
        """
        expect = str(Program([FuncDecl(Id("isPrime"), [VarDecl(Id("n"), NumberType()), VarDecl(Id("a"), ArrayType([3.0], StringType()))]), FuncDecl(Id("main"), [])]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5(self):
        input = """func areDivisors(number num1, number num2) return ((num1 % num2 = 0) or (num2 % num1 = 0))
func main()
begin
var num1 <- readNumber()
var num2 <- readNumber()
if (areDivisors(num1, num2)) writeString("Yes")
else writeString("No")
end
        """
        expect = str(Program([FuncDecl(Id("areDivisors"), [VarDecl(Id("num1"), NumberType()), VarDecl(Id("num2"), NumberType())], Return(BinaryOp("or", BinaryOp("=", BinaryOp("%", Id("num1"), Id("num2")), NumberLiteral(0.0)), BinaryOp("=", BinaryOp("%", Id("num2"), Id("num1")), NumberLiteral(0.0))))),
                              FuncDecl(Id("main"),[], Block([VarDecl(Id("num1"), varInit = CallExpr(Id("readNumber"), []), modifier = "var"), VarDecl(Id("num2"), varInit = CallExpr(Id("readNumber"), []), modifier = "var"), 
                                                             If(CallExpr(Id("areDivisors"), [Id("num1"), Id("num2")]), CallStmt(Id("writeString"), [StringLiteral("Yes")]), [], CallStmt(Id("writeString"), [StringLiteral("No")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_6(self):
        input = """func isPrime(number x)
func main()
begin
    number x <- readNumber()
    if (isPrime(x)) writeString("Yes")
        else writeString("No")
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
        expect = str(Program([FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType())]),
                              FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), NumberType(), varInit = CallExpr(Id("readNumber"), [])),
                                                              If(CallExpr(Id("isPrime"), [Id("x")]), CallStmt(Id("writeString"), [StringLiteral("Yes")]), [], CallStmt(Id("writeString"), [StringLiteral("No")]))])),
                                FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType())], Block([If(BinaryOp("<=", Id("x"), NumberLiteral(1.0)), Return(BooleanLiteral(False)), [], None),
                                                                                                 VarDecl(Id("i"), varInit = NumberLiteral(2.0), modifier = "var"),
                                                                                                 For(Id("i"), BinaryOp(">", Id("i"), BinaryOp("/", Id("x"), NumberLiteral(2.0))), NumberLiteral(1.0), Block([If(BinaryOp("=", BinaryOp("%", Id("x"), Id("i")), NumberLiteral(0.0)), Return(BooleanLiteral(False)), [], None)])),
                                                                                                 Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_7(self):
        input = """func main()
begin
aPI <- 3.14
l[3] <- value * aPI ## This is a comment
end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Assign(Id("aPI"), NumberLiteral(3.14)), 
                                                              Assign(ArrayCell(Id("l"), [NumberLiteral(3.0)]), BinaryOp("*", Id("value"), Id("aPI")))]))]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_8(self):
        input = """
            string a
            bool b
            string c <- 1
            bool d <- 1
        """
        expect = str(Program([
                VarDecl(Id("a"), StringType()),
                VarDecl(Id("b"), BoolType()),
                VarDecl(Id("c"), StringType(), None, NumberLiteral(1.0)),
                VarDecl(Id("d"), BoolType(), None, NumberLiteral(1.0))
            ]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_9(self):
        input = """
            string a[5] <- 1
            string b[5]
        """
        expect = str(Program([
                VarDecl(Id("a"), ArrayType([5.0], StringType()), None, NumberLiteral(1.0)),
                VarDecl(Id("b"), ArrayType([5.0], StringType()))
            ]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10(self):
        input = """
            number a[5,3,4.2] <- 1
            bool b[2,3,4]
        """
        expect = str(Program([
                VarDecl(Id("a"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, NumberLiteral(1.0)),
                VarDecl(Id("b"), ArrayType([2.0, 3.0, 4.0], BoolType()))
            ]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_11(self):
        input = """
            dynamic a <- 1
            dynamic b
        """
        expect = str(Program([
                    VarDecl(Id("a"), None, "dynamic", NumberLiteral(1.0)),
                    VarDecl(Id("b"), None, "dynamic")
                ]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_12(self):
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
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_13(self):
        input = """
            var x <- [1, "a", true, false]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_14(self):
        input = """
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number a[1,2])
                return
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), ArrayType([1.0, 2.0], NumberType()))], Return(None))
                ]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_15(self):
        input = """
            var x <- [[1], [1]]
            var x <- [[1]]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)]), ArrayLiteral([NumberLiteral(1.0)])])),
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)])]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 315))
    
    def test_16(self):
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
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_17(self):
        input = """
            var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(1.0)), NumberLiteral(2.0)), BinaryOp("<=", NumberLiteral(4.0), BinaryOp("+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(5.0), BinaryOp("*", Id("a"), NumberLiteral(3.0))), Id("c")), UnaryOp("-", NumberLiteral(1.0))), UnaryOp("not", UnaryOp("-", NumberLiteral(2.0)))))))
            ]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_18(self):
        input = """
            var x <- -a[1+2] ... 2
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", UnaryOp("-", ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))])), NumberLiteral(2.0)))
                ]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_19(self):
        input = """
            var x <- fun()
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), []))
                ]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20(self):
        input = """
            var x <- fun(1+1, "a")
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), StringLiteral("a")]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21(self):
        input = """
            var x <- fun(fun())
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [CallExpr(Id("fun"), [])]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_22(self):
        input = """
            var x <- (2 ... 3) ... 4
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("...", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(4.0)))
                ]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23(self):
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
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_24(self):
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
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_25(self):
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
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26(self):
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
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27(self):
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
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28(self):
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
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29(self):
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
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_30(self):
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
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_31(self):
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
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_32(self):
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
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_33(self):
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
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_34(self):
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
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_35(self):
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
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_36(self):
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
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_37(self):
        input = """
        func main ()
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
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_38(self):
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
            else 
                g()
        elif (7) 
            h()
        end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(NumberLiteral(1.0), 
               If(NumberLiteral(2.0), 
                  CallStmt(Id("b"), []), 
                  [[NumberLiteral(3.0), If(NumberLiteral(4.0), 
                                           CallStmt(Id("c"), []),
                                           [[NumberLiteral(5.0), CallStmt(Id("d"), [])]],
                                           CallStmt(Id("e"), []))],
                    [NumberLiteral(6.0), CallStmt(Id("f"), [])]], 
                  CallStmt(Id("g"), [])), 
                [[NumberLiteral(7.0), CallStmt(Id("h"), [])]],
                None
        )]))]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_39(self):
        input = """
        func main() begin
        if (1) 
            for i until i=10 by 1
                if (2) return
                elif (3) return
                else  return
        end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(NumberLiteral(1.0),
               For(Id("i"), 
                   BinaryOp("=", Id("i"), NumberLiteral(10.0)), 
                   NumberLiteral(1.0), 
                   If(NumberLiteral(2.0),
                      Return(),
                      [[NumberLiteral(3.0), Return()]],
                      Return())),
               [],
               None)
            ]))]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_40(self):
        input = """
            var x <- [1, "a", true, false]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_41(self):
        input = """## looping test
func main()
begin
    if (a > b)
        if (a > b) number c1
        elif (a > b) number c2
        elif (a > b) number c3
        else number c4
    else
        x <- x100 + 1
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(BinaryOp(">", Id("a"), Id("b")), If(BinaryOp(">", Id("a"), Id("b")), VarDecl(Id("c1"), NumberType()), [[BinaryOp(">", Id("a"), Id("b")), VarDecl(Id("c2"), NumberType())], [BinaryOp(">", Id("a"), Id("b")), VarDecl(Id("c3"), NumberType())]], VarDecl(Id("c4"), NumberType())), [], Assign(Id("x"), BinaryOp("+", Id("x100"), NumberLiteral(1.0))))]))]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_42(self):
        input = """
            number a[3]
        """
        expect = str(Program([
                VarDecl(Id("a"), ArrayType([3.0], NumberType()))
            ]))
        self.assertTrue(TestAST.test(input, expect, 342))
        
    def test_43(self):
        input = """
            string abcxyz <- 1
        """
        expect = str(Program([
                VarDecl(Id("abcxyz"), StringType(), None, NumberLiteral(1.0))
            ]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_44(self):
        input = """ 
            ##12
            func main(number a) begin
                ##12
                \n
                break
            end
                ##12
                ##12
            func main(number a)
            ##12        
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], Block([Break()])), 
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())])
                ]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_45(self):
        input = """func foo() begin
            i <- [1,2, [1 + 2], [1 + 2, 3 + 4]] + 5 + (str...lit > (v <= t...c))
            end
        """
        expect = str(Program([
                    FuncDecl(Id("foo"), [], Block([
                        Assign(Id("i"), BinaryOp("+", BinaryOp("+", ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), ArrayLiteral([BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))]), ArrayLiteral([BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), BinaryOp("+", NumberLiteral(3.0), NumberLiteral(4.0))])]), NumberLiteral(5.0)), BinaryOp("...", Id("str"), BinaryOp(">", Id("lit"), BinaryOp("...", BinaryOp("<=", Id("v"), Id("t")), Id("c"))))))]))]))
        self.assertTrue(TestAST.test(input, expect, 345))
    
    def test_46(self):
        input = """\t\tfunc main()
            begin 
                a <- 100
                b <- -1000E-10
                c <- true and false
                d <- a * b % 10 / 56.4E-2
            end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        Assign(Id("a"), NumberLiteral(100.0)), 
                        Assign(Id("b"), UnaryOp("-", NumberLiteral(1000E-10))), 
                        Assign(Id("c"), BinaryOp("and", BooleanLiteral(True), BooleanLiteral(False))), 
                        Assign(Id("d"), BinaryOp("/", BinaryOp("%", BinaryOp("*", Id("a"), Id("b")), NumberLiteral(10.0)), NumberLiteral(56.4E-2)))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_47(self):
        input = """func main() begin 
            IF <- 1000
            FoR <- \"string\"
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Assign(Id("IF"), NumberLiteral(1000.0)), Assign(Id("FoR"), StringLiteral("string"))]))]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_48(self):
        input = """func main() begin
            number a<-10
            string b[1] <- [\"hello\"]
            bool c[1,2,3] <- [[[true,false],[true,false]],[[true,false],[true,false]],[[true,false],[true,false]]]
        
        end



        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        VarDecl(Id("a"), NumberType(), None, NumberLiteral(10.0)), 
                        VarDecl(Id("b"), ArrayType([1.0], StringType()), None, ArrayLiteral([StringLiteral("hello")])), 
                        VarDecl(Id("c"), ArrayType([1.0, 2.0, 3.0], BoolType()), None, ArrayLiteral([
                            ArrayLiteral([ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)]), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])]), 
                            ArrayLiteral([ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)]), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])]), 
                            ArrayLiteral([ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)]), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])])
                        ]))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 348))
    
    def test_49(self):
        input = """
            func loop(string a[1, 2, 3, 3], number _112_[0], bool cc_c)
            begin
                if (a > b)
                    for a until a + 1 by b + 1 if (a > b)
                            if (a > b) number c
                            elif (a > b) number c
                            elif (a > b) number c
                            else number c
                        else
                            break
                else
                    if (a < b)
                        if (a == b) number c
                    else number c
            end
        """
        expect = str(Program([
            FuncDecl(Id("loop"), [VarDecl(Id("a"), ArrayType([1.0, 2.0, 3.0, 3.0], StringType())), VarDecl(Id("_112_"), ArrayType([0.0], NumberType())), VarDecl(Id("cc_c"), BoolType())], Block([
                If(BinaryOp(">", Id("a"), Id("b")),
                For(Id("a"), BinaryOp("+", Id("a"), NumberLiteral(1.0)), BinaryOp("+", Id("b"), NumberLiteral(1.0)),
                    If(BinaryOp(">", Id("a"), Id("b")),
                        If(BinaryOp(">", Id("a"), Id("b")), VarDecl(Id("c"), NumberType()), [
                            (BinaryOp(">", Id("a"), Id("b")), VarDecl(Id("c"), NumberType())), 
                            (BinaryOp(">", Id("a"), Id("b")), VarDecl(Id("c"), NumberType()))
                            ], VarDecl(Id("c"), NumberType())  
                        ), [], Break()
                    )
                ), [], If(BinaryOp("<", Id("a"), Id("b")), If(BinaryOp("==", Id("a"), Id("b")), VarDecl(Id("c"), NumberType()), [], VarDecl(Id("c"), NumberType())), [])
            )
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_50(self):
        input = """
            func foo()
                return "'"'"'""
            var a <- 3
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Return(StringLiteral("""'"'"'\""""))), VarDecl(Id("a"), None, "var", NumberLiteral(3.0))]))
        print(expect)
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51(self):
        input = """
            var a <- 1
        """
        expect = str(Program([
                    VarDecl(Id("a"), None, "var", NumberLiteral(1.0))
                ]))
        self.assertTrue(TestAST.test(input, expect, 351))
        
    def test_52(self):
        input = """
            func main()
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], None)
                ]))
        self.assertTrue(TestAST.test(input, expect, 352))
        
    def test_53(self):
        input = """
            func main()
                begin
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_54(self):
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
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test_55(self):
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
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_56(self):
            input = """
                number a
                string b
                bool c
            """
            expect = str(Program([VarDecl(Id("a"), NumberType()), VarDecl(
                Id("b"), StringType()), VarDecl(Id("c"), BoolType())]))
            self.assertTrue(TestAST.test(input, expect, 356))

        
    def test_57(self):
        input = """
            string a <- "hello"
            number b <- 1
            bool c <- true 
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, StringLiteral("hello")), VarDecl(
            Id("b"), NumberType(), None, NumberLiteral(1.0)), VarDecl(Id("c"), BoolType(), None, BooleanLiteral(True))
        ]))
        self.assertTrue(TestAST.test(input, expect, 357))

    
    def test_58(self):
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
        self.assertTrue(TestAST.test(input, expect, 358))

    
    def test_59(self):
        input = """
            number a[4,5]
            number b[2,3] <- [[1,2,3],[4,5,6]] 
        """
        expect = str(
            Program([VarDecl(Id("a"), ArrayType([4.0, 5.0], NumberType()), None, None), VarDecl(Id("b"), ArrayType([2.0, 3.0], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 359))

    
    def test_60(self):
        input = """
            number a[1.2,3.4]<-"hello"
            bool b[1,2]
            string c[2,3]<-[[1,2,3],[4,5,6]]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([1.2, 3.4], NumberType()), None, StringLiteral("hello")), VarDecl(Id("b"), ArrayType([1.0, 2.0], BoolType())), VarDecl(Id("c"), ArrayType(
            [2.0, 3.0], StringType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]))]))
        self.assertTrue(TestAST.test(input, expect, 360))


    def test_61(self):
        input = """
            var a <- 1
            dynamic b <- "hello"
            var c <- true 
        """
        expect = str(Program([VarDecl(Id("a"), None, "var", NumberLiteral(1.0)), VarDecl(
            Id("b"), None, "dynamic", StringLiteral("hello")), VarDecl(Id("c"), None, "var", BooleanLiteral(True))]))
        self.assertTrue(TestAST.test(input, expect, 361))

    
    def test_62(self):
        input = """ 
            dynamic b
        """
        expect = str(Program([VarDecl(Id("b"), None, "dynamic", None)]))
        self.assertTrue(TestAST.test(input, expect, 362))

    
    def test_63(self):
        input = """
            func main() 
        """
        expect = str(Program([FuncDecl(Id("main"), [], None)]))
        self.assertTrue(TestAST.test(input, expect, 363))

    
    def test_64(self):
        input = """ 
            func main() begin
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 364))

    
    def test_65(self):
        input = """
            func main() return 0
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return(NumberLiteral(0.0)))])
                    )
        self.assertTrue(TestAST.test(input, expect, 365))

    
    def test_66(self):
        input = """ 
            func main()
                begin 
                    break
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Break()]))]))
        self.assertTrue(TestAST.test(input, expect, 366))

    
    def test_67(self):
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
        self.assertTrue(TestAST.test(input, expect, 367))
    
    def test_68(self):
        input = """
            var a <- [1,"hello",true]
        """
        expect = str(Program([VarDecl(Id("a"), None, "var", ArrayLiteral(
            [NumberLiteral(1.0), StringLiteral("hello"), BooleanLiteral(True)]))]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_69(self):
        input = """
            var a <- laptopLenovo()
        """
        expect = str(
            Program([VarDecl(Id("a"), None, "var", CallExpr(Id("laptopLenovo"), []))]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_70(self):
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
        self.assertTrue(TestAST.test(input, expect, 370))

    
    def test_71(self):
        input = """
            func main()
                begin
                    for i until i < 10 by i=i+1
                        print(i) 
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)),
                                                                BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), NumberLiteral(1.0))), CallStmt(Id("print"), [Id("i")]))]))]))
        self.assertTrue(TestAST.test(input, expect, 371))

    
    def test_72(self):
        input = """
            func main()
                begin
                    a <- b
                    continue
                end
        """
        expect = str(Program(
            [FuncDecl(Id("main"), [], Block([Assign(Id("a"), Id("b")), Continue()]))]))
        self.assertTrue(TestAST.test(input, expect, 372))


    def test_73(self):
        input = """
            func quickSort(number arr[10], number low, number high)
                begin
                    hehe <- 1
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
        expect = str(Program([FuncDecl(Id("quickSort"), [VarDecl(Id("arr"), ArrayType([10.0], NumberType())), VarDecl(Id("low"), NumberType()), VarDecl(Id("high"), NumberType())], Block([Assign(Id("hehe"), NumberLiteral(1.0)), Return(NumberLiteral(0.0))])), FuncDecl(Id("main"), [], Block([VarDecl(Id("arr"), ArrayType([10.0], NumberType()), None, ArrayLiteral(
            [NumberLiteral(4.0), NumberLiteral(3.0), NumberLiteral(2.0), NumberLiteral(1.0), NumberLiteral(5.0), NumberLiteral(7.0), NumberLiteral(6.0), NumberLiteral(8.0), NumberLiteral(9.0), NumberLiteral(0.0)])), CallStmt(Id("quickSort"), [Id("arr"), NumberLiteral(0.0), NumberLiteral(9.0)]), CallStmt(Id("print"), [Id("arr")]), Return(NumberLiteral(0.0))]))]))
        self.assertTrue(TestAST.test(input, expect, 373))

    
    def test_74(self):
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
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        VarDecl(Id("a"), None, "var", NumberLiteral(1.0)),
                        VarDecl(Id("b"), None, "var", NumberLiteral(2.0)),
                        VarDecl(Id("c"), None, "var", NumberLiteral(3.0)),
                        If(BinaryOp("<", Id("a"), Id("b")), CallStmt(Id("print"), [StringLiteral("a < b")]),
                            [(BinaryOp(">", Id("a"), Id("b")), CallStmt(Id("print"), [StringLiteral("a > b")]))], 
                            CallStmt(Id("print"), [StringLiteral("a = b")])), 
                        Return(NumberLiteral(0.0))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 374))

    
    def test_75(self):
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
        expect = str(Program([
                    FuncDecl(Id("call"), [], Block([
                        Continue(), 
                        Continue(), 
                        Break(), 
                        Break(), 
                        Assign(Id("no"), Id("yes")),
                        Block([Return(NumberLiteral(0.0))]), 
                        For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)), BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), NumberLiteral(1.0))),
                            CallStmt(Id("print"), [Id("i")])), 
                        Return(NumberLiteral(0.0))
                    ])), 
                    FuncDecl(Id("main"), [], Block([CallStmt(Id("call"), [])]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_76(self):
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
        self.assertTrue(TestAST.test(input, expect, 377))
    
    
    def test_77(self):
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
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_78(self):
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
                    FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()), VarDecl(Id("a"), StringType()), VarDecl(Id("a"), ArrayType([2.0], BoolType()))], Block([
                        For(Id("i"), NumberLiteral(0.0), NumberLiteral(1.0), 
                            For(Id("j"), NumberLiteral(0.0), UnaryOp('-', NumberLiteral(1.0)), Block([]))),
                    ])),
                    FuncDecl(Id("foo"), [VarDecl(Id("arr"), ArrayType([1.0, 2.0], NumberType())), VarDecl(Id("arr"), ArrayType([1.0, 9.0], StringType()))], Return(None))
                ]))
        self.assertTrue(TestAST.test(input, expect, 378))
    
    
    def test_79(self):
        input = """
            var a <- foo(1 + 1, foo(100)[2, 1 + 1], foo([1, 9], [0, 9]))
        """
        expect = str(Program([
                    VarDecl(Id("a"), None, "var", CallExpr(Id("foo"), [
                        BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), 
                        ArrayCell(CallExpr(Id("foo"), [NumberLiteral(100.0)]), [NumberLiteral(2.0), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0))]), 
                        CallExpr(Id("foo"), [ArrayLiteral([NumberLiteral(1.0), NumberLiteral(9.0)]), ArrayLiteral([NumberLiteral(0.0), NumberLiteral(9.0)])])
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_80(self):
        input = input = """
            func main()
            begin
            if ("p" ... "p" == "L") gpa <- 10.0
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(BinaryOp("...", StringLiteral("p"), BinaryOp("==", StringLiteral("p"), StringLiteral("L"))), Assign(Id("gpa"), NumberLiteral(10.0)), [], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_81(self):
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
        expect = str(Program([
                    FuncDecl(Id("square"), [VarDecl(Id("x"), NumberType(), None, None)], Return(BinaryOp("*", Id("x"), Id("x")))), 
                    FuncDecl(Id("cube"), [VarDecl(Id("x"), NumberType(), None, None)], Return(BinaryOp("*", BinaryOp("*", Id("x"), Id("x")), Id("x")))), 
                    FuncDecl(Id("main"), [], Block([
                        VarDecl(Id("value"), None, "var", NumberLiteral(4.0)), 
                        VarDecl(Id("squared"), None, "var", CallExpr(Id("square"), [Id("value")])), 
                        VarDecl(Id("cubed"), None, "var", CallExpr(Id("cube"), [Id("value")])), 
                        CallStmt(Id("print"), [StringLiteral("Square:"), Id("squared"), StringLiteral(" Cube:"), Id("cubed")])
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 381))
    
    
    def test_82(self):
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
        expect = str(Program([
                    FuncDecl(Id("multiply"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Block([
                        Return(BinaryOp("*", Id("a"), Id("b")))
                    ])), 
                    FuncDecl(Id("calculate"), [VarDecl(Id("x"), NumberType(), None, None), VarDecl(Id("y"), NumberType(), None, None)], Block([
                        VarDecl(Id("result"), None, "var", BinaryOp("+", CallExpr(Id("multiply"), [Id("x"), Id("y")]), CallExpr(Id("multiply"), [BinaryOp("+", Id("x"), Id("y")), BinaryOp("-", Id("y"), Id("x"))]))), 
                        Return(Id("result"))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_83(self):
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
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_84(self):
        input = """func main() begin
            string s <- \"abc\\n\\t'\"\"
            string ss <- \"123.\\t\\b\"
            s <- s...ss
            s <- s...ss
            return s
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("s"), StringType(), None, StringLiteral("abc\\n\\t'\"")), VarDecl(Id("ss"), StringType(), None, StringLiteral("123.\\t\\b")), Assign(Id("s"), BinaryOp("...", Id("s"), Id("ss"))), Assign(Id("s"), BinaryOp("...", Id("s"), Id("ss"))), Return(Id("s"))]))]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_85(self):
        input = """string strarr[3] <- [\"123E.-3\",\"hello\"...\"world\",\"\\n\\b\\f\"]
        number numarr[3] <- [3+4,3-1*23,20.3+12.7+1.]
        func main()
        begin
            for i until i>=size(strarr) by 1
                print(extract(strarr[i],numarr[i]))
        end

        func extract(string a, number b)
            return a[b]
        """
        expect = str(Program([
                    VarDecl(Id("strarr"), ArrayType([3.0], StringType()), None, ArrayLiteral([StringLiteral("123E.-3"), BinaryOp("...", StringLiteral("hello"), StringLiteral("world")), StringLiteral("\\n\\b\\f")])), 
                    VarDecl(Id("numarr"), ArrayType([3.0], NumberType()), None, ArrayLiteral([BinaryOp("+", NumberLiteral(3.0), NumberLiteral(4.0)), BinaryOp("-", NumberLiteral(3.0), BinaryOp("*", NumberLiteral(1.0), NumberLiteral(23.0))), BinaryOp("+", BinaryOp("+", NumberLiteral(20.3), NumberLiteral(12.7)), NumberLiteral(1.))])), 
                    FuncDecl(Id("main"), [], Block([
                        For(Id("i"), BinaryOp(">=", Id("i"), CallExpr(Id("size"), [Id("strarr")])), NumberLiteral(1.0), CallStmt(Id("print"), [CallExpr(Id("extract"), [ArrayCell(Id("strarr"), [Id("i")]), ArrayCell(Id("numarr"), [Id("i")])])]))
                    ])), 
                    FuncDecl(Id("extract"), [VarDecl(Id("a"), StringType()), VarDecl(Id("b"), NumberType())], Return(ArrayCell(Id("a"), [Id("b")])))
                ]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_86(self):
        input = """func main() 


        begin


            number au<-100
            var bc<--2e-3
            number c
            c<-au*bc+100/1000
            number arr[4] <- [au,bc,c,au+bc+c]

            return arr[3]
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("au"), NumberType(), None, NumberLiteral(100.0)), VarDecl(Id("bc"), None, "var", UnaryOp("-", NumberLiteral(2e-3))), VarDecl(Id("c"), NumberType()), Assign(Id("c"), BinaryOp("+", BinaryOp("*", Id("au"), Id("bc")), BinaryOp("/", NumberLiteral(100.0), NumberLiteral(1000.0)))), VarDecl(Id("arr"), ArrayType([4.0], NumberType()), None, ArrayLiteral([Id("au"), Id("bc"), Id("c"), BinaryOp("+", BinaryOp("+", Id("au"), Id("bc")), Id("c"))])), Return(ArrayCell(Id("arr"), [NumberLiteral(3.0)]))]))]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_87(self):
        input = """func main() begin
            if ((a <= b) and (b != c) or (d > e)) x <- 1
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(BinaryOp("or", BinaryOp("and", BinaryOp("<=", Id("a"), Id("b")), BinaryOp("!=", Id("b"), Id("c"))), BinaryOp(">", Id("d"), Id("e"))), Assign(Id("x"), NumberLiteral(1.0)), [])]))]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_88(self):
        input = """func main() begin

            a <- true or false and not false
            return a or 1
        end

        

        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Assign(Id("a"), BinaryOp("and", BinaryOp("or", BooleanLiteral(True), BooleanLiteral(False)), UnaryOp("not", BooleanLiteral(False)))), Return(BinaryOp("or", Id("a"), NumberLiteral(1.0)))]))]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_89(self):
        input = """func main() begin
            number a[2, 3] <- [[1,2,3],[4,5,6]]
            for i until i >= 2 by 1 begin
                for j until j >= 3 by 1 begin
                    a[i, j] <- i + j
                end
            end
        end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])])), 
                        For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(2.0)), NumberLiteral(1.0), Block([
                            For(Id("j"), BinaryOp(">=", Id("j"), NumberLiteral(3.0)), NumberLiteral(1.0), Block([
                                Assign(ArrayCell(Id("a"), [Id("i"), Id("j")]), BinaryOp("+", Id("i"), Id("j")))
                            ]))
                        ]))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_90(self):
        input = """func main() begin
            printString(\"---*---\")
            printString(\"--***--\")
            printString(\"-*****-\")
            printString(\"-******\")
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([CallStmt(Id("printString"), [StringLiteral("---*---")]), CallStmt(Id("printString"), [StringLiteral("--***--")]), CallStmt(Id("printString"), [StringLiteral("-*****-")]), CallStmt(Id("printString"), [StringLiteral("-******")])]))]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_91(self):
        input = """func funct(number _, number __) begin
            s <- 3
        end

        func main() begin
            a[1+2,2*3] <- _ + __
        end

        """
        expect = str(Program([FuncDecl(Id("funct"), [VarDecl(Id("_"), NumberType()), VarDecl(Id("__"), NumberType())], Block([Assign(Id("s"), NumberLiteral(3.0))])), FuncDecl(Id("main"), [], Block([Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), BinaryOp("*", NumberLiteral(2.0), NumberLiteral(3.0))]), BinaryOp("+", Id("_"), Id("__")))]))]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_92(self):
        input = """func main(number a, number b) begin
            if (a+b != x) begin
                return a+b
            end
            else begin
                return a-b
            end
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), VarDecl(Id("b"), NumberType())], Block([If(BinaryOp("!=", BinaryOp("+", Id("a"), Id("b")), Id("x")), Block([Return(BinaryOp("+", Id("a"), Id("b")))]), [], Block([Return(BinaryOp("-", Id("a"), Id("b")))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_93(self):
        input = """func main() begin
            if (abc >= 234 and not def) begin
                _var <- arr[1, 5]
            end
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(BinaryOp(">=", Id("abc"), BinaryOp("and", NumberLiteral(234.0), UnaryOp("not", Id("def")))), Block([Assign(Id("_var"), ArrayCell(Id("arr"), [NumberLiteral(1.0), NumberLiteral(5.0)]))]), [])]))]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_94(self):
        input = """func main() begin
            number a_1 <- funcfunc()
            for a_1 until exp = 1000 and not exp2 by a + arr[0] begin
                return 
            end
        end

        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        VarDecl(Id("a_1"), NumberType(), None, CallExpr(Id("funcfunc"), [])), 
                        For(Id("a_1"), BinaryOp("=", Id("exp"), BinaryOp("and", NumberLiteral(1000.0), UnaryOp("not", Id("exp2")))), BinaryOp("+", Id("a"), ArrayCell(Id("arr"), [NumberLiteral(0.0)])), 
                            Block([Return()]))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_95(self):
        input = """func main() begin
            number a <- foo(bar(1 + 2, 3 * 4), baz(5 - 6))
            bool b <- ((a or false) and true) or not a
            number c[4, 3] 
            c <- temp(a, b, (a + b - 2 * a - 3 * b), foo((a * b), a + b))
            var d <- c[2, 0] + c[3, 1] - c[2, 2]
            return d
        end

        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        VarDecl(Id("a"), NumberType(), None, CallExpr(Id("foo"), [CallExpr(Id("bar"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), BinaryOp("*", NumberLiteral(3.0), NumberLiteral(4.0))]), CallExpr(Id("baz"), [BinaryOp("-", NumberLiteral(5.0), NumberLiteral(6.0))])])), 
                        VarDecl(Id("b"), BoolType(), None, BinaryOp("or", BinaryOp("and", BinaryOp("or", Id("a"), BooleanLiteral(False)), BooleanLiteral(True)), UnaryOp("not", Id("a")))), 
                        VarDecl(Id("c"), ArrayType([4.0, 3.0], NumberType())), 
                        Assign(Id("c"), CallExpr(Id("temp"), [Id("a"), Id("b"), BinaryOp("-", BinaryOp("-", BinaryOp("+", Id("a"), Id("b")), BinaryOp("*", NumberLiteral(2.0), Id("a"))), BinaryOp("*", NumberLiteral(3.0), Id("b"))), CallExpr(Id("foo"), [BinaryOp("*", Id("a"), Id("b")), BinaryOp("+", Id("a"), Id("b"))])])), 
                        VarDecl(Id("d"), None, "var", BinaryOp("-", BinaryOp("+", ArrayCell(Id("c"), [NumberLiteral(2.0), NumberLiteral(0.0)]), ArrayCell(Id("c"), [NumberLiteral(3.0), NumberLiteral(1.0)])), ArrayCell(Id("c"), [NumberLiteral(2.0),NumberLiteral(2.0)]))), 
                        Return(Id("d"))
                        ]))]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_96(self):
        input = """func main() begin
        end
        func main() begin
            return true and not (false and \"NA\")
        end

        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([])), FuncDecl(Id("main"), [], Block([Return(BinaryOp("and", BooleanLiteral(True), UnaryOp("not", BinaryOp("and", BooleanLiteral(False), StringLiteral("NA")))))]))]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_97(self):
        input = """func main() begin
            if (a = 1) begin
                if (b = 2) begin
                    x <- 1
                end 
                else begin
                    x <- 0
                end
            end 
            else begin
                x <- -1
            end
        end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(BinaryOp("=", Id("a"), NumberLiteral(1.0)), Block([If(BinaryOp("=", Id("b"), NumberLiteral(2.0)), Block([Assign(Id("x"), NumberLiteral(1.0))]), [], Block([Assign(Id("x"), NumberLiteral(0.0))]))]), [], Block([Assign(Id("x"), UnaryOp("-", NumberLiteral(1.0)))]))]))]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_98(self):
        input = """func fibo(number n) begin
            if (n <= 2) return 1
            number f1 <- 0
            number f2 <- 1
            number f3 <- f1 + f2
            number i <- 2
            for i until i > n by 1 begin
                f3 <- f1 + f2
                f1 <- f2
                f2 <- f3
            end
            return f3
        end
        func main() begin 
            return fibo(50)
        end
        """
        expect = str(Program([
                    FuncDecl(Id("fibo"), [VarDecl(Id("n"), NumberType())], Block([
                        If(BinaryOp("<=", Id("n"), NumberLiteral(2.0)), Return(NumberLiteral(1.0)), []), 
                        VarDecl(Id("f1"), NumberType(), None, NumberLiteral(0.0)), 
                        VarDecl(Id("f2"), NumberType(), None, NumberLiteral(1.0)), 
                        VarDecl(Id("f3"), NumberType(), None, BinaryOp("+", Id("f1"), Id("f2"))), 
                        VarDecl(Id("i"), NumberType(), None, NumberLiteral(2.0)), 
                        For(Id("i"), BinaryOp(">", Id("i"), Id("n")), NumberLiteral(1.0), Block([
                            Assign(Id("f3"), BinaryOp("+", Id("f1"), Id("f2"))), 
                            Assign(Id("f1"), Id("f2")), 
                            Assign(Id("f2"), Id("f3"))
                        ])), 
                        Return(Id("f3"))])), 
                    FuncDecl(Id("main"), [], Block([Return(CallExpr(Id("fibo"), [NumberLiteral(50.0)]))]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_99(self):
        input = """func main() begin
            x <- 10
            i <- 0
            for i until i > x by x-2
                if (i >= 1) break
                elif (x <= 1) continue
                elif (a[10,2+3] < b[1,2-2,3*4]) funcfunc(1,2,3)
                else i <- i*10
        end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        Assign(Id("x"), NumberLiteral(10.0)), 
                        Assign(Id("i"), NumberLiteral(0.0)), 
                        For(Id("i"), BinaryOp(">", Id("i"), Id("x")), BinaryOp("-", Id("x"), NumberLiteral(2.0)), 
                            If(BinaryOp(">=", Id("i"), NumberLiteral(1.0)), Break(), [
                                (BinaryOp("<=", Id("x"), NumberLiteral(1.0)), Continue()), 
                                (BinaryOp("<", ArrayCell(Id("a"), [NumberLiteral(10.0), BinaryOp("+", NumberLiteral(2.0), NumberLiteral(3.0))]), ArrayCell(Id("b"), [NumberLiteral(1.0), BinaryOp("-", NumberLiteral(2.0), NumberLiteral(2.0)), BinaryOp("*", NumberLiteral(3.0), NumberLiteral(4.0))])), CallStmt(Id("funcfunc"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
                            ], Assign(Id("i"), BinaryOp("*", Id("i"), NumberLiteral(10.0)))))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_100(self):
        input = """func main() begin
                for i until temp1*temp2%(temp3-temp4)=temp5 by 1e-3 begin
                if (i%x=1) then<-5
                elif (i%x=2) eles<-10
                else i<-i/2
            end
        end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                        For(Id("i"), BinaryOp("=", BinaryOp("%", BinaryOp("*", Id("temp1"), Id("temp2")), BinaryOp("-", Id("temp3"), Id("temp4"))), Id("temp5")), NumberLiteral(0.001), Block([
                            If(BinaryOp("=", BinaryOp("%", Id("i"), Id("x")), NumberLiteral(1.0)), Assign(Id("then"), NumberLiteral(5.0)), [
                                (BinaryOp("=", BinaryOp("%", Id("i"), Id("x")), NumberLiteral(2.0)), Assign(Id("eles"), NumberLiteral(10.0)))
                                ], Assign(Id("i"), BinaryOp("/", Id("i"), NumberLiteral(2.0))))
                        ]))
                    ]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 400))