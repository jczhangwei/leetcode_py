#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (48.38%)
# Likes:    8211
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 2.1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# 
# 
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 
#
from typing import *
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i =0
        t = {} 
        while i < len(nums):
            cur = nums[i]
            sub = target - cur
            sub_i = t.get(sub)
            if sub_i is not None:
                return [sub_i, i]
            else:
                t[cur] = i
            i += 1
            
# @lc code=end
