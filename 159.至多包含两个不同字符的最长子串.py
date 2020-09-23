#
# @lc app=leetcode.cn id=159 lang=python3
#
# [159] 至多包含两个不同字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/
#
# algorithms
# Medium (74.65%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 4.5K
# Testcase Example:  "eceba"
#
# 给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。
#
# 示例 1:
#
# 输入: "eceba"
# 输出: 3
# 解释: t 是 "ece"，长度为3。
# 示例 2:
#
# 输入: "ccaabbb"
# 输出: 5
# 解释: t 是 "aabbb"，长度为5。


from typing import *

# @lc code=start


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_count = {}
        l = len(s)
        i = 0
        j = 0
        while j < l:
            char_count[s[j]] = (char_count.get(s[j]) or 0) + 1
            j += 1
            if sum(1 for x in char_count.values() if x > 0) > 2:
                char_count[s[i]] = max(0, (char_count.get(s[i] or 0) - 1))
                i += 1

        return j - i
        # @lc code=end


print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))
print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))
