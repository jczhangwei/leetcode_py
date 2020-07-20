#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (39.71%)
# Likes:    502
# Dislikes: 0
# Total Accepted:    197.9K
# Total Submissions: 498.2K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#
from typing import *
# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(haystack)
        n = len(needle)

        if n <= 0:
            return 0
        
        i = 0
        while i <= l - n:
            if haystack[i] == needle[0]:
                j = 0
                while j < n and i < l:
                    if haystack[i] == needle[j]:
                        i+=1        ## 有数值的增加，就要在d循环条件里检查上确界
                        j+=1
                        if j == n:
                            return i - j
                    else:
                        i = i - j + 1
                        j = 0

            i+=1

        return -1 

# @lc code=end


assert Solution().strStr("hello", "ll") == 2
assert Solution().strStr("aaaaa", "bba") == -1
assert Solution().strStr("", "bba") == -1
assert Solution().strStr("aaaaa", "") == 0
assert Solution().strStr("a", "a") == 0
assert Solution().strStr("aaa", "aaa") == 0
assert Solution().strStr("mississippi", "issipi") == -1
