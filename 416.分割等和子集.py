#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (47.64%)
# Likes:    307
# Dislikes: 0
# Total Accepted:    37K
# Total Submissions: 76.9K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 注意:
#
#
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
#
#
# 示例 1:
#
# 输入: [1, 5, 11, 5]
#
# 输出: true
#
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#
#
#
#
# 示例 2:
#
# 输入: [1, 2, 3, 5]
#
# 输出: false
#
# 解释: 数组不能分割成两个元素和相等的子集.
#
#
#
#
#
from typing import *

# @lc code=start


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        l = len(nums)
        if(s % 2 != 0 or l <= 0):
            return False
        t = int(s / 2)
        dp = [[False for j in range(t + 1)] for i in range(l)]
        if nums[0] <= t:
            dp[0][nums[0]] = True

        for i in range(1, l):
            for j in range(t + 1):
                dp[i][j] = dp[i - 1][j]
                if j - nums[i] == 0:
                    dp[i][j] = True
                elif nums[i] < j:
                    dp[i][j] = dp[i - 1][j] or dp[i-1][j - nums[i]]

        return dp[l - 1][t]
    
    def canPartition2(self, nums: List[int]) -> bool:
        s = sum(nums)
        l = len(nums)
        if(s % 2 != 0 or l <= 0):
            return False
        t = int(s / 2)
        dp = [[(j == 0 ) for j in range(t + 1)] for i in range(l + 1)]
        
        for i in range(1, l + 1):
            for j in range(1, t + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j] 
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]];
                
        return dp[l][t]


    def canPartition3(self, nums: List[int]) -> bool:
        s = sum(nums)
        l = len(nums)
        if(s % 2 != 0 or l <= 0):
            return False
        t = int(s / 2)
    
        dp = [False for j in range(t + 1)]
        dp[0] = True

        for i in range(0, l):
            for j in range(t, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]
        
        return dp[t]
        


# @lc code=end


assert Solution().canPartition([]) == False
assert Solution().canPartition([0]) == True
assert Solution().canPartition([1, 5, 11, 5]) == True
assert Solution().canPartition([1, 2, 3, 5]) == False

assert Solution().canPartition2([]) == False
assert Solution().canPartition2([0]) == True
assert Solution().canPartition2([1, 5, 11, 5]) == True
assert Solution().canPartition2([1, 2, 3, 5]) == False
