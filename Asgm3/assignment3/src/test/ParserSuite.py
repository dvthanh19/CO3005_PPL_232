import unittest
from TestUtils import TestParser



class ParserSuite(unittest.TestCase):
    
    def test0(self):
        input = """
            func main()
            begin
                if (kk<-88)
                return 1
            end
        """
        expect = "Error on line 4 col 22: <-"
        self.assertTrue(TestParser.test(input, expect, 200))
  
    
    def test1(self):
        input = """
            dynamic a <- 1
            dynamic b
		"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        
    
    def test2(self):
        input = """
            number a <- 1
            number b
            string c <- "hello world!"
            bool d <- true
		"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
        
    
    def test3(self):
        input = """
            number a <- 1
            number a[10] <- 1 + [1, 2, 3 + 1]
            string c <- "hello" ... " world!"
		"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    
    
    def test4(self):
        input = """
            number a <- 1
            func foo(number a, string b, bool c[99])
		"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    
    
    def test5(self):
        input = """
            number a <- 1
            func foo(number a <- 5, string b, bool c[1])
		"""
        expect = "Error on line 3 col 30: <-"
        self.assertTrue(TestParser.test(input, expect, 205))
        
    
    def test6(self):
        input = """
            number a <- 1
            func foo(bool b, bool c[69 + 96])
		"""
        expect = "Error on line 3 col 39: +"
        self.assertTrue(TestParser.test(input, expect, 206))
        
    
    def test7(self):
        input = """
            number a <- 1
            func foo(bool b, bool c[6969])
            begin
                a <- 1   ## comment
                b[1, 2, 3] <- (99999 + 1 > 2 + 3) * a[1 + 9]
            end
		"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    
    def test8(self):
        input = """
            number a <- 1
            func foo(bool b, bool c[6969])
            begin
                a <- 1
                ## comment
                a[] <- 1
            end
        """
        expect = "Error on line 7 col 18: ]"
        self.assertTrue(TestParser.test(input, expect, 208))
        
    
    def test9(self):
        input = """
            number a <- 1
            func foo()
            return
            
            func foofoo() return "'"PPL-Assignment1'""
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
        
    
    
    
    def test10(self):
        input = """
            number a <- 1
            func foo()
            begin
            end
            
            func foofoo() return "'"PPL-Assignment1'""
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    
    
    def test11(self):
        input = """
            number a <- 1
            func foo() begin return "PPL" end
        """
        expect = "Error on line 3 col 29: return"
        self.assertTrue(TestParser.test(input, expect, 211))
        
    
    def test12(self):
        input = """
            number a <- 1
            func foo() begin 
                return "PPL"
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    

    
    def test_13(self):
        input = '''

func kIN ()
	begin
		begin
		end
  
		## |*kXgAK
		continue
	end
var wi <- 1
func Honh (number xBQ, number pmG[13,532E+29]) return 

func kJE (number pU[9e+37,58], string KZ[51,334,786.701])
	return false

'''
        expect = '''successful'''
        self.assertTrue(TestParser.test(input, expect, 213))
    
    
    
    def test14(self):    
        input = """
            func foo(number foo[2])
            begin
                a[1] <- c[foo(arr1) + foo(arr2), "PPL_PPL"] + 2 + ("I love " ... "PPL ") ... "very much"
                return "PPL"
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    
    
    def test15(self):
        input = """
            func foo(number foo[2])
            begin
                number avgScore <- 10*0.1 + 9.3*0.3 + 10*0.2 + 9.75*0.4
                string a <- "Average_score: " + toSTring(avgScore)
                if (a >= 9.5) print("A+")
                else if (a >= 8.5) print("A")
                elif (a >= 8) print("B+")
                elif (a >= 7) print("B")
                else print("C+")
                return 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        
    
    def test16(self):
        input = """
            func foo(number foo[2])
            begin
                if (a)
                    return 1
                elif (b)
                    if (c)
                        return 2
                    elif (d)
                        if (e) return 3
                        elif (f) return 4
                        elif (g) return 5
                        else
                            return
                    else if (h) return arr[1 + 9] + arr[1 + (121 + 144 + 169) > 3]
                elif (i) return arr[123]
                else
                    if (j) return
                    else return
                
                return 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
        
    
    def test17(self):
        input = """
            func foo(number foo[2])
            begin
                for i until i > 10 by 1
                begin
                    begin
                        begin
                            if (__a__) return "OK"
                            elif (true) if (b) return "OK"..."notsure..."
                            else
                            begin
                                string __d__ <-- "__d__"
                                foo(__d__)
                            end
                        end
                    end
                end
                return 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
        
    
    
    def test18(self):
        input = """
            func foo(number foo[1])
                a <- 1
        """
        expect = "Error on line 3 col 16: a"
        self.assertTrue(TestParser.test(input, expect, 218))
    
    
    
    def test19(self):
        input = """
            func foo(number foo[1])
            begin
                for i until i > 10 by 1
                begin
                    if (i % 2 = 0)
                        ## comment 
                        i <- [1,2, [1 + 2], [1 + 2, 3 + 4]] + 5 + (str...lit > ((nhp >= p...pl)...d))
                    else
                        for i until i > 10 by 1
                        begin
                            abc <- 123
                            
                            begin
                            end
                            begin
                            end
                        end 
                end
            end
            
            ## comment
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        
        
    
    def test20(self):
        input = """
            func foo(number foo[1])
                return 1

            func foo(number a123)
            
            func foo(string a[1][2])
        
        
        """
        expect = "Error on line 7 col 32: ["
        self.assertTrue(TestParser.test(input, expect, 220))
        
    
    def test21(self):
        input = """
            func foo(number foo[1])
            begin
                dynamic a <- "abc'"!!!'"\\n"
            end

            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    
    
    def test22(self):
        input = """
            func foo(number foo[1])
            begin
                dynamic a <- "\\\ \t hello"
            end

            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    
    
    def test23(self):
            input = '''
    func zvz ()
        return "'"'"'""
var E2
    func Ow (number nj[65,484.398,0], number t2T[5,4.602], string DlM)
        begin
            ## Ok/MVZydJT1QZnKsLj^
            ## )`+b?/tNH$
            ## gydY46Y"P
        end
    func R1v6 (var A4a[5.355,0.199])
        return 9.105
    func Ztn ()
        return

    '''
            expect = '''Error on line 4 col 7: \n'''
            self.assertTrue(TestParser.test(input,expect,223))

    
    def test24(self):
        
        input = """ 
            number ppl
            
            ## comment
            number ppl <- 0
            bool a[122,15]
            bool a[122,15] <- 1 + 1 / 2 * 3
            string b[3]
            ## 12 
            
            string b[3] <- 2 ... " tring"
            var i <- 0
            dynamic i
            dynamic i <- 0
            ## comment
             
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))   
    
    
    def test25(self):
        input = """ 
            dynamic PpL[5] <- 3
        """
        expect = "Error on line 2 col 23: ["          
        self.assertTrue(TestParser.test(input, expect, 225)) 
        
    
    def test26(self):
        input = """ 
            bool a["string"]
            bool a[[1,2]]
            bool a[1+1]
        """
        expect = "Error on line 2 col 19: string"
        self.assertTrue(TestParser.test(input, expect, 226))

    
    def test27(self):
        input = """ 
            bool a[1,]
        """
        expect = "Error on line 2 col 21: ]"
        self.assertTrue(TestParser.test(input, expect, 227))

    
    def test28(self):
        input = """ 
            var a[1]
        """
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 228))

    
    def test29(self):
        input = """ 
            func main()
            func main(number f1)
            func main(number a[5],bool x[5,2,3], bool a[5,2,3], string b, bool c)
            func main(number num1, number num2)
                var PpL <- 1
            func main(number f1 <- c)
        """
        expect = "Error on line 7 col 32: <-"
        self.assertTrue(TestParser.test(input, expect, 229))

    
    def test30(self):
        input = """ 
            func main()
            ## comment
            func main() func main(dynamic a) ## comment
        """
        expect = "Error on line 4 col 24: func"
        self.assertTrue(TestParser.test(input, expect, 230))

    
    def test31(self):
        input = """ 
            func main(var a)
        """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 231))

    
    def test32(self):
        input = """ 
            ##12
            ##12
            
            func main(number a) var c <- 1
        """
        expect = "Error on line 5 col 32: var"
        self.assertTrue(TestParser.test(input, expect, 232))

    
    def test33(self):
        input = """ 
            func main(string a) 
                begin 
                    break ## 12
                end
            func main(dynamic a) 
        """
        expect = "Error on line 6 col 22: dynamic"
        self.assertTrue(TestParser.test(input, expect, 233))

    
    def test34(self):
        input = """ 
            func main(number a[1,2,3]) ##12
                break
        """
        expect = "Error on line 3 col 16: break"
        self.assertTrue(TestParser.test(input, expect, 234))

    
    def test35(self):
        input = """ 
            ##12
            func main(number a) 
                ##12
                
                begin 
                    break
                end
                
                ##12
                ##12
            func main(number a)
            ##12        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    
    def test36(self):
        input = """ 
            ## 12
            
            var a <- 1 ## 12
            ## 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    
    def test37(self):
        input = """var a <- 1"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 237))

    
    def test38(self):
        input = """func main(number a) """
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 238))

    
    def test39(self):
        input = """ var PpL <- "PPL" ... "nhp" 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    
    def test40(self):
        input = """ var PpL <- "PPL" ... 123 ... "nhp" 
        """
        expect = "Error on line 1 col 26: ..."
        self.assertTrue(TestParser.test(input, expect, 240))

    
    def test41(self):
        input = """ 
            var PpL1 <- true > "true" 
            var PpL2 <- true >= "true"
            var PpL3 <- true = "true"
            var PpL4 <- true == "true"
            var PpL5 <- true < "true"
            var PpL6 <- true <= "true"
            var PpL7 <- true >= "true" ... 1 > 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    
    def test42(self):
        input = """ var PpL <- true > x >= z 
        """
        expect = "Error on line 1 col 21: >="
        self.assertTrue(TestParser.test(input, expect, 242))

    
    def test43(self):
        input = """ 
            var PpL1 <- true and "true" or 1 
            var PpL2 <- 1 and 2 and 3 or 4 or 4
            var PpL3 <- 1 + 2 - 2 + 3 and 3
            var PpL4 <- 1 / 2 * 3 % 4
            var PpL5 <- 1 / 2 / 2 * 3 % 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    
    def test44(self):
        input = """var PpL <- true >= "true" and 1 > 2
        """
        expect = "Error on line 1 col 32: >"
        self.assertTrue(TestParser.test(input, expect, 244))

    
    def test45(self):
        input = """ 
            var PpL1 <- -1 * not 1
            var PpL2 <- not not not----C
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    
    def test46(self):
        input = """var PpL <- - not 1
        """
        expect = "Error on line 1 col 13: not"
        self.assertTrue(TestParser.test(input, expect, 246))

    
    def test47(self):
        input = """ 
            var PpL1 <- a[1] + 1
            var PpL2 <- array[1,1+2][1][2,3]
            var PpL3 <- array[1,(1)...2,array[ar[(1*2) and 1]],array[2]]
            var PpL4 <- a[1] + fun()[1,fun()] 
            var PpL5 <- 1[1]
        """
        expect = "Error on line 3 col 36: ["
        self.assertTrue(TestParser.test(input, expect, 247))

    
    def test48(self):
        input = """var PpL <- a[]
        """
        expect = "Error on line 1 col 13: ]"

        self.assertTrue(TestParser.test(input, expect, 248))

    
    def test49(self):
        input = """ 
            var PpL1 <- a()
            var PpL2 <- a(1,2)
            var PpL3 <- a(x,array[2])[2]
            var PpL4 <- a(z,k[3] ... 2)[1,2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    
    def test50(self):
        input = """var PPL <- a()()
        """
        expect = "Error on line 1 col 14: ("

        self.assertTrue(TestParser.test(input, expect, 250))

    
    def test51(self):
        input = """ 
            var PpL1 <- a() + 1 / 2 *3 <= 3 ... "v" >= 2
            var PpL2 <- a(1,2)[1,2,3 ... 2] + false + true
            var PpL3 <- a(z,k[2,3,"2"] ... 2)[true]
            var PpL4 <- (a ... 3) ... b and (a >= b) < b[1, b[1]]
            var PpL5 <-  ["tr", 2, 3, 4, 5] + [[1, 2 + 2 * 2 / 3, 3], [4, 5, 6]]
            var PpL6 <- a(x,array[2])[2,3+2,true,false]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    
    def test52(self):
        input = """var PpL <- a[1]()
        """
        expect = "Error on line 1 col 15: ("
        self.assertTrue(TestParser.test(input, expect, 252))

    
    def test53(self):
        input = """
        ## comment
        func main()

            ## comment
            begin
            aPI <- 3.14
            end
            ## comment
            
        ## comment
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    
    def test54(self):
        input = """
        func main() begin 
        end
        func main() 
            begin 
                ## comment0
            end
        func main()
            ## comment1
            begin
                ## comment2
                
                ## comment3
                PpL1 <- 1 + 2 + fun()
                PpL2[1+a] <- 1
                
                ## comment4
                PpL3[3+4,2,4] <- 1
                
                ## comment5
            end
            ## comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    
    def test55(self):
        input = """
        func main()
            begin
            aPI + 1 <- 3.14
            end
        """
        expect = "Error on line 4 col 16: +"
        self.assertTrue(TestParser.test(input, expect, 255))

    
    def test56(self):
        input = """
        func main()
            begin
            aPI()<- 3.14
            end
        """
        expect = "Error on line 4 col 17: <-"
        self.assertTrue(TestParser.test(input, expect, 256))

    
    def test57(self):
        input = """
        func main()
            begin
            (aPI)[2]<- 3.14
            end
        """
        expect = "Error on line 4 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 257))

    
    def test58(self):
        input = """
        func main()
            begin   
                if(1+1) api <- 1
                ## comment0
                
                if(1+1) 
                    ## comment1
                    
                    api <- 1
                    ## comment2
                else api <- 1
                ## comment3
                
                if (1) api <- 1
                elif (1 ... 2)
                    ## comment1
                    
                    api <- 1
                    ## comment2
                elif (1) api <- 1
                
                if (1) api <- 1
                elif (1 ... 2) api <- 1
                elif (1) api <- 1
                else api <- 1   
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    
    def test59(self):
        input = """
        func main()
            begin   
                if (api <- 1)
            end
        """
        expect = "Error on line 4 col 24: <-"
        self.assertTrue(TestParser.test(input, expect, 236))        
        
        #! test for break Continue
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
                ## comment
                
                a <- 1
            ## comment
            end
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259)) 
         
        
    def test60(self):
        input = """
        func main()
            begin
            for i[1] until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 260))


    def test61(self):
        input = """
        func main()
            begin
            for i+1 until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 261))


    def test62(self):
        input = """
        func main()
        begin 
            break
            continue
            for i until i >= 10 by 1 + 1 ... 3 / 2
                begin
                    break
                    continue
                end
                
            for i until i >= 10 by 1 print(1)
            for i until i >= 10 by 1 
                print(1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))


    def test63(self):
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input, expect, 263))


    def test64(self):
        input = """
        func main()
            return 1 + 1
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))


    def test65(self):
        input = """
        func main()
            begin
            main()
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))


    def test66(self):
        input = """
        func main()
        begin 
            return ([1,2,3]) + 1
            return main()
            main(1,2)
            fun()
            main([1,2,3], 1+2, a, c ... e)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))


    def test67(self):
        input = """
        func main()
            return return()
        """
        expect = "Error on line 3 col 19: return"
        self.assertTrue(TestParser.test(input, expect, 267))


    def test68(self):
        input = """
        func main()
            return break
        """
        expect = "Error on line 3 col 19: break"
        self.assertTrue(TestParser.test(input, expect, 268))


    def test69(self):
        input = """
        func main()
            begin
                begin
                    begin
                        x <- 1
                    end
                    
                    begin
                        return true
                    end
                    
                    return false
                end
                
                begin
                end
                return true
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))


    def test70(self):
        input = """var aPI <- 3.14"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 270))


    def test71(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))


    def test72(self):
        input = """
            func isPrime(number x)
            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
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
            
            
            for i until i > x / 2 by 1 + 1 var c <- 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))


    def test73(self):
        input = """
        func a() return 1 ## 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))


    def test74(self):
        input = """
            number x <- x number x <- y
        """
        expect = "Error on line 2 col 26: number"
        self.assertTrue(TestParser.test(input, expect, 274))


    def test75(self):
        input = """
        func a()
        begin
        end
        
        func a()
        begin

            number x <- x
            
        end
        
        func a()
        begin 
        end
        func a() begin 
        end
        func a() begin 
        end
        func a() begin ## comment
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))


    def test76(self):
        input = """    
        func a()
        begin
            break continue
        end
        """
        expect = "Error on line 4 col 18: continue"
        self.assertTrue(TestParser.test(input, expect, 276))


    def test77(self):
        input = """    
        func a()
        begin
            return 1 break
        end
        """
        expect = "Error on line 4 col 21: break"
        self.assertTrue(TestParser.test(input, expect, 277))


    def test78(self):
        input = """    
        func a()
        begin
            if (x <= 1) ## comment1
                begin   ## comment2
                    number a[1] <- [["str"],[1,2,3], 1 + 2 + 5]
                end
            if (x <= -1)
                return -1
        end ## comment3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))


    def test79(self):
        input = """    
        func a()
            fun()
        """
        expect = "Error on line 3 col 12: fun"
        self.assertTrue(TestParser.test(input, expect, 279))    
    
    
    def test80(self):
        input = """    
        func a()
            if x <= 1 return false
        """
        expect = "Error on line 3 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 280))


    def test81(self):
        input = """    
        func a()
            return if x <= 1 return false
        """
        expect = "Error on line 3 col 19: if"
        self.assertTrue(TestParser.test(input, expect, 281))


    def test82(self):
        input = """    
        func a()
            return 
        var a <- []
        """
        expect = "Error on line 4 col 18: ]"
        self.assertTrue(TestParser.test(input, expect, 282))


    def test83(self):
        input = """    
        func a(number a[1+1])
        """
        expect = "Error on line 2 col 25: +"
        self.assertTrue(TestParser.test(input, expect, 283))


    def test84(self):
        input = """    
            var a <- a[1][1]
        """
        expect = "Error on line 2 col 25: ["
        self.assertTrue(TestParser.test(input, expect, 284))


    def test85(self):
        input = """    
            var a <- 1[1]
        """
        expect = "Error on line 2 col 22: ["
        self.assertTrue(TestParser.test(input, expect, 285))


    def test86(self):
        input = """
        """
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 285)) 
        
        input = """    
        func a()
            begin
                a[1][2] <- 1
            end
        """
        expect = "Error on line 4 col 20: ["
        self.assertTrue(TestParser.test(input, expect, 286))


    def test87(self):
        input = """    
            var a <- [1,2,3][1]
        """
        expect = "Error on line 2 col 28: ["
        self.assertTrue(TestParser.test(input, expect, 287))


    def test88(self):
        input = """    
            string a[1+1]
        """
        expect = "Error on line 2 col 22: +"
        self.assertTrue(TestParser.test(input, expect, 288))


    def test89(self):
        input = """    
        func a()
            begin a <- 1
            end
        """
        expect = "Error on line 3 col 18: a"
        self.assertTrue(TestParser.test(input, expect, 289))


    def test90(self):
        input = """    
        func a()
            begin
            end var c <- 1
        """
        expect = "Error on line 4 col 16: var"
        self.assertTrue(TestParser.test(input, expect, 290))


    def test91(self):
        input = """    
        func a()
            begin
                c()[1] <- 1
            end
        """
        expect = "Error on line 4 col 19: ["
        self.assertTrue(TestParser.test(input, expect, 291))


    def test92(self):
        input = """    
        func a()
            begin
                c <- (1)[1]
            end
        """
        expect = "Error on line 4 col 24: ["
        self.assertTrue(TestParser.test(input, expect, 292))


    def test93(self):
        input = """    
        func a()
            begin
                var c <- 1 var c <- 1
            end
        """
        expect = "Error on line 4 col 27: var"
        self.assertTrue(TestParser.test(input, expect, 293))


    def test94(self):
        input = """    
        func a()
            begin
                PpL[] <- 1
            end
        """
        expect = "Error on line 4 col 20: ]"
        self.assertTrue(TestParser.test(input, expect, 294))


    def test95(self):
        input = """    
        func a()
            begin
                1 <- 2
            end
        """
        expect = "Error on line 4 col 16: 1"
        self.assertTrue(TestParser.test(input, expect, 295))


    def test96(self):
        input = """    
            func a(string s["2"])
        """
        expect = "Error on line 2 col 28: 2"
        self.assertTrue(TestParser.test(input, expect, 296))


    def test97(self):
        input = """    
            var c <- a()
            [1]
        """
        expect = "Error on line 3 col 12: ["
        self.assertTrue(TestParser.test(input, expect, 297))


    def test98(self):
        input = """    
            func a()
            begin
                fun() fun()
            end
        """
        expect = "Error on line 4 col 22: fun"
        self.assertTrue(TestParser.test(input, expect, 298))


    def test99(self):
        input = """    
            number a[1][2] <- 1
        """
        expect = "Error on line 2 col 23: ["
        self.assertTrue(TestParser.test(input, expect, 299))
        

