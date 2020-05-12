#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (35.90%)
# Likes:    464
# Dislikes: 0
# Total Accepted:    38.5K
# Total Submissions: 107.2K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
#
# 说明：
#
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
#
#
#

# @lc code=start


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        right = 0
        left = 0
        valid = 0
        size = len(s)
        valid_s = ""
        for c in t:
            window[c] = 0
            need[c] = (need.get(c) or 0) + 1

        while right < size:
            right_c = s[right]
            n = need.get(right_c)
            right = right + 1
            if n is not None:
                window[right_c] = window[right_c] + 1
            if window.get(right_c) is not None and window[right_c] == need[right_c]:
                valid = valid + 1

            while valid == len(need):
                new_s = s[left:right]
                if len(valid_s) <= 0 or len(valid_s) > len(new_s):
                    valid_s = new_s

                left_c = s[left]
                n = need.get(left_c)
                left = left + 1

                if n is not None:
                    window[left_c] = max(window[left_c] - 1, 0)
                    if window[left_c] < n:
                        valid = valid - 1

        return valid_s

# @lc code=end
