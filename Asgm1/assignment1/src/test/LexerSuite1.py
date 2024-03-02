import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # def test_simple_string(self):
    #     """test simple string"""
    #     self.assertTrue(TestLexer.test("'Yanxi Palace - 2018'","'Yanxi Palace - 2018',<EOF>",101))

    # def test_complex_string(self):
    #     """test complex string"""
    #     self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
    
    
    # def test1(self):
        # self.assertTrue(TestLexer.test('"kkkk\'"',"1,<EOF>", 'test'))  
    
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """ "'a" """
        expect = "successful"
        self.assertTrue(TestLexer.test(input,expect,290)) 
    
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """if (a>0) return 1
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input,expect,299))  