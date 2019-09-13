
import math

class Solution:
    
    def mergeSort(self, nums, start, end):
        s = end - start
        if s <= 0:
            return nums
        elif s <= 1:
            if nums[start] > nums[end]:
                nums[start], nums[end] = nums[end], nums[start]
            return nums

        m = math.floor((end - start) / 2) + start
        self.mergeSort(nums, start, m)
        self.mergeSort(nums, m + 1, end)

        temp = []
        i = start
        j = m + 1
        for k in range(end - start + 1):
            if j > end or ( i <= m and nums[i] <= nums[j]):
                temp.append(nums[i])
                i = i+1
            elif i > m or (j <= end and j <= end):
                temp.append(nums[j])
                j = j + 1
        for k, v in enumerate(temp):
            nums[start] = v
            start = start + 1
        return nums


    def doTest(self):
        # case = [23, 89, 39, 3, 1, 0, 88, 421, 7]
        case = [5,2,3,1]

        nums = list(case)
        self.mergeSort(nums, 0, len(nums) - 1)
        print("mergeSort: ", nums)
