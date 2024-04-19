import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # SINGLE TEST
    
    # def test0(self):
    #     input = """
    #         dynamic x
    #         number a[3] <- [x]
    #         func f()
    #         begin
    #             x <- [1,2,3]
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x)))"
    #     self.assertTrue(TestChecker.test(input, expect, 400))     
    
    # def test1(self):
    #     input = """ 
    #         func main()
    #         begin
    #             dynamic x
    #             dynamic y
    #             number a[2,2] <- [y, [x,x]]
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 401))
    
    
    # def test2(self):
    #     input = """ 
    #         func main()
    #         begin
    #             dynamic x
    #             number a[2,2] <- [x,[x,x]]
                
    #         end
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
    #     self.assertTrue(TestChecker.test(input, expect, 402))
    
    # def test3(self):
    #     input = """ 
    #         func main()
    #         begin
    #             dynamic x
    #             dynamic y
    #             number a[2,2] <- [x, [y]]
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(Id(x), ArrayLit(Id(y))))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))
    
    # def test4(self):
    #     input = """
    #         func main()
    #         begin
    #             var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
    #             writeNumber(x)
    #         end
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
    #     self.assertTrue(TestChecker.test(input, expect, 404))
    
    # def test5(self):
    #     input = """
    #         dynamic x
    #         number a
    #         var y <- [a, a]
    #         number arr[2,2] <- [x, [y]]
        
    #         func main() return
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(Id(x), ArrayLit(Id(y))))"
    #     self.assertTrue(TestChecker.test(input, expect, 405))
    
    
    # def test6(self):
    #     input = """
    #         number a
    #         var y <- [a, a]
    #         number arr[2,2] <- [a, [y]]
        
    #         func main() return
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(Id(a), ArrayLit(Id(y)))"
    #     self.assertTrue(TestChecker.test(input, expect, 406))
        
    
    
    # def test7(self):
    #     input = """
    #         dynamic x
    #         dynamic y
    #         number arr[2,2,1] <- [[y,[x]], [x,x]]
        
    #         func main() return
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 407))
        
    def test8(self):
        input = """
            func foo() begin
                ## dynamic x
                dynamic y
                return [[y], [y]]
                ## return x
                ## return [[1], [2]]
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
        self.assertTrue(TestChecker.test(input, expect, 408))  
        
        