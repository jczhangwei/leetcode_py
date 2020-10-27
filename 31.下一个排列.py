#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (34.59%)
# Likes:    709
# Dislikes: 0
# Total Accepted:    95.7K
# Total Submissions: 276.5K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#
from typing import *
# @lc code=start


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def revert(nums, start, end):
            i = start
            j = end - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        l = len(nums)
        t1 = - 1
        for i in range(l - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                t1 = i - 1
                break

        t2 = l - 1
        if t1 >= 0:    
            for i in range(l - 1, t1, -1):
                if nums[i] > nums[t1]:
                    t2 = i
                    break
            nums[t1], nums[t2] = nums[t2], nums[t1]
        revert(nums, t1 + 1, l)


# @lc code=end
t1 = [1,2,3] 
t2 = [3,2,1] 
t3 = [1,1,5] 
t4 = [2,3,1] 
Solution().nextPermutation(t4)
Solution().nextPermutation(t1)
Solution().nextPermutation(t2)
Solution().nextPermutation(t3)

print(t1, t2, t3, t4)