#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (35.42%)
# Likes:    124
# Dislikes: 0
# Total Accepted:    25.5K
# Total Submissions: 71.8K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
# 
# 示例1:
# 
# 
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
# 
# 
# 
# 
# 示例2:
# 
# 
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
# 
# 
# 
# 
# 注意：
# 
# 
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        need = {}
        valid = 0
        left = 0
        right =0

        for a in s1:
            need[a] = (need.get(a) or 0) + 1

        while right < len(s2):    
            right_c = s2[right]
            right += 1
            if need.get(right_c) is not None:
                window[right_c] = (window.get(right_c) or 0) + 1
                if window[right_c] == need[right_c]:
                    valid += 1

            while valid >= len(need):
                if right - left == len(s1):
                    print(left, right, window, valid)
                    return True
                left_c = s2[left]
                left += 1
                if need.get(left_c) is not None:
                    window[left_c] -= 1
                    if window[left_c] < need[left_c]:
                        valid -= 1

        return False
# @lc code=end
