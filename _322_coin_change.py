import math
import sys


class Sollution:

    def coinChange(self, coins, amount):
        values = []
        values.insert(0, 0)
        for i in range(1, amount + 1):
            m = sys.maxsize
            for k, c in enumerate(coins):
                p = i - c
                if p >= 0:
                    v = values[p] + 1
                    if v < m:
                        m = v
            values.insert(i,  m)
        res = values[amount]
        if res is sys.maxsize:
            res = -1
        
        return res
