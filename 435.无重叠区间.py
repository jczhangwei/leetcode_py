#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
# https://leetcode-cn.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (45.74%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    19K
# Total Submissions: 41.7K
# Testcase Example:  '[[1,2]]'
#
# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
# 
# 注意:
# 
# 
# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
# 
# 
# 示例 1:
# 
# 
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
# 
# 输出: 1
# 
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
# 
# 
# 示例 2:
# 
# 
# 输入: [ [1,2], [1,2], [1,2] ]
# 
# 输出: 2
# 
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
# 
# 
# 示例 3:
# 
# 
# 输入: [ [1,2], [2,3] ]
# 
# 输出: 0
# 
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
# 
# 
#
from typing import *

# @lc code=start
class Solution:
    def notCross(self, interval1, interval2):
        return interval1[0] >= interval2[1] or interval1[1] <= interval2[0]

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        l = len(intervals)
        if l <= 0:
            return 0

        dp = [1]
        msi = 1
        for i in range(1, l):
            dp.append(0)
            m = 0
            for j in range(i - 1, -1, -1):
                if self.notCross(intervals[i], intervals[j]):
                    m = max(dp[j], m)
            dp[i] = m + 1
            msi = max(dp[i], msi)
        
        return l - msi
        

# @lc code=end

assert Solution().eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3] ]) == 1
assert Solution().eraseOverlapIntervals([]) == 0
assert Solution().eraseOverlapIntervals([ [1,2], [1,2], [1,2] ]) == 2
assert Solution().eraseOverlapIntervals([ [1,2], [2,3] ]) == 0
