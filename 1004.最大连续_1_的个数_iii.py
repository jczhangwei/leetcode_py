#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
# https://leetcode-cn.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (53.45%)
# Likes:    104
# Dislikes: 0
# Total Accepted:    14.4K
# Total Submissions: 26.4K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
#
# 返回仅包含 1 的最长（连续）子数组的长度。
#
#
#
# 示例 1：
#
# 输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
#
# 示例 2：
#
# 输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。
#
#
#
# 提示：
#
#
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] 为 0 或 1 
#
#
#
from typing import *

# @lc code=start


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        one_num = 0
        i = 0
        j = 0
        l = len(A)
        while j < l:
            if A[j] == 1:
                one_num += 1
            j += 1
            if j - i > K + one_num:
                if A[i] == 1:
                    one_num -= 1
                i += 1

        return j - i
        # @lc code=end


print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution().longestOnes(
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
