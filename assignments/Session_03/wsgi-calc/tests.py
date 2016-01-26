import os
import unittest
import sys


class AdditionTestCase(unittest.TestCase):
    """unit tests for the addition method in our server
        Static test - server need not be running
    """

    def test_no_operand_values(self):
        from calculator import addition
        operands = ""
        expected_values = "Operands provided: []"
        actual = addition(operands)
        self.assertTrue(expected_values in actual)

    def test_no_operand_result(self):
        from calculator import addition
        operands = ""
        expected_result = "0"
        actual = addition(operands)
        self.assertTrue(expected_result in actual)

    def test_one_operand_values(self):
        from calculator import addition
        operands = "4"
        expected_values = "Operands provided: [4]"
        actual = addition(operands)
        self.assertTrue(expected_values in actual)

    def test_one_operand_result(self):
        from calculator import addition
        operands = "4"
        expected_result = "4"
        actual = addition(operands)
        self.assertTrue(expected_result in actual)

    def test_three_operands_values(self):
        from calculator import addition
        operands = '/4/5/-1'
        expected_values = "Operands provided: [4, 5, -1]"
        actual = addition(operands)
        self.assertTrue(expected_values in actual)

    def test_three_operands_result(self):
        from calculator import addition
        operands = '/4/5/-1'
        expected_result = "Sum of operands: 8"
        actual = addition(operands)
        self.assertTrue(expected_result in actual)


class SubtractionTestCase(unittest.TestCase):
    """unit tests for the subtraction method in our server
        Static test - server need not be running
    """

    def test_no_operand_values(self):
        from calculator import subtraction
        operands = ""
        expected_values = "Operands provided: []"
        actual = subtraction(operands)
        self.assertTrue(expected_values in actual)

    def test_no_operand_result(self):
        from calculator import subtraction
        operands = ""
        expected_result = "0"
        actual = subtraction(operands)
        self.assertTrue(expected_result in actual)

    def test_one_operand_values(self):
        from calculator import subtraction
        operands = "5"
        expected_values = "Operands provided: [5]"
        actual = subtraction(operands)
        self.assertTrue(expected_values in actual)

    def test_one_operand_result(self):
        from calculator import subtraction
        operands = "5"
        expected_result = "5"
        actual = subtraction(operands)
        self.assertTrue(expected_result in actual)

    def test_three_operands_values(self):
        from calculator import subtraction
        operands = '/9/12/-1'
        expected_values = "Operands provided: [9, 12, -1]"
        actual = subtraction(operands)
        self.assertTrue(expected_values in actual)

    def test_three_operands_result(self):
        from calculator import subtraction
        operands = '/9/12/-1'
        expected_result = "Difference  of operands: -2"
        actual = subtraction(operands)
        self.assertTrue(expected_result in actual)


class MultiplicationTestCase(unittest.TestCase):
    """unit tests for the multiplication method in our server
        Static test - server need not be running
    """

    def test_no_operand_values(self):
        from calculator import multiplication
        operands = ""
        expected_values = "Operands provided: []"
        actual = multiplication(operands)
        self.assertTrue(expected_values in actual)

    def test_no_operand_result(self):
        from calculator import multiplication
        operands = ""
        expected_result = "0"
        actual = multiplication(operands)
        self.assertTrue(expected_result in actual)

    def test_one_operand_values(self):
        from calculator import multiplication
        operands = "99"
        expected_values = "Operands provided: [99]"
        actual = multiplication(operands)
        self.assertTrue(expected_values in actual)

    def test_one_operand_result(self):
        from calculator import multiplication
        operands = "99"
        expected_result = "99"
        actual = multiplication(operands)
        self.assertTrue(expected_result in actual)

    def test_three_operands_values(self):
        from calculator import multiplication
        operands = '/-34/2/-1'
        expected_values = "Operands provided: [-34, 2, -1]"
        actual = multiplication(operands)
        self.assertTrue(expected_values in actual)

    def test_three_operands_result(self):
        from calculator import multiplication
        operands = '/-34/2/-1'
        expected_result = "Result of operand multiplication: 68"
        actual = multiplication(operands)
        self.assertTrue(expected_result in actual)

class DivisionTestCase(unittest.TestCase):
    """unit tests for the division method in our server
        Static test - server need not be running
    """

    def test_no_operand_values(self):
        from calculator import division
        operands = ""
        expected_values = "Operands provided: []"
        actual = division(operands)
        self.assertTrue(expected_values in actual)

    def test_no_operand_result(self):
        from calculator import division
        operands = ""
        expected_result = "0"
        actual = division(operands)
        self.assertTrue(expected_result in actual)

    def test_one_operand_values(self):
        from calculator import division
        operands = "-16"
        expected_values = "Operands provided: [-16]"
        actual = division(operands)
        self.assertTrue(expected_values in actual)

    def test_one_operand_result(self):
        from calculator import division
        operands = "-16"
        expected_result = "-16"
        actual = division(operands)
        self.assertTrue(expected_result in actual)

    def test_three_operands_values(self):
        from calculator import division
        operands = '/-34/2/-1'
        expected_values = "Operands provided: [-34, 2, -1]"
        actual = division(operands)
        self.assertTrue(expected_values in actual)

    def test_three_operands_result(self):
        from calculator import division
        operands = '/-34/2/-1'
        expected_result = "Result of operand division: 17"
        actual = division(operands)
        self.assertTrue(expected_result in actual)

    def test_one_operand_divide_by_zero(self):
        from calculator import division
        operands = "0"
        expected_values = "Operands provided: [0]"
        actual = division(operands)
        self.assertTrue(expected_values in actual)

    def test_three_operands_divide_by_zero_first_value(self):
        from calculator import division
        operands = "/0/2/-1"
        expected_values = "Operands provided: [0, 2, -1]"
        actual = division(operands)
        self.assertTrue(expected_values in actual)

    def test_three_operands_divide_by_zero_second_value(self):
        from calculator import division
        operands = "/2/0/12"
        try:
            actual = division(operands)
        except (ZeroDivisionError, Exception) as e:
            exception = 'yes'
        self.assertTrue(exception == 'yes')

    def test_three_operands_divide_by_zero_third_value(self):
        from calculator import division
        operands = "/2/12/0"
        try:
            actual = division(operands)
        except (ZeroDivisionError, Exception) as e:
            exception = 'yes'
        self.assertTrue(exception == 'yes')


if __name__ == '__main__':
    unittest.main()