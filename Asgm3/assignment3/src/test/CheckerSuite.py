
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