#
# @lc app=leetcode.cn id=249 lang=python3
#
# [249] 移位字符串分组
#
# https://leetcode-cn.com/problems/group-shifted-strings/description/
#
# algorithms
# Medium (62.44%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    3K
# Total Submissions: 4.8K
# Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
#
# 给定一个字符串，对该字符串可以进行 “移位” 的操作，也就是将字符串中每个字母都变为其在字母表中后续的字母，比如："abc" ->
# "bcd"。这样，我们可以持续进行 “移位” 操作，从而生成如下移位序列：
#
# "abc" -> "bcd" -> ... -> "xyz"
#
# 给定一个包含仅小写字母字符串的列表，将该列表中所有满足 “移位” 操作规律的组合进行分组并返回。
#
#
#
# 示例：
#
# 输入：["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
# 输出：
# [
# ⁠ ["abc","bcd","xyz"],
# ⁠ ["az","ba"],
# ⁠ ["acef"],
# ⁠ ["a","z"]
# ]
# 解释：可以认为字母表首尾相接，所以 'z' 的后续为 'a'，所以 ["az","ba"] 也满足 “移位” 操作规律。
#
#
from typing import *
# @lc code=start


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def getSign(s: str):
            if len(s) <= 0:
                return -1
            dis = ord(s[0])
            sign = len(s)
            for i in range(1, len(s)):
                sign += (26 ** i) * (((ord(s[i]) - dis) + 26) % 26)
            return sign

        res = {}
        for _, s in enumerate(strings):
            sign = getSign(s)
            if not res.get(sign):
                res[sign] = []
            res[sign].append(s)
        return list(res.values())

        # @lc code=end


print(Solution().groupStrings(
    ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
print(Solution().groupStrings(["aa", "bb", "b"]))  # [["b"],["aa","bb"]]
r = Solution().groupStrings(["fpbnsbrkbcyzdmmmoisaa",
                             "cpjtwqcdwbldwwrryuclcngw",
                             "a",
                             "fnuqwejouqzrif",
                             "js",
                             "qcpr",
                             "zghmdiaqmfelr",
                             "iedda",
                             "l",
                             "dgwlvcyubde",
                             "lpt",
                             "qzq",
                             "zkddvitlk",
                             "xbogegswmad",
                             "mkndeyrh",
                             "llofdjckor",
                             "lebzshcb",
                             "firomjjlidqpsdeqyn",
                             "dclpiqbypjpfafukqmjnjg",
                             "lbpabjpcmkyivbtgdwhzlxa",
                             "wmalmuanxvjtgmerohskwil",
                             "yxgkdlwtkekavapflheieb",
                             "oraxvssurmzybmnzhw",
                             "ohecvkfe",
                             "kknecibjnq",
                             "wuxnoibr",  
                             "gkxpnpbfvjm",
                             "lwpphufxw",
                             "sbs",
                             "txb",
                             "ilbqahdzgij",
                             "i",
                             "zvuur",
                             "yfglchzpledkq",
                             "eqdf",
                             "nw",
                             "aiplrzejplumda",
                             "d",
                             "huoybvhibgqibbwwdzhqhslb",
                             "rbnzendwnoklpyyyauemm"])
# print(r)  # [["a","d","i","l"],["eqdf","qcpr"],["lpt","txb"],["yfglchzpledkq","zghmdiaqmfelr"],["kknecibjnq","llofdjckor"],["cpjtwqcdwbldwwrryuclcngw","huoybvhibgqibbwwdzhqhslb"],["lbpabjpcmkyivbtgdwhzlxa","wmalmuanxvjtgmerohskwil"],["iedda","zvuur"],["js","nw"],["lebzshcb","ohecvkfe"],["dgwlvcyubde","ilbqahdzgij"],["lwpphufxw","zkddvitlk"],["qzq","sbs"],["dclpiqbypjpfafukqmjnjg","yxgkdlwtkekavapflheieb"],["mkndeyrh","wuxnoibr"],["firomjjlidqpsdeqyn","oraxvssurmzybmnzhw"],["gkxpnpbfvjm","xbogegswmad"],["fpbnsbrkbcyzdmmmoisaa","rbnzendwnoklpyyyauemm"],["aiplrzejplumda","fnuqwejouqzrif"]]


cor = [["a", "d", "i", "l"], ["eqdf", "qcpr"], ["lpt", "txb"], ["yfglchzpledkq", "zghmdiaqmfelr"], ["kknecibjnq", "llofdjckor"], ["cpjtwqcdwbldwwrryuclcngw", "huoybvhibgqibbwwdzhqhslb"], ["lbpabjpcmkyivbtgdwhzlxa", "wmalmuanxvjtgmerohskwil"], ["iedda", "zvuur"], ["js", "nw"], ["lebzshcb", "ohecvkfe"], [
    "dgwlvcyubde", "ilbqahdzgij"], ["lwpphufxw", "zkddvitlk"], ["qzq", "sbs"], ["dclpiqbypjpfafukqmjnjg", "yxgkdlwtkekavapflheieb"], ["mkndeyrh", "wuxnoibr"], ["firomjjlidqpsdeqyn", "oraxvssurmzybmnzhw"], ["gkxpnpbfvjm", "xbogegswmad"], ["fpbnsbrkbcyzdmmmoisaa", "rbnzendwnoklpyyyauemm"], ["aiplrzejplumda", "fnuqwejouqzrif"]]


def testS(l):
    for _, i in enumerate(l):
        i.sort()
    p = [str(i) for i in l]
    p.sort()
    return p


print(testS(r))
print(testS(cor))
