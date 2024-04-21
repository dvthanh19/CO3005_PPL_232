import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    ################################################################
    ###### OFFICIAL TEST
    ################################################################
    def test_1(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = """number a
        func main() begin
        end
        func readNumber() begin
        end
        """
        expect = "Redeclared Function: readNumber"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        input = """func foo()
        func main() begin
        end
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """number a
        var a <- 0
        func main() begin
        end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_5(self):
        input = """number a <- "x"
        func main () begin
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(x))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_6(self):
        input = """string a <- "x" ... 8
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., StringLit(x), NumLit(8.0))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_7(self):
        input = """number a[3] <- [1,2,"x"]
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), StringLit(x))"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_8(self):
        input = """number a <- -"x"
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: UnaryOp(-, StringLit(x))"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_9(self):
        input = """number a <- not "a"
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: UnaryOp(not, StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test_10(self):
        input = """string a[3] <- [1,2,3]
        func main () begin
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], StringType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        input = """dynamic a
        number b <- a + 5
        func main () begin
        string c <- a
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c), StringType, None, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        input = """var a <- "x"
        number b <- a
        func main () begin
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), NumberType, None, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = """func a (number x) begin
        end
        number b <- a
        func main () begin
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_14(self):
        input = """number a[3] <- [1,2,3]
        string b <- a[2] + 5
        func main () begin
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, BinaryOp(+, ArrayCell(Id(a), [NumLit(2.0)]), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        input = """func lessThan (number a, number b) begin
        return a < b
        end
        bool b <- lessThan(1)
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(lessThan), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_16(self):
        input = """func lessThan (number a, number b) begin
        return a < b
        end
        bool b <- lessThan(1, "a")
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(lessThan), [NumLit(1.0), StringLit(a)])"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """func lessThan (number a, number b) begin
        var c <- a < b
        end
        bool b <- lessThan(1, 2)
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(lessThan), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        input = """func lessThan (number a, number b) begin
        var c <- a < b
        return c
        end
        func main () begin
        string b <- lessThan(1, 2)
        return
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, CallExpr(Id(lessThan), [NumLit(1.0), NumLit(2.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        input = """func lessThan (number a, number b) begin
        var c <- a < b
        return c
        end
        func main () begin
        string a
        var c <- lessThan(a, 2)
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(lessThan), [Id(a), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input = """
        func main () begin
        dynamic a
        var b <- a
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input = """
        func main () begin
        dynamic a
        dynamic b
        b <- a
        end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        input = """
        func main () begin
        string a
        var b <- a
        bool c <- b
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c), BoolType, None, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        input = """
        func main () begin
        string a
        dynamic b
        b <- a
        bool c <- b
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c), BoolType, None, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        input = """func compare (number a, number b) begin
        if (a > b)
        return "more"
        else return 3
        end
        func main () begin
        end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        input = """number a[2,3] <- [[1,2,3],[2]]
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        input = """number a[2,3] <- [[1,2,3],[2,3,4]]
        func main () begin
        var i <- 2
        for i until i > x / 2 by 1
        begin
            if (x % i = 0) return false
        end
        end
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        input = """
        func main () begin
        var i <- 2
        dynamic x
        for i until x by 1
        begin
            if (x % i = 0) return false
        end
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(%, Id(x), Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        input = """
        func main () begin
        var i <- 2
        dynamic x
        for i until x by 1
        begin
            if (4 % i = 0) break
        end
        continue
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_29(self):
        input = """
        func main () begin
        var i <- 0
        dynamic x
        for i until i > 3 by 1
        begin
            x <- 5
        end
        x <- x ... "a"
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(x), StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        input = """
        func main () begin
        var i <- 0
        for i until i > 3 by 1
        begin
            var a <- 5
        end
        a <- a + 8
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_31(self):
        input = """
        func main () begin
        var a <- 5
        begin
        var a <- "hello"
        end
        a <- "no"
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(no))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        input = """number a <- 7
        func main () begin
        a <- 14
        var a <- true
        if (a = 5) return
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(=, Id(a), NumLit(5.0))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_33(self):
        input = """func isTrue()
        func main() begin
        isTrue()
        end
        func isTrue() begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_34(self):
        input = """func isPrime(number x)
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
        func main()
        begin
            number x <- readNumber()
            if (isPrime(x)) writeString("Yes")
                else writeString("No")
            writeString(4)
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [NumLit(4.0)])"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_34(self):
        input = """func isPrime(number x)
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
        func main()
        begin
            number x <- readNumber()
            if (isPrime(x)) writeString("Yes")
                else writeString("No")
            writeString(4)
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [NumLit(4.0)])"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_35(self):
        input = """func areDivisors(number num1, number num2) return 
        func main()
        begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(areDivisors), [Id(num1), Id(num2)])"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        input = """func fibonacci(number x) begin
        var i <- 0
        number a <- 0
        number b <- 1
        for i until i = a by 1 begin
            var c <- a + b
            a <- b
            b <- c
        end
        return a
        end 
        func main() begin
        number a <- readNumber()
        var b <- writeNumber(fibonacci(a))
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(writeNumber), [CallExpr(Id(fibonacci), [Id(a)])])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input = """
        func main() begin
        string a <- readString()
        if (a == "1") writeString("Welcome")
        elif (a == "2") writeString("Thank you")
        elif (a == "4") a <- 5
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(5.0))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        input = """
        func main() begin
        dynamic a
        a <- (a + 4 > 4) or (5 = 4)
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BinaryOp(or, BinaryOp(>, BinaryOp(+, Id(a), NumLit(4.0)), NumLit(4.0)), BinaryOp(=, NumLit(5.0), NumLit(4.0))))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        input = """
        func main() begin
        dynamic a <- [1,2,3]
        number b[5] <- a
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([5.0], NumberType), None, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        input = """func inc (number x)
        func main() begin
        var a <- inc(2) ... "abc"
        end
        func inc (number y) return y + 1
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(+, Id(y), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_41(self):
        input = """func inc (number x) return 0
        number inc
        func main() begin
        var a <- inc(2) ... "abc"
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., CallExpr(Id(inc), [NumLit(2.0)]), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        input = """dynamic a
        func foo() return a
        func main()
        begin
            number num <- foo()
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        input = """
        func foo() begin
        number x
        end
        func main()
        begin
            number num <- foo()
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        input = """
        func main()
        begin
            var c <- c
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        input = """
            func foo()
            begin
                number a <- 10
                for a until a > 10 by 1
                begin
                    number b <- 20
                end
                
                if (a = 1)
                begin
                    number c <- 30
                    return true
                end
                elif (a > 1)
                    number e <- 20
                else
                begin
                    number d <- 40
                    return 1
                end
            end
            
            func main()
            begin
                bool a <- foo()
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_46(self):
        input = """
        func main()
        begin
            dynamic x
            x <- (x = 1) or ("abc" == "abc")
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(==, StringLit(abc), StringLit(abc))))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        input = """
        func a (number x) return x
        var a <- "a"
        func main()
        begin
            number b <- a(2)
            b <- a
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_48(self):
        input = """
        string a[3]
        func main()
        begin
            a <- [1,2,3]
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_49(self):
        input = """
        string a[3]
        func main()
        begin
            number c[2, 3, 4] <- [[[1,2,3,4],[5,6,7,8],[1,2,3,4]], [[1,2,3,4],[5,6,7,8],[1,2,3,4]]]
            if (true) return [1,2,3]
            else return [1,2]
        end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_50(self):
        input = """
        number b <- 1
        number a[2] <- [1,b]
        func main() begin
            a <- [[1,2,true],"hello"]
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_51(self):
            input = """
                dynamic a
                dynamic b
                dynamic c
                dynamic d
                dynamic e
                dynamic f
                dynamic g
                dynamic h
                func main() begin
                    number x[2, 2, 2] <- [[[a, b], [c, d]], [[e, f], [g, h]]]
                end
            """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 451))

    def test_52(self):
        input = """
            func main()
            begin
                var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
                writeNumber(x)
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_53(self):
        input = """
            func main()
            begin
                var x <- [[1, 2, 3], [4, [5, 6]]]
                writeNumber(x)
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(4.0), ArrayLit(NumLit(5.0), NumLit(6.0)))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_54(self):
        input = """
            func main()
            begin
                dynamic y
                var x <- [[1, 2, 3], y]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))

    ########## TEST NÀY LÀ TEST INFER ARRAY CELL NHA (TUỲ IDEA IMPLEMENT MÀ NHẬN INFER HAY KHÔNG NHA)
    def test_55(self):
        input = """
            func main() begin
                dynamic a
                number b[2,1] <- [a[0],1]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([2.0, 1.0], NumberType), None, ArrayLit(ArrayCell(Id(a), [NumLit(0.0)]), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    ########## TEST NÀY LÀ TEST INFER ARRAY CELL NHA (TUỲ IDEA IMPLEMENT MÀ NHẬN INFER HAY KHÔNG NHA)
    def test_56(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[b, 1]
                b <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_57(self):
        input = """
            number a
            func f(string a) begin
                number a <- a + a
                string x <- x ... "hello"
                return x
            end
            func main() begin
                string a <- f(a)
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_58(self):
        input = """
            func foo(number a[2,2]) return
        
            func main()
            begin
                dynamic x
                foo([[x,x], [x,x]])
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_59(self):
        input = """
            func foo(number a)

            func main() begin
            var a <- foo(foo(1))
            end

            func foo(number a) return 1
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_60(self):
        input = """
            func main() begin
                var x <- [1, x]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), None, var, ArrayLit(NumLit(1.0), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        input = """
            func foo(number a)

            func main() begin
                dynamic a
                number x[6]
                for a until foo(1) >= 10 by x[5] continue
            end

            func foo(number b) return 1
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_62(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b >= 10 by c continue
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_63(self):
        input = """
            dynamic a
            dynamic b
            dynamic c

            func foo(number d)

            number x[2, 3] <- c

            func main() begin
                c[1] <- [a, b, foo(1)]
            end

            func foo(number d) return 1 + 1
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 4630))

    def test_64(self):
        input = """
            dynamic a
            dynamic b
            func main() begin
                number x[2] <- [a,b]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test_65(self):
        input = """
            dynamic a
            string x <- [a]
            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), StringType, None, ArrayLit(Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_66(self):
        input = """
            func foo() return true

            func foo1() begin
                if (true) return 1 + foo()
            end

            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_67(self):
        input = """
            func main() begin
                string a
                if (true) number a <- 1
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_68(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                number x[2, 1] <- [a, [b]]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_69(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                dynamic c
                number x[2] <- [a, [b, c]]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), ArrayType([2.0], NumberType), None, ArrayLit(Id(a), ArrayLit(Id(b), Id(c))))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_70(self):
        input = """
            func foo(string x) return ["hello", "hi"]

            func main() begin
                dynamic a
                string b <- a ... foo(a)[1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_71(self):
        input = """
            func foo(string x) return ["hello", "hi"]

            func main() begin
                dynamic a
                string b <- a ... foo(a)[1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_72(self):
        input = """
            func foo(string a, bool b) return [[1, 2], [1, 2]]
            func main() begin
                dynamic a
                dynamic b   
                number x <- 1 + foo(a, b)[1, 2]
                a <- "hello"
                b <- not (a == "hi")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))

    ########## TEST NÀY LÀ TEST INFER ARRAY CELL NHA (TUỲ IDEA IMPLEMENT MÀ NHẬN INFER HAY KHÔNG NHA)
    def test_73(self):
        input = """
            func main() begin
                dynamic a
                number b <- a[2]
                a <- ["hello", "world"]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(StringLit(hello), StringLit(world)))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    ########## TEST NÀY LÀ TEST INFER ARRAY CELL NHA (TUỲ IDEA IMPLEMENT MÀ NHẬN INFER HAY KHÔNG NHA)
    def test_74(self):
        input = """
            func main() begin
                dynamic a
                number b <- a[2]
                a <- [1, 2, 3]
                a <- [4, 5, 6, 7]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0), NumLit(7.0)))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_75(self):
        input = """
        func foo()
        begin
            return
        end
        
        func main()
        begin
            bool a <- foo()
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_76(self):
        input = """
            func main() begin
                dynamic a
                number b
                if (a) begin
                    bool b <- true
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_77(self):
        input = """
            func foo(number a, string b)
            begin
                dynamic a
                return a

                return b
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_78(self):      
        input = """
            func main() begin
                dynamic x
                var y <- not not not x
                x <- y
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test_79(self):
        input = """
            func main() begin
                dynamic x
                var y <- ----------x
                x <- y
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_80(self):
        input = """
            func main() begin
                var x <- - x + 1 and true or false
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, BinaryOp(+, UnaryOp(-, Id(x)), NumLit(1.0)), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_81(self):
        input = """
        func main()
            begin
                dynamic num
                bool arr <- num and (num > num)
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_82(self):
        input = """
            func main() begin
                number a[2]
                dynamic b
                dynamic c
                number x <- a[-b]
                a <- [not c and true or not false and 1 > 2, x - 3 - 3]
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, BinaryOp(or, BinaryOp(and, UnaryOp(not, Id(c)), BooleanLit(True)), UnaryOp(not, BooleanLit(False))), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_83(self):
        input = """
            func main() begin
                string a[2]
                dynamic b
                var x <- a[-----b % 3]
                dynamic c <- x == x
                var y <- [not c and true or not false and (1 > 2), (x ... x) == x]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 483))

    # ...
    def test_84(self):
        input = """
            func main() begin
                dynamic x
                dynamic y
                number a[2] <- [1, [x, y]] 
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(y)))"
        # Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))
        self.assertTrue(TestChecker.test(input, expect, 484))

    # ... 
    # def test_85(self):
    #     input = """
    #         func main() begin
    #             dynamic x
    #             string y[2] <- [[x], x]
    #         end
    #     """
    #     expect = "Type Cannot Be Inferred: VarDecl(Id(y), ArrayType([2.0], StringType), None, ArrayLit(ArrayLit(Id(x)), Id(x)))"
    #     self.assertTrue(TestChecker.test(input, expect, 485))

    def test_86(self):
        input = """
            func foo() return [1, 2]
            func main() begin
                dynamic x <- [1, foo()[1]]
                x <- foo()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))

    ########## TEST NÀY LÀ TEST INFER ARRAY CELL NHA (TUỲ IDEA IMPLEMENT MÀ NHẬN INFER HAY KHÔNG NHA)
    def test_87(self):
        input = """
            func foo()
            func main() begin
                number a <- foo()[2]
                number b[3]
                b <- foo()
            end
            func foo() return [1, 2, 3]
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 536))

    def test_88(self):
        input = """
        dynamic a
        number b <- a[0]
        string c <- a[1]
        func main()
        begin
            a <- [1,2,3]
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c), StringType, None, ArrayCell(Id(a), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_89(self):
        input = """
        func foo(number a)
        func foo(string a) begin
        end
        func main()
        begin
        end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self):
        input = """func foo()
        func foo()
        func foo() begin
        end
        func main()
        begin
        end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_91(self):
        input = """
        func main()
        begin
            dynamic a
            string x <- [a]
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), StringType, None, ArrayLit(Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_92(self):
        input = """func foo() return [[1,2],[3,4]]
        func main()
        begin
            number a <- foo()[1,2]
        end
        func abc(number a, number a) return a
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_93(self):
        input = """
        dynamic a
        dynamic b <- [a, [1,2,3]]
        func main()
        begin
            a <- [2,3,4]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_94(self):
        input = """
        func foo(number a, number b)

        func main()
        begin
            return 1 + foo(1, 2)
        end
        func foo(number a, number b)
        begin
            return "hello"
        end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(hello))"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_95(self):
        input = """
        dynamic a
        func main() begin
            if (true) return 1
            else return a
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_96(self):
        input = """
        dynamic a
        func main() begin
            if (true) return a
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_97(self):
        input = """
        dynamic a
        func main() begin
        if ([a]) return
        end
        """
        expect = "Type Cannot Be Inferred: If((ArrayLit(Id(a)), Return()), [], None)"
        # Type Mismatch In Statement: If((ArrayLit(Id(a)), Return()), [], None)
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_98(self):
        input = """
        number x[3,3] <- [[1,2,[1,3,4]],[2,4,6],[3,5]]
        func main() begin
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), ArrayLit(NumLit(1.0), NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_99(self):
        input = """
        dynamic a
        dynamic b
        dynamic c
        number x[3,3] <- [a,b,c]
        func main() begin
            a <- [1,2,3]
            b <- [2,4,6]
            c <- [3,5]
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), ArrayLit(NumLit(3.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 499))
        
    def test_100(self):
        input = """
        dynamic a
        number b[2] <- [a, 1]
        func main() begin
            a <- "hello"
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(hello))"
        self.assertTrue(TestChecker.test(input, expect, 500))
















    ################################################################
    # DƯỚI ĐÂY LÀ TEST TOÀN BỘ BÀI, BỎ COMMENT HẾT TẤT CẢ ĐỂ TEST HẾT 1 THỂ NẾU MUỐN 

    def test_no_entry_point(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_1_No_entry_point(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
        
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
        
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
        input = """
            number VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_2_NoDefinition(self):
        input = """
            func foo(number a)
            func foo(number a) return     
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))

        input = """
            func foo(number a) return   
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
        
        input = """
            func foo(number a) 
        
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test_3_Redeclared(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
        input = """
            func foo() return
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
        input = """
            func foo() return
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 414))
        
        input = """
            number foo
            func foo() return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                end
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                    string a
                end
                
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                string c
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c, string c)
            begin
            end
            
            func main() return
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 421))
        
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                begin
                    number a
                end
                number a
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
        
        input = """
            func foo(number a) 
            func foo(number b) return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))
        
        input = """
            func foo(number a) 
            func foo(string a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
        input = """
            func foo(number a) 
            func foo(number a, string c) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
        input = """
            func foo(number a, string c) 
            func foo(number a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test_3_Undeclared(self):
        input = """
            number a <- a
            func main() begin
                number b <- a
                number c <- e
            end
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
        input = """
            func a() return 1
            func main() begin
                number b <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 427))
        
        input = """
            func a() return 1
            func main() begin
                number a
                begin 
                    number d
                end
                number b <- a
                number c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 428))
        
        # input = """
        #     func a() begin
        #         a()
        #     end
        #     func main() begin
        #         a()
        #         b()
        #     end
        # """
        # expect = "Undeclared Function: b"
        # self.assertTrue(TestChecker.test(input, expect, 429))
        
        input = """
            func a() return
            func main() begin
                number a
                a()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
        
        input = """
            func a()
            func main() begin
                a()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_4_MustInLoop(self):
        input = """
            func main() begin
                var i <- 2
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    
                    for i until true by 1
                    begin
                        break
                        continue
                    end
                    break
                    continue
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))
        
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
        input = """
            func main() begin
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test_5_TypeCannotBeInferred(self):
        input = """
            dynamic VoTien
            var a <- VoTien

            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 435))
        
        input = """
            number VoTien
            var a <- VoTien
            number b <- a

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))
        
        input = """
            dynamic VoTien
            number a <- VoTien
            number b <- VoTien

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))
        
        input = """
            func foo() begin
                dynamic a
                return a
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
        input = """
            func foo() begin
                return 1
                dynamic a
                return a
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))
        
        input = """
            func foo() begin
                number a
                return a
                return 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))
        
        input = """
            func foo() begin
                dynamic a
                dynamic b
                a <- b
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 441))
        
        input = """
            func foo() begin
                number a
                dynamic b
                a <- b
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))
        
        input = """
            func foo() begin
                number a
                dynamic b
                b <- a
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_6_TypeMismatchInStatement(self):
        input = """
            number a <- "1"

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 444))
        
        input = """
            number a[1,2] <- [[1,2]]

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))
        
        input = """
            number a[1,2,3] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 446))

        input = """
            number a[1] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 447))       

        input = """
            func foo() return

            func main()begin
                foo()
                foo(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 448))    
        
        input = """
            func foo(number a) return

            func main()begin
                foo()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 449))     
        
        input = """
            func foo(number a) return

            func main()begin
                foo("1")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 450))    
        
        input = """
            func foo(number a) return

            func main()begin
                dynamic a
                foo(a)
                number c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))                

        input = """
            func main()begin
                dynamic a
                if (a) return
                a <- true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))     
        
        input = """
            func main()begin
                var a <- 1
                if (a) return
            end
        """
        expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 453))                 

        input = """
            func main()begin
                dynamic a
                if (a) begin
                    number a
                end
                elif (a) return
                else begin
                    number a
                end
                
                if(true) begin
                    number a
                end
                elif (1)
                begin 
                    number a
                end
            end
        """
        expect = "Type Mismatch In Statement: If((BooleanLit(True), Block([VarDecl(Id(a), NumberType, None, None)])), [(NumLit(1.0), Block([VarDecl(Id(a), NumberType, None, None)]))], None)"
        self.assertTrue(TestChecker.test(input, expect, 454)) 
        
        input = """
            func foo() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b by c return
                a <- 1
                b <- true
                c <- 1
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))   
        
        input = """
            func foo() begin
                var a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 456))    
        
        input = """
            func foo() begin
                dynamic a 
                var b <- 2
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 457))  

        input = """
            func foo() begin
                dynamic a 
                dynamic b
                var c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 458))    
        
        input = """
            func foo() begin
                number a
                return 1
                return a
                return "!"
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(!))"
        self.assertTrue(TestChecker.test(input, expect, 459))  
        
        
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 460))  

    def test_6_TypeMismatchInExpression(self):
        input = """
            func foo() return 1

            func main() begin
                var a <- foo()
                var b <- foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 462))
        
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 465))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + 1
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))
        
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- 1 + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
        

        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- - left
                left <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 469))
        
        input = """
            func main() begin
                number a[1,2]
                number b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- b[1]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, ArrayCell(Id(b), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 4710))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[b, 1]
                b <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a["1"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 473))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,2,3]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 474))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,3]
                c <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))
        
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1]
                c <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))
        
        # input = """
        #     func VoTien()
        #     func main() begin
        #         number VoTien_ <- VoTien()
        #     end
        #     func VoTien() begin
        #     end
        # """
        # # expect = "???"
        # expect = ""
        # self.assertTrue(TestChecker.test(input, expect, 477))
        
        input = """
            dynamic VoTien
            var x <- VoTien and (VoTien > VoTien)
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(VoTien), Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 478))

        input = """
            dynamic VoTien
            var x <- VoTien + VoTien * VoTien
            number y <- VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 479))
        
        input = """
            dynamic VoTien
            var x <- VoTien > VoTien ... VoTien < VoTien
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., BinaryOp(>, Id(VoTien), Id(VoTien)), BinaryOp(<, Id(VoTien), Id(VoTien)))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_7_full(self):
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) writeString("Yes")
                else writeString("No")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))
        
        input = """
            func isPrime(number x)
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))
        
        input = """
            var VoTien <- VoTien
            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(VoTien), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 483))

        # input = """
        #     func main() return main()
        # """
        # expect = "Type Cannot Be Inferred: Return(CallExpr(Id(main), []))"
        # self.assertTrue(TestChecker.test(input, expect, 484))
            
    def test_arraylit(self):
        
        input = """
            dynamic x
            number a <- [x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))"
        # Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))
        self.assertTrue(TestChecker.test(input, expect, 484))        
        
        input = """
            dynamic x
            number a[3] <- [x]
            func f()
            begin
                x <- [1,2,3]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 485))        
        
        input = """
            dynamic x
            number a[3] <- [x, 1, 2]
            func  main()
            begin
                x <- 1
            end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))     
        

        input = """
            dynamic x
            number a[3] <- [x, x, x]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))   
        
        input = """
            dynamic x
            number a[3] <- [x, x, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x), Id(x), StringLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 488))   
        
        input = """
            dynamic x
            number a[3] <- [x, 1, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), NumLit(1.0), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 489))  
        
        input = """
            dynamic x
            number a[3] <- [x, [x,x], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 490))  

        input = """
            dynamic x
            number a[3] <- [1, [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 4910))    
        
        input = """
            dynamic x
            number a[3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 492))     
        
        input = """
            dynamic x
            number a[3,3] <- [[1,2,3], x, x]
            func  main()
            begin
                x <- [1,2,3]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))     
        
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))  
        
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 495)) 
        
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 496)) 
        
        input = """
            dynamic x
            number a[1,1,1,1] <- [[[x]]]
            func  main()
            begin
                x <- [1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 4971)) 
        
        
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[[1,2], x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498)) 
        
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[x, x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499)) 
  
        input = """
            dynamic x
            var a <- [x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 500))  
        
        input = """
            func foo() begin
                dynamic x
                return [x]                
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 501))  
        
        input = """
            func foo() begin
                dynamic x
                return [x, [1,2]]                
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502))  
        
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[y], [y]]
                return x
                return [[1], [2]]
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
        self.assertTrue(TestChecker.test(input, expect, 503))  
        
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, y]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 504)) 
        
        
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, [y]]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 505)) 
        
        
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo(x)
                x <- [[2,2], [2,3]]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 506)) 
        
        # ...
        # input = """
        #     func foo(number a[2,2]) return
        #     func main() begin
        #         dynamic x
        #         foo([x])
        #         x <- [1]
        #     end
        # """
        # expect = "Type Mismatch In Statement: CallStmt(Id(foo), [ArrayLit(Id(x))])"
        # self.assertTrue(TestChecker.test(input, expect, 507)) 

        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 508)) 
        
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 509)) 
        
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo(x)
                x <- [1,2]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), ArrayLit(NumLit(1.0), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 510)) 

    def test_return(self):
        input = """
            func main() begin 
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 511))   

        input = """
            func main() begin 
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 512))   

        input = """
            func main() begin 
                return 1
                begin
                    return "string"
                end
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 513))    
        
        input = """
            func main() begin 
                dynamic i
                return 1
                return i
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 514))  
        
        input = """
            func fun() begin
                return 
                return
                return 1
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 515))       
        
        input = """
            func fun() begin
                return 1
                return "string"
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 516))    
        
        input = """
            func fun() begin
                number a[3]
                return [1, 4, 3]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 517))   
        
        input = """
            func fun() begin
                number a[2,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 518))    
        
        input = """
            func fun() begin
                number a[3,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 519))  
        
        input = """
            func fun() begin
                number a[2,2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 520))   
        
        input = """
            func fun() begin
                string a[2,2, 3]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 521))  
        
        input = """
            func fun() begin
                string a[2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 522))   
        
        input = """
            func fun() begin
                string a[1,1,1,1,1]
                return a
                return [[[[["1"]]]]]
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 523))     
        
        input = """
            func fun() begin
                return [1,2]
                return [3,4]
            end
            
            func fun1() begin
                return [[1,2], [3,4]]
                return [[1,5], [3,4]]
            end
            
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 524)) 
        
        
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun3()
            end
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(fun3), []))"
        self.assertTrue(TestChecker.test(input, expect, 525)) 
        
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun1()
            end
            func fun3() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 526)) 

        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               number a <- fun3()
            end
            func fun3() return "1"  
        """
        expect = "Type Mismatch In Statement: Return(StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 527)) 
        
                
        input = """
            func fun1() return [1,2]
            func fun2() return [3,4]
            func fun3()
            
            func main() begin 
               return fun1()
               return fun2()
               return fun3()
            end 
        """
        expect = "No Function Definition: fun3"
        self.assertTrue(TestChecker.test(input, expect, 528)) 
        

    def test_Assign(self):
        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                b <- c
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 529)) 
        

        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                a <- c
                b <- c
                return a
                return b
                return c
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 530))   
        
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                a <- c
                c <- b

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 531))   
        
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                c <- a
                b <- c

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 532))      
        
        input = """
            func main() begin 
                number a[1,3]
                dynamic c
                c <- [[1,2,3]]
                c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 533))   
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                c <- foo()
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(c), CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 534)) 
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [[1,2,3]]
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 535))
        
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [1,2,3]
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 535))

    ########################################################################
    # STRESS TEST BELOW, WARNINGGGGGGG

    def test_1(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_2(self):
        input = """number a
        func main() begin
        end
        func readNumber() begin
        end
        """
        expect = "Redeclared Function: readNumber"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_3(self):
        input = """func foo()
        func main() begin
        end
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_4(self):
        input = """number a
        var a <- 0
        func main() begin
        end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_5(self):
        input = """number a <- "x"
        func main () begin
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(x))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_6(self):
        input = """string a <- "x" ... 8
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., StringLit(x), NumLit(8.0))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_7(self):
        input = """number a[3] <- [1,2,"x"]
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), StringLit(x))"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_8(self):
        input = """number a <- -"x"
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: UnaryOp(-, StringLit(x))"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_9(self):
        input = """number a <- not "a"
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: UnaryOp(not, StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test_10(self):
        input = """string a[3] <- [1,2,3]
        func main () begin
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], StringType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        input = """dynamic a
        number b <- a + 5
        func main () begin
        string c <- a
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c), StringType, None, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        input = """var a <- "x"
        number b <- a
        func main () begin
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), NumberType, None, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_130(self):
        input = """func a (number x) begin
        end
        number b <- a
        func main () begin
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 4130))

    def test_131(self):
        input = """
        number b <- a + 5
        func main () begin
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 4131))

    def test_14(self):
        input = """number a[3] <- [1,2,3]
        string b <- a[2] + 5
        func main () begin
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, BinaryOp(+, ArrayCell(Id(a), [NumLit(2.0)]), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        input = """func lessThan (number a, number b) begin
        return a < b
        end
        bool b <- lessThan(1)
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(lessThan), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_16(self):
        input = """func lessThan (number a, number b) begin
        return a < b
        end
        bool b <- lessThan(1, "a")
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(lessThan), [NumLit(1.0), StringLit(a)])"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """func lessThan (number a, number b) begin
        var c <- a < b
        end
        bool b <- lessThan(1, 2)
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(lessThan), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        input = """func lessThan (number a, number b) begin
        var c <- a < b
        return c
        end
        func main () begin
        string b <- lessThan(1, 2)
        return
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, CallExpr(Id(lessThan), [NumLit(1.0), NumLit(2.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        input = """func lessThan (number a, number b) begin
        var c <- a < b
        return c
        end
        func main () begin
        string a
        var c <- lessThan(a, 2)
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(lessThan), [Id(a), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input = """
        func main () begin
        dynamic a
        var b <- a
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input = """
        func main () begin
        dynamic a
        dynamic b
        b <- a
        end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        input = """
        func main () begin
        string a
        var b <- a
        bool c <- b
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c), BoolType, None, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        input = """
        func main () begin
        string a
        dynamic b
        b <- a
        bool c <- b
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c), BoolType, None, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        input = """func compare (number a, number b) begin
        if (a > b)
        return "more"
        else return 3
        end
        func main () begin
        end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        input = """number a[2,3] <- [[1,2,3],[2]]
        func main () begin
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        input = """number a[2,3] <- [[1,2,3],[2,3,4]]
        func main () begin
        var i <- 2
        for i until i > x / 2 by 1
        begin
            if (x % i = 0) return false
        end
        end
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        input = """
        func main () begin
        var i <- 2
        dynamic x
        for i until x by 1
        begin
            if (x % i = 0) return false
        end
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(%, Id(x), Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        input = """
        func main () begin
        var i <- 2
        dynamic x
        for i until x by 1
        begin
            if (4 % i = 0) break
        end
        continue
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_29(self):
        input = """
        func main () begin
        var i <- 0
        dynamic x
        for i until i > 3 by 1
        begin
            x <- 5
        end
        x <- x ... "a"
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(x), StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        input = """
        func main () begin
        var i <- 0
        for i until i > 3 by 1
        begin
            var a <- 5
        end
        a <- a + 8
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_31(self):
        input = """
        func main () begin
        var a <- 5
        begin
        var a <- "hello"
        end
        a <- "no"
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(no))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        input = """number a <- 7
        func main () begin
        a <- 14
        var a <- true
        if (a = 5) return
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(=, Id(a), NumLit(5.0))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_33(self):
        input = """func isTrue()
        func main() begin
        isTrue()
        end
        func isTrue() begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_34(self):
        input = """func isPrime(number x)
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
        func main()
        begin
            number x <- readNumber()
            if (isPrime(x)) writeString("Yes")
                else writeString("No")
            writeString(4)
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [NumLit(4.0)])"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_34(self):
        input = """func isPrime(number x)
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
        func main()
        begin
            number x <- readNumber()
            if (isPrime(x)) writeString("Yes")
                else writeString("No")
            writeString(4)
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [NumLit(4.0)])"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_35(self):
        input = """func areDivisors(number num1, number num2) return 
        func main()
        begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(areDivisors), [Id(num1), Id(num2)])"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        input = """func fibonacci(number x) begin
        var i <- 0
        number a <- 0
        number b <- 1
        for i until i = a by 1 begin
            var c <- a + b
            a <- b
            b <- c
        end
        return a
        end 
        func main() begin
        number a <- readNumber()
        var b <- writeNumber(fibonacci(a))
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(writeNumber), [CallExpr(Id(fibonacci), [Id(a)])])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input = """
        func main() begin
        string a <- readString()
        if (a == "1") writeString("Welcome")
        elif (a == "2") writeString("Thank you")
        elif (a == "4") a <- 5
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(5.0))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        input = """
        func main() begin
        dynamic a
        a <- (a + 4 > 4) or (5 = 4)
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BinaryOp(or, BinaryOp(>, BinaryOp(+, Id(a), NumLit(4.0)), NumLit(4.0)), BinaryOp(=, NumLit(5.0), NumLit(4.0))))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        input = """
        func main() begin
        dynamic a <- [1,2,3]
        number b[5] <- a
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([5.0], NumberType), None, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        input = """func inc (number x)
        func main() begin
        var a <- inc(2) ... "abc"
        end
        func inc (number y) return y + 1
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(+, Id(y), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_41(self):
        input = """func inc (number x) return 0
        number inc
        func main() begin
        var a <- inc(2) ... "abc"
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., CallExpr(Id(inc), [NumLit(2.0)]), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        input = """dynamic a
        func foo() return a
        func main()
        begin
            number num <- foo()
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        input = """
        func foo() begin
        number x
        end
        func main()
        begin
            number num <- foo()
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        input = """
        func main()
        begin
            var c <- c
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    # def test_45(self):
    #     input = """func foo() begin
    #     foo()
    #     end
    #     func main()
    #     begin
    #         number a[4] <- [1, true, false, "a"]
    #     end
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), BooleanLit(True), BooleanLit(False), StringLit(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_46(self):
        input = """
        func main()
        begin
            dynamic x
            x <- (x = 1) or ("abc" == "abc")
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(==, StringLit(abc), StringLit(abc))))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        input = """
        func a (number x) return x
        var a <- "a"
        func main()
        begin
            number b <- a(2)
            b <- a
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_48(self):
        input = """
        string a[3]
        func main()
        begin
            a <- [1,2,3]
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_49(self):
        input = """
        string a[3]
        func main()
        begin
            number c[2, 3, 4] <- [[[1,2,3,4],[5,6,7,8],[1,2,3,4]], [[1,2,3,4],[5,6,7,8],[1,2,3,4]]]
            if (true) return [1,2,3]
            else return [1,2]
        end
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_50(self):
        input = """
        number b <- 1
        number a[2] <- [1,b]
        func main() begin
        a <- [[1,2,true],"hello"]
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_88(self):
        input = """
        dynamic a
        number b <- a[0]
        string c <- a[1]
        func main()
        begin
            a <- [1,2,3]
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c), StringType, None, ArrayCell(Id(a), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_89(self):
        input = """
        func foo(number a)
        func foo(string a) begin
        end
        func main()
        begin
        end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self):
        input = """func foo()
        func foo()
        func foo() begin
        end
        func main()
        begin
        end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_91(self):
        input = """
        func main()
        begin
            dynamic a
            string x <- [a]
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), StringType, None, ArrayLit(Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_92(self):
        input = """func foo() return [[1,2],[3,4]]
        func main()
        begin
        number a <- foo()[1,2]
        end
        func abc(number a, number a) return a
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_93(self):
        input = """
        dynamic a
        dynamic b <- [a, [1,2,3]]
        func main()
        begin
        a <- [2,3,4]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_94(self):
        input = """
        func foo(number a, number b)

        func main()
        begin
            return 1 + foo(1, 2)
        end
        func foo(number a, number b)
        begin
            return "hello"
        end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(hello))"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_95(self):
        input = """
        dynamic a
        func main() begin
        if (true) return 1
        else return a
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_96(self):
        input = """
        dynamic a
        func main() begin
        if (true) return a
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    # def test_97(self):
    #     input = """
    #     dynamic a
    #     func main() begin
    #     if ([a]) return
    #     end
    #     """
    #     expect = "Type Mismatch In Statement: If((ArrayLit(Id(a)), Return()), [], None)"
    #     self.assertTrue(TestChecker.test(input, expect, 497))

    def test_98(self):
        input = """
        number x[3,3] <- [[1,2,[1,3,4]],[2,4,6],[3,5]]
        func main() begin
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), ArrayLit(NumLit(1.0), NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_99(self):
        input = """
        dynamic a
        dynamic b
        dynamic c
        number x[3,3] <- [a,b,c]
        func main() begin
        a <- [1,2,3]
        b <- [2,4,6]
        c <- [3,5]
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), ArrayLit(NumLit(3.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 499))
        
    def test_100(self):
        input = """
        dynamic a
        number b[2] <- [a, 1]
        func main() begin
        a <- "hello"
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(hello))"
        self.assertTrue(TestChecker.test(input, expect, 500))


    def test_1000(self):
            input = """
                dynamic a
                dynamic b
                dynamic c
                dynamic d
                dynamic e
                dynamic f
                dynamic g
                dynamic h
                func main() begin
                    number x[2, 2, 2] <- [[[a, b], [c, d]], [[e, f], [g, h]]]
                end
            """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 1000))

    def test_1001(self):
        input = """
            func main()
            begin
                var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
                writeNumber(x)
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 1001))

    def test_1002(self):
        input = """
            func main()
            begin
                var x <- [[1, 2, 3], [4, [5, 6]]]
                writeNumber(x)
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(4.0), ArrayLit(NumLit(5.0), NumLit(6.0)))"
        self.assertTrue(TestChecker.test(input, expect, 1001))

    def test_1003(self):
        input = """
            func main()
            begin
                dynamic y
                var x <- [[1, 2, 3], y]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1003))

    # def test_1004(self):
    #     input = """
    #         func main()
    #         begin
    #             dynamic a
    #             a[0] <- [1, 2, 3]
    #         end
    #     """
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
    #     self.assertTrue(TestChecker.test(input, expect, 1004))

    def test_1005(self):
        input = """
            func main() begin
                dynamic a
                number b[2,1] <- [a[0],1]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([2.0, 1.0], NumberType), None, ArrayLit(ArrayCell(Id(a), [NumLit(0.0)]), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 1005))

    def test_1006(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[b, 1]
                b <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1006))

    def test_1007(self):
        input = """
            number a
            func f(string a) begin
                number a <- a + a
                string x <- x ... "hello"
                return x
            end
            func main() begin
                string a <- f(a)
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1007))

    def test_1008(self):
        input = """
            func foo(number a[2,2]) return
        
            func main()
            begin
                dynamic x
                foo([[x,x], [x,x]])
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1008))

    def test_1009(self):
        input = """
            func foo(number a)

            func main() begin
            var a <- foo(foo(1))
            end

            func foo(number a) return 1
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1009))

    def test_1010(self):
        input = """
            func main() begin
                var x <- [1, x]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), None, var, ArrayLit(NumLit(1.0), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 1010))

    def test_1011(self):
        input = """
            func foo(number a)

            func main() begin
                dynamic a
                number x[6]
                for a until foo(1) >= 10 by x[5] continue
            end

            func foo(number b) return 1
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1011))

    def test_1012(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b >= 10 by c continue
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1012))

    # Special test
    def test_1013(self):
        input = """
            dynamic a
            dynamic b
            dynamic c

            func foo(number d)

            number x[2, 3] <- c

            func main() begin
                c[1] <- [a, b, foo(1)]
            end

            func foo(number d) return 1 + 1
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1013))

    def test_1014(self):
        input = """
            dynamic a
            dynamic b
            func main() begin
                number x[2] <- [a,b]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1014))
    
    def test_1015(self):
        input = """
            dynamic a
            string x <- [a]
            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), StringType, None, ArrayLit(Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 1015))

    def test_1016(self):
        input = """
            func foo() return true

            func foo1() begin
                if (true) return 1 + foo()
            end

            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 1016))

    def test_1017(self):
        input = """
            func main() begin
                string a
                if (true) number a <- 1
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 1017))

    def test_1018(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                number x[2, 1] <- [a, [b]]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1018))

    def test_1019(self):
        input = """
            func main() begin
                dynamic a
                dynamic b
                dynamic c
                number x[2] <- [a, [b, c]]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), ArrayType([2.0], NumberType), None, ArrayLit(Id(a), ArrayLit(Id(b), Id(c))))"
        self.assertTrue(TestChecker.test(input, expect, 1019))

    def test_1020(self):
        input = """
            func foo(string x) return ["hello", "hi"]

            func main() begin
                dynamic a
                string b <- a ... foo(a)[1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1020))

    def test_1021(self):
        input = """
            func foo(string x) return ["hello", "hi"]

            func main() begin
                dynamic a
                string b <- a ... foo(a)[1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1021))

    def test_1022(self):
        input = """
            func foo(string a, bool b) return [[1, 2], [1, 2]]
            func main() begin
                dynamic a
                dynamic b   
                number x <- 1 + foo(a, b)[1, 2]
                a <- "hello"
                b <- not (a == "hi")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1022))

    def test_1023(self):
        input = """
            func main() begin
                dynamic a
                number b <- a[2]
                a <- ["hello", "world"]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(StringLit(hello), StringLit(world)))"
        self.assertTrue(TestChecker.test(input, expect, 1023))

    def test_1024(self):
        input = """
            func main() begin
                dynamic a
                number b <- a[2]
                a <- [1, 2, 3]
                a <- [4, 5, 6]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 1024))

    def test_1025(self):
        input = """
            func foo(number a) return

            func main() begin
                dynamic x
                foo([x])
            end
        """
        expect = "Type Cannot Be Inferred: CallStmt(Id(foo), [ArrayLit(Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 1025))
    
    def test_1026(self):
        input = """
            dynamic a
            number x <- 1 - 2 + 3 - 4 * 5 + 6 - [a]
            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), NumberType, None, BinaryOp(-, BinaryOp(+, BinaryOp(-, BinaryOp(+, BinaryOp(-, NumLit(1.0), NumLit(2.0)), NumLit(3.0)), BinaryOp(*, NumLit(4.0), NumLit(5.0))), NumLit(6.0)), ArrayLit(Id(a))))"
        self.assertTrue(TestChecker.test(input, expect, 1026))

    def test_1027(self):
        input = """
            dynamic a
            func main() begin
                dynamic i
                for i until [a] + 1 by 1
                    return
            end
        """
        expect = "Type Cannot Be Inferred: For(Id(i), BinaryOp(+, ArrayLit(Id(a)), NumLit(1.0)), NumLit(1.0), Return())"
        # Type Mismatch In Expression: BinaryOp(+, ArrayLit(Id(a)), NumLit(1.0))
        self.assertTrue(TestChecker.test(input, expect, 1027))

    def test_1028(self):
        input = """
            dynamic a
            func main() begin
                if ([a + 1] + 1) return
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, ArrayLit(BinaryOp(+, Id(a), NumLit(1.0))), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 1028))

    def test_1029(self):
        input = """
            dynamic a
            func main() begin
                dynamic b
                dynamic c
                dynamic d
                b <- [a, 1, [c, d]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(a), NumLit(1.0), ArrayLit(Id(c), Id(d)))"
        self.assertTrue(TestChecker.test(input, expect, 1029))