import math


class Sollution:

    def isPalindrome(self, x):
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        k = 0
        while x > k:
            k = k * 10 + x % 10
            x = x // 10
        
        return x == k or x == k // 10
            

    def doTest(self):
        s1 = 11
        r = self.isPalindrome(s1)
        print("isPalindrome: ", r)
        assert(r == True)
