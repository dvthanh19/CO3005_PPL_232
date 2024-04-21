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
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(y), ArrayLit(Id(x))), ArrayLit(Id(x), Id(x)))"
    #     self.assertTrue(TestChecker.test(input, expect, 407))
        
    # def test8(self):
    #     input = """
    #         func foo() begin
    #             ## dynamic x
    #             dynamic y
    #             return [[y], [y]]
    #             return x
    #             return [[1], [2]]
    #         end
    #         func main() return 
    #     """
    #     expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
    #     self.assertTrue(TestChecker.test(input, expect, 408))
            
    # def test9(self):
    #     input = """
    #         dynamic x
    #         dynamic y
    #         number arr[2,2,1] <- [[[y],[x]], [x,x]]
            
    #         func main() return 
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(x))), ArrayLit(Id(x), Id(x)))"
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    
    # def test10(self):
    #     input = """
    #         dynamic x
    #         dynamic y
    #         number arr[1,2,2] <- [[y,[x]]]
            
    #         func main() return 
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([1.0, 2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(y), ArrayLit(Id(x)))))"
    #     self.assertTrue(TestChecker.test(input, expect, 410))
        
    # def test11(self):
    #     input = """
    #         dynamic x
    #         dynamic y
    #         number arr[1,2,2,3] <- [[y,[x,x]]]
            
    #         func main() return 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 411))
    
    # def test11(self):
    #     input = """
    #         dynamic x
    #         dynamic y
    #         number arr[2,2,2,3] <- [[x,y], [y,x]]
            
    #         func main() return 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 411))
    
    # def test12(self):
    #     input = """
    #         dynamic x
    #         dynamic y
    #         number arr[2,2,2,3] <- [[x,y], [y,x]]
            
    #         func main() return 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 412))  
    
    # def test13(self):
    #     input = """
    #         dynamic x
    #         dynamic y
    #         number arr[2,2,2,1] <- [[[x,[1]],y],[y,[[1],x]]]
            
    #         func main() return 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 413))
        
    # def test14(self):
    #     input = """
    #         dynamic x
    #         dynamic y
    #         number arr[2,3,1] <- [[x, [1], [2]], [[0], [1], [x]]]
            
    #         func main() return 
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(0.0)), ArrayLit(NumLit(1.0)), ArrayLit(Id(x)))"
    #     self.assertTrue(TestChecker.test(input, expect, 414))
    
    # def test15(self):
    #     input = """
    #         dynamic x
    #         dynamic y
    #         number arr[2,3,1] <- [x, x, x]
            
    #         func main() return 
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 3.0, 1.0], NumberType), None, ArrayLit(Id(x), Id(x), Id(x)))"
    #     self.assertTrue(TestChecker.test(input, expect, 415))
    
    # def test16(self):
    #     input = """
    #         dynamic x
    #         dynamic y
    #         number arr[2,2,2,4] <- [[y,y], [x,x]]
    #         func main() return 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 416))
        
    # def test17(self):
    #     input = """
    #         dynamic x
    #         func main()
    #         begin
    #             var y <- x[0, 0] + 1
    #             writeNumber(y)
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 417))
    
    # def test18(self):
    #     input = """
    #         func f(number x)
    #         begin
    #             dynamic x <- (x - 2) * (x + true)
    #         end
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input, expect, 418))
        
    # def test19(self):
    #     input = """
    #         func foo1()
    #         begin
    #             dynamic x 
    #             return x
    #         end
            
    #         func main()
    #         begin
                
    #         end
    #     """
    #     expect = "Type Cannot Be Inferred: Return(Id(x))"
    #     self.assertTrue(TestChecker.test(input, expect, 419))
    
    # def test20(self):
    #     input = """
    #         dynamic a
            
    #         func main() 
    #         begin
    #             if ([a]) return
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: If((ArrayLit(Id(a)), Return()), [], None)"
    #     self.assertTrue(TestChecker.test(input, expect, 420))

    # def test21(self):
    #     input = """
    #         string a
    #         string arr[1,1,2] <- [[[a, a]]]
    #         string b[2,3] <- [a, ["","",""]] 
            
    #         func main() return
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(Id(a), ArrayLit(StringLit(), StringLit(), StringLit()))"
    #     self.assertTrue(TestChecker.test(input, expect, 421))
        
    # def test21(self):
    #     input = """
    #         func foo(number a, string b)
    #         func foo(number a, string b)
    #         begin
    #             dynamic a
    #             return [b]
    #             return [a]
    #         end
            
    #         func main() return
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 421))
                
    # def test22(self):
    #     input = """
    #         func foo(number a, string b)
    #         begin
    #             dynamic a
    #             return a
                
    #             return b
    #         end
            
    #         func main() return
    #     """
    #     expect = "Type Cannot Be Inferred: Return(Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 422))
    
    # def test23(self):
    #     input = """
    #         dynamic a
    #         func main()
    #         begin
    #             var i <- a[2] ... 2.75
    #         end
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(..., ArrayCell(Id(a), [NumLit(2.0)]), NumLit(2.75))"
    #     self.assertTrue(TestChecker.test(input, expect, 423))
    
    # def test24(self):
    #     input = """
    #         dynamic a
    #         func main()
    #         begin
    #             dynamic a
    #             var b <- a[2]
                
    #         end
    #     """
    #     expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, ArrayCell(Id(a), [NumLit(2.0)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 424))
    
    # def test25(self):
    #     input = """
    #         dynamic a
    #         func main()
    #         begin
    #             dynamic a
    #             number b[2,2] <- [a[2], [1,1]]
    #             number c[2] <- a[2]
                
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 424))
        
    # def test26(self):
    #     input = """
    #         func main() begin
    #             dynamic x
    #             dynamic y
    #             number a[2] <- [1, [x, y]] 
    #         end
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(y)))"
    #     self.assertTrue(TestChecker.test(input, expect, 426))
    
    # ...
    # def test27(self):
    #     input = """
    #         dynamic x
    #         number a <- [x]
    #     """
    #     expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))"
    #     # Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))
    #     self.assertTrue(TestChecker.test(input, expect, 427))
    
    # def test28(self):
    #     input = """
    #         func foo()
    #         func main() begin
    #             number a <- foo()[2]
    #             number b[3]
    #             b <- foo()
    #         end
    #         func foo() return [1, 2, 3]
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 100))
        
    # def test29(self):
    #     input = """
    #         func main() begin
    #             dynamic a
    #             number b <- a[2]
    #             a <- [1, 2, 3]
    #             a <- [4, 5, 6, 7]
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0), NumLit(7.0)))"
    #     self.assertTrue(TestChecker.test(input, expect, 101))

    
    # def test31(self):
    #     input = """
    #         func main() begin
    #             dynamic a
    #             number b <- a[2]
    #             a <- [1, 2, 3]
    #             a <- [4, 5, 6]
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 103))
    
    # def test32(self):
    #     input = """
    #         dynamic a
    #         func main() begin
    #             if ([a + 1] + 1) return
    #         end
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+, ArrayLit(BinaryOp(+, Id(a), NumLit(1.0))), NumLit(1.0))"
    #     self.assertTrue(TestChecker.test(input, expect, 104))
    
    # def test33(self):
    #     input = """
    #         dynamic a
    #         func main() begin
    #             dynamic i
    #             for i until [a] + 1 by 1
    #                 return
    #         end
    #     """
    #     expect = "Type Cannot Be Inferred: For(Id(i), BinaryOp(+, ArrayLit(Id(a)), NumLit(1.0)), NumLit(1.0), Return())"
    #     self.assertTrue(TestChecker.test(input, expect, 105))

    # def test34(self):
    #     input = """
    #         dynamic a
    #         func main() begin
    #             if ([a + 1] + 1) return
    #         end
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+, ArrayLit(BinaryOp(+, Id(a), NumLit(1.0))), NumLit(1.0))"
    #     self.assertTrue(TestChecker.test(input, expect, 106))
    
    # def test35(self):
    #     input = """
    #         func foo()
    #         func main() begin
    #             number a <- foo()[2]
    #             number b[3]
    #             b <- foo()
    #         end
    #         func foo() return [1, 2, 3]
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 107))
    
    
    # def test36(self):
    #     input = """
    #         func main() begin
    #             dynamic a
    #             number b <- a[2]
    #             a <- ["hello", "world"]
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(StringLit(hello), StringLit(world)))"
    #     self.assertTrue(TestChecker.test(input, expect, 108))
        
    def test37(self):
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
        self.assertTrue(TestChecker.test(input, expect, 109))
    
    
    def test38(self):
        input = """
            func main() begin
                dynamic a
                number b <- a[2]
                a <- ["hello", "world"]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(StringLit(hello), StringLit(world)))"
        self.assertTrue(TestChecker.test(input, expect, 110))