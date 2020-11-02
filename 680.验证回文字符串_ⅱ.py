#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (39.90%)
# Likes:    280
# Dislikes: 0
# Total Accepted:    55K
# Total Submissions: 137.8K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
# 示例 1:
#
#
# 输入: "aba"
# 输出: True
#
#
# 示例 2:
#
#
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
#
#
# 注意:
#
#
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
#
#
#
from typing import *
# @lc code=start


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(s: str, start, end):
            i = start
            j = end
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isValid(s, i + 1, j) or isValid(s, i, j - 1)
            i += 1
            j -= 1

        return True

# @lc code=end


print(Solution().validPalindrome("abca"))
print(Solution().validPalindrome("aba"))
print(Solution().validPalindrome(""))
print(Solution().validPalindrome("a"))
print(Solution().validPalindrome("abc"))
