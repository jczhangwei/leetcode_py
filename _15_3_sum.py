import math


class Sollution:
    def threeSum(self, nums):
        nums.sort()
        l = len(nums)
        res = []
        for k, n in enumerate(nums):
            if k > 0 and nums[k - 1] == n:
                continue
            if n > 0:
                break
            
            i = k + 1
            j = l - 1

            while i < j :
                r = n + nums[i] + nums[j]
                if r == 0:
                    res.append([n, nums[i], nums[j]])
                    
                if r <= 0:
                    i = i + 1
                    while nums[i - 1] == nums[i] and i < j:
                        i = i + 1

                if r >= 0:
                    j = j - 1
                    while nums[j] == nums[j + 1] and i < j:
                        j = j - 1


        return res
