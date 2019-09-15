import math


class Sollution:

    def myAtoi(self, s):
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        num = 0
        sign = 1
        start = False
        for i, c in enumerate(s):
            if c == '-' or c == '+':
                if not start:
                    start = True
                    if c == '-':
                        sign = -1
                else:
                    break
            elif not start and c == ' ':
                continue
            else:
                o = ord(c)
                if o >= 48 and o <= 57:
                    start = True
                    n = o - 48
                    num = num * 10 + n
                else:
                    break
                    
        num = num * sign
        num = min(max(num, MIN_INT), MAX_INT)

        return num
            

    def doTest(self):
        s1 = "  12 3 asdfwpenf"
        r = self.myAtoi(s1)
        print("_8_string_to_integer: ", r)
        assert(r == 12)
