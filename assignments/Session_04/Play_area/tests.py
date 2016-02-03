import os
import unittest
import sys


class AdditionTestCase(unittest.TestCase):
    """unit tests for the addition method in our server
        Static test - server need not be running
    """

    def test_get_inspection_page(self):
        from calculator import addition
        operands = ""
        expected_values = "Operands provided: []"
        actual = addition(operands)
        self.assertTrue(expected_values in actual)


if __name__ == '__main__':
    unittest.main()