#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (39.40%)
# Likes:    628
# Dislikes: 0
# Total Accepted:    90.5K
# Total Submissions: 227.6K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 
# 
# 示例 1:
# 
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 
# 示例 2:
# 
# 输入: coins = [2], amount = 3
# 输出: -1
# 
# 
# 
# 说明:
# 你可以认为每种硬币的数量是无限的。
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float("inf")
        dp = [0] + [inf for a in range(1, amount + 1)]
        
        for i in range(amount + 1):
            for c in coins:
                if i - c < 0:
                    continue
                dp[i] = min(dp[i], dp[i - c] + 1)
        
        if (dp[amount] != None) and dp[amount] <= amount:
            return dp[amount]

        return -1
            
# @lc code=end

