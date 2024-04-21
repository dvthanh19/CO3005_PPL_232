import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test0(self):
        input="""func main() 
            begin
            dynamic x
            dynamic y
            dynamic z
            dynamic t
            number a[2,4,1] <- [[y,y,[t],[z]], [x,x,x,x]]
            number b[1] <- y
            number c[1] <- x
            number d <- z
            number e <- t
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test1(self):    
        input="""func main()
            begin
            dynamic x
            dynamic y
            dynamic z
            number a[2,2,1] <- [[x,x], [y,y,y]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x), Id(x)), ArrayLit(Id(y), Id(y), Id(y)))"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test2(self): 
        input="""func main() 
            begin
            dynamic x
            dynamic y
            dynamic z
            dynamic t
            number a[2,2,1] <- [z, [[x, x], [y, [x]]]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x), Id(x)), ArrayLit(Id(y), ArrayLit(Id(x))))"
        # Type Mismatch In Expression: ArrayLit(Id(z), ArrayLit(ArrayLit(Id(x), Id(x)), ArrayLit(Id(y), ArrayLit(Id(x)))))
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test3(self): 
        input="""func main() 
            begin
            dynamic x
            dynamic y
            dynamic z
            number a[2,2,1] <- [[x,x,x,[z]],[y,y,y]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x), Id(x), Id(x), ArrayLit(Id(z))), ArrayLit(Id(y), Id(y), Id(y)))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test4(self):
        input="""
        func main() 
            begin
                dynamic x
                dynamic y
                dynamic z
                
                number a[2,1,3] <- [[x], y]
                number b[3] <- x
                dynamic c <- y
                number e[1,2,3] <- z
                number f[1,2,3] <- e
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    # def test5(self):
    #     input="""
    #     func main() 
    #         begin
    #             dynamic x
    #             dynamic y
    #             dynamic z
                
    #             number a[2,1,3] <- [[x], y]
    #             number b[2,2,1,3] <- [y,[z, z]]
    #         end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))











