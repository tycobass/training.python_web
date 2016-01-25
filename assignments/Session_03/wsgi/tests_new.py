import os
import unittest
import sys


CRLF = '\r\n'
CRLF_BYTES = CRLF.encode('utf8')



class AdditionTestCase(unittest.TestCase):
    """unit tests for the addition method in our server

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
        #import pdb; pdb.set_trace()    ###import debugger
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

if __name__ == '__main__':
    unittest.main()

#Debugging stuff follows
"""
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HTTPServerFunctionalTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
"""

"""
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HTTPServerFunctionalTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
"""
###python tests.py ResolveURITestCase.test_file_resource
###python tests.py HTTPServerFunctionalTestCase.test_get_request
####import pdb; pdb.set_trace()    ###import debugger
#print('!!!!! function_under_test mimetype_one =', mimetype, '\n', file=sys.stderr)  #debug - remove !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
