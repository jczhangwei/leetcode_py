#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (33.08%)
# Likes:    911
# Dislikes: 0
# Total Accepted:    95.1K
# Total Submissions: 283.4K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#
#
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#
#
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if(len(s) < 2):
            return 0

        dp = [0]
        if(s[0] == "(" and s[1] == ")"):
            dp.append(2)
        else:
            dp.append(0)

        for i in range(2, len(s)):
            dp.append(0)
            if(s[i] == ")"):
                if(s[i - 1] == "("):
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]

        return max(dp)

    def longestValidParentheses2(self, s: str) -> int:
        
        return max(dp)

# @lc code=end


print(Solution().longestValidParentheses("(()"))
print(Solution().longestValidParentheses("()"))
print(Solution().longestValidParentheses(""))
print(Solution().longestValidParentheses("(()))())("))

print(Solution().longestValidParentheses2("(()"))
print(Solution().longestValidParentheses2("()"))
print(Solution().longestValidParentheses2(""))
print(Solution().longestValidParentheses2("(()))())("))
