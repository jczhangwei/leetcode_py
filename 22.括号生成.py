#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.40%)
# Likes:    1442
# Dislikes: 0
# Total Accepted:    202.6K
# Total Submissions: 264.8K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例：
#
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
#
#
#
from typing import *
# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        total = [[None], ["()"]]
        for i in range(2, n + 1):
            l = []
            for j in range(i):
                p = total[j]
                q = total[i - 1 - j]
                for l_p in p:
                    for l_q in q:
                        if l_p == None:
                            l_p = ""
                        if l_q == None:
                            l_q = ""
                        l.append("(" + l_p + ")" + l_q)
            total.append(l)

        return total[n]

# @lc code=end


print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(3))
