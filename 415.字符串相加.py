#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (51.85%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    82.9K
# Total Submissions: 159.9K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
#
#
# 提示：
#
#
# num1 和num2 的长度都小于 5100
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
#
#
#
from typing import *
# @lc code=start


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        up = 0
        i = len(num1) - 1
        j = len(num2) - 1
        z_ord = ord("0")
        while i >= 0 or j >= 0 or up > 0:
            x = 0
            y = 0
            if i >= 0:
                x = ord(num1[i]) - z_ord
            if j >= 0:
                y = ord(num2[j]) - z_ord

            r = x + y + up
            up = r // 10
            res = str(r % 10) + res
            i -= 1
            j -= 1
        return res


# @lc code=end

print(Solution().addStrings("123", "458"))