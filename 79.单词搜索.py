#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (43.63%)
# Likes:    698
# Dislikes: 0
# Total Accepted:    122.4K
# Total Submissions: 279.9K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例:
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
#
#
# 提示：
#
#
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
#
#
#
from typing import *
# @lc code=start


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h = len(board)
        if h <= 0:
            return False
        w = len(board[0])
        if w <= 0:
            return False

        def find(x, y, cur_w, path=set()):
            n = board[y][x]
            if len(cur_w) <= 0 or len(cur_w) <= 1 and cur_w[0] == n:
                return True

            res = False
            if n == cur_w[0]:
                cur_w = cur_w[1:]
                path.add((x, y))
                if x - 1 >= 0 and (x - 1, y) not in path:
                    res = res or find(x - 1, y, cur_w, set(path))
                if x + 1 < w and (x + 1, y) not in path:
                    res = res or find(x + 1, y, cur_w, set(path))
                if y + 1 < h and (x, y + 1) not in path:
                    res = res or find(x, y + 1, cur_w, set(path))
                if y - 1 >= 0 and (x, y - 1) not in path:
                    res = res or find(x, y - 1, cur_w, set(path))

            return res

        for x in range(w):
            for y in range(h):
                n = board[y][x]
                res = find(x, y, word, set())
                if res:
                    return True

        return False

# @lc code=end

board = [
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
]
print(Solution().exist(board, "ABCESEEEFS"))

board = [
    ["C", "A", "A"],
    ["A", "A", "A"],
    ["B", "C", "D"]
]
print(Solution().exist(board, "AAB"))
board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]

print(Solution().exist(board, "ABCCED"))
print(Solution().exist(board, "SEE"))
print(Solution().exist(board, "ABCB"))
