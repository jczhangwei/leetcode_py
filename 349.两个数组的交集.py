#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (70.48%)
# Likes:    229
# Dislikes: 0
# Total Accepted:    92.6K
# Total Submissions: 131.1K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
# 
# 
# 示例 2：
# 
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 
# 
# 
# 说明：
# 
# 
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
# 
# 
#
from typing import *
# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        res = set()
        for k, v in enumerate(nums2):
            if v in s1:
                res.add(v)
        
        return list(res)
        
# @lc code=end

