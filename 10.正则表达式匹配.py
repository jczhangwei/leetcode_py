#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (28.24%)
# Likes:    1366
# Dislikes: 0
# Total Accepted:    97.2K
# Total Submissions: 326.2K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# 
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 
# 
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
# 
# 说明:
# 
# 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 
# 
# 示例 1:
# 
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
# 
# 示例 3:
# 
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
# 
# 示例 4:
# 
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 
# 
# 示例 5:
# 
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
# 
#
from typing import *
# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls = len(s)
        lp = len(p)
        dp = [[False for j in range(lp + 1)] for i in range(ls + 1)]
        def match(a, b):
            if a == 0:
                return False
            if lp > 0 and p[b - 1]==".":
                return True

            return s[a - 1] == p[b - 1]

        dp[0][0] = True

        for i in range(0, ls + 1):
            for j in range(1, lp + 1):
                if p[j - 1] == "*":
                    if match(i, j - 1):
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
                else :
                    if match(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
            
        
        return dp[ls][lp]
                        
                        
                        
                    
# @lc code=end


# assert Solution().isMatch("aa", "a") == False
assert Solution().isMatch("aa", "a*") == True
assert Solution().isMatch("ab", ".*") == True
assert Solution().isMatch("aab", "c*a*b") == True
assert Solution().isMatch("mississippi", "mis*is*p*.") == False
