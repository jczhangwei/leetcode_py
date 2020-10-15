#
# @lc app=leetcode.cn id=311 lang=python3
#
#
# https://leetcode-cn.com/problems/sparse-matrix-multiplication/

# 311. 稀疏矩阵的乘法
# 给你两个 稀疏矩阵 A 和 B，请你返回 AB 的结果。你可以默认 A 的列数等于 B 的行数。

# 请仔细阅读下面的示例。

 

# 示例：

# 输入：

# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]

# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]

# 输出：

#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |
# 通过次数1,861提交次数2,440

from typing import *
# @lc code=start
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        pass
# @lc code=end

