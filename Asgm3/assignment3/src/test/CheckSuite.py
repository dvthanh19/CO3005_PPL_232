import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    #  NO ENTRY POINT
    def test0(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))


    def test1(self):
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    
    def test2(self):
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    
    def test3(self):
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 403))
   

    # NO DEFINITION 
    def test5(self):
        input = """
            func foo(number a)
            func foo(number a) return     
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    
    def test6(self):
        input = """
            func foo(number a) return   
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    
    def test7(self):
        input = """
            func foo(number a) 
        
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    
    
    # REDECLARED
    def test8(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 408))
    
      
    def test9(self):
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    
    def test10(self):
        input = """
            func foo() return
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 410))
            
    
    def test11(self):
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 411))
            
    
    def test12(self):
        input = """
            func foo() return
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))
            
    
    def test13(self):
        input = """
            number foo
            func foo() return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 413))     
    
    
    def test21(self):
        input = """
            func foo(number a) 
            func foo(number b) return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))
  
    
    def test22(self):
        input = """
            func foo(number a) 
            func foo(string a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 422))
            
   
    def test23(self):
        input = """
            func foo(number a) 
            func foo(number a, string c) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 423))
            
   
    def test24(self):
        input = """
            func foo(number a, string c) 
            func foo(number a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))



    
    # UNDECLARED
    def test25(self):
        input = """
            number a <- a
            func main() begin
                number b <- a
                number c <- e
            end
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 425))

  
    def test26(self):
        input = """
            func a()
            func main() begin
                a()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 426))

    
    def test27(self):
        input = """
            func a() return 1
            func main() begin
                number b <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 427))


    def test28(self):
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

    
    def test29(self):
        input = """
            func a() begin
                a()
            end
            func main() begin
                a()
                b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 429))


    def test30(self):
        input = """
            func a() return
            func main() begin
                number a
                a()
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
          
          
          
    # MUST IN LOOP
    def test31(self):
        input = """
                func main() begin
                    continue
                end
            """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    
    def test32(self):
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
    
    
    def test33(self):
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
        
    # TYPE CANNOT BE INFERRED 
    def test34(self):
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
        self.assertTrue(TestChecker.test(input, expect, 434))
  
    
    def test38(self):
        input = """
            func foo() begin
                dynamic a
                return a
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 438))
    
    
    def test39(self):
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
    
    
    def test40(self):
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
    
    
    def test41(self):
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
    
    
    def test42(self):
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
        
        
        
    
    # TYPE MISMATCH IN STATEMENT
    def test43(self):
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 443)) 
    
    
    def test44(self):
        input = """
            number a <- "1"

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    
    def test45(self):
        input = """
            number a[1,2] <- [[1,2]]

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))
    
   
    def test46(self):
        input = """
            number a[1,2,3] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 446))

     
    def test47(self):
        input = """
            number a[1] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 447))       

    
    def test48(self):
        input = """
            func foo() return

            func main()begin
                foo()
                foo(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 448))    
    
    
    def test49(self):
        input = """
            func foo(number a) return

            func main()begin
                foo()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 449))     
    
    
    def test50(self):
        input = """
            func foo(number a) return

            func main()begin
                foo("1")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 450))    
    
    
    def test51(self):
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
    
    
    def test52(self):
        input = """
            func main()begin
                dynamic a
                if (a) return
                a <- true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))     
        

    def test53(self):
        input = """
            func main()begin
                dynamic a <- 1
                if (a) return
            end
        """
        expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 453))                 


    def test55(self):
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
        

    def test56(self):
        input = """
            func foo() begin
                dynamic a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 456))    
        

    def test57(self):
        input = """
            func foo() begin
                dynamic a 
                dynamic b <- 2
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 457))  


    def test58(self):
        input = """
            func foo() begin
                dynamic a 
                dynamic b
                dynamic c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 458))    
    
    
    def test59(self):
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
        
        
         



    # TYPE MISMATCH IN EXPRESSION
    def test61(self):    
        input = """
            func foo() return 1

            func main() begin
                var a <- foo()
                var b <- foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
        
    def test62(self):    
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 462))
        
        
    def test63(self):    
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
        
    def test64(self):    
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
        
    def test65(self):    
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 465))
        
        
    def test66(self):    
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
        
        
    def test67(self):    
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
        
        
    def test68(self):    
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
        

    def test69(self):    
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
        
        
    def test70(self):    
        input = """
            func main() begin
                number a[1,2]
                number b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
        
    def test71(self):    
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- b[1]
            end
        """
        # expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])" # ...
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, ArrayCell(Id(b), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 471))
        
        
    def test72(self):    
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
        
        
    def test73(self):    
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a["1"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 473))
        
        
    def test74(self):    
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,2,3]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 474))
        
        
    def test75(self):    
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
        
        
    def test76(self):    
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
    
        
    # FULL TEST
    def test80(self):
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
        self.assertTrue(TestChecker.test(input, expect, 480))
        
        
    def test81(self):
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
# Type Mismatch In Statement: If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None)
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    
    def test83(self):
        input = """
            func main() return main()
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(main), []))"
        self.assertTrue(TestChecker.test(input, expect, 483))




    # ARRAY LITERAL     
    def test84(self):
        input = """
            dynamic x
            number a <- [x]
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 484))        
        
        
    def test85(self):
        input = """
            dynamic x
            number a[3] <- [x]
            func f()
            begin
                x <- [1,2,3]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 485))        
        
        
    def test86(self):
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
        

    def test87(self):
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
        
        
    def test88(self):
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
       
        
    def test89(self):
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
        
        
    def test90(self):
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


    def test91(self):
        input = """
            dynamic x
            number a[3] <- [1, [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 491))    
       
        
    def test92(self):
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


    def test93(self):
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

        
    def test94(self):
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
       
        
    def test95(self):
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
     
        
    def test96(self):
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
      
        
    def test97(self):
        input = """
            dynamic x
            number a[1,1,1,1] <- [[[x]]]
            func  main()
            begin
                x <- [1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497)) 
        
        
    def test98(self):
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
        

    def test99(self):
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
  

    def test100(self):
        input = """
            dynamic x
            var a <- [x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 500))  
        

    # def test101(self):
    #     input = """
    #         func foo() begin
    #             dynamic x
    #             return [x]                
    #         end
    #         func main() return 
    #     """
    #     expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x)))"
    #     self.assertTrue(TestChecker.test(input, expect, 501))  
        

    # def test102(self):
    #     input = """
    #         func foo() begin
    #             dynamic x
    #             return [x, [1,2]]                
    #         end
    #         func main() return 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 502))  
        
        
    # def test103(self):
    #     input = """
    #         func foo() begin
    #             dynamic x
    #             dynamic y
    #             return [[y], [y]]
    #             return x
    #             return [[1], [2]]
    #         end
    #         func main() return 
    #     """
    #     expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
    #     self.assertTrue(TestChecker.test(input, expect, 503))  
        
        
    # def test104(self):
    #     input = """
    #         func foo() begin
    #             dynamic x
    #             dynamic y
    #             return [[1], [2]]
    #             return [x, y]
    #             x <- [1]
    #             y <- x
    #         end
    #         func main() return 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 504)) 
        
        
    # def test105(self):
    #     input = """
    #         func foo() begin
    #             dynamic x
    #             dynamic y
    #             return [[1], [2]]
    #             return [x, [y]]
    #             x <- [1]
    #             y <- x
    #         end
    #         func main() return 
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(y), Id(x))"
    #     self.assertTrue(TestChecker.test(input, expect, 505))
        
        
    # def test106(self):
    #     input = """
    #         func foo(number a[2,2]) return
    #         func main() begin
    #             dynamic x
    #             foo(x)
    #             x <- [[2,2], [2,3]]
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 506))
    
    
    # def test107(self):
    #     input = """
    #         func foo(number a[2,2]) return
    #         func main() begin
    #             dynamic x
    #             foo([x])
    #             x <- [1]
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: CallStmt(Id(foo), [ArrayLit(Id(x))])"
    #     self.assertTrue(TestChecker.test(input, expect, 507))
    
    
    # def test108(self):
    #     input = """
    #         func foo(number a[2,2]) return
    #         func main() begin
    #             dynamic x
    #             foo([x, x])
    #             x <- [1,2]
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 508)) 
    
    
    # def test109(self):
    #     input = """
    #         func foo(number a[2,2]) return 1
    #         func main() begin
    #             dynamic x
    #             var a <- foo([x, x])
    #             x <- [1,2]
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 509)) 
    #     # Type Mismatch In Expression: CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))])
    
    
    # def test110(self):
    #     input = """
    #         func foo(number a[2,2]) return 1
    #         func main() begin
    #             dynamic x
    #             var a <- foo(x)
    #             x <- [1,2]
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(x), ArrayLit(NumLit(1.0), NumLit(2.0)))"
    #     self.assertTrue(TestChecker.test(input, expect, 510)) 




    # # RETURN
    # def test111(self):
    #     input = """
    #         func main() begin 
    #             return
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 511))   


    # def test112(self):
    #     input = """
    #         func main() begin 
    #             return 1
    #         end
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 512))   
    
   
    # def test113(self):
    #     input = """
    #         func fun() begin
    #             number a[3]
    #             return [1, 4, 3]
    #             return a
    #         end
    #         func main() begin 
               
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 513))   
        
        
    # def test114(self):
    #     input = """
    #         func fun() begin
    #             number a[2,2]
    #             return [[1,2], [3,4]]
    #             return a
    #         end
    #         func main() begin 
               
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 514))    
        
        
    # def test115(self):
    #     input = """
    #         func fun() begin
    #             number a[3,2]
    #             return [[1,2], [3,4]]
    #             return a
    #         end
    #         func main() begin 
               
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: Return(Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 515))  
        
        
    # def test116(self):
    #     input = """
    #         func fun() begin
    #             number a[2,2]
    #             return a
    #             return [["1","2"], ["3","4"]]
    #         end
    #         func main() begin 
               
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
    #     self.assertTrue(TestChecker.test(input, expect, 516))   
        
        
    # def test117(self):
    #     input = """
    #         func fun() begin
    #             string a[2,2, 3]
    #             return a
    #             return [["1","2"], ["3","4"]]
    #         end
    #         func main() begin 
               
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
    #     self.assertTrue(TestChecker.test(input, expect, 517))  
        
        
    # def test118(self):
    #     input = """
    #         func fun() begin
    #             string a[2]
    #             return a
    #             return [["1","2"], ["3","4"]]
    #         end
    #         func main() begin 
               
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
    #     self.assertTrue(TestChecker.test(input, expect, 518))   
        
        
    # def test119(self):
    #     input = """
    #         func fun() begin
    #             string a[1,1,1,1,1]
    #             return a
    #             return [[[[["1"]]]]]
    #         end
    #         func main() begin 
               
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 519))     
        
        
    # def test120(self):
    #     input = """
    #         func fun() begin
    #             return [1,2]
    #             return [3,4]
    #         end
            
    #         func fun1() begin
    #             return [[1,2], [3,4]]
    #             return [[1,5], [3,4]]
    #         end
            
    #         func main() begin 
               
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 520)) 
        
        
    # def test121(self):
    #     input = """
    #         func fun1() return 1
    #         func fun2() return
    #         func fun3()
            
    #         func main() begin 
    #            return fun3()
    #         end
    #     """
    #     expect = "Type Cannot Be Inferred: Return(CallExpr(Id(fun3), []))"
    #     self.assertTrue(TestChecker.test(input, expect, 521)) 
        
        
    # def test122(self):
    #     input = """
    #         func fun1() return 1
    #         func fun2() return
    #         func fun3()
            
    #         func main() begin 
    #            return fun1()
    #         end
    #         func fun3() return 1   
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 522)) 

        
    # def test123(self):
    #     input = """
    #         func fun1() return 1
    #         func fun2() return
    #         func fun3()
            
    #         func main() begin 
    #            number a <- fun3()
    #         end
    #         func fun3() return "1"  
    #     """
    #     expect = "Type Mismatch In Statement: Return(StringLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 523)) 
        
                
    # def test124(self):
    #     input = """
    #         func fun1() return [1,2]
    #         func fun2() return [3,4]
    #         func fun3()
            
    #         func main() begin 
    #            return fun1()
    #            return fun2()
    #            return fun3()
    #         end 
    #     """
    #     expect = "No Function Definition: fun3"
    #     self.assertTrue(TestChecker.test(input, expect, 524)) 


    # def test125(self):
    #     input = """
    #         func main() begin 
    #             return 1
    #             begin
    #                 return "string"
    #             end
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: Return(StringLit(string))"
    #     self.assertTrue(TestChecker.test(input, expect, 525))


    # def test126(self):        
    #     input = """
    #         func main() begin 
    #             dynamic i
    #             return 1
    #             return i
    #         end
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 526))  
        
        
    # def test127(self):
    #     input = """
    #         func fun() begin
    #             return 
    #             return
    #             return 1
    #         end
    #         func main() begin 
               
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
    #     self.assertTrue(TestChecker.test(input, expect, 527))       
        
        
    # def test128(self):
    #     input = """
    #         func fun() begin
    #             return 1
    #             return "string"
    #         end
    #         func main() begin 
               
    #         end
    #     """
    #     expect = "Type Mismatch In Statement: Return(StringLit(string))"
    #     self.assertTrue(TestChecker.test(input, expect, 528))    
        
        


    # # ASSIGN
    # def test129(self):
    #     input = """
    #         func main() begin 
    #             number a
    #             dynamic b
    #             dynamic c
    #             b <- c
    #         end
    #     """
    #     expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(c))"
    #     self.assertTrue(TestChecker.test(input, expect, 529)) 
        

    # def test130(self):  
    #     input = """
    #         func main() begin 
    #             number a
    #             dynamic b
    #             dynamic c
    #             a <- c
    #             b <- c
    #             return a
    #             return b
    #             return c
    #         end
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 630))   
        
        
    # def test131(self):
    #     input = """
    #         func main() begin 
    #             number a
    #             string b
    #             dynamic c
    #             a <- c
    #             c <- b

    #         end
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(b))"
    #     self.assertTrue(TestChecker.test(input, expect, 531))   
        
        
    # def test132(self):
    #     input = """
    #         func main() begin 
    #             number a
    #             string b
    #             dynamic c
    #             c <- a
    #             b <- c

    #         end
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(c))"
    #     self.assertTrue(TestChecker.test(input, expect, 532))      
        
        
    # def test133(self):
    #     input = """
    #         func main() begin 
    #             number a[1,3]
    #             dynamic c
    #             c <- [[1,2,3]]
    #             c <- a
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 533))   
        
        
    # def test134(self):
    #     input = """
    #         func foo()
    #         func main() begin 
    #             number a[1,3]
    #             dynamic c
    #             c <- foo()
    #         end
    #     """
    #     expect = "Type Cannot Be Inferred: AssignStmt(Id(c), CallExpr(Id(foo), []))"
    #     self.assertTrue(TestChecker.test(input, expect, 534)) 
        
        
    # def test135(self):
    #     input = """
    #         func foo()
    #         func main() begin 
    #             number a[1,3]
    #             dynamic c
    #             a <- foo()
    #         end
    #         func foo()
    #             return [[1,2,3]]
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 535))
        
        
    # def test136(self):
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
        self.assertTrue(TestChecker.test(input, expect, 536))