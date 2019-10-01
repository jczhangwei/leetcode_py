import math
import sys


class Sollution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        l = len(nums)
        if l < 3:
            return
        res = sys.maxsize
        for k, n in enumerate(nums):
            if k > 0 and n == nums[k - 1]:
                continue
            i = k + 1
            j = l - 1
            while i < j:
                a = n + nums[i] + nums[j]
                if abs(target - a) < abs(target - res):
                    res = a
                if a > target and i < j:
                    j = j - 1
                    while nums[j] == nums[j + 1] and i < j:
                        j = j - 1
                if a < target and i < j:
                    i = i + 1
                    while nums[i] == nums[i - 1] and i < j:
                        i = i + 1
                if a == target:
                    return a
        return res
