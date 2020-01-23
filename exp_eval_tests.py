# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01a(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_01b(self):
        self.assertAlmostEqual(postfix_eval("8 1 >>"), 4)
        self.assertAlmostEqual(postfix_eval("8 1 <<"), 16)

    def test_postfix_eval_01c(self):
        self.assertAlmostEqual(postfix_eval("8 2 **"), 64)

    def test_postfix_eval_01d(self):
        self.assertAlmostEqual(postfix_eval("18.5 -2 *"), -37)
        self.assertAlmostEqual(postfix_eval("-18.52 -0.78 +"), -19.3)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03a(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03b(self):
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_infix_to_postfix_01a(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("32 >> 2 >> 1"), "32 2 >> 1 >>")

    def test_infix_to_postfix_01b(self):
        self.assertEqual(infix_to_postfix("32 >> 2 << 1"), "32 2 >> 1 <<")

    def test_infix_to_postfix_01c(self):
        self.assertEqual(infix_to_postfix("3 ** 2 ** 2"), "3 2 2 ** **")

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("( 5 - 3 ) * 4"), "5 3 - 4 *")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix("70 - -3 * 10"), "70 -3 10 * -")

    def test_infix_to_postfix_04(self):
        self.assertEqual(infix_to_postfix("70.52 - 3.5 * 10.05"), "70.52 3.5 10.05 * -")

    def test_infix_to_postfix_05(self):
        self.assertEqual(infix_to_postfix("-70.52 - 3.5 * 10.05"), "-70.52 3.5 10.05 * -")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

if __name__ == "__main__":
    unittest.main()
