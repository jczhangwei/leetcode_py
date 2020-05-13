#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (43.42%)
# Likes:    263
# Dislikes: 0
# Total Accepted:    25.2K
# Total Submissions: 58.1K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
# 
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
# 
# 说明：
# 
# 
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 
# 
# 示例 1:
# 
# 
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
# 
# 
# 示例 2:
# 
# 
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
# 
# 
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        window = {}
        left = 0
        right = 0
        valid = 0
        res = []

        for c in p:
            need[c] = (need.get(c) or 0 ) + 1
        
        while right < len(s):
            right_c = s[right]
            right += 1
            if need.get(right_c) is not None:
                window[right_c] = (window.get(right_c) or 0) + 1
                if window[right_c] == need[right_c]:
                    valid += 1
            
            while right - left > len(p):
                left_c = s[left]
                left += 1
                if need.get(left_c) is not None:
                    window[left_c] -= 1
                    if window[left_c] < need[left_c]:
                        valid -= 1

            if valid == len(need):
                res.append(left)
                
        
        return res
            
# @lc code=end

