import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_1_scope(self):
        input = """
        func main()
        begin
            var a <- 2
            begin
                var a <- 3
                writeNumber(a)
            end
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_2_vardecl(self):
        input = """
        func main()
        begin
            dynamic a
            a <- 8
            writeNumber(a)
        end
        """
        expect = "8.0"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

        input = """
        var a <- 1
        func main()
        begin
            writeNumber(a)
            var a <- 2
            writeNumber(a)
            begin
                var a <- 3
                writeNumber(a)
            end
        end
        """
        expect = "1.02.03.0"
        self.assertTrue(TestCodeGen.test(input, expect, 502))


        input = """
        func foo(number a)
        begin
            writeNumber(a)
            a <- 3
            writeNumber(a)
        end
        func main()
        begin
            var a <- 1
            writeNumber(a)
            foo(2)
            writeNumber(a)
        end
        """
        expect = "1.02.03.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

        input = """
        func foo(number a)
        begin
            writeNumber(a)
            a <- 3
            writeNumber(a)
        end
        func main()
        begin
            var a <- 1
            writeNumber(a)
            foo(2)
            writeNumber(a)
        end
        """
        expect = "1.02.03.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

        input = """
        func main()
        begin
            string a <- "Hello World"
            writeString(a)
        end
        """
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

        input = """
        func main()
        begin
            var a <- true
            writeBool(a)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_3_arraylit(self):
        input = """
        func main()
        begin
            number a[3] <- [1, 2, 3]
            writeNumber(a[0])
            writeNumber(a[1])
            writeNumber(a[2])
        end
        """
        expect = "1.02.03.0"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

        input = """
        func main()
        begin
            string a[3] <- ["A", "B", "C"]
            writeString(a[0])
            writeString(a[1])
            writeString(a[2])
        end
        """
        expect = "ABC"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

        input = """
        func main()
        begin
            bool a[3] <- [true, false, true]
            writeBool(a[0])
            writeBool(a[1])
            writeBool(a[2])
        end
        """
        expect = "truefalsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

        input = """
        func main()
        begin
            number a[2,1] <- [[1], [2]]
            writeNumber(a[0,0])
            writeNumber(a[1,0])
        end
        """
        expect = "1.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

        input = """
        func main()
        begin
            number a[2,1]
            a[0] <- [1]
            a[1] <- [2]
            writeNumber(a[0,0])
            writeNumber(a[1,0])
        end
        """
        expect = "1.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

        input = """
        func main()
        begin
            number a[1,1,1]
            a[0] <- [[1]]
            writeNumber(a[0,0,0])
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

        input = """
        func main()
        begin
            var x <- 0
            number a[2,1] <- [[x], [x+1]]
            writeNumber(a[0,0])
            writeNumber(a[1,0])
        end
        """
        expect = "0.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_4_unary(self):
        input = """
        func main()
        begin
            var a <- 1
            writeNumber(-a)
        end
        """
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

        input = """
        func main()
        begin
            var a <- true
            writeBool(not a)
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

        input = """
        func main()
        begin
            writeNumber(-(-1))
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_5_binary(self):
        input = """
        func main()
        begin
            writeNumber(1 + 2)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

        input = """
        func main()
        begin
            writeNumber(1 - 2)
        end
        """
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

        input = """
        func main()
        begin
            writeNumber(1 * 2)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

        input = """
        func main()
        begin
            writeNumber(1 / 2)
        end
        """
        expect = "0.5"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

        input = """
        func main()
        begin
            writeNumber(1 % 2)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

        input = """
        func main()
        begin
            writeBool(1 < 2)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

        input = """
        func main()
        begin
            writeBool(1 <= 2)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

        input = """
        func main()
        begin
            writeBool(1 > 2)
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

        input = """
        func main()
        begin
            writeBool(1 >= 2)
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

        input = """
        func main()
        begin
            writeBool(1 = 2)
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

        input = """
        func main()
        begin
            writeBool(true and false)
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

        input = """
        func main()
        begin
            writeBool(true or false)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

        input = """
        func main()
        begin
            writeString("Hello" ... "World")
        end
        """
        expect = "HelloWorld"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

        input = """
        func main()
        begin
            writeBool("Hello" == "World")
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_6_arrcell(self):
        input = """
        func main()
        begin
            number a[3] <- [1, 2, 3]
            writeNumber(a[1])
            a[1] <- 4
            writeNumber(a[1])
        end
        """
        expect = "2.04.0"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

        input = """
        func main()
        begin
            number a[1] <- [1]
            number b[2,1] <- [a, [2]]
            writeNumber(b[0,0])
            writeNumber(b[1,0])
            number c[2,1] <- [[2],a]
            writeNumber(c[0,0])
            writeNumber(c[1,0])
        end
        """
        expect = "1.02.02.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

        input = """
        func foo(number a)
        begin
            a <- 3
        end
        func main()
        begin
            number b[3] <- [1, 2, 3]
            foo(b[0])
            writeNumber(b[0])
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

        input = """
        func foo(number a[1])
        begin
            a[0] <- 3
        end
        func main()
        begin
            number b[3,1] <- [[1], [2], [3]]
            foo(b[0])
            writeNumber(b[0,0])
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_7_if(self):
        input = """
        func main()
        begin
            if (true)
                writeString("True")
            else
                writeString("False")
        end
        """
        expect = "True"
        self.assertTrue(TestCodeGen.test(input, expect, 533))


        input = """
        func main()
        begin
            if (false)
                writeString("True")
            elif (false)
                writeString("False")
            else
                writeString("Else")
        end
        """
        expect = "Else"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

        input = """
        func main()
        begin
            if (false)
                writeString("True")
            elif (true)
                writeString("Elif")

        end
        """
        expect = "Elif"
        self.assertTrue(TestCodeGen.test(input, expect, 535))


        input = """
        func main()
        begin
            if ((1 > 0) and (1 < 2))
            begin
                writeString("If1\\n")
                writeString("If2\\n")
            end
            else
                writeString("Else")

        end
        """
        expect = "If1\nIf2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 536))


        input = """
        func main()
        begin
            if (false)
                    writeString("A")
            elif (true)
            begin
                if (true)
                    writeString("B")
                else
                    writeString("C") 
                writeString("D")
            end
            writeString("E")
        end
        """
        expect = "BDE"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

        input = """
        func main()
        begin
            if (1 < 0)
                    writeString("A")
            elif (1 > 0)
            begin
                if (1 > 0)
                    writeString("B")
                else
                    writeString("C") 
                writeString("D")
            end
            writeString("E")
        end
        """
        expect = "BDE"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_8_for(self):
        input = """
        func main()
        begin
            var i <- 0
            for i until i >= 3 by 1
                writeNumber(i)
            writeNumber(i)
        end
        """
        expect = "0.01.02.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

        input = """
        func main()
        begin
            var i <- 0
            for i until i >= 3 by 1
            begin
                writeNumber(i)
                break
            end
            writeNumber(i)
        end
        """
        expect = "0.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 539))


        input = """
        func main()
        begin
            var i <- 0
            for i until i >= 3 by 1
            begin
                writeNumber(i)
                continue
                writeString("A")
            end
            writeNumber(i)
        end
        """
        expect = "0.01.02.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

        input = """
        func main()
        begin
            var i <- 0
            for i until i >= 3 by 1
            begin
                writeNumber(i)
                if (i = 1)
                    break
            end
            writeNumber(i)
        end
        """
        expect = "0.01.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

        input = """
        func main()
        begin
            var i <- 0
            for i until i >= 3 by 1
            begin
                var j <- 0
                for j until j >= 3 by 1 
                    writeNumber(j)
                writeNumber(j)
            end
            writeNumber(i)
        end
        """
        expect = "0.01.02.00.00.01.02.00.00.01.02.00.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

        input = """
        func main()
        begin
            var i <- 0
            var j <- 0
            for i until i >= 3 by 1
            begin
                for j until j >= 3 by 1 
                    writeNumber(j)
                writeNumber(j)
            end
            writeNumber(i)
        end
        """
        expect = "0.01.02.00.00.01.02.00.00.01.02.00.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_9_assign(self):
        input = """
        func main()
        begin
            var a <- 1
            a <- 2
            writeNumber(a)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

        input = """
        func main()
        begin
            dynamic a 
            a <- "AA"
            writeString(a)
        end
        """
        expect = "AA"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

        input = """
        func main()
        begin
            var a <- true
            a <- false
            writeBool(a)
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

        input = """
        func main()
        begin
            var a <- 1
            var b <- 2
            a <- b
            writeNumber(a)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

        input = """
        func main()
        begin
            var a <- 1
            var b <- 2
            a <- b + 1
            writeNumber(a)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

        input = """
        func main()
        begin
            number a[3]
            a[0] <- 1
            a[1] <- 2
            a[2] <- 3
            writeNumber(a[0])
            writeNumber(a[1])
            writeNumber(a[2])
        end
        """
        expect = "1.02.03.0"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

        input = """
        func main()
        begin
            number a[3,1]
            a[0,0] <- 1
            a[1,0] <- 2
            a[2,0] <- 3
            writeNumber(a[0,0])
            writeNumber(a[1,0])
            writeNumber(a[2,0])
        end
        """
        expect = "1.02.03.0"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

        input = """
        func main()
        begin
            var a <- "AAA"
            dynamic b
            b <- a
            writeString(b)
        end
        """
        expect = "AAA"
        self.assertTrue(TestCodeGen.test(input, expect, 551))


        input = """
        func foo()
        begin
            number a[3] <- [1, 2, 3]
            return a[0]
        end
        func main()
        begin
            dynamic b
            b <- foo()
            writeNumber(b)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

        input = """
        func foo()
        begin
            number a[3] <- [1, 2, 3]
            return a[0] + a[1]
        end
        func main()
        begin
            dynamic b
            b <- foo()
            writeNumber(b)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_10_func(self):
        input = """
        func foo()
        func main()
        begin
            number a[3] <- [foo(), foo(), foo()]
            writeNumber(a[0])
            writeNumber(a[1])
            writeNumber(a[2])
        end
        func foo()
            return 1
        """
        expect = "1.01.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

        input = """
        func foo()
        func main()
        begin
            var a <- foo() + 1
            writeNumber(a)
        end
        func foo()
            return 1
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

        input = """
        func foo()
        func main()
        begin
            writeString(foo())
        end
        func foo()
            return "Hello"
        """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

        input = """
        func foo(string a) 
        begin 
            a <- a ... " World"
        end
        func main()
        begin
            string a <- "Hello"
            foo(a)
            writeString(a)
        end
        """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

        input = """
        func foo()
        func main()
        begin
            dynamic a
            a <- [foo() + 1, foo(), foo()]
            writeNumber(a[0])
            writeNumber(a[1])
            writeNumber(a[2])
        end
        func foo()
            return 1
        """
        expect = "2.01.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 558))


        input = """
            number a[3]
        func main()
        begin
            a[0] <- a[0] + 1
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_11_globe(self):
        input = """
        dynamic a
        func foo()
        begin
            writeNumber(a)
        end
        func main()
        begin
            a <- 1
            writeNumber(a)
            a <- 2
            foo()
        end
        """
        expect = "1.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

        input = """
        number a[2]
        func main ()
        begin
           a[0] <- a[1] + 1
        writeNumber(a[0])
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 561))
    
    def test_11_globe(self):
        input = """
        ## number a[2] <- [1, 2]
        ## func foo()
        ## begin
        ##     writeNumber(a[0])
        ## end

        func main ()
        begin
            ## writeNumber(a[0])
            ## a[0] <- 2
            ## foo()
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 562))
        



   

   


    

    





