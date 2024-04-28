import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """func main()
        begin
            dynamic c
            if (c > 1)
                return
            elif (c < 1)
                c <- a 
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestAST.test(input, expect, 300))