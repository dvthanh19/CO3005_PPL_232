
import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # SELF TEST 
    
    def test0(self):
        input = """
        func main()
        begin
            dynamic x
            dynamic y
            number a[2, 1] <- [[x], [y]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))
    
    
    def test1(self):
        input = """
        func main() 
        begin
            dynamic x
            dynamic a <- [[[x]], [[[1]]]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    
    def test2(self):
        input = """
        func main() 
        begin
            dynamic x 
            x <- [1, x]
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), ArrayLit(NumLit(1.0), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    
    def test3(self):
        input = """
            func a()
            func main() begin 
                a()
            end
            func a() return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    
    def test4(self):
        input = """
            func foo(number a[2,2]) return  1
            
            func foo2()
            begin
                dynamic x
                return foo([[x,x], [x,x]])
                
                string a
                
                dynamic y
                return foo([[y,y], [y]])
            end
            
            func main()
            begin
                
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(y), Id(y)), ArrayLit(Id(y)))"
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    
    def test5(self):
        input = """
            func f()
            begin
                number c[3,2] <- [[6,7],[4,5],[4,5]]
                return c[2,0]
            end
            func main() 
            begin
                number a <- f()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    
    def test6(self):
        input = """
            func foo(number a, number a)

            func a()
            begin
                return foo(1, 2)
            end

            func foo(number a, number b)
            begin
                return 0
            end
            
            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(foo), [NumLit(1.0), NumLit(2.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    
    def test7(self):
        input = """ 
            func foo() 
                return 1
            
            func main()
            begin
                if (foo()) return
            end
        """
        expect = "Type Mismatch In Statement: If((CallExpr(Id(foo), []), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test8(self):
        input = """ 
            func main()
            begin
                dynamic x
                dynamic y
                number a[2,2] <- [x, [x,x]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 408)) 