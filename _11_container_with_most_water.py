import math


class Sollution:

    def maxArea(self, height):
        l = len(height)
        m = 0
        i = 0
        j = l - 1
        while i < j:
            m = max(m, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1

        return m
