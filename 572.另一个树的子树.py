#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#
# https://leetcode-cn.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (47.10%)
# Likes:    392
# Dislikes: 0
# Total Accepted:    53.3K
# Total Submissions: 113.1K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s
# 也可以看做它自身的一棵子树。
#
# 示例 1:
# 给定的树 s:
#
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
#
#
# 给定的树 t：
#
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
#
# 返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
#
# 示例 2:
# 给定的树 s：
#
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
#
#
# 给定的树 t：
#
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
#
# 返回 false。
#
#
from typing import *
from tools import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def isSame(s:TreeNode, t:TreeNode):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return isSame(s.left, t.left) and isSame(s.right, t.right)

        def isSub(s: TreeNode, t: TreeNode):
            if not t:
                return True
            if not s:
                return False
            return isSub(s.left, t) or isSub(s.right, t) or isSame(s, t)
        
        return isSub(s, t)

# @lc code=end
