#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (46.51%)
# Likes:    284
# Dislikes: 0
# Total Accepted:    171.9K
# Total Submissions: 369.4K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
#
#
# 示例 2:
#
# 输入: "race a car"
# 输出: false
#
#
#
from typing import *
# @lc code=start


class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = 0
        q = len(s) - 1
        while p < q:
            while not(s[p].isdecimal() or s[p].isalpha()) and p < len(s) - 1:
                p += 1
            while not(s[q].isdecimal() or s[q].isalpha()) and q > 0:
                q -= 1
            if p < q and s[p].lower() != s[q].lower():
                return False
            p += 1
            q -= 1
        return True
        # @lc code=end


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
