import math


class Sollution:

    def longestCommonPrefix(self, strs):
        res = ""
        if len(strs) > 0 and len(strs[0]) > 0:
            for i, m in enumerate(strs[0]):
                fail = False
                for _, v in enumerate(strs):
                    if len(v) <= i or v[i] != m:
                        fail = True
                        break
      
                if fail:
                    break           
                else:
                    res = res + m
        return res
