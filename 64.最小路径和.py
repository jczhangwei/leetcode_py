#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (65.70%)
# Likes:    489
# Dislikes: 0
# Total Accepted:    91.6K
# Total Submissions: 139.4K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid):
        if len(grid) <= 0:
            return 0
        dp = []
        for i,vi in enumerate(grid):
            dp.append([])
            if len(grid[i]) <= 0:
                return 0
            for j,vij in enumerate(vi):
                dp[i].append(0)
                if i<=0 and j<=0:
                    p = 0
                elif i> 0 and j> 0:
                    p = min(dp[i - 1][j], dp[i][j - 1])
                elif i<= 0:
                    p = dp[i][j - 1]
                else:
                    p = dp[i - 1][j]

                dp[i][j] = p + grid[i][j]

        return dp[len(grid) - 1][len(grid[0]) - 1]

res = (Solution()).minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print("")
print(res)
# @lc code=end

