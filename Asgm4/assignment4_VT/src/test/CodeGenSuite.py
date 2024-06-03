import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    # #* test cơ bản về hàm main và các hàm write
    # def test0(self):
    #     input = """
    #     func main ()
    #     begin
    #         writeNumber(1)
    #         writeBool(true)
    #         writeString("votien")
    #     end
    #     """
    #     expect = "1.0\ntrue\nvotien\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 500))
    
   
    
    def test0(self):
        input = """
        func main ()
        begin
            return 
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 500))
    
    
     # def test1(self):
    #     input = """
    #     number a
    #     func main ()
    #     begin
    #         number b
    #         return 
    #     end
    #     """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))
        
