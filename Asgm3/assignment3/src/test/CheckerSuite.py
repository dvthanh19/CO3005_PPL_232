import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    def test_Votien_1(self):
        input = """
            func foo(number a, string a)
            func foo(number a, string a) return 
            func main() return
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 101))

    def test_Votien_2(self):
        input = """
            func foo(number a, string a)
            func foo(number a) return
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 102))


    def test_Votien_3(self):
        input = """
            func foo(number a[1,2,3])
            func foo(number a[1,2]) return
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 103))

    def test_Votien_4(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                number b
                if (true) number b
            end
            func main() return
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 104))
        
    def test_Votien_5(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                if (true) number b
                else number b
            end
            func main() return
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 105))

    def test_Votien_6(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                if (true) number b
                
                for b until true by 1
                    number b
            end
            func main() return
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 106))
        
    def test_Votien_7(self):
        input = """
            number a
            func foo(number a)
            begin
                number a
                if (true)
                begin
                    number a
                end
                
                begin
                    number a
                end
                
                for a until true by 1
                begin
                    number a
                end
            end
            func main() 
            begin
                number a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 107))        


    def test_Votien_8(self):
        input = """
            func main() 
            begin
                dynamic x
                if ([x]) x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: If((ArrayLit(Id(x)), AssignStmt(Id(x), NumLit(1.0))), [], None)"
        _expect = "Type Mismatch In Statement: If((ArrayLit(Id(x)), AssignStmt(Id(x), NumLit(1.0))), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 108)) 
    
    # ... 
    def test_Votien_9(self):
        input = """
            func main() 
            begin
                dynamic x
                dynamic y
                for x until y[1] by 1
                    return
            end
        """
        expect = ""
        VoTien_expect = "Type Cannot Be Inferred: For(Id(x), ArrayCell(Id(y), [NumLit(1.0)]), NumLit(1.0), Return())"
        self.assertTrue(TestChecker.test(input, expect, 109)) 
        
    def test_Votien_10(self):
        input = """
            func main() 
            begin
                dynamic x
                dynamic y
                for x until true by x[1]
                    return
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 110)) 
               

    def test_Votien_11(self):
        input = """
            func main() 
            begin
                dynamic x
                dynamic y
                for x until true by x[1]
                    return
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 111)) 
               
    def test_Votien_12(self):
        input = """
            func main() 
            begin
                dynamic x
                return x[1]
            end
        """
        expect = "Type Cannot Be Inferred: Return(ArrayCell(Id(x), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 112))   
        
    def test_Votien_13(self):
        input = """
            func main() 
            begin
                dynamic x
                return [x, [x, x]]
            end
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x), ArrayLit(Id(x), Id(x))))"
        _expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 113))                

    def test_Votien_13(self):
        input = """
            func foo(number a) return 1
            func main() 
            begin
                dynamic x
                number a <- 1 + foo([[x]])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), CallExpr(Id(foo), [ArrayLit(ArrayLit(Id(x)))])))"
        _expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(ArrayLit(Id(x)))])"
        self.assertTrue(TestChecker.test(input, expect, 113)) 
                       
    def test_Votien_14(self):
        input = """
            func foo(number a) return 1
            func main() 
            begin
                dynamic x
                dynamic y
                var a <- [x, [[1,2]], [[y, 1]]]
                x <- [[0,0]]
                y <- x[0,0]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 114)) 


    def test_Votien_15(self):
        input = """
            func foo(number a) return
            func main() 
            begin
                return foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 115)) 
    
  
    # def test_Votien_16(self):
    #     input = """
    #         func foo(number a) return 1
    #         func main() 
    #         begin
    #             dynamic x
    #             var a <- 1 * 2 + 3 * foo([x, x])
    #         end
    #     """
    #     expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(+, BinaryOp(*, NumLit(1.0), NumLit(2.0)), BinaryOp(*, NumLit(3.0), CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]))))"
    #     _expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])"        
    #     self.assertTrue(TestChecker.test(input, expect, 116)) 

    def test_Votien_17(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- foo([x, x]) ... foo([x, x])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(..., CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])))"
        _expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 117)) 

    def test_Votien_18(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- foo([x, x]) ... foo([x, x])
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(..., CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])))"
        _expect = "Type Cannot Be Inferred: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 118))    

     
    def test_Votien_19(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- x ... foo([x, x])
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 119))     
        
    def test_Votien_20(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- x ... foo([x, x])
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 120))     
        
        
    def test_Votien_21(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- foo([x, x]) ... x
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, BinaryOp(..., CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), Id(x)))"
        _expect = "Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 121))   
        
        
    def test_Votien_22(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- [[1,2,3], [x,x]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 122))   
        
    def test_Votien_23(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- [[1,2,3], [x,x]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 123))   
        
    def test_Votien_24(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                number a[1,1,1,1] <- [[[[x]]]]
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 124))  
        
    def test_Votien_25(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                number a <- 1 + [[[[x]]]]
                x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), ArrayLit(ArrayLit(ArrayLit(ArrayLit(Id(x)))))))"
        _expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), ArrayLit(ArrayLit(ArrayLit(ArrayLit(Id(x))))))"
        self.assertTrue(TestChecker.test(input, expect, 125))  
    
    
    
    