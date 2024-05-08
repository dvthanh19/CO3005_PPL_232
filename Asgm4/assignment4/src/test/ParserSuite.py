import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
