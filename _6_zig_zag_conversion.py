import math


class Sollution:
    def extend(self, s, start, end):
        l = len(s)
        while start >= 0 and end < l and start<=end and s[start] == s[end]:
            start = start - 1
            end = end + 1
        return end - start - 1

    def convert(self, s, numRows):
        for r in range(numRows):
            start = r
            interval = r * 2 - 2
            

    def doTest(self):
        s1 = "cabcddcbaaaad"
        r = self.longestPalindrome(s1)
        print("longestPalindrome: ", r)
