#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (42.28%)
# Likes:    483
# Dislikes: 0
# Total Accepted:    89K
# Total Submissions: 209.2K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
'5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
#
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#
#
# 示例:
#
# 现有矩阵 matrix 如下：
#
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
#
#
# 给定 target = 5，返回 true。
#
# 给定 target = 20，返回 false。
#
#

# @lc code=start


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        h = len(matrix)
        if h <= 0:
            return False
        w = len(matrix[0])
        if w <= 0:
            return False

        i = w - 1
        j = 0
        while i >= 0 and j < h:
            if matrix[j][i] > target:
                i -= 1
                continue
            elif matrix[j][i] < target:
                j += 1
                continue
            else:
                return True

        return False

# @lc code=end


m = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
m = [[1, 1]]
print(Solution().searchMatrix(m, 20))
