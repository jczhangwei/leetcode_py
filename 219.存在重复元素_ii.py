#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# https://leetcode-cn.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (40.19%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    61.2K
# Total Submissions: 151.5K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的
# 绝对值 至多为 k。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 
# 示例 2:
# 
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 
# 示例 3:
# 
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
# 
#
from typing import *
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        l = len(nums)
        for i in range(l):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s) > k:
                s.remove(nums[i - k])
        
        return False
# @lc code=end

print(Solution().containsNearbyDuplicate([1,2,3,1,2,3],2))