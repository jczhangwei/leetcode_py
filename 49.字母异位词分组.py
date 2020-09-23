#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (63.65%)
# Likes:    477
# Dislikes: 0
# Total Accepted:    108.3K
# Total Submissions: 170.1K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# 说明：
#
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
#
#
#
from typing import *

# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        start = ord("a")
        for _, ss in enumerate(strs):
            pat = [0] * 26
            for _, s in enumerate(ss):
                pat[ord(s) - start] += 1
            pat = tuple(pat)
            if not store.get(pat):
                store[pat] = []
            store[pat].append(ss)
        return list(store.values())

# @lc code=end


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
