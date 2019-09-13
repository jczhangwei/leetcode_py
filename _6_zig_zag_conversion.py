import math


class Sollution:

    def convert(self, s, numRows):
        l = len(s)
        res = []
        if numRows >= 1:
            i = 0
            while i< l:
                res.append(s[i])
                i = i + max(1,  numRows * 2 - 2)

        for r in range(1, numRows - 1):
            i = r
            c = 0
            while i < l:
                res.append(s[i])
                t = (c % 2)
                i = i + (2 * (numRows - r - 1) * (1 - t)) + (2 * r * t)
                c = c + 1

        if numRows > 1:
            i = numRows - 1
            while i < l:
                res.append(s[i])
                i = i + numRows * 2 - 2
        
        return str.join("", res)
            

    def doTest(self):
        s1 = "ABCDEFGHIJKLM"
        s1 = "A"
        r = self.convert(s1, 1)
        print("_6_zig_zag_conversion: ", r)
        assert(r == "A" )
