import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """var a <- ZcExpr
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))



    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """number a[1,2] <- 7 + [[1]]
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))
    
    
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """number a[1,2] <- 1 ... 3
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,204))
        
    
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """func foo(number a, number b)
    #     begin
    #         var a <- 1
    #         b <- 2
    #     end
    #     """
        
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,299))
    
    