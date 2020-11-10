#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (43.20%)
# Likes:    775
# Dislikes: 0
# Total Accepted:    82.8K
# Total Submissions: 191.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
#
# 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
#
#
#
# 示例 1：
#
# 输入：[1,2,3]
#
# ⁠      1
# ⁠     / \
# ⁠    2   3
#
# 输出：6
#
#
# 示例 2：
#
# 输入：[-10,9,20,null,null,15,7]
#
# -10
# / \
# 9  20
# /  \
# 15   7
#
# 输出：42
#
#
from tools import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self) -> None:
        self.sumValue = -float("inf")

    def maxValue(self, root: TreeNode):
        if not root:
            return 0

        left_value = max(self.maxValue(root.left), 0)
        right_value = max(self.maxValue(root.right), 0)

        value = left_value + right_value + root.val
        self.sumValue = max(self.sumValue, value)

        return root.val + max(left_value, right_value)

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxValue(root)
        return self.sumValue
# @lc code=end


print(Solution().maxPathSum(buildTree([-10, 9, 20, None, None, 15, 7])))
print(Solution().maxPathSum(buildTree([-10, -10, -10])))
