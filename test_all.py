
import unittest

import _9_palindrome_number
import _10_regular_expression_matching
import _11_container_with_most_water

class TestForSolutions(unittest.TestCase):
    
    def test_9_1(self):
        case = [
            (12312, False),
            (1221, True)
        ]
        for k, v in enumerate(case):
            self.assertEqual(_9_palindrome_number.Sollution().isPalindrome(v[0]), v[1])

    def test_11(self):
        case = [
             ([1,8,6,2,5,4,8,3,7], 49)
        ]
        for k, v in enumerate(case):
            self.assertEqual(_11_container_with_most_water.Sollution().maxArea(v[0]), v[1])

    def test_10(self):
        case = [
             ("aa", "a*", True),
             ("aa", "a", False),
             ("ab", ".*", True),
             ("aab", "c*a*b*", True),
             ("mississippi", "mis*is*p*.", False),
        ]
        for k, v in enumerate(case):
            self.assertEqual(
                _11_container_with_most_water.Sollution().isMatch(v[0], v[1]), v[3])
