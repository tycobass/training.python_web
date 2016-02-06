import os
import unittest
import sys


class get_Inspection_page(unittest.TestCase):
    """unit tests for the addition method in our server
        Static test - server need not be running
    """

    def test_get_inspection_page(self):
        from mashup_5 import get_inspection_page
        use_params = {
        'Inspection_Start': '2/1/2015',
        'Inspection_End': '2/10/2015',
        'Zip_Code': '98105',
        'Violation_Red_Points': '200'
        }
        operands = ""
        expected_values = "Operands provided: []"
        actual = addition(operands)
        self.assertTrue(expected_values in actual)


if __name__ == '__main__':
    unittest.main()