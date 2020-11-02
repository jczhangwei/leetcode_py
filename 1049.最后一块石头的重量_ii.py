#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#
# https://leetcode-cn.com/problems/last-stone-weight-ii/description/
#
# algorithms
# Medium (48.15%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 12.7K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# 有一堆石头，每块石头的重量都是正整数。
# 
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
# 
# 
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 
# 
# 最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
# 
# 
# 
# 示例：
# 
# 输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
# 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
# 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
# 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
# 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
# 
# 
#
from typing import *
# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        l = len(stones)
        ss = sum(stones)
        s = ss // 2
        # dp[i][j]表示面对第 i个石头时， 容量j的背包的最大重量
        dp = [[0 for x in range(s + 1)] for x in range(l + 1)]
        for i in range(1, l + 1):
            w = stones[i - 1]
            for j in range(s + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j >= w:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + w)

        return ss - 2 * dp[l][s]
# @lc code=end

