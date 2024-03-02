import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test1(self):
        """Simple program: int main() {} """
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    
    def test2(self):
        """Simple program: int main() {} """
        input = """func main()
                begin
                    if (true) return 1
                    elif (true) return 1
                    elif (true) return 1
                    else return 1
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
