#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#
# https://leetcode-cn.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (54.04%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 20.9K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
#
# 两棵树重复是指它们具有相同的结构以及相同的结点值。
#
# 示例 1：
#
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
#
#
# 下面是两个重复的子树：
#
# ⁠     2
# ⁠    /
# ⁠   4
#
#
# 和
#
# ⁠   4
#
#
# 因此，你需要以列表的形式返回上述重复子树的根结点。
#
#
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        store = collections.defaultdict()
        store.default_factory = store.__len__
        count = collections.Counter()

        def getId(node:  TreeNode):
            if node == None:
                return
            id = store[node.val, getId(node.left), getId(node.right)]
            count[id] += 1
            if count[id] == 2:
                res.append(node)

            return id

        getId(root)
        return res

# @lc code=end
