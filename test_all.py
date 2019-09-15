
import unittest

import _9_palindrome_number

class TestForSolutions(unittest.TestCase):
    
    def test_9_1(self):
        case = [
            (12312, False),
            (1221, True)
        ]
        for k, v in enumerate(case):
            self.assertEqual(_9_palindrome_number.Sollution().isPalindrome(v[0]), v[1])

    