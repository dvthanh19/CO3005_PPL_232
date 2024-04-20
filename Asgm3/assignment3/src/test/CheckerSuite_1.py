import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test0(self):
        input = """
            number a
            number a
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test1(self):
        input = """
            number a
            func foo(number a,string a)
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    # .......
    def test2(self):
        input = """
            number a
            func foo(number a,string a)
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self):
        input = """
            func foo()
            func foo()
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test4(self):
        input = """
            func foo() return
            func foo() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test5(self):
        input = """
            func foo() return
            func foo() 
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test6(self):
        input = """
            func foo(number a,string b) 
            func foo(string a,number b) 
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test7(self):
        input = """
            func foo(number a,string b) 
            func foo(number a,string b) 
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test8(self):
        input = """
            ## func foo(number a, string b) 
            ## func foo(number a, string b) begin
            ## end
            func main() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test9(self):
        input = """
            number a
            func foo(number a,string a)
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test10(self):
        input = """
            number a
            func foo(number a, string b)
                begin
                    c <- a
                end
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test11(self):
        input = """
            number a
            number b
            var c <- d
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 411))

    # def test12(self):
    #     input = """
    #         number a
    #         number b
    #         func main() begin
    #             c <- d
    #         end
    #     """
    #     expect = "Undeclared Identifier: c"
    #     self.assertTrue(TestChecker.test(input, expect, 412))

    def test13(self):
        input = """
            number a
            number b
            func foo(number a,string b) begin
            end
            func main() begin
                foo1()
            end
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test14(self):
        input = """
            number a[2,3]
            number c
            func foo() begin
                c[1,2]<-5
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(c), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test15(self):
        input = """
            number a[2,3]
            number c
            func foo() begin
                c["1","2"]<-5
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(c), [StringLit(1), StringLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test16(self):
        input = """
            number a[2,3]
            number c
            func foo() begin
                a["1","2"]<-5
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1), StringLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test17(self):
        input = """
            number a[2,3]
            number c
            func foo() begin
                a[2,3] <- 5
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test18(self):
        input = """
            number a[2,3]
            number c
            func foo() begin
                a[2,3]<-"5"
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(2.0), NumLit(3.0)]), StringLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test19(self):
        input = """
            number a
            string b
            func foo() begin
                number c <- a + b
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test20(self):
        input = """
            bool a
            bool b
            func foo() begin
                number c <- a + b
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test21(self):
        input = """
            bool a
            bool b
            func foo() begin
                number c <- -a
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: UnaryOp(-, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test22(self):
        input = """
            number a
            bool b
            func foo() begin
                number c <- -a
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test23(self):
        input = """
            number a
            bool b
            func foo() begin
                number c <- -a
            end
            func foo1() begin
                b <- foo()
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test24(self):
        input = """
            number a
            bool b
            func foo() begin
                number c <- -a
                return true
            end
            func foo1() begin
                b <- foo()
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test25(self):
        input = """
            number a
            func foo() return
            func main() begin
                number b <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test26(self):
        input = """
            dynamic a
            func foo() return
            func main() begin
                var b <- a
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test27(self):
        input = """
            var a<-5
            func foo() return
            func main() begin
                var b <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 427))

    # def test28(self):
    #     input = """
    #         dynamic a
    #         func foo() return
    #         func main() begin
    #             var b <- a and (a>b)
    #         end
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(>, Id(a), Id(b))"
    #     self.assertTrue(TestChecker.test(input, expect, 428))

    def test29(self):
        input = """
            dynamic a
            func foo() return
            func main() begin
                var b <- a and true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 429))

    # def test30(self):
    #     input = """
    #         dynamic a
    #         func foo() return
    #         func main() begin
    #             var y <- a + foo(x)
    #         end
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x)])"
    #     self.assertTrue(TestChecker.test(input, expect, 430))

    # def test31(self):
    #     input = """
    #         dynamic a
    #         func foo(number a) return
    #         func main() begin
    #             var y <- a + foo(x)
    #         end
    #     """
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input, expect, 431))

    def test32(self):
        input = """
            dynamic a
            dynamic x
            func foo(number a) return
            func main() begin
                var y <- a + foo(x)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test33(self):
        input = """
            dynamic a
            dynamic x
            func foo(number a) return a
            func main() begin
                var y <- a + foo(x)
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))

    # def test34(self):
    #     input = """
    #         dynamic a
    #         dynamic x
    #         func foo(number a) return a
    #         func main() begin
    #             foo(x, y)
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(x), Id(y)])"
    #     self.assertTrue(TestChecker.test(input, expect, 434))

    def test35(self):
        input = """
            dynamic a
            dynamic x
            dynamic y
            func foo(number a,string b) return 
            func main() begin
                foo(x,y)
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test36(self):
        input = """
            dynamic a
            dynamic x
            dynamic y
            func foo(number a,string b) return
            func main() begin
                number a <- foo(x,y)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x), Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test37(self):
        input = """
            dynamic a
            dynamic b
            func main() begin
                a<-b
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test38(self):
        input = """
            dynamic a
            dynamic b
            number c
            func main() begin
                b <- c
                a <- b
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test39(self):
        input = """
            dynamic a
            dynamic b
            number c[2,3]
            func main() begin
                b <- c
                a <- b
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test40(self):
        input = """
            dynamic a
            var b <- [2,3,4,5]
            number c[2,3]
            func main() begin
                b <- [2,3,4,5]
                a <- b
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test41(self):
        input = """
            dynamic a
            dynamic b
            number c[2,3]
            func main() begin
                b <- [2,3,4,a]
                a <- b
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test42(self):
        input = """
            dynamic a
            dynamic b
            number c[2,3]
            func main() begin
                b <- [2,3,4,a]
                c <- b
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    # def test43(self):
        input = """
            dynamic a
            dynamic b
            number c[2,3]
            dynamic d
            func main() begin
                b <- [2,3,4,a]
                d <- b
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test44(self):
        input = """
            dynamic a
            dynamic b
            number c[2,3]
            dynamic d
            func main() begin
                b <- [2,3,4,a]
                d <- b
                if(a) begin
                    a <- b
                end
            end
        """
        expect = "Type Mismatch In Statement: If((Id(a), Block([AssignStmt(Id(a), Id(b))])), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test45(self):
        input = """
            dynamic a
            dynamic b
            number c[2,3]
            dynamic d
            func main() begin
                b <- [2,3,4,a]
                d <- b
                if(1) begin
                    a <- b
                end
            end
        """
        expect = "Type Mismatch In Statement: If((NumLit(1.0), Block([AssignStmt(Id(a), Id(b))])), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test46(self):
        input = """
            dynamic a
            dynamic b
            number c[2,3]
            dynamic d
            func main() begin
                b <- [2,3,4,a]
                d <- b
                if(true) begin
                    writeString("hehe")
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test47(self):
        input = """
            func foo() return
            func foo1() begin
                foo <- 2
            end
            func main() return
        """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test48(self):
        input = """
            func foo() return
            func foo1() begin
                number a[2,3]
                number b[2,3,4]
                a <- b
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test49(self):
        input = """
            func foo() return 1
            func foo1() begin
                foo()
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 449))

    # def test50(self):
    #     input = """
    #         func foo(number x, number y) return 
    #         func foo1() begin
    #             foo(x)
    #         end
    #         func main() return
    #     """
    #     expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(x)])"
    #     self.assertTrue(TestChecker.test(input, expect, 450))

    def test51(self):
        input = """
            func foo(number x,string y) return 
            func foo1() begin
                number y
                string x
                foo(x,y)
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(x), Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test52(self):
        input = """
            func foo() begin
                return 
                return "hehe"
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(hehe))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test53(self):
        input = """
            func foo() begin
                return "hehe"
                return 
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test54(self):
        input = """
            func a()
            func foo() begin
                return "hehe"
            end
            func main() return
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test55(self):
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test56(self):
        input = """
            func main() begin
                continue
                break
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test57(self):
        input = """
            func foo() begin
                ## continue
                ## break
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test58(self):
        input = """
            func a()
            func main() begin 
                a()
            end
            func a() return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 458))