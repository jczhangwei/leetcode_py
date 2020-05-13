#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (34.42%)
# Likes:    3641
# Dislikes: 0
# Total Accepted:    482.6K
# Total Submissions: 1.4M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0
        right = 0
        invalid = 0
        res = 0
        while right < len(s):
            right_c = s[right]
            right += 1
            window[right_c] = (window.get(right_c) or 0) + 1

            while window[right_c] > 1:
                left_c = s[left]
                left += 1
                window[left_c] = window[left_c] - 1
                            
            res = max(res, right - left)

        return res
             
# @lc code=end

