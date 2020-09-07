#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (54.10%)
# Likes:    307
# Dislikes: 0
# Total Accepted:    42.6K
# Total Submissions: 78.7K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 
# 
# 
# 示例：
# 
# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
#
from typing import *
# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if len(A) <= 0 or len(B) <= 0:
            return []
        dp = [[0 for i in range(len(B) + 1)] for j in range(len(A) + 1)]

        res = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else 0
                res = max(res, dp[i][j])
        return res

class Solution2:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def maxLenght(a, b, length):
            r = 0
            m= 0
            for i in range(length) :
                if A[a + i] == B[b + i]:
                    m += 1
                    r = max(r, m) 
                else:
                     m = 0
            
            return r

        r = 0
        m = len(A)
        n = len(B)
        for i in range(m):
            r = max(r, maxLenght(i, 0, min(m - i, n)))
        for i in range(n):
            r = max(r, maxLenght(0, i, min(n - i, m)))
        
        return r

# @lc code=end

print(Solution().findLength([1,2,3,2,1], [3,2,1,4,7]))
print(Solution2().findLength([1,2,3,2,1], [3,2,1,4,7]))