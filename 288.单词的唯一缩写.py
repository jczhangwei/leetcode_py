#
# @lc app=leetcode.cn id=288 lang=python3
#
# [288] 单词的唯一缩写
#
# https://leetcode-cn.com/problems/unique-word-abbreviation/description/
#
# algorithms
# Medium (33.91%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    1.8K
# Total Submissions: 5.4K
# Testcase Example:  '["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]\n' + 
#                     '[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]'
#
# 一个单词的缩写需要遵循 <起始字母><中间字母数><结尾字母> 这样的格式。
# 
# 以下是一些单词缩写的范例：
# 
# a) it                      --> it    (没有缩写)
# 
# ⁠    1
# ⁠    ↓
# b) d|o|g                   --> d1g
# 
# ⁠             1    1  1
# ⁠    1---5----0----5--8
# ⁠    ↓   ↓    ↓    ↓  ↓    
# c) i|nternationalizatio|n  --> i18n
# 
# ⁠             1
# ⁠    1---5----0
# ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
# 
# 
# 请你判断单词缩写在字典中是否唯一。当单词的缩写满足下面任何一个条件是，可以认为该单词缩写是唯一的：
# 
# 
# 字典 dictionary 中没有任何其他单词的缩写与该单词 word 的缩写相同。
# 字典 dictionary 中的所有缩写与该单词 word 的缩写相同的单词都与 word 相同。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：
# ["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]
# [[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]
# 输出：
# [null,false,true,false,true]
# 
# 解释：
# ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake",
# "card"]);
# validWordAbbr.isUnique("dear"); // return False
# validWordAbbr.isUnique("cart"); // return True
# validWordAbbr.isUnique("cane"); // return False
# validWordAbbr.isUnique("make"); // return True
# 
# 
# 
# 
# 提示：
# 
# 
# 每个单词都只由小写字符组成
# 
# 
#
from typing import * 
# @lc code=start
class ValidWordAbbr:
    def getAbbr(self, word):
        l = len(word)
        if not l:
            return 0
        return word[0] + str(l - 2) + word[l - 1]

    def __init__(self, dictionary: List[str]):
        self.store = store = {}
        for i, v in enumerate(dictionary):
            abbr = self.getAbbr(v)
            info = store[abbr] = store.get(abbr) or [0, None]
            if info[0] >= 0:
                info[0] += 1

            if info[1] and info[1] != v:
                info[0] = -1
            info[1] = v

    def isUnique(self, word: str) -> bool:
        info = self.store.get(self.getAbbr(word))
        return (not info) or info[0] == 0  or info[1] == word and (not info[0] < 0)


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
# @lc code=end
validWordAbbr = ValidWordAbbr(["deer", "door", "cake", "card"]);
print(validWordAbbr.isUnique("dear")) # return False
print(validWordAbbr.isUnique("cart")) # return True
print(validWordAbbr.isUnique("cane")) # return False
print(validWordAbbr.isUnique("make")) # return True

