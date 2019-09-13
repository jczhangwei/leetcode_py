import math


class Sollution:

    def reverse(self, x):
        mn = -2**31
        mm = 2**31 - 1
        res = 0
        s = 1
        if x < 0:
            s = -1
        x = abs(x)
        while x > 0:
            t = x % 10
            x = math.floor(x / 10)
            res = res * 10 + t
        
        res = res * s
        if res <mn or res > mm:
            res = 0

        return res
            

    def doTest(self):
        s1 = 123
        r = self.reverse(s1)
        print("7_reverse_integer: ", r)
        assert(r == 321)
