#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (41.35%)
# Likes:    529
# Dislikes: 0
# Total Accepted:    88K
# Total Submissions: 212.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#
#
# 示例 2:
#
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#


# [[1, 1, 1, 1, 1, 1, 1],
#  [1, 2, 2, 2, 2, 2, 1],
#  [1, 2, 3, 3, 3, 2, 1],
#  [1, 2, 2, 2, 2, 2, 1],
#  [1, 1, 1, 1, 1, 1, 1]]

#
#
from typing import *
# @lc code=start


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return []
        res = []
        width = len(matrix[0])
        height = len(matrix)
        cur_x = -1
        cur_y = 0
        dir_x = 1
        dir_y = 1
        while True:
            # move by x
            for i in range(width):
                cur_x += dir_x
                res.append(matrix[cur_y][cur_x])
            dir_x = -dir_x
            height -= 1
            if height <= 0:
                break

            for i in range(height):
                cur_y += dir_y
                res.append(matrix[cur_y][cur_x])
            dir_y = -dir_y
            width -= 1
            if width <= 0:
                break

        return res

        # @lc code=end


print(Solution().spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
