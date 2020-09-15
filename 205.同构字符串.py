#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode-cn.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (47.42%)
# Likes:    237
# Dislikes: 0
# Total Accepted:    51.8K
# Total Submissions: 109.1K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t，判断它们是否是同构的。
#
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
#
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 示例 1:
#
# 输入: s = "egg", t = "add"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "foo", t = "bar"
# 输出: false
#
# 示例 3:
#
# 输入: s = "paper", t = "title"
# 输出: true
#
# 说明:
# 你可以假设 s 和 t 具有相同的长度。
#
#
from math import fabs
from tkinter.constants import S
from typing import *
# 同构代表两个字符串中每个位置上字符在自身第一次出现的索引相同
# @lc code=start


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ss = {}
        st = {}
        for i in range(len(s)):
            a1 = s[i]
            a2 = t[i]
            if ((ss.__contains__(a1)) or (st.__contains__(a2))):
                if (not ss.__contains__(a1) or not st.__contains__(a2)) or (ss[a1] != st[a2]):
                    return False
            ss[a1] = i
            st[a2] = i

        return True 
# @lc code=end


Solution2().isIsomorphic("foo", "tkk")
Solution2().isIsomorphic("ab", "aa")
