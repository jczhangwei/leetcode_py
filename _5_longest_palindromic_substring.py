import math


class Sollution:
    def extend(self, s, start, end):
        l = len(s)
        while start >= 0 and end < l and start<=end and s[start] == s[end]:
            start = start - 1
            end = end + 1
        return end - start - 1

    def longestPalindrome(self, s):
        if len(s) < 1:
            return ""
        start, end = 0, 0
        for i, v in enumerate(s):
            l1 = self.extend(s, i, i)
            l2 = self.extend(s, i, i + 1)
            l = max(l1, l2)
            if l > end - start + 1:
                if l1 > l2:
                    h = math.floor((l1 - 1) / 2)
                    start = i - h
                    end = i + h
                else :
                    h = math.floor(l2 / 2)
                    start = i - math.floor(l2 / 2 - 1)
                    end = i + math.floor(l2 / 2)
        return s[start:end + 1]

    def doTest(self):
        s1 = "cabcddcbaaaad"
        r = self.longestPalindrome(s1)
        print("longestPalindrome: ", r)
