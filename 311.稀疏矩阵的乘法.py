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

from collections import defaultdict
from typing import *
import collections
# @lc code=start


class Solution:
    def multiply(self, A: List[List[int]],
                 B: List[List[int]]) -> List[List[int]]:
        indexA = {}
        for i in range(len(A)):
            indexA[i] = {}
            for j in range(len(A[0])):
                if A[i][j]:
                    indexA[i][j] = A[i][j]

        indexB = {}
        for j in range(len(B[0])):
            indexB[j] = {}
            for i in range(len(B)):
                if B[i][j]:
                    indexB[j][i] = B[i][j]

        res = [[0 for i in range(len(B[0]))] for i in range(len(A))]
        for i in range(len(indexA)):
            for j in range(len(indexB)):
                for k, v in indexA[i].items():
                    if indexB[j].get(k):
                        res[i][j] = res[i][j] + indexA[i][k] * indexB[j][k]

        return res


class Solution2:
    def multiply(self, A: List[List[int]],
                 B: List[List[int]]) -> List[List[int]]:
        res = [[0 for i in range(len(B[0]))] for i in range(len(A))]
        for i in range(len(res)):
            for j in range(len(res[0])):
                for k in range(len(A[0])):
                    res[i][j] = res[i][j] + A[i][k] * B[k][j]

        return res


# @lc code=end


print(Solution().multiply([[1, 0, 0], [-1, 0, 3]],
                          [[7, 0, 0], [0, 0, 0], [0, 0, 1]]))
print(Solution().multiply([[1, -5]], [[12], [-1]]))
