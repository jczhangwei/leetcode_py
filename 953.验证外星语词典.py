#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#
# https://leetcode-cn.com/problems/verifying-an-alien-dictionary/description/
#
# algorithms
# Easy (56.86%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    8.7K
# Total Submissions: 15.4K
# Testcase Example:  '["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"'
#
# 某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。
#
# 给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回
# false。
#
#
#
# 示例 1：
#
# 输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# 输出：true
# 解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
#
# 示例 2：
#
# 输入：words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# 输出：false
# 解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。
#
# 示例 3：
#
# 输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# 输出：false
# 解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中
# '∅' 是空白字符，定义为比任何其他字符都小（更多信息）。
#
#
#
#
# 提示：
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# 在 words[i] 和 order 中的所有字符都是英文小写字母。
#
#
#
from typing import *
# @lc code=start


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        mp = {}
        for i, c in enumerate(order):
            mp[c] = i
        for i in range(1, len(words)):
            w = words[i]
            pre = words[i - 1]
            t = 0
            lw = len(w)
            lp = len(pre)
            for j in range(min(lw, lp)):
                if w[j] != pre[j]:
                    break
                t += 1
            if (lw <= t and lp > t) or (lw > t and lp > t and mp[w[t]] < mp[pre[t]]):
                return False

        return True

# @lc code=end


print(Solution().isAlienSorted(["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
print(Solution().isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
