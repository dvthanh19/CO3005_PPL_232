import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test0(self):
        input = """
        func main ()
        begin
            bool arr[2,2] <- [[true, false], [false, true]]
            writeBool(arr[1,1])
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
        
    
    # def test0(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeNumber(1)
    #         writeBool(true)
    #         writeString("vthanh")
    #     end
    #     """
    #     expect = "1.0truevthanh"
    #     self.assertTrue(TestCodeGen.test(input, expect, 500))
    
    
#     def test1(self):
#         input = """
#         func main ()
#         begin
#             writeNumber(1.0)
#             writeBool(false)
#             writeString("")
#         end
#         """
#         expect = "1.0false"
#         self.assertTrue(TestCodeGen.test(input, expect, 501))
    

#     def test2(self):
#         input = """
#         number a <- 1
#         func main ()
#         begin
#             writeNumber(a)
#         end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 502))   
    
    
#     def test3(self):
#         input = """
#         number a <- 1
#         func main ()
#         begin
#             number a <- 2
#             writeNumber(a)
#         end
#         """
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 503))  
    
    
#     def test4(self):
#         input = """
#         number a <- 1
#         func main ()
#         begin
#             begin
#                 number a <- 2
#             end
#             writeNumber(a)
#         end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 504))
    
    
#     def test5(self):
#         input = """
#         number a <- 1
#         func main ()
#         begin
#             begin
#                 number a <- 2
#                 writeNumber(a)
#             end
#             writeNumber(a)
#         end
#         """
#         expect = "2.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 505))  
    
        
#     def test6(self):
#         input = """
#         dynamic a
#         func main ()
#         begin
#             bool b <- true
#             begin
#                 a <- b
#             end
#             writeBool(a)
#         end
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input, expect, 506)) 
    
    
#     def test7(self):
#         input = """
#         dynamic a
#         func main ()
#         begin
#             var b <- "ppl"
#             begin
#                 a <- b
#             end
#             writeString(a)
#         end
#         """
#         expect = "ppl"
#         self.assertTrue(TestCodeGen.test(input, expect, 507))


#     def test8(self):
#         input = """
#         dynamic a <-1
#         func foo(number a)
#         begin
#             writeNumber(a)
#         end
#         func main ()
#         begin
#             foo(2)
#         end
#         """
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 508)) 
    
    
#     def test9(self):
#         input = """
#         dynamic a <-1
#         func foo(number a)
#         begin
#             var a <- 3
#             writeNumber(a)
#         end
#         func main ()
#         begin
#             foo(2)
#         end
#         """
#         expect = "3.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 509)) 
    

#     def test10(self):
#         input = """
#         func foo(number a)
#         begin
#             return a
#         end
#         func main ()
#         begin
#             writeNumber(foo(2))
#         end
#         """
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 510)) 
        
    
#     def test11(self):
#         input = """
#         func foo(number a)
#         begin
#             return true
#         end
#         func main ()
#         begin
#             writeBool(foo(2))
#         end
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input, expect, 511)) 
        
    
#     def test12(self):
#         input = """
#         func foo(string a)
#         begin
#             return a
#         end
#         func main ()
#         begin
#             writeString(foo("ppl"))
#         end
#         """
#         expect = "ppl"
#         self.assertTrue(TestCodeGen.test(input, expect, 512))  
    
    
#     def test13(self):
#         input = """
#         func main()
#         begin
#             number a[3] <- [1, 2, 3]
#             writeNumber(a[0])
#             writeNumber(a[1])
#             writeNumber(a[2])
#         end
#         """
#         expect = "1.02.03.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 513))

    
#     def test14(self):
#         input = """
#         func main()
#         begin
#             string a[3] <- ["A", "B", "C"]
#             writeString(a[0])
#             writeString(a[1])
#             writeString(a[2])
#         end
#         """
#         expect = "ABC"
#         self.assertTrue(TestCodeGen.test(input, expect, 514))

    
#     def test15(self):
#         input = """
#         func foo()
#             return true
#         func main ()
#         begin
#             var a <- foo() ## true
#             writeBool(a)
#         end
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input, expect, 515))  
        
    
#     def test16(self):
#         input = """
#         func foo()
#             return "ppl"
#         func main ()
#         begin
#             var a <- foo() ## true
#             writeString(a)
#         end
#         """
#         expect = "ppl"
#         self.assertTrue(TestCodeGen.test(input, expect, 516)) 
    

#     def test17(self):
#         input = """
#         func main ()
#         begin
#             writeNumber(1 + 1)
#             writeNumber(1 - 1)
#             writeNumber(1 * 2)
#             writeNumber(1 / 2)
#             writeNumber(7.5%3.5)
#             writeNumber(7.8%3.38)
#         end
#         """
#         expect = "2.00.02.00.50.51.04"
#         self.assertTrue(TestCodeGen.test(input, expect, 517))


#     def test18(self):        
#         input = """
#         func main ()
#         begin
#             writeNumber(1 + 1 + 1)
#             writeNumber(1 + 1 * 3 - 1 * 2 / 2)
#             writeNumber(2 * 3 % 2)
#         end
#         """
#         expect = "3.03.00.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 518))


#     def test19(self):        
#         input = """
#         func main ()
#         begin
#             writeBool(1 > 2) ## push -1
#             writeBool(2 > 1) ## push 1
#             writeBool(1 > 1) ## push 0
#         end
#         """
#         expect = "falsetruefalse"
#         self.assertTrue(TestCodeGen.test(input, expect, 519))


#     def test20(self):        
#         input = """
#         func main ()
#         begin
#             writeBool(1 >= 2)
#             writeBool(2 >= 1) 
#             writeBool(1 >= 1) 
#         end
#         """
#         expect = "falsetruetrue"
#         self.assertTrue(TestCodeGen.test(input, expect, 520))


#     def test21(self):        
#         input = """
#         func main ()
#         begin
#             writeBool(1 < 2) 
#             writeBool(2 < 1) 
#             writeBool(1 < 1) 
#         end
#         """
#         expect = "truefalsefalse"
#         self.assertTrue(TestCodeGen.test(input, expect, 521))


#     def test22(self):        
#         input = """
#         func main ()
#         begin
#             writeBool(1 <= 2) 
#             writeBool(2 <= 1) 
#             writeBool(1 <= 1) 
#         end
#         """
#         expect = "truefalsetrue"
#         self.assertTrue(TestCodeGen.test(input, expect, 522))


#     def test23(self):        
#         input = """
#         func main ()
#         begin
#             writeBool(1 != 2) 
#             writeBool(2 != 1) 
#             writeBool(1 != 1) 
#         end
#         """
#         expect = "truetruefalse"
#         self.assertTrue(TestCodeGen.test(input, expect, 523))


#     def test24(self):        
#         input = """
#         func main ()
#         begin
#             writeBool(1 = 2) 
#             writeBool(2 = 1) 
#             writeBool(1 = 1) 
#         end
#         """
#         expect = "falsefalsetrue"
#         self.assertTrue(TestCodeGen.test(input, expect, 524))


#     def test25(self):        
#         input = """
#         func main ()
#         begin
#             writeBool(true and true) 
#             writeBool(true and false)
#             writeBool(false and true) 
#             writeBool(false and false)  
#         end
#         """
#         expect = "truefalsefalsefalse"
#         self.assertTrue(TestCodeGen.test(input, expect, 525))


#     def test26(self):        
#         input = """
#         func main ()
#         begin
#             writeBool(true or true) 
#             writeBool(true or false)
#             writeBool(false or true) 
#             writeBool(false or false)  
#         end
#         """
#         expect = "truetruetruefalse"
#         self.assertTrue(TestCodeGen.test(input, expect, 526))


#     def test27(self):        
#         input = """
#         func main ()
#         begin
#             writeBool(true or true and false or true) 
#         end
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input, expect, 527))


#     def test28(self):        
#         input = """
#         func main ()
#         begin
#             writeString("ppl" ... "_tnbd") 
#         end
#         """
#         expect = "ppl_tnbd"
#         self.assertTrue(TestCodeGen.test(input, expect, 528))  

    
#     def test29(self):
        
#         input = """
#         func main ()
#         begin
#             writeBool("ppl" == "8.5") 
#             writeBool("ppl" == "ppl")
#         end
#         """
#         expect = "falsetrue"
#         self.assertTrue(TestCodeGen.test(input, expect, 529))


#     def test30(self):        
#         input = """
#         func main ()
#         begin
#             writeBool(not not true) 
#             writeBool(not true)
#             writeBool(not false)
#         end
#         """
#         expect = "truefalsetrue"
#         self.assertTrue(TestCodeGen.test(input, expect, 530))


#     def test31(self):        
#         input = """
#         func main ()
#         begin
#             writeNumber(--1) 
#             writeNumber(-1)
#         end
#         """
#         expect = "1.0-1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 531))
    
    
#     def test32(self): 
#         input = """
#         func main ()
#         begin
#             var i <- 0
#             for i until i >= 2 by 1
#                 writeNumber(i)
                
#             writeNumber(i)
#         end
#         """
#         expect = "0.01.00.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 532))
    
    
#     def test33(self):         
#         input = """
#         func main ()
#         begin
#             var i <- 0
#             for i until i >= 2 by 1
#             begin
#                 i <- 1000
#                 break
#             end
#             writeNumber(i)
#         end
#         """
#         expect = "0.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 533))
    
    
#     def test34(self): 
#         input = """
#         func main ()
#         begin
#             var i <- 0
#             for i until i > 2 by 1
#                 writeNumber(i)
#         end
#         """
#         expect = "0.01.02.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 534))
    
    
#     def test35(self):     
#         input = """
#         func main ()
#         begin
#             var i <- 0
#             for i until i > 2 by 2
#                 writeNumber(i)
#         end
#         """
#         expect = "0.02.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 535))
    
    
#     def test36(self):         
#         input = """
#         func main ()
#         begin
#             var i <- 3
#             for i until i > 2 by 2
#                 writeNumber(i)
#         end
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 536))
    
    
#     def test37(self):         
#         input = """
#         func main ()
#         begin
#             var i <- 0
#             for i until i >= 2 by 1
#             begin
#                 writeNumber(i)
#                 continue
#                 writeNumber(i)
#             end
#         end
#         """
#         expect = "0.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 537))
    
    
#     def test38(self):         
#         input = """
#         func main ()
#         begin
#             var i <- 0
#             for i until i >= 2 by 1
#             begin
#                 writeNumber(i)
#                 break
#                 writeNumber(i)
#             end
#         end
#         """
#         expect = "0.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 538))
    
    
#     def test39(self):         
#         input = """
#         func main ()
#         begin
#             var i <- 0
#             for i until i >= 2 by 1
#                 break
#         end
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input, expect, 539))   
    
    
#     def test40(self): 
#         input = """
#         number a[2]
#         func main ()
#         begin
#             writeNumber(a[1])
#         end
#         """
#         expect = "0.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 540)) 

        
#     def test41(self):     
#         input = """
#         number a[2]
#         func main ()
#         begin
#             writeNumber(a[1] + 1)
#         end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 541)) 

    
#     def test42(self):     
#         input = """
#         number a[2]
#         func main ()
#         begin
#             var x <- a[0]
#             writeNumber(x)
#         end
#         """
#         expect = "0.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 542)) 

       
#     def test43(self):     
#         input = """
#         func main ()
#         begin
#             number a[2]
#             var x <- a[0] + 2.5
#             writeNumber(x)
#         end
#         """
#         expect = "2.5"
#         self.assertTrue(TestCodeGen.test(input, expect, 543)) 

       
#     def test44(self):     
#         input = """
#         number a[2, 3]
#         func main ()
#         begin
#            writeNumber(a[0,0])
#         end
#         """
#         expect = "0.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 544)) 

    
#     def test45(self):     
#         input = """
#         func main ()
#         begin
#             number a[2, 3]
#            writeNumber(a[0,0])
#         end
#         """
#         expect = "0.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 545)) 

    
#     def test46(self):     
#         input = """
#         func main ()
#         begin
#             number a[2,2,2,2]
#            writeNumber(a[0,0,0,0])
#         end
#         """
#         expect = "0.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 546)) 

    
#     def test47(self):     
#         input = """
#         func main ()
#         begin
#             number a[2,2,2,2]
#             var c <- a[0,0,0]
#            writeNumber(c[0])
#         end
#         """
#         expect = "0.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 547)) 

    
#     def test48(self):     
#         input = """
#         number a[2]
#         func main ()
#         begin
#            a[1] <- 1
#            writeNumber(a[1])
#         end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 548)) 

    
#     def test49(self):     
#         input = """
#         number a[2]
#         func main ()
#         begin
#            a[1] <- a[0] + 1
#            writeNumber(a[1])
#         end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 549)) 

    
#     def test50(self):
#         input = """
#         func main()
#         begin
#             number a[1,1,1]
#             a[0] <- [[1]]
#             writeNumber(a[0,0,0])
#         end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 550))

    
#     def test51(self):     
#         input = """
#         number a[2,2]
#         func main ()
#         begin
#            a[1,1] <- a[0,0] + 1
#            writeNumber(a[1,1])
#         end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 551)) 

    
#     def test52(self):     
#         input = """
#         func main ()
#         begin
#             number a[2,2]
#            a[1,1] <- a[0,0] + 1
#            writeNumber(a[1,1])
#         end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 552))
    
            
#     def test53(self):     
#         input = """
#         func main ()
#         begin
#             number a[2,2]
#            var b <- a[0]
#            b[0] <- 1
#            writeNumber(a[0,0])
#            writeNumber(b[0])
#         end
#         """
#         expect = "1.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 553))
    
    
#     def test54(self):     
#         input = """
#         bool a[2]
#         bool b[2,2]
#         func main ()
#         begin
#             writeBool(a[1])
#             writeBool(b[0,0])
#             a[0] <- true
#             writeBool(a[0])
#             b[0,0] <- true
#             writeBool(b[0,0])
#             var c <- b[0]
#             c[1] <- true
#             writeBool(b[0,1])
#         end
#         """
#         expect = "falsefalsetruetruetrue"
#         self.assertTrue(TestCodeGen.test(input, expect, 554))
    
    
#     def test55(self):     
#         input = """
#         func main ()
#         begin
#             bool a[2]
#             bool b[2,2]
#             writeBool(a[1])
#             writeBool(b[0,0])
#             a[0] <- true
#             writeBool(a[0])
#             b[0,0] <- true
#             writeBool(b[0,0])
#             var c <- b[0]
#             c[1] <- true
#             writeBool(b[0,1])
#         end
#         """
#         expect = "falsefalsetruetruetrue"
#         self.assertTrue(TestCodeGen.test(input, expect, 555)) 
    

#     def test56(self): 
#         input = """
#         number a[2] <- [1,2]
#         func main ()
#         begin
#             writeNumber(a[1])
#             writeNumber(a[0])
#         end
#         """
#         expect = "2.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 556))


#     def test57(self):     
#         input = """
#         func main ()
#         begin
#             number a[2] <- [1,2]
#             writeNumber(a[1])
#             writeNumber(a[0])
#         end
#         """
#         expect = "2.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 557))


#     def test58(self):   
        
#         input = """
#         func main ()
#         begin
#             dynamic a 
#             a <- [1,2]
#             writeNumber(a[1])
#             writeNumber(a[0])
#         end
#         """
#         expect = "2.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 558))


#     def test59(self):      
#         input = """
#         dynamic a 
#         func main ()
#         begin
#             a <- [1,2]
#             writeNumber(a[1])
#             writeNumber(a[0])
#         end
#         """
#         expect = "2.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 559))


#     def test60(self):     
#         input = """
#         var a <- [1,2]
#         func main ()
#         begin
#             writeNumber(a[1])
#             writeNumber(a[0])
#         end
#         """
#         expect = "2.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 560))


#     def test61(self):      
#         input = """
#         func main ()
#         begin
#             var a <- [3,2]
#             writeNumber(a[1])
#             writeNumber(a[0])
#         end
#         """
#         expect = "2.03.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 561))


#     def test62(self):    
#         input = """
#         func main ()
#         begin
#             var a <- [[1],[2]]
#             writeNumber(a[1,0])
#             writeNumber(a[0,0])
#         end
#         """
#         expect = "2.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 562))


#     def test63(self):    
#         input = """
#         var a <- [[1],[2]]
#         func main ()
#         begin
#             writeNumber(a[1,0])
#             writeNumber(a[0,0])
#         end
#         """
#         expect = "2.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 563))


#     def test64(self):    
#         input = """
#         number a[2,1] <- [[1],[2]]
#         func main ()
#         begin
#             writeNumber(a[1,0])
#             writeNumber(a[0,0])
#         end
#         """
#         expect = "2.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 564))


#     def test65(self):    
#         input = """
#         func main ()
#         begin
#             number a[2,1] <- [[1],[2]]
#             writeNumber(a[1,0])
#             writeNumber(a[0,0])
#         end
#         """
#         expect = "2.01.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 565))


#     def test66(self):     
#         input = """
#         var b <- [true]
#         func main ()
#         begin
#             bool a[2,1] <- [[true],[false]]
#             writeBool(a[1,0])
#             writeBool(a[0,0])
#             writeBool(b[0])
#         end
#         """
#         expect = "falsetruetrue"
#         self.assertTrue(TestCodeGen.test(input, expect, 566))


#     def test67(self):    
#         input = """
#         bool a[2,1] <- [[true],[false]]
#         func main ()
#         begin
#             var b <- [true]
#             writeBool(a[1,0])
#             writeBool(a[0,0])
#             writeBool(b[0])
#         end
#         """
#         expect = "falsetruetrue"
#         self.assertTrue(TestCodeGen.test(input, expect, 567))


#     def test68(self):    
#         input = """
#         string a[2,1] <- [["v"],["o"]]
#         func main ()
#         begin
#             var b <- ["tien"]
#             writeString(a[1,0])
#             writeString(a[0,0])
#             writeString(b[0])
#         end
#         """
#         expect = "ovtien"
#         self.assertTrue(TestCodeGen.test(input, expect, 568))


#     def test69(self):       
#         input = """
#         string b[1] <- ["tien"]
#         func main ()
#         begin
#             var a <- [["v"],["o"]]
#             writeString(a[1,0])
#             writeString(a[0,0])
#             writeString(b[0])
#         end
#         """
#         expect = "ovtien"
#         self.assertTrue(TestCodeGen.test(input, expect, 569))


#     def test70(self):     
#         input = """
#         var a <- [[[[1]]]]
#         func main ()
#         begin
#             var b <- a[0]
#             var c <- b[0]
#             var d <- c[0]
#             d[0] <- 2
#             writeNumber(a[0,0,0,0])
#         end
#         """
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 570))


#     def test71(self):    
#         input = """
#         var a <- [[[[1]]]]
#         func main ()
#         begin
#             var b <- a[0]
#             var c <- b[0]
#             var d <- c[0]
#             a[0,0,0,0] <- 4
#             writeNumber(d[0])
#         end
#         """
#         expect = "4.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 571))


#     def test72(self):    
#         input = """
#         func foo(number a[2])
#         begin
#             a[1] <- 2
#         end
#         func main ()
#         begin
#             number a[2]
#             writeNumber(a[0])
#             foo(a)
#             writeNumber(a[1])
#         end
#         """
#         expect = "0.02.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 572))
        

#     def test73(self):
#         input = """
#         func foo()
#         begin
#             writeNumber(1.0)
#             return
#             writeNumber(1.0)
#         end        
#         func main ()
#         begin
#             foo()
#         end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 573))   
    
    
#     def test74(self):
#         input = """
#         func foo(string a)
#         begin
#             writeString(a)
#         end        
#         func main ()
#         begin
#             foo("ppl")
#         end
#         """
#         expect = "ppl"
#         self.assertTrue(TestCodeGen.test(input, expect, 574))

        
#     def test75(self):
#         input = """
#         func foo(string a)   
#         func main ()
#         begin
#             foo("ppl")
#         end
#         func foo(string a)
#         begin
#             writeString(a)
#         end     
#         """
#         expect = "ppl"
#         self.assertTrue(TestCodeGen.test(input, expect, 575))

        
#     def test76(self):
#         input = """
#         func foo(string a, bool b)   
#         func main ()
#         begin
#             foo("ppl", true)
#         end
#         func foo(string a, bool b)
#         begin
#             writeString(a)
#             writeBool(true)
#         end     
#         """
#         expect = "ppltrue"
#         self.assertTrue(TestCodeGen.test(input, expect, 576))

        
#     def test77(self):

#         input = """
#         func foo()
#         begin
#             writeString("1")
#         end  
#         func foo1()
#         begin
#             writeString("2")
#         end  
#         func main ()
#         begin
#             foo()
#             foo1()
#         end
   
#         """
#         expect = "12"
#         self.assertTrue(TestCodeGen.test(input, expect, 577))

    
#     def test78(self):
#         input = """
#         func foo(number a)
#         begin
#             writeNumber(a)
#         end  
#         func main ()
#         begin
#             dynamic a
#             a <- 1
#             foo(a)
#         end
   
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 578))
 

#     def test79(self):
#         input = """
#             func main()
#             begin
#                 if (true) writeNumber(1)
#                 else writeNumber(0)
#             end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 579)) 
    
    
#     def test80(self):
#         input = """
#             func main()
#             begin
#                 if (2 = 2) writeNumber(1)
#             end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 580))
         

#     def test81(self):                                      
#         input = """
#             func main()
#             begin
#                 var a <- 1
#                 if (a = 0) writeNumber(1)
#                 elif (a = 1) writeNumber(2)
#                 elif (a = 2) writeNumber(3)
#             end
#         """
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 581))


#     def test82(self):
#         input = """
#             func main()
#             begin
#                 var a <- 2
#                 if (a = 0) writeNumber(1)
#                 elif (a = 1) writeNumber(2)
#                 elif (a = 2) writeNumber(3)
#             end
#         """
#         expect = "3.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 582))
         
    
#     def test83(self):
#         input = """
#             func main()
#             begin
#                 var a <- 0
#                 if (a = 0) writeNumber(1)
#                 elif (a = 1) writeNumber(2)
#                 elif (a = 2) writeNumber(3)
#             end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 583))


#     def test84(self):
#         input = """
#         func main()
#         begin
#             number a[1,1,1]
#             a[0] <- [[1]]
#             writeNumber(a[0,0,0])
#         end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 584))

    
#     def test85(self):
#         input = """
#             func main()
#             begin
#                 var a <- -1
#                 if (a = 0) writeNumber(1)
#                 elif (a = 1) writeNumber(2)
#                 elif (a = 2) writeNumber(3)
#                 else writeNumber(4)
#             end
#         """
#         expect = "4.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 585))
        

#     def test86(self): 
#         input = """
#             func main()
#             begin
#                 dynamic a
                
#                 begin 
#                     a <- 1
#                 end
#                     writeNumber(a)
#             end
#         """
#         expect = "1.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 586)) 
    
    
#     def test87(self):
#         input = """
#         func main()
#         begin
#             var i <- 0
#             for i until i >= 3 by 1
#                 writeNumber(i)
#             writeNumber(i)
#         end
#         """
#         expect = "0.01.02.00.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 587))

    
#     def test88(self):
#         input = """
#         func main()
#         begin
#             var i <- 0
#             for i until i >= 3 by 1
#             begin
#                 writeNumber(i)
#                 break
#             end
#             writeNumber(i)
#         end
#         """
#         expect = "0.00.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 588))


#     def test89(self):
#         input = """
#         func main()
#         begin
#             var i <- 0
#             for i until i >= 3 by 1
#             begin
#                 writeNumber(i)
#                 continue
#                 writeString("A")
#             end
#             writeNumber(i)
#         end
#         """
#         expect = "0.01.02.00.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 589))
    
    
#     def test90(self):  
#         input = """
# func areDivisors(number num1, number num2)
# return ((num1 % num2 = 0) or (num2 % num1 = 0))
# func main()
# begin
# var num1 <- 3
# var num2 <- 4
# if (areDivisors(num1, num2)) writeString("Yes")
# else writeString("No")
# end

#         """
#         expect = "No"
#         self.assertTrue(TestCodeGen.test(input, expect, 590))  
    
    
#     def test91(self):
#         input = """
# func areDivisors(number num1, number num2)
# return ((num1 % num2 = 0) or (num2 % num1 = 0))
# func main()
# begin
# var num1 <- 2
# var num2 <- 4
# if (areDivisors(num1, num2)) writeString("Yes")
# else writeString("No")
# end

#         """
#         expect = "Yes"
#         self.assertTrue(TestCodeGen.test(input, expect, 591))  
    
    
#     def test92(self):  
#         input = """
# func isPrime(number x)
# func main()
# begin
# number x <- 7
# if (isPrime(x)) writeString("Yes")
# else writeString("No")
# end
# func isPrime(number x)
# begin
# if (x <= 1) return false
# var i <- 2
# for i until i > x / 2 by 1
# begin
# if (x % i = 0) return false
    
# end
# return true
# end

#         """
#         expect = "Yes"
#         self.assertTrue(TestCodeGen.test(input, expect, 592))
    
    
#     def test93(self):  
#         input = """
#     func isPrime(number x)
#     func main()
#     begin
#     number x <- 59
#     if (isPrime(x)) writeString("Yes")
#     else writeString("No")
#     end
#     func isPrime(number x)
#     begin
#     if (x <= 1) return false
#     var i <- 2
#     for i until i > x / 2 by 1
#     begin
#     if (x % i = 0) return false
        
#     end
#     return true
#     end

#             """
#         expect = "Yes"
#         self.assertTrue(TestCodeGen.test(input, expect, 593))
    
    
#     def test94(self):              
#         input = """
# func isPrime(number x)
# func main()
# begin
# number x <- -9
# if (isPrime(x)) writeString("Yes")
# else writeString("No")
# end
# func isPrime(number x)
# begin
# if (x <= 1) return false
# var i <- 2
# for i until i > x / 2 by 1
# begin
# if (x % i = 0) return false
    
# end
# return true
# end

#         """
#         expect = "No"
#         self.assertTrue(TestCodeGen.test(input, expect, 594))
        
    
#     def test95(self):     
#         input = """
# func isPrime(number x)
# func main()
# begin
# number x <- 24
# if (isPrime(x)) writeString("Yes")
# else writeString("No")
# end
# func isPrime(number x)
# begin
# if (x <= 1) return false
# var i <- 2
# for i until i > x / 2 by 1
# begin
# if (x % i = 0) return false
# end
# return true
# end

#         """
#         expect = "No"
#         self.assertTrue(TestCodeGen.test(input, expect, 595))                            
    
    
#     def test96(self):
#         input = """
#         func main()
#         begin
#             var a <- 1
#             a <- 2
#             writeNumber(a)
#         end
#         """
#         expect = "2.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 596))

    
#     def test97(self):
#         input = """
#         func main()
#         begin
#             dynamic a 
#             a <- "MA"
#             writeString(a)
#         end
#         """
#         expect = "MA"
#         self.assertTrue(TestCodeGen.test(input, expect, 597))

    
#     def test98(self):
#         input = """
#         func main()
#         begin
#             var a <- false
#             a <- true
#             writeBool(a)
#         end
#         """
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input, expect, 598))

    
#     def test99(self):
#         input = """
#         func main()
#         begin
#             var a <- 1
#             var b <- 3
#             writeNumber(a)
#             a <- b
#             writeNumber(a)
#         end
#         """
#         expect = "1.03.0"
#         self.assertTrue(TestCodeGen.test(input, expect, 599))

    