#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (59.35%)
# Likes:    922
# Dislikes: 0
# Total Accepted:    62.8K
# Total Submissions: 105.9K
# Testcase Example:  '"horse"\n"ros"'
#
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
# 
# 你可以对一个单词进行如下三种操作：
# 
# 
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 
# 
# 
# 
# 示例 1：
# 
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
# 
# 示例 2：
# 
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# 
#
# 子字符串不包含i,j指向位置的字母, 这样才能用0来表示空字符串

# @lc code=start
class Solution:
    def minDistance(self, word1, word2):
        dp = []
        for i in range(len(word1) + 1):
            dp.append([])
            for j in range(len(word2) + 1):
                dp[i].append(0)
                
                if i * j == 0:
                    dp[i][j] = max(i, j)
                else:
                    c1 = word1[i - 1]
                    c2 = word2[j - 1]
                    if c1 == c2:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],dp[i - 1][j - 1]) + 1

        return dp[len(word1)][len(word2)]            


        
print((Solution()).minDistance("intention","execution"))
# @lc code=end

